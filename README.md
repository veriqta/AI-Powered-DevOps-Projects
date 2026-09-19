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

## The 50 Projects

### CI/CD and Software Delivery

| ID | Project | Level | What You Will Build |
|---:|---|---|---|
| 001 | AI-Powered CI Failure Triage Engine | Foundation | A system that collects failed job evidence, identifies likely failure classes, separates code failures from environment failures and produces an evidence-linked triage report. |
| 002 | Flaky Test Intelligence and Quarantine Advisor | Intermediate | A test-history analyzer that detects intermittent failures, measures flakiness, identifies shared failure patterns and recommends review candidates without automatically hiding tests. |
| 003 | Deployment Change Risk Scorer | Intermediate | A pre-deployment service that combines change size, affected services, ownership, test results, dependency criticality and deployment history to produce a reviewable risk assessment. |
| 004 | Pipeline Bottleneck and Queue-Time Investigator | Intermediate | A pipeline analytics system that explains slow builds, runner contention, repeated work, cache misses and queue delays using CI telemetry and historical baselines. |
| 005 | Release Readiness Evidence Synthesizer | Advanced | A release review system that gathers tests, security checks, approvals, unresolved incidents, change records and service health into one evidence-backed release recommendation. |
| 006 | Progressive Delivery Canary Analysis Controller | Advanced | A canary-analysis service that compares baseline and candidate telemetry, explains regressions and recommends continue, pause or rollback while keeping the deployment controller authoritative. |
| 007 | Rollback Decision Support Workbench | Advanced | An incident-time decision tool that correlates deployment changes, service health, dependencies and rollback constraints to prepare a safe rollback recommendation for human approval. |
| 008 | Cross-Repository Release Dependency Risk Mapper | Senior Capstone | A system that maps release dependencies across repositories, services, packages and environments, then identifies incompatible versions and coordinated-release risks. |

### Kubernetes and Container Operations

| ID | Project | Level | What You Will Build |
|---:|---|---|---|
| 009 | Kubernetes CrashLoopBackOff Evidence Investigator | Foundation | A diagnostic workbench that collects pod state, events, logs, probes, configuration and recent changes to explain why a workload repeatedly crashes. |
| 010 | Pod Scheduling Failure Reasoning Engine | Foundation | A scheduler-evidence analyzer for resource pressure, affinity, taints, topology, quotas, storage and policy failures, with every conclusion tied to cluster facts. |
| 011 | Kubernetes Resource Right-Sizing Recommender | Intermediate | A recommendation system that evaluates requests, limits, utilization, throttling, restarts and workload patterns before proposing safer resource settings. |
| 012 | Helm Upgrade Failure Diagnostic Workbench | Intermediate | A release investigation tool that compares chart values, rendered manifests, hooks, Kubernetes events and release history to isolate failed upgrade conditions. |
| 013 | Kubernetes Configuration Drift and Intent Analyzer | Intermediate | A system that compares declared manifests, Git state and live cluster resources, explains meaningful drift and separates approved mutations from unexpected changes. |
| 014 | Cluster Event Correlation and Incident Timeline Builder | Advanced | A multi-source timeline engine that connects Kubernetes events, audit records, controller activity, deployments and workload symptoms during an incident. |
| 015 | Workload Autoscaling Behavior Analyst | Advanced | An HPA and VPA investigation system that explains delayed scaling, unstable recommendations, metric gaps, oscillation and capacity constraints. |
| 016 | Multi-Cluster Upgrade Risk and Compatibility Assessor | Senior Capstone | A fleet-level service that evaluates API removals, add-ons, policies, workloads, node versions and operational dependencies before a Kubernetes upgrade. |

### Cloud Infrastructure and Infrastructure as Code

| ID | Project | Level | What You Will Build |
|---:|---|---|---|
| 017 | Terraform Plan Change Explainer and Risk Gate | Foundation | A pull-request service that translates Terraform plans into affected resources, destructive changes, dependency impact and evidence-based review questions. |
| 018 | Infrastructure Drift Root-Cause Investigator | Intermediate | A drift investigation system that compares declared state, stored state, cloud inventory, audit activity and deployment history to identify likely causes. |
| 019 | Cloud IAM Least-Privilege Recommendation Reviewer | Intermediate | An access-review tool that analyzes granted permissions and observed use, proposes narrower policies and requires deterministic validation before approval. |
| 020 | Cloud Network Reachability Misconfiguration Investigator | Intermediate | A network evidence system that examines routes, security rules, load balancers, DNS and service configuration to explain failed or unintended connectivity. |
| 021 | Infrastructure-as-Code Policy Exception Analyzer | Advanced | A policy workflow that evaluates exception requests against resource context, ownership, exposure, compensating controls and expiry requirements. |
| 022 | Cloud Migration Dependency Discovery Engine | Advanced | A discovery system that converts inventory, telemetry, configuration and network evidence into an application dependency map and migration-wave recommendations. |
| 023 | Disaster Recovery Configuration Readiness Assessor | Advanced | A readiness service that checks backup, replication, failover, identity, DNS and recovery evidence against declared recovery objectives. |
| 024 | Multi-Cloud Configuration Consistency Auditor | Senior Capstone | A cross-cloud control system that maps equivalent services, detects policy and configuration gaps and explains where platform standards diverge. |

### Observability and Incident Response

| ID | Project | Level | What You Will Build |
|---:|---|---|---|
| 025 | Alert Noise Reduction and Incident Grouping System | Foundation | An alert-processing service that groups related notifications using topology, timing and labels while preserving routing rules and critical-alert safeguards. |
| 026 | SLO Breach Evidence Investigator | Intermediate | A system that traces an SLO breach through service-level indicators, deployments, dependencies and saturation signals to produce testable hypotheses. |
| 027 | Distributed Trace Anomaly Investigator | Intermediate | A trace-analysis tool that finds abnormal paths, slow spans, retry storms and dependency changes, then explains them with direct trace references. |
| 028 | Metric-to-Change Correlation Engine | Intermediate | A change-intelligence service that compares metric anomalies with deployments, feature flags, configuration updates and infrastructure events. |
| 029 | Production Incident Timeline Reconstruction System | Advanced | An evidence-preserving incident tool that merges logs, alerts, traces, tickets, chat exports and change events into a sourced chronological timeline. |
| 030 | Runbook Retrieval and Step Validation Assistant | Advanced | A retrieval system that selects relevant runbook sections, checks prerequisites and warns when instructions do not match the current environment. |
| 031 | Post-Incident Action Item Quality Reviewer | Advanced | A review service that checks whether corrective actions address contributing conditions, have owners, contain verification and avoid vague commitments. |
| 032 | On-Call Handoff and Operational Context Generator | Senior Capstone | A shift-handoff system that summarizes active incidents, recent changes, degraded services, expiring mitigations and unresolved risks from verified operational sources. |

### Platform Engineering and Developer Experience

| ID | Project | Level | What You Will Build |
|---:|---|---|---|
| 033 | Service Onboarding Readiness Reviewer | Foundation | A review tool that checks a new service for ownership, deployment, observability, security, reliability, support and documentation requirements. |
| 034 | Golden Path Configuration Generator and Policy Validator | Intermediate | A platform service that generates an initial service configuration from approved templates and validates every result against platform policies. |
| 035 | Developer Self-Service Request Risk Classifier | Intermediate | A request workflow that classifies infrastructure and access requests, identifies required approvals and routes unusual cases for human review. |
| 036 | Internal Developer Portal Content Quality Auditor | Intermediate | A documentation analyzer that detects stale ownership, broken instructions, missing operational context and inconsistent service metadata. |
| 037 | Platform API Usage and Friction Analyzer | Advanced | A product-analytics system that combines API errors, latency, support requests and workflow telemetry to identify platform adoption barriers. |
| 038 | Engineering Standards Compliance Evidence Collector | Senior Capstone | A platform-level service that gathers proof of testing, ownership, observability, security and lifecycle compliance without relying on self-attestation alone. |

### SRE, Reliability and Capacity

| ID | Project | Level | What You Will Build |
|---:|---|---|---|
| 039 | Error Budget Burn Forecast and Decision Advisor | Intermediate | A forecasting tool that projects budget consumption, explains uncertainty and supports release or reliability decisions without replacing SLO policy. |
| 040 | Capacity Saturation Forecasting Workbench | Intermediate | A capacity-planning system that models demand, headroom, seasonality and failure capacity, then compares scale-up and scale-out scenarios. |
| 041 | Dependency Reliability Risk Mapper | Advanced | A service graph that combines dependency criticality, historical failures, ownership and fallback behavior to expose concentrated reliability risk. |
| 042 | Toil Discovery and Automation Prioritization Engine | Advanced | An engineering-work analyzer that identifies repetitive operational tasks and ranks automation candidates by effort, frequency, risk and expected value. |
| 043 | Resilience Experiment Design and Safety Reviewer | Senior Capstone | A system that turns reliability hypotheses into bounded experiments with blast-radius limits, abort conditions, required approvals and measurable outcomes. |

### DevSecOps and Software Supply Chain

| ID | Project | Level | What You Will Build |
|---:|---|---|---|
| 044 | Vulnerability Exploitability and Remediation Prioritizer | Intermediate | A prioritization system that combines scanner findings, runtime exposure, package reachability, asset importance and available fixes without replacing the scanner. |
| 045 | Software Supply Chain Provenance Anomaly Investigator | Advanced | A provenance-analysis service that detects unexpected builders, dependencies, signatures, artifact origins and release-path changes. |
| 046 | Secrets Exposure Triage and Rotation Planner | Advanced | A response tool that classifies an exposed credential, maps affected systems, prepares containment and rotation steps and tracks verification evidence. |
| 047 | Container Image Risk Change Analyzer | Senior Capstone | A release gate that compares image versions, vulnerabilities, packages, provenance, configuration and runtime relevance to explain whether risk increased. |

### FinOps and Sustainable Operations

| ID | Project | Level | What You Will Build |
|---:|---|---|---|
| 048 | Cloud Cost Anomaly Root-Cause Investigator | Intermediate | A cost investigation system that correlates billing changes with deployments, scaling, pricing, resource creation and ownership evidence. |
| 049 | Idle Resource Waste Detection and Action Planner | Advanced | A waste-analysis service that combines utilization, schedules, dependencies and ownership to recommend safe rightsizing, scheduling or retirement actions. |
| 050 | Workload Cost-Performance Scenario Advisor | Senior Capstone | A decision workbench that compares architecture, capacity, reliability and pricing scenarios while showing cost, performance and operational trade-offs. |

Project release details and implementation status are maintained in the [Project Catalogue](PROJECT-CATALOG.md).

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
        ↓
Build the deterministic baseline
        ↓
Add the bounded AI capability
        ↓
Validate normal and unsafe outputs
        ↓
Introduce controlled failures
        ↓
Observe, troubleshoot and recover
        ↓
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

## Repository Structure

```text
ai-powered-devops-projects/
├── README.md
├── PROJECT-CATALOG.md
├── PROJECT-STANDARDS.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
├── docs/
├── projects/
├── shared/
└── .github/
```

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

Copyright © 2026 Ann, operating under the VERIQTA name. All rights reserved.

The repository may be used for personal, non-commercial learning under the terms in [LICENSE](LICENSE). Learners may publish their own original implementations with the required attribution. Republishing the supplied guides, solutions, assessments or substantial repository content requires written permission.

## Maintained by VERIQTA

VERIQTA creates practical engineering resources for DevOps, SRE, platform, cloud and production engineering.

Website: [veriqta.com](https://veriqta.com)

GitHub: [VERIQTA](https://github.com/veriqta)
