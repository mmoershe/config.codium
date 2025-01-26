#!/bin/bash

# Check if extensions.txt exists
if [ ! -f "extensions.txt" ]; then
    echo "Error: extensions.txt not found in the current directory."
    exit 1
fi

# Install extensions listed in extensions.txt
echo "Installing extensions from extensions.txt..."
xargs -n1 codium --install-extension <extensions.txt

if [ $? -eq 0 ]; then
    echo "All extensions installed successfully."
else
    echo "Error occurred while installing extensions."
fi
