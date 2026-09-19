# Setup Problems

## `python3` is not found

Install Python 3.11 or newer using the operating-system instructions in `getting-started/system-configuration.md`. Confirm with `python3 --version`. On Windows, `py -3.11` may be the correct launcher.

## The virtual environment cannot be created

On Debian or Ubuntu, the `venv` package may be missing:

```bash
sudo apt-get update
sudo apt-get install python3-venv
```

Use the package manager approved for the workstation. Do not use `sudo pip install`.

## Activation is blocked in PowerShell

Use WSL as recommended, or allow locally created scripts for the current user according to organizational policy:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Do not weaken a managed endpoint policy without authorization.

## `ci-failure-triage` is not found

Confirm that the virtual environment is active, then reinstall:

```bash
python -m pip install -e .
python -m pip show ai-powered-ci-failure-triage
```

You can also verify the module directly:

```bash
python -m ci_triage --help
```

## Installation uses the wrong Python

Compare these commands:

```bash
which python
python --version
python -m pip --version
```

They should point into `.venv`. Deactivate and recreate the environment if they do not.

## A script reports permission denied

Restore executable permissions:

```bash
chmod +x scripts/*.sh
```

On Windows, run the equivalent commands from WSL or invoke the underlying Python command documented in the script.

