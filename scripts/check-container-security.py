import yaml
import subprocess
import os
from shutil import which

# If trivy is not installed, install it
if not which('trivy'):
    print("Trivy is not installed. Installing now...")
    subprocess.run(['brew', 'install', 'trivy'])

# Load Docker images from YAML file
with open('docker/docker_containers.yaml', 'r') as file:
    docker_containers = yaml.safe_load(file)

# Check each Docker image for security vulnerabilities
unique_images = set()
for container in docker_containers:
    image = container['image']
    container_name = container['container_name']
    output_file = 'docker/security-reports/' + container_name + ".json"
    output_table_file = 'docker/security-reports/' + container_name + ".txt"

    if image not in unique_images:
        unique_images.add(image)
        print(f"Checking {image} for security vulnerabilities...")
        subprocess.run(['trivy', 'image', '--scanners', 'vuln', '--severity', 'HIGH,CRITICAL', '--format', 'json', '--output', output_file, image])
        print('Converting JSON output to table')
        subprocess.run(['trivy', 'convert', '--format', 'table', '--output', output_table_file, output_file])

