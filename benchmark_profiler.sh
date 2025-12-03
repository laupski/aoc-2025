#!/bin/bash

# Profile script for Advent of Code 2025
# Runs kernprof on all part1.py and part2.py files from 25-12-01 to 25-12-25

set -euo pipefail

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed"
    exit 1
fi

for day in $(seq -w 1 25); do
    dir="25-12-$day"
    
    if [[ -d "$dir" ]]; then
        if [[ -f "$dir/part1.py" ]]; then
            echo "════════════════════════════════════════"
            echo " Profiling $dir/part1.py"
            echo "════════════════════════════════════════"
            uv run kernprof -l -v "$dir/part1.py"
            rm -f part1.py.lprof
            echo ""
        fi
        
        if [[ -f "$dir/part2.py" ]]; then
            echo "════════════════════════════════════════"
            echo " Profiling $dir/part2.py"
            echo "════════════════════════════════════════"
            uv run kernprof -l -v "$dir/part2.py"
            rm -f part2.py.lprof
            echo ""
        fi
    fi
done
