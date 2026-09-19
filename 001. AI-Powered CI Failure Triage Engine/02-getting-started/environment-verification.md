# Environment Verification

Run:

```bash
./scripts/verify-environment.sh
./scripts/validate-samples.sh
python -m unittest discover -s tests -v
```

Expected results:

- Python 3.11 or newer is reported.
- Git is available.
- Five fixtures validate.
- Every test reports `ok`.
- The command exits with status 0.

Then run:

```bash
ci-failure-triage --input sample-data/runner-failure.json --format json
```

Confirm:

- `schema_version` is `1.0`.
- The category is `runner_infrastructure`.
- Evidence references exist.
- `ai_explanation` is `null`.
- No token or secret value appears.

