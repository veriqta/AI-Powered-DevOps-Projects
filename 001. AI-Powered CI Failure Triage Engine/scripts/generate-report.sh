#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
output_dir="$project_dir/output"
mkdir -p "$output_dir"
python3 -m ci_triage --input "$project_dir/sample-data/test-failure.json" --format json --output "$output_dir/triage-report.json"
echo "Created output/triage-report.json"

