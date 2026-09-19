# Explaining the Project

## Thirty-second version

“I built a read-only CI failure triage engine for GitHub Actions. It collects a selected failed run or accepts local fixtures, redacts sensitive values, normalizes job logs, and applies evidence-backed deterministic rules. An optional model can explain the result, but strict validation prevents it from changing the class or inventing evidence. The system produces an auditable JSON report and degrades safely when GitHub or the model is unavailable.”

## Two-minute version

Structure the explanation around five decisions:

1. **Problem:** engineers lose time opening jobs and scanning repetitive CI output.
2. **Boundary:** the first release supports GitHub Actions and performs read-only triage, not remediation.
3. **Pipeline:** acquire, bound, redact, normalize, classify, optionally explain, validate, and report.
4. **Safety:** least-privilege tokens, untrusted-log handling, deterministic authority, evidence references, and graceful model failure.
5. **Evidence:** automated tests, synthetic failure fixtures, failure exercises, and observable limitations.

## Deep-dive prompts

Be prepared to draw the trust boundaries, explain rule precedence, show a report, trace one evidence ID to its input line, demonstrate a rejected AI response, and identify the next production control you would add.

Avoid claiming perfect root-cause detection. The system identifies a supported failure class from available evidence and recommends an investigation path.

