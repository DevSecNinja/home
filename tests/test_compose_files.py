import os
import re
import subprocess
import unittest
import yaml

class TestDockerComposeFiles(unittest.TestCase):

    important_properties = {
        'security_opt': ['no-new-privileges=true'],
        'environment': [r'(?:- )?(TZ|TIMEZONE)[:=]\s*\${TZ}'],
        'restart': 'always',
        'mem_limit': [r'^\d+[bBkKmMgG]?$']
    }

    def get_compose_files(self):
        root_dir = os.path.join(os.path.dirname(__file__), '..')
        for folder in ['docker/ansible/templates/compose-modules']:
            folder_dir = os.path.join(root_dir, folder)
            for filename in os.listdir(folder_dir):
                if filename.endswith('.yml') or filename.endswith('.yaml'):
                    with open(os.path.join(folder_dir, filename), 'r') as f:
                        function_content = f.read()
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

                            for pattern in required_patterns:
                                matched = False
                                for value in actual_values:
                                    if re.match(pattern, value):
                                        matched = True
                                        break
                                self.assertTrue(matched, f"{file_name} service {service} is missing required value '{pattern}' for {prop}")
                        else:
                            self.fail(f"{file_name} service {service} is missing important property {prop}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
