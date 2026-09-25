# Contributing

Thank you for helping improve AI-Powered DevOps Projects.

Contributions should improve technical accuracy, safety, reproducibility, accessibility, or the learning experience. Every contribution must be suitable for a public engineering repository.

## Before contributing

1. Read the [Code of Conduct](CODE_OF_CONDUCT.md).
2. Review [Project Standards](PROJECT-STANDARDS.md).
3. Search existing issues and pull requests.
4. Open an issue before proposing a new project or a major architectural change.
5. Never submit credentials, private logs, customer data, proprietary code, or copyrighted course material.

## Contribution types

Contributions may include:

- Corrections to commands, code, diagrams, or explanations
- Cross-platform setup improvements
- Tests and validation scripts
- Safer examples and stronger security controls
- New failure scenarios and recovery procedures
- Accessibility and documentation improvements
- Dependency and compatibility updates
- Complete project proposals that meet repository standards

## Local workflow

```bash
git clone https://github.com/YOUR-USERNAME/AI-Powered-DevOps-Projects.git
cd AI-Powered-DevOps-Projects
git checkout -b type/short-description
```

Use a descriptive branch prefix such as `docs/`, `fix/`, `feature/`, `security/`, or `project/`.

Run every project-specific test and validation command before opening a pull request. Include the commands and results in the pull request description.

## Pull request requirements

A pull request must:

- Address one clear problem
- Explain why the change is needed
- Describe what changed
- Include verification evidence
- Update tests and documentation when behavior changes
- Preserve safe defaults
- Avoid unrelated formatting or file changes
- Pass repository checks

Project code must include expected behavior, failure behavior, cleanup instructions, and a method for confirming that cleanup succeeded.

## AI-assisted contributions

AI tools may assist with research, drafting, and implementation, but contributors remain responsible for every submitted line. Verify generated commands, dependencies, citations, licenses, security assumptions, and test results. Do not submit fabricated output or claim that unexecuted code was tested.

## Commit messages

Use clear, focused messages:

```text
fix(project-001): handle malformed workflow logs

docs(project-031): clarify local cluster prerequisites

test(project-051): add unreachable dependency case
```

## Reviews

Maintainers may request changes for correctness, scope, safety, maintainability, or teaching quality. Approval does not transfer responsibility for third-party licenses or sensitive information to the repository.

