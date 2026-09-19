# Lab 00: Environment and Baseline

## Objective

Prepare an isolated development environment and prove that the supplied project works before changing it.

## Follow first

- [Prerequisites](../prerequisites/README.md)
- [Getting Started](../getting-started/README.md)
- [Project Guide Part 00](../project-guide/part-00-orientation-and-setup/README.md)

## Steps

1. Clone a fork or learner repository.
2. Enter `projects/001-ai-powered-ci-failure-triage-engine`.
3. Create a project branch:

   ```bash
   git switch -c project-001-ci-triage
   ```

4. Verify Python and Git:

   ```bash
   python3 --version
   git --version
   ```

5. Run the setup script:

   ```bash
   chmod +x scripts/*.sh
   ./scripts/setup.sh
   source .venv/bin/activate
   ```

6. Verify the installation:

   ```bash
   ./scripts/verify-environment.sh
   ci-failure-triage --help
   python -m unittest discover -s tests -v
   ```

7. Inspect `.env.example` without adding credentials.
8. Record the operating system, Python version, Git version, branch, and test result.

## Expected result

The CLI help opens, the supplied tests pass, and the repository remains free of secrets and generated output.

## Deliverable

A completed lab record containing the environment versions, verification output, and confirmation that `.env` is not tracked.

## Completion gate

- [ ] Python 3.11 or newer is active.
- [ ] The project runs inside `.venv`.
- [ ] All baseline tests pass.
- [ ] No API key is required.

