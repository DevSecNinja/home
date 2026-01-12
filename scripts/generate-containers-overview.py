import os
import yaml
import re
from collections import defaultdict

important_properties = {
    'container_name',
    'image',
    'labels'
}

def get_compose_files():
    root_dir = os.path.join(os.path.dirname(__file__), '..')
    for folder in ['docker/ansible/templates/compose-modules']:
        folder_dir = os.path.join(root_dir, folder)
        for filename in os.listdir(folder_dir):
            if filename.endswith('.yml') or filename.endswith('.yaml'):
                with open(os.path.join(folder_dir, filename), 'r') as f:
                    file_content = f.read()
                deprecation_notice = None
                if "DEPRECATION NOTICE" in file_content:
                    deprecation_notice = str([x.strip() for x in file_content.split("#### DEPRECATION NOTICE")[1].split("#")[2:6] if x][1])
                yield folder, filename, file_content, deprecation_notice

def parse_compose_content(content):
    return yaml.safe_load(content)

def get_important_properties():
    important_properties_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    for folder, file_name, function_content, deprecation_notice in get_compose_files():
        compose_dict = parse_compose_content(function_content)
        services = compose_dict['services']

        for service, config in sorted(services.items()):
            for prop in important_properties:
                if prop in config:
                    actual_values = config[prop]

                    # Check for Traefik labels
                    if prop == 'labels' and 'traefik.enable=true' in actual_values:
                        host_label = next((label for label in actual_values if 'rule=Host' in label), None)
                        if host_label:
                            traefik_url = re.findall(r'Host\(`(.*)\`', host_label)
                            if traefik_url:
                                important_properties_dict[(folder, file_name)][service]["url"] = traefik_url
                        else:
                            important_properties_dict[(folder, file_name)][service]["url"] = [f'{config["container_name"]}.$DOMAINNAME']
                        continue

                    # Convert dictionary to list of strings
                    if isinstance(actual_values, dict):
                        actual_values = [f"{key}: {value}" for key, value in actual_values.items()]
                    elif isinstance(actual_values, str):
                        actual_values = [actual_values]

                    important_properties_dict[(folder, file_name)][service][prop] = actual_values
            if deprecation_notice:
                important_properties_dict[(folder, file_name)][service]["Deprecation Notice"] = [deprecation_notice]
    return important_properties_dict

def write_markdown_file(important_properties_dict):
    with open('docker/docker_containers.md', 'w') as f:
        f.write("# Docker Information")
        for (folder, file_name), services in sorted(important_properties_dict.items()):
            f.write(f"\n\n## {folder}/{file_name}")
            for service, props in sorted(services.items()):
                f.write(f"\n\n### Service: {service}")
                for prop, values in sorted(props.items()):
                    if prop == "Deprecation Notice":
                        f.write(f"\n\n> :warning: **{prop}:** {', '.join(values)}")
                    else:
                        if prop == "url" and "Deprecation Notice" not in props:
                            f.write(f"\n\n**{prop}:** {', '.join(values)}")
                        elif prop != "url":
                            f.write(f"\n\n**{prop}:** {', '.join(values)}")
        f.write("\n")

def write_yaml(important_properties_dict):
    yaml_data = []
    for (folder, file_name), services in sorted(important_properties_dict.items()):
        for service, props in sorted(services.items()):
            container_name = props.get('container_name')
            image = props.get('image')
            deprecation_notice = props.get('Deprecation Notice')
            url = props.get('url')
            if container_name and image and not deprecation_notice:
                if url:
                    yaml_data.append({'container_name': container_name[0], 'image': image[0], 'url': url[0]})
                else:
                    yaml_data.append({'container_name': container_name[0], 'image': image[0]})
    with open('docker/docker_containers.yaml', 'w') as f:
        yaml.dump(yaml_data, f)

if __name__ == "__main__":
    important_property_values = get_important_properties()
    write_markdown_file(important_property_values)
    write_yaml(important_property_values)
