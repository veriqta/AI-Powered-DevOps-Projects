#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
command -v python3 >/dev/null || { echo "FAIL: python3 is required"; exit 1; }
python3 -c 'import sys; assert sys.version_info >= (3, 11), "Python 3.11+ required"'
command -v git >/dev/null || { echo "FAIL: git is required"; exit 1; }
test -f "$project_dir/pyproject.toml"
test -d "$project_dir/sample-data"
echo "PASS: Python $(python3 --version 2>&1), Git $(git --version), and project files are ready."

