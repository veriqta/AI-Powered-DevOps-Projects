#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
output_dir="$project_dir/output"
mkdir -p "$output_dir"
for fixture in "$project_dir"/sample-data/*.json; do
  name="$(basename "$fixture" .json)"
  python3 -m ci_triage --input "$fixture" --format json --output "$output_dir/$name-report.json" "$@"
done
echo "Created reports in output/."
