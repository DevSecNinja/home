import os
import subprocess
import unittest

class TestFunctionsHelp(unittest.TestCase):

    def get_compose_files(self):
        root_dir = os.path.join(os.path.dirname(__file__), '..')
        for folder in ['templates/compose-modules']:
            folder_dir = os.path.join(root_dir, folder)
            for filename in os.listdir(folder_dir):
                if not '.' in filename and not filename.startswith('_'):
                    with open(os.path.join(folder_dir, filename), 'r') as f:
                        function_content = f.read()
                    yield folder, filename, function_content

    def test_filename_hyphens(self):
        for folder, file_name, function_content in self.get_compose_files():
            with self.subTest(file_name=file_name, folder_name=folder):
                underscore_present = '_' in file_name
                self.assertFalse(underscore_present, f"{file_name} contains underscore(s) instead of hyphen(s).")


if __name__ == "__main__":
    unittest.main(verbosity=2)
