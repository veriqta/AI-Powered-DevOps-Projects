# Expected Results

Exact timestamps and file paths may differ. The classifications below should not.

| Fixture | Expected classification | Expected signal |
|---|---|---|
| `test-failure.json` | `test_failure` | assertion or test-suite failure |
| `dependency-failure.json` | `dependency_failure` | package resolution or installation failure |
| `runner-failure.json` | `runner_infrastructure` | runner or hosted-agent disruption |
| `permission-failure.json` | `permission_or_secret` | authorization, token, or secret access failure |
| `unknown-failure.json` | `unknown` | insufficient evidence for a supported class |

A successful terminal run resembles:

```text
CI FAILURE TRIAGE REPORT
Run: Pull request checks (1001)
Conclusion: failure
Primary class: test_failure
Confidence: 0.93
```

The JSON report should contain:

- run identity and source metadata;
- a deterministic classification and confidence;
- redacted, numbered evidence;
- recommended human investigation steps;
- limitations and audit metadata;
- an optional validated AI explanation only when requested and available.

When `--output` is supplied, successful execution writes the report without printing it. The program should exit with status `0` for a valid report and status `2` for invalid input or unrecoverable acquisition errors. A CI failure classification is data, not a failure of the triage command itself.
