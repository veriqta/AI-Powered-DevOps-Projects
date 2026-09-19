# Part 01: Operational Problem and Context

## Problem

A failed CI run often requires an engineer to open several jobs, scan repeated logs, identify the first actionable signal, and communicate a concise diagnosis. The cost is interruption and delayed feedback, not merely log-reading time.

## Learning outcomes

- identify users and operational decisions;
- define success without promising perfect root-cause detection;
- separate triage from remediation;
- define measurable functional and safety requirements.

## Activities

1. Describe a realistic failed-pipeline response from notification to escalation.
2. Identify primary users: DevOps, platform, CI, and software engineers.
3. Define inputs, outputs, exclusions, and authorization assumptions.
4. Write success measures such as triage completion rate, latency, unknown rate, and evidence traceability.
5. Define failure costs: false diagnosis, data leakage, model cost, and unsafe action.

## Build task

Create `docs/problem-statement.md` in a learner repository containing the operational problem, personas, jobs to be done, scope, non-goals, and measurable acceptance criteria. Do not claim a target accuracy without an evaluation dataset.

## Expected result

The project is framed as decision support: it reduces the time required to reach a defensible first investigation step while keeping humans responsible for consequential action.

## Completion gate

- [ ] The user and operational decision are explicit.
- [ ] Triage and remediation are separated.
- [ ] Success and failure are measurable.
- [ ] Security, privacy, and cost are requirements.

Next: [Part 02](../part-02-architecture-and-data-design/README.md)

