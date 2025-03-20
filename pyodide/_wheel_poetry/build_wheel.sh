#!/bin/bash
set -e

# Ensure Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Please install it first."
    exit 1
fi

# Build the wheel
poetry build -f wheel
