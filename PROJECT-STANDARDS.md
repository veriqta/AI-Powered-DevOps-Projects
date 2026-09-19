# Project Standards

Every numbered project must meet these standards before it is marked Ready.

## 1. Operational Relevance

The README must identify a real DevOps, SRE, platform, cloud, DevSecOps or FinOps problem, the engineer who encounters it and the operational decision the project supports.

## 2. Justified AI Use

State:

- what the model does;
- why deterministic logic alone is insufficient;
- what remains deterministic;
- what happens when AI is disabled, unavailable or wrong.

A chatbot interface is not enough.

## 3. Bounded Scope

A project is one coherent system, not a complete discipline. The required path should normally take 12–30 focused hours. Advanced extensions must be optional.

## 4. Working Implementation

Provide runnable code, setup, configuration examples, safe fixtures, expected output and cleanup. Placeholder implementations cannot be marked Ready.

## 5. Production Architecture

Document components, data flows, trust boundaries, dependencies, failure behavior and operational ownership. See [Architecture Standards](docs/architecture-standards.md).

## 6. Safety and Data Handling

Follow [AI Safety Standards](docs/ai-safety-standards.md). Use synthetic data by default, least privilege, bounded inputs, structured validation and human approval for high-impact actions.

## 7. Testing

Required coverage includes:

- unit tests for core logic;
- integration tests across important boundaries;
- malformed and oversized input;
- timeout and dependency failure;
- unsafe or injected content;
- model-disabled behavior;
- schema and evidence validation;
- cleanup and repeatability.

## 8. CI and Security Checks

The project must automate relevant formatting, tests, dependency review, secret scanning and artifact checks. Workflows must use least privilege and pinned actions where practical.

## 9. Observability and Cost

Document useful logs, metrics, traces or audit events. Bound model requests, retries, tokens and cost. Avoid logging sensitive prompts and model content.

## 10. Failure Exercises

Include controlled failures with expected signals, investigation steps, evidence and recovery. Learners must explain why the failure occurred, not only copy a fix.

## 11. Documentation

Each project must include:

- public README;
- prerequisites;
- architecture;
- setup and cleanup;
- usage;
- tests;
- security and data notes;
- failure exercises;
- limitations;
- portfolio evidence checklist.

## 12. Completion Gate

A project is complete when:

- a fresh clone can follow setup successfully;
- tests pass without hidden services;
- AI failure does not create unsafe behavior;
- no real secrets or sensitive data are present;
- expected outputs match the documentation;
- architecture and operational evidence are reviewable;
- cleanup removes only project-created resources.

