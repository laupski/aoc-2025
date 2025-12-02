#!/bin/bash

set -euo pipefail

# Check if hyperfine is installed
if ! command -v hyperfine &> /dev/null; then
    echo "Error: hyperfine is not installed. Run mise install."
    exit 1
fi

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed"
    exit 1
fi

# Build list of scripts to benchmark
SCRIPTS=()

for day in $(seq -w 1 25); do
    dir="25-12-$day"
    
    if [[ -d "$dir" ]]; then
        if [[ -f "$dir/part1.py" ]]; then
            SCRIPTS+=(-n "$dir/part1" "uv run $dir/part1.py")
            echo "Found $dir/part1.py"
        fi
        
        if [[ -f "$dir/part2.py" ]]; then
            SCRIPTS+=(-n "$dir/part2" "uv run $dir/part2.py")
            echo "Found $dir/part2.py"
        fi
    fi
done

if [[ ${#SCRIPTS[@]} -eq 0 ]]; then
    echo "No scripts found to benchmark"
    exit 1
fi

echo ""
hyperfine --warmup 1 --runs 5 "${SCRIPTS[@]}"
