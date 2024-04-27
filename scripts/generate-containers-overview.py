import os
import yaml
import re
from collections import defaultdict

important_properties = {
    'container_name',
    'image'
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
    important_properties_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))
    for folder, file_name, function_content, deprecation_notice in get_compose_files():
        compose_dict = parse_compose_content(function_content)
        services = compose_dict['services']

        for service, config in sorted(services.items()):
            for prop in important_properties:
                if prop in config:
                    actual_values = config[prop]

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
        f.write("# Docker Information\n\n")
        for (folder, file_name), services in sorted(important_properties_dict.items()):
            f.write(f"## {folder}/{file_name}\n\n")
            for service, props in sorted(services.items()):
                f.write(f"### Service: {service}\n\n")
                for prop, values in sorted(props.items()):
                    if prop == "Deprecation Notice":
                        f.write(f"> :warning: **{prop}:** {', '.join(values)}\n\n")
                    else:
                        f.write(f"**{prop}:** {', '.join(values)}\n\n")

if __name__ == "__main__":
    important_property_values = get_important_properties()
    write_markdown_file(important_property_values)
