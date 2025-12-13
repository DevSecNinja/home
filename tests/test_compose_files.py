import os
import re
import unittest
import yaml

class TestDockerComposeFiles(unittest.TestCase):

    important_properties = {
        'container_name': [r'^.+'],
        'environment': [r'(?:- )?(?:TZ|TIMEZONE|TIME_ZONE)[:=]\s*\${TZ(?::-[^}]+)?}'],
        'image': [r'.+:[\w\.-]+@sha256:[0-9a-fA-F]{64}$'],
        'mem_limit': [r'^(?:\d+[bBkKmMgG]?|\$\{[A-Za-z_][A-Za-z0-9_]*(?::-[^}]*)?\})$'],
        'restart': [r'^(always|no|on-failure)$'],
        'security_opt': ['no-new-privileges=true']
    }

    def get_compose_files(self):
        root_dir = os.path.join(os.path.dirname(__file__), '..')
        for folder in ['docker/ansible/templates/compose-modules']:
            folder_dir = os.path.join(root_dir, folder)
            for filename in os.listdir(folder_dir):
                if filename.endswith('.yml') or filename.endswith('.yaml'):
                    with open(os.path.join(folder_dir, filename), 'r') as f:
                        function_content = f.read()
                    if "DEPRECATION NOTICE" in function_content:
                        continue
                    yield folder, filename, function_content

    def parse_compose_content(self, content):
        return yaml.safe_load(content)

    def test_filename_hyphens(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                underscore_present = '_' in file_name
                self.assertFalse(underscore_present, f"{file_name} contains underscore(s) instead of hyphen(s).")

    def test_filename_extension(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                yaml_extension_present = '.yaml' in file_name
                self.assertFalse(yaml_extension_present, f"{file_name} contains .yaml extension instead of .yml.")

    def test_important_properties(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                compose_dict = self.parse_compose_content(function_content)
                services = compose_dict['services']

                for service, config in services.items():
                    for prop, required_patterns in self.important_properties.items():
                        if prop in config:
                            actual_values = config[prop]

                            # Convert dictionary to list of strings
                            if isinstance(actual_values, dict):
                                actual_values = [f"{key}: {value}" for key, value in actual_values.items()]
                            elif isinstance(actual_values, str):
                                actual_values = [actual_values]

                            for pattern in required_patterns:
                                matched = False
                                for value in actual_values:
                                    if re.match(pattern, str(value)): # Added str() to handle non-string values
                                        matched = True
                                        break
                                self.assertTrue(matched, f"{file_name} service {service} is missing required value '{pattern}' for {prop}")
                        else:
                            self.fail(f"{file_name} service {service} is missing important property {prop}")

    def test_db_backup_services(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                compose_dict = self.parse_compose_content(function_content)
                services = compose_dict['services']

                for service in services.keys():
                    if service.endswith('-db'):
                        backup_service = f"{service}-backup"
                        self.assertIn(backup_service, services, f"{file_name} is missing the {backup_service} service for {service}")

    def test_no_swarm_deploy_configuration(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                compose_dict = self.parse_compose_content(function_content)
                services = compose_dict['services']

                for service, config in services.items():
                    self.assertNotIn('deploy', config, f"{file_name} service {service} contains 'deploy' configuration which is for Docker Swarm mode and should not be used")

    def test_traefik_router_service_labels(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                compose_dict = self.parse_compose_content(function_content)
                services = compose_dict['services']

                for service, config in services.items():
                    if 'labels' in config:
                        labels = config['labels']

                        # Convert labels to list of strings if it's a dictionary
                        if isinstance(labels, dict):
                            labels = [f"{key}={value}" for key, value in labels.items()]
                        elif isinstance(labels, str):
                            labels = [labels]

                        # Find all Traefik router service labels
                        for label in labels:
                            label_str = str(label)
                            # Match traefik.http.routers.{router-name}.service={service-name}
                            router_service_match = re.match(r'traefik\.http\.routers\.(.+)\.service=(.+)', label_str)

                            if router_service_match:
                                router_name = router_service_match.group(1)
                                service_value = router_service_match.group(2)

                                # The service value should NOT end with -svc or -service
                                self.assertFalse(service_value.endswith('-svc'),
                                    f"{file_name} service {service} has Traefik router '{router_name}' with service value '{service_value}' ending with '-svc'. This should be removed.")
                                self.assertFalse(service_value.endswith('-service'),
                                    f"{file_name} service {service} has Traefik router '{router_name}' with service value '{service_value}' ending with '-service'. This should be removed.")

                                # The service value should NOT start with svc- or service-
                                self.assertFalse(service_value.startswith('svc-'),
                                    f"{file_name} service {service} has Traefik router '{router_name}' with service value '{service_value}' starting with 'svc-'. This should be removed.")
                                self.assertFalse(service_value.startswith('service-'),
                                    f"{file_name} service {service} has Traefik router '{router_name}' with service value '{service_value}' starting with 'service-'. This should be removed.")

                                # Extract the expected service name from router name
                                # Remove common router suffixes like -rtr, -noauth-rtr, -monitor-rtr, etc.
                                expected_service = re.sub(r'-(?:rtr|noauth-rtr|monitor-rtr)$', '', router_name)

                                # The service value should match the router name minus the '-rtr' suffix
                                self.assertEqual(service_value, expected_service,
                                    f"{file_name} service {service} has Traefik router '{router_name}' with incorrect service value '{service_value}'. Expected '{expected_service}' (router name minus suffix).")

    def test_traefik_label_consistency(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                compose_dict = self.parse_compose_content(function_content)
                services = compose_dict['services']

                for service, config in services.items():
                    if 'labels' in config:
                        labels = config['labels']

                        # Convert labels to list of strings if it's a dictionary
                        if isinstance(labels, dict):
                            labels = [f"{key}={value}" for key, value in labels.items()]
                        elif isinstance(labels, str):
                            labels = [labels]

                        # Check if Traefik is enabled
                        traefik_enabled = False
                        docker_network = None
                        routers = []
                        service_definitions = []

                        for label in labels:
                            label_str = str(label)

                            # Check for traefik.enable=true
                            if label_str == 'traefik.enable=true':
                                traefik_enabled = True

                            # Extract docker network
                            network_match = re.match(r'traefik\.docker\.network=(.+)', label_str)
                            if network_match:
                                docker_network = network_match.group(1)

                            # Find router definitions (rule, middlewares, service) - support both HTTP and UDP
                            router_match = re.match(r'traefik\.(http|udp)\.routers\.([^.]+)\.(.+)=(.+)', label_str)
                            if router_match:
                                protocol = router_match.group(1)
                                router_name = router_match.group(2)
                                router_property = router_match.group(3)
                                router_value = router_match.group(4)
                                routers.append((router_name, router_property, router_value, protocol))

                            # Find service port definitions - support both HTTP and UDP
                            service_match = re.match(r'traefik\.(http|udp)\.services\.([^.]+)\.loadbalancer\.server\.port=(.+)', label_str)
                            if service_match:
                                protocol = service_match.group(1)
                                service_name = service_match.group(2)
                                port = service_match.group(3)
                                service_definitions.append((service_name, port, protocol))

                        # If Traefik is enabled, validate required labels
                        if traefik_enabled:
                            # Must have docker network
                            self.assertIsNotNone(docker_network,
                                f"{file_name} service {service} has traefik.enable=true but missing traefik.docker.network label")

                            # Network should follow naming pattern: *-frontend (except for auth services which can use *-backend)
                            if docker_network:
                                is_auth_service = 'auth' in service.lower() or 'auth' in file_name.lower()
                                valid_network_suffix = docker_network.endswith('-frontend') or (is_auth_service and docker_network.endswith('-backend'))
                                if not valid_network_suffix:
                                    expected_pattern = "'{name}-frontend' or '{name}-backend' for auth services" if is_auth_service else "'{name}-frontend'"
                                    self.fail(f"{file_name} service {service} Traefik network '{docker_network}' should follow expected pattern: {expected_pattern}")

                            # Network should be defined in networks section
                            if docker_network and 'networks' in compose_dict:
                                network_names = list(compose_dict['networks'].keys())
                                self.assertIn(docker_network, network_names,
                                    f"{file_name} service {service} Traefik network '{docker_network}' is not defined in networks section")

                            # Must have at least one router
                            self.assertTrue(len(routers) > 0,
                                f"{file_name} service {service} has traefik.enable=true but no traefik.http.routers.* or traefik.udp.routers.* labels")

                            # Group routers by name and protocol to validate completeness
                            router_groups = {}
                            for router_name, router_property, router_value, protocol in routers:
                                key = f"{router_name}_{protocol}"
                                if key not in router_groups:
                                    router_groups[key] = {'name': router_name, 'protocol': protocol, 'props': {}}
                                router_groups[key]['props'][router_property] = router_value

                            # Each router must have service, and HTTP routers should have rule (UDP routers don't always need rule)
                            for router_key, router_data in router_groups.items():
                                router_name = router_data['name']
                                protocol = router_data['protocol']
                                router_props = router_data['props']

                                self.assertIn('service', router_props,
                                    f"{file_name} service {service} Traefik {protocol} router '{router_name}' is missing service definition")

                                # HTTP routers should have rule (but allow automatic inference when domain matches container name)
                                if protocol == 'http':
                                    # Only require rule if it's not a monitor-only router or has middlewares
                                    if 'middlewares' in router_props or not router_name.endswith('-monitor-rtr'):
                                        if 'rule' not in router_props:
                                            # Check if rule can be automatically inferred (container name matches expected domain)
                                            container_name = config.get('container_name', service)
                                            # If router name starts with container name, rule can be inferred
                                            if not router_name.startswith(container_name):
                                                self.fail(f"{file_name} service {service} Traefik HTTP router '{router_name}' is missing rule definition and cannot be automatically inferred (router name doesn't match container name '{container_name}')")

                                    # If rule exists, it should contain Host() for HTTP
                                    if 'rule' in router_props:
                                        rule = router_props['rule']
                                        self.assertRegex(rule, r'Host\(`[^`]+`\)',
                                            f"{file_name} service {service} Traefik HTTP router '{router_name}' rule '{rule}' should contain Host() definition")

                                    # HTTP routers should have middleware chains (except monitor routers and auth services)
                                    is_auth_service = 'auth' in service.lower() or 'auth' in file_name.lower()
                                    if not router_name.endswith('-monitor-rtr') and not is_auth_service:
                                        self.assertIn('middlewares', router_props,
                                            f"{file_name} service {service} Traefik HTTP router '{router_name}' is missing middlewares definition")

                                    # Middleware should follow expected pattern: chain-*@file (if present)
                                    if 'middlewares' in router_props:
                                        middlewares = router_props['middlewares']
                                        self.assertRegex(middlewares, r'^chain-[^@]+@file$',
                                            f"{file_name} service {service} Traefik HTTP router '{router_name}' middlewares '{middlewares}' should follow pattern 'chain-{{name}}@file'")

                            # Must have at least one service port definition
                            self.assertTrue(len(service_definitions) > 0,
                                f"{file_name} service {service} has traefik.enable=true but no traefik.http.services.* or traefik.udp.services.* loadbalancer.server.port labels")

                            # Validate port values are valid
                            for svc_name, port, protocol in service_definitions:
                                # Port should not be empty
                                self.assertTrue(port and str(port).strip(),
                                    f"{file_name} service {service} Traefik service '{svc_name}' has empty or invalid port value")

                                # Port should be numeric
                                try:
                                    port_num = int(str(port).strip())
                                except ValueError:
                                    self.fail(f"{file_name} service {service} Traefik service '{svc_name}' has non-numeric port '{port}'. Port must be a valid number.")

                                # Port should be in valid range (1-65535)
                                self.assertTrue(1 <= port_num <= 65535,
                                    f"{file_name} service {service} Traefik service '{svc_name}' has invalid port '{port_num}'. Port must be between 1 and 65535.")

                            # Validate that router services match defined services
                            defined_service_names = [svc_name for svc_name, port, protocol in service_definitions]
                            for router_key, router_data in router_groups.items():
                                router_props = router_data['props']
                                router_name = router_data['name']
                                if 'service' in router_props:
                                    router_service = router_props['service']
                                    self.assertIn(router_service, defined_service_names,
                                        f"{file_name} service {service} Traefik router '{router_name}' references service '{router_service}' but no matching traefik.*.services.{router_service}.loadbalancer.server.port label found")

    def test_traefik_redundant_rules(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                compose_dict = self.parse_compose_content(function_content)
                services = compose_dict['services']

                for service, config in services.items():
                    if 'labels' in config:
                        labels = config['labels']

                        # Convert labels to list of strings if it's a dictionary
                        if isinstance(labels, dict):
                            labels = [f"{key}={value}" for key, value in labels.items()]
                        elif isinstance(labels, str):
                            labels = [labels]

                        container_name = config.get('container_name', service)

                        # Find router rules that might be redundant
                        for label in labels:
                            label_str = str(label)
                            # Match traefik.http.routers.{router-name}.rule=Host(`{domain}`)
                            rule_match = re.match(r'traefik\.http\.routers\.([^.]+)\.rule=Host\(`([^`]+)`\)', label_str)

                            if rule_match:
                                router_name = rule_match.group(1)
                                domain = rule_match.group(2)

                                # Check if this is a simple domain that matches container name
                                # Expected pattern: {container_name}.$DOMAINNAME
                                expected_domain = f"{container_name}.$DOMAINNAME"

                                # Skip monitor, noauth, and other special routers - only check main routers
                                if router_name.endswith('-rtr') and not any(suffix in router_name for suffix in ['-monitor-', '-noauth-', '-auth-']):
                                    base_router_name = router_name.replace('-rtr', '')

                                    # If the domain matches the expected auto-inferred domain, the rule is redundant
                                    if domain == expected_domain and base_router_name == container_name:
                                        self.fail(f"{file_name} service {service} has redundant Traefik rule '{domain}' for router '{router_name}'. This rule can be automatically inferred from container name '{container_name}' and should be removed.")

if __name__ == "__main__":
    unittest.main(verbosity=2)
