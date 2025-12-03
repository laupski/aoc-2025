#!/bin/bash

# Profile script for Advent of Code 2025
# Runs kernprof on all part1.py and part2.py files from 25-12-01 to 25-12-25

set -euo pipefail

# Check if uv is installed
if ! command -v ruff &> /dev/null; then
    echo "Error: ruff is not installed"
    exit 1
fi

for day in $(seq -w 1 25); do
    dir="25-12-$day"
    
    if [[ -d "$dir" ]]; then
        if [[ -f "$dir/part1.py" ]]; then
            ruff format "$dir/part1.py"
        fi
        
        if [[ -f "$dir/part2.py" ]]; then
            ruff format "$dir/part2.py"
        fi
    fi
done
