# Part 00: Orientation and Setup

## Purpose

Prepare a reproducible workstation and understand the project’s safety boundary before analyzing CI data.

## Learning outcomes

- explain what the system does and deliberately does not do;
- create an isolated Python environment;
- install and verify the CLI;
- distinguish local fixture mode from live GitHub mode;
- protect credentials and organizational logs.

## Steps

1. Read the project [README](../../README.md) and [prerequisites](../../prerequisites/README.md).
2. Complete [system configuration](../../getting-started/system-configuration.md).
3. Clone the learner’s own fork or repository, enter this project directory, and create a feature branch.
4. Run `./scripts/setup.sh` or perform the documented manual installation.
5. Run `./scripts/verify-environment.sh`.
6. Run `ci-failure-triage --help`.
7. Read `.env.example`; do not add real secrets yet.
8. Record the Python version, operating system, branch, and verification result.

## Validation

```bash
./scripts/verify-environment.sh
python -m unittest discover -s tests -v
```

## Evidence

Capture sanitized terminal output and the completed [readiness checklist](../../getting-started/readiness-checklist.md).

## Completion gate

- [ ] Required commands work inside `.venv`.
- [ ] The local workflow requires no token or paid service.
- [ ] The read-only and no-remediation boundaries can be explained.
- [ ] No secret or private log has been copied into the project.

Next: [Part 01](../part-01-operational-problem-and-context/README.md)

