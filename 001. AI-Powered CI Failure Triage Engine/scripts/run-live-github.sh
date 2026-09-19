#!/usr/bin/env bash
set -euo pipefail
if (($# != 2)); then echo "Usage: $0 OWNER/REPO RUN_ID" >&2; exit 2; fi
: "${GITHUB_TOKEN:?Set a fine-grained token with Actions: read for private repositories}"
python3 -m ci_triage --repository "$1" --run-id "$2"

