#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
output_dir="$project_dir/output"
if [[ -L "$output_dir" ]]; then echo "Refusing to clean a symlink" >&2; exit 1; fi
if [[ -d "$output_dir" ]]; then
  find "$output_dir" -mindepth 1 -maxdepth 1 -delete
  rmdir "$output_dir"
  echo "Removed generated output."
else
  echo "Nothing to clean."
fi

