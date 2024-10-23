#!/bin/bash

echo "Extension installation script starting..."

# Define extensions array
extensions=(
    # Home Assistant
    "emilast.LogFileHighlighter"
    "esbenp.prettier-vscode"
    "ESPHome.esphome-vscode"
    "keesschollaart.vscode-home-assistant"
    "lukas-tr.materialdesignicons-intellisense"
    "netcorext.uuid-generator"
    "oderwat.indent-rainbow"
    "redhat.vscode-yaml"
    "usernamehw.errorlens"
)

# Install extensions
for extension in "${extensions[@]}"; do
    echo "Installing extension: $extension"
    /usr/local/bin/install-extension "$extension" || echo "Failed to install $extension"
done

echo "Extension installation complete!"
