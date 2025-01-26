#!/bin/bash

# Export the list of installed extensions
echo "Saving installed extensions to extensions.txt..."
codium --list-extensions >extensions.txt

if [ $? -eq 0 ]; then
    echo "Extensions list saved to extensions.txt."
else
    echo "Error occurred while saving extensions."
fi
