# Submission Guidelines

A completed project should be understandable and reproducible without a private explanation from its author.

## Required Submission Evidence

- repository URL and project ID;
- completed project README;
- architecture and data-flow diagram;
- setup and cleanup record;
- test and CI results;
- example normal output;
- example degraded or failure output;
- security and data-handling explanation;
- model-disabled or deterministic fallback result;
- limitations and next improvements;
- short demonstration video or annotated screenshots.

## Learner Repository

You may document work in your own repository. Preserve the upstream project ID and link to the original project. State clearly which work is yours and which files came from the reference project.

Recommended structure:

```text
project-012-name/
├── README.md
├── src/
├── tests/
├── sample-data/
├── docs/
│   ├── architecture.md
│   ├── decisions/
│   ├── security.md
│   └── evidence.md
├── scripts/
├── .github/workflows/
└── LICENSE
```

## Evidence Quality

Evidence must be:

- produced by the submitted implementation;
- reproducible from documented commands;
- free from secrets and production data;
- connected to a requirement or decision;
- honest about failures and limitations.

Do not submit copied outputs, fabricated CI screenshots or unreviewed model claims.

## Final Review

Before submission, clone into a clean location, follow the README and run every required command. A reviewer should be able to reproduce the primary outcome and at least one failure scenario.

