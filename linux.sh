#!/bin/bash

set -e

INSTALL_DIR="/usr/local/bin"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing Ubutool..."

if [ "$EUID" -ne 0 ]; then
    echo "Please run this installer with sudo."
    echo "Example: sudo ./linux.sh"
    exit 1
fi

if [ ! -f "$SCRIPT_DIR/ubutool.py" ]; then
    echo "Error: ubutool.py was not found."
    exit 1
fi

cp "$SCRIPT_DIR/ubutool.py" "$INSTALL_DIR/ubutool"
chmod +x "$INSTALL_DIR/ubutool"

echo "Ubutool has been installed successfully!"
echo "Run it with: ubutool"
