# AI-Powered DevOps Projects

Real-world projects for DevOps, SRE, platform, cloud and DevSecOps engineers who want to use AI in production engineering.

AI is becoming part of how engineering teams investigate failures, review changes, manage infrastructure, improve reliability and support developers. I created this repository to make that transition practical.

The collection contains 50 hands-on projects built around problems engineers encounter in real environments. These are not chatbot exercises or thin wrappers around a model API. Each project combines AI with automation, infrastructure, observability, security, testing and sound engineering judgment.

## What You Will Build

Projects in this repository cover work such as:

- investigating deployment and CI/CD failures;
- reviewing infrastructure changes and Terraform plans;
- analyzing Kubernetes incidents and workload behavior;
- correlating logs, metrics, traces and events;
- improving incident response and post-incident analysis;
- detecting configuration drift and operational risk;
- supporting platform engineering and developer self-service;
- prioritizing vulnerabilities and software supply-chain findings;
- forecasting capacity and identifying reliability risks;
- investigating cloud cost anomalies;
- validating AI output before it influences an operational decision.

Every project ends with a working system, tests, failure scenarios, architecture documentation and evidence that can be presented in a technical interview or engineering portfolio.

## Who This Repository Is For

This repository is designed for:

- DevOps engineers;
- site reliability engineers;
- platform engineers;
- cloud engineers;
- DevSecOps engineers;
- infrastructure engineers;
- software engineers moving into production engineering;
- technical learners building practical AI and operations experience.

The projects range from production foundations to senior-level capstones. Each project lists its own prerequisites, tools and expected completion time.

## What Makes a Project Production-Focused

A completed project must do more than return an AI-generated answer. It must show how the system behaves when inputs are incomplete, dependencies fail, model output is wrong or operational risk is high.

Every project includes:

- a real engineering problem;
- a defined operational user and outcome;
- a justified role for AI;
- deterministic rules, policies or validation;
- safe synthetic data;
- architecture and data-flow documentation;
- automated tests and CI checks;
- security and privacy controls;
- observability and cost considerations;
- model-disabled or degraded behavior;
- controlled failure exercises;
- cleanup instructions;
- portfolio evidence and known limitations.

The model may explain, classify, correlate, summarize or recommend. It does not become the source of truth, bypass engineering controls or receive unrestricted access to production systems.

## Project Areas

The 50 projects are organized across the main areas of modern production engineering.

| Project area | Focus |
|---|---|
| CI/CD and software delivery | Pipeline failures, deployment risk, release evidence and change analysis |
| Kubernetes and containers | Workload diagnosis, scheduling, scaling, configuration and cluster operations |
| Cloud infrastructure and IaC | Terraform, cloud configuration, drift, identity, networking and change review |
| Observability and incident response | Logs, metrics, traces, alerts, timelines and incident evidence |
| Platform engineering | Golden paths, service onboarding, developer experience and internal platforms |
| SRE and reliability | SLOs, error budgets, capacity, dependency risk and resilience |
| DevSecOps and supply chain | Vulnerabilities, secrets, policy evidence and software provenance |
| FinOps and sustainable operations | Cost anomalies, waste, forecasting and resource efficiency |

See the complete [Project Catalogue](PROJECT-CATALOG.md).

## How the Projects Progress

| Level | What to expect |
|---|---|
| Foundation | One focused workflow, local or simulated infrastructure, deterministic baseline and a bounded AI task |
| Intermediate | Multiple components, external interfaces, structured validation and controlled failures |
| Advanced | Cross-system evidence, policy boundaries, asynchronous workflows and production trade-offs |
| Senior Capstone | Platform-level problems, multi-team ownership, reliability objectives and architectural decisions |

Read [Project Levels](docs/project-levels.md) for the complete expectations.

## How Each Project Works

Projects follow the same engineering sequence:

```text
Understand the problem
        â†“
Build the deterministic baseline
        â†“
Add the bounded AI capability
        â†“
Validate normal and unsafe outputs
        â†“
Introduce controlled failures
        â†“
Observe, troubleshoot and recover
        â†“
Document the evidence and trade-offs
```

This approach keeps the work practical. Learners build early, test continuously and finish with something they can explain.

## Getting Started

1. Review the [Project Catalogue](PROJECT-CATALOG.md).
2. Choose a project that matches your role and current level.
3. Read the project prerequisites and architecture.
4. Fork or clone the repository.
5. Create a branch for your project work.
6. Follow the setup and implementation guide.
7. Run the tests and security checks.
8. Complete the failure exercises.
9. Document your results using the submission guidance.
10. Present the finished project in your own repository or portfolio.

Role-based routes are available in [Learning Paths](docs/learning-paths.md).


| Path | Contents |
|---|---|
| [projects/](projects/README.md) | Numbered project implementations |
| [docs/](docs/learning-paths.md) | Learning paths, project levels, architecture, safety and portfolio guidance |
| [shared/](shared/README.md) | Reusable templates, schemas, policies and approved fixtures |
| [PROJECT-STANDARDS.md](PROJECT-STANDARDS.md) | Requirements every project must satisfy |
| [ROADMAP.md](ROADMAP.md) | Repository development and release direction |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution process and review requirements |
| [SECURITY.md](SECURITY.md) | Security reporting and data-handling rules |

## Core Engineering Principles

### Evidence before conclusions

Operational evidence comes from systems, telemetry, configuration and validated outputs. AI-generated explanations remain hypotheses until the evidence supports them.

### Deterministic controls remain authoritative

Policies, schemas, tests, approval rules and safety limits do not become optional because a model is available.

### AI must fail safely

Projects must handle timeouts, malformed responses, rate limits, unavailable providers, prompt injection and unsupported claims.

### Production data stays protected

Use synthetic or explicitly authorized data. Do not commit credentials, customer information, production logs or private infrastructure details.

### Humans approve high-impact actions

Deployment, rollback, deletion, access changes and other consequential actions require clear authorization and review.

Read the complete [AI Safety Standards](docs/ai-safety-standards.md).

## Documenting Your Work

Learners are encouraged to create their own implementation repository and document:

- architecture decisions;
- setup and deployment;
- tests and CI results;
- normal and degraded outputs;
- failure investigations;
- security controls;
- cost and performance observations;
- limitations and future improvements.

Use the [Submission Guidelines](docs/submission-guidelines.md) and [Portfolio Guidance](docs/portfolio-guidance.md).

## Contributing

Contributions are welcome from engineers, reviewers, technical writers and learners.

Before contributing:

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Review the [Project Standards](PROJECT-STANDARDS.md).
3. Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
4. Do not include secrets, production data or proprietary material.
5. Open a project proposal before creating a new numbered project.

Useful contributions include tests, failure scenarios, documentation corrections, architecture improvements and reproducibility reviews.

## License

Copyright Â© 2026 Ann, operating under the VERIQTA name. All rights reserved.

The repository may be used for personal, non-commercial learning under the terms in [LICENSE](LICENSE). Learners may publish their own original implementations with the required attribution. Republishing the supplied guides, solutions, assessments or substantial repository content requires written permission.

## Maintained by VERIQTA

VERIQTA creates practical engineering resources for DevOps, SRE, platform, cloud and production engineering.

Website: [veriqta.com](https://veriqta.com)

GitHub: [VERIQTA](https://github.com/veriqta)

