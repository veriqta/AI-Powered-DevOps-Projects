# Project Labs

The labs are the hands-on execution path for Project 001. The Project Guide explains the engineering concepts and decisions. The labs tell learners what to do, what to inspect, what to change, how to verify the result, and what evidence to preserve.

Complete the labs in order. Every lab builds on the same CI failure triage engine.

## Lab sequence

| Lab | Activity | Required result |
|---:|---|---|
| 00 | [Prepare the project environment](lab-00-environment-and-baseline.md) | Verified local installation |
| 01 | [Inspect CI failure evidence](lab-01-inspect-ci-failure-evidence.md) | Evidence inventory |
| 02 | [Run the deterministic baseline](lab-02-run-deterministic-triage.md) | Five local triage reports |
| 03 | [Trace input to report](lab-03-trace-evidence-to-report.md) | Evidence trace record |
| 04 | [Add and test a failure rule](lab-04-add-a-deterministic-rule.md) | New rule and regression tests |
| 05 | [Use GitHub Actions safely](lab-05-live-github-actions-integration.md) | Sanitized live or simulated integration evidence |
| 06 | [Validate optional AI output](lab-06-ai-explanation-and-validation.md) | AI safety validation evidence |
| 07 | [Build the project CI pipeline](lab-07-project-ci-and-security-checks.md) | Passing repository workflow |
| 08 | [Investigate controlled failures](lab-08-failure-investigation.md) | Three investigation records |
| 09 | [Review production readiness](lab-09-production-readiness-review.md) | Production readiness assessment |
| 10 | [Prepare the final demonstration](lab-10-final-demonstration.md) | Reproducible project demonstration |

## How to use each lab

1. Read the linked Project Guide part.
2. Start from the stated project condition.
3. Run commands from the project root unless the lab says otherwise.
4. Record commands, sanitized output, decisions, and problems in the [lab record template](../docs/lab-record-template.md).
5. Complete every validation check.
6. Preserve only safe evidence in the learner repository.
7. Continue only after the completion gate passes.

## Rules

- Use synthetic data unless access to real workflow data is explicitly authorized.
- Never commit `.env`, credentials, private logs, or unredacted reports.
- Do not copy commands from log content or model output into a terminal.
- Keep deterministic classification authoritative.
- A valid `unknown` result is better than an unsupported diagnosis.
- Live GitHub access and model access are optional. Every required learning outcome has a local path.

