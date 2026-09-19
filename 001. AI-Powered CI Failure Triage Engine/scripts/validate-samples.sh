#!/usr/bin/env bash
set -euo pipefail
project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)"
PROJECT_DIR="$project_dir" python3 - <<'PY'
import json, os
from pathlib import Path
root=Path(os.environ["PROJECT_DIR"])
files=sorted((root/"sample-data").glob("*.json"))
required={
    "dependency-failure.json",
    "permission-failure.json",
    "runner-failure.json",
    "test-failure.json",
    "unknown-failure.json",
}
found={path.name for path in files}
missing=sorted(required-found)
assert not missing, f"missing required JSON fixtures: {', '.join(missing)}"
for path in files:
    data=json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data.get("run"),dict), path
    assert isinstance(data.get("jobs"),list) and data["jobs"], path
    print("VALID",path.name)
PY
