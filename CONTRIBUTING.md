# Contributing to AI-Powered DevOps Projects

Thank you for helping build practical AI systems for production engineering.

## Before Contributing

Read:

- [Project Standards](PROJECT-STANDARDS.md)
- [AI Safety Standards](docs/ai-safety-standards.md)
- [Architecture Standards](docs/architecture-standards.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)

Do not open a pull request containing production logs, customer information, credentials or copied proprietary material.

## Ways to Contribute

- Propose a project that fills a catalogue gap.
- Improve an approved project.
- Add tests or failure scenarios.
- Correct technical documentation.
- Improve accessibility or onboarding.
- Report a security problem privately.
- Review reproducibility on a supported environment.

## Project Proposal Process

Open a project proposal issue before creating a numbered folder. Include:

1. Operational problem and affected engineering role.
2. Evidence that the problem occurs in real workflows.
3. Why AI is useful and what remains deterministic.
4. Expected inputs, outputs and integrations.
5. Threats, sensitive data and required approvals.
6. Offline or degraded behavior.
7. Test strategy and controlled failure scenarios.
8. Expected portfolio evidence.
9. Similar catalogue projects and how duplication is avoided.
10. Estimated scope and level.

A project number is assigned only after approval.

## Development Workflow

1. Fork the repository.
2. Create a focused branch.
3. Copy `projects/_template/` only for an approved project.
4. Make small, reviewable commits.
5. Run tests, formatting, link checks and security checks.
6. Update documentation with behavior changes.
7. Complete the pull request template.
8. Respond to review without removing required safeguards.

Suggested branch names:

```text
project/012-short-name
fix/012-parser-timeout
docs/architecture-guidance
```

## Pull Request Requirements

A project contribution must provide:

- reproducible setup and cleanup;
- no committed secrets;
- safe synthetic fixtures;
- tests for normal, failure and misuse paths;
- deterministic baseline or validation logic;
- AI boundary, prompt and output controls;
- architecture and data-flow documentation;
- operational signals and cost limits;
- supported environments and known limitations;
- evidence that all required checks pass.

Maintainers may request scope reduction when a contribution attempts to become a separate course.

## Commit Guidance

Use concise messages:

```text
feat(project-012): add bounded deployment evidence collector
test(project-012): cover malformed model response
docs(project-012): record external model boundary
fix(project-012): reject unsafe artifact path
```

## Review Principles

Reviews prioritize correctness, operational realism, reproducibility, safety and maintainability. Large amounts of generated content do not substitute for working code or evidence.

By contributing, you confirm that you have the right to submit the contribution and agree to the contribution terms in [LICENSE](LICENSE). You retain copyright in your original contribution while granting the repository owner the rights needed to use, adapt and maintain it as part of this repository.
