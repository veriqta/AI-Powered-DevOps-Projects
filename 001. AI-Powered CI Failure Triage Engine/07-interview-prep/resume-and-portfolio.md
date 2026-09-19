# Resume and Portfolio Guidance

## Resume pattern

Use an action, system, engineering constraint, and verified result:

> Built a read-only GitHub Actions failure-triage CLI that redacts CI logs, classifies evidence with deterministic rules, validates optional AI explanations, and produces auditable JSON incident reports; verified with automated tests and controlled failure scenarios.

Add numbers only after measuring them. Useful measures include fixture coverage, test count, median local triage time, model validation rejection cases, and unknown-class rate on an authorized dataset.

## Portfolio page

Include:

- the operational problem and intended users;
- a compact architecture diagram;
- a sanitized demonstration;
- one deterministic report and one safe-degradation example;
- test and CI evidence;
- threat boundaries and least-privilege choices;
- limitations and a realistic production roadmap.

## Avoid

- publishing proprietary logs or repository identifiers;
- claiming an LLM “finds the root cause” when evidence is incomplete;
- presenting generated sample results as production impact;
- listing tools without explaining the engineering decisions;
- claiming automatic remediation, multi-provider support, or accuracy that was not implemented and measured.

