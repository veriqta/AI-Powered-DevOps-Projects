# Scenario 02: Unknown Classification

Run the unknown fixture and resist the temptation to label it without evidence.

```bash
ci-failure-triage --input sample-data/unknown-failure.json --output output/unknown.json
```

Document what additional evidence would be required, propose a rule only if a stable signal exists, and describe the harm of a confident but unsupported class. Success means preserving `unknown` until evidence justifies a change.

