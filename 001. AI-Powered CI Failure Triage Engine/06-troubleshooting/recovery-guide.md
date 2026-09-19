# Recovery Guide

## Return to a known-good local state

```bash
deactivate 2>/dev/null || true
./scripts/cleanup.sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
make verify
```

The cleanup script removes generated output only. It does not delete source, tests, fixtures, or learner documentation.

## Isolate the failing layer

1. Run a supplied fixture without AI.
2. Run the complete local test suite.
3. Validate the custom input independently.
4. Add live GitHub acquisition.
5. Add optional AI last.

The first failing layer identifies the appropriate recovery path.

## Recover from suspected credential exposure

1. Stop using the credential.
2. Revoke or rotate it in the issuing system.
3. Remove it from working files and generated reports.
4. If committed, follow the hosting provider’s secret-removal process; deleting the latest file is insufficient because history remains.
5. Add a regression test and document the incident without reproducing the secret.

## Recover from a false classification

1. Preserve the sanitized input as a regression fixture.
2. Identify which rule matched and which evidence triggered it.
3. Narrow rule conditions instead of changing confidence cosmetically.
4. Add a positive test and a nearby negative test.
5. Run the entire suite to detect unintended precedence changes.
6. Record the behavior change in project documentation.

## Request help safely

Include the project version, Python version, operating system, exact sanitized command, exit code, sanitized stack trace, and whether the issue reproduces with supplied fixtures. Never include `.env`, access tokens, private repository URLs, or raw organizational logs.

