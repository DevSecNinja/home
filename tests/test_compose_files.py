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

if __name__ == "__main__":
    unittest.main(verbosity=2)
