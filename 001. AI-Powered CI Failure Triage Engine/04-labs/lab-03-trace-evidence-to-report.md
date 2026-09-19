# Lab 03: Trace Evidence to Report

## Objective

Prove how raw CI evidence becomes a bounded, redacted, evidence-linked finding.

## Steps

1. Open `sample-data/permission-failure.json`.
2. Run:

   ```bash
   ci-failure-triage \
     --input sample-data/permission-failure.json \
     --format json \
     --output output/permission-trace.json
   ```

3. Locate the source log line that triggered the classification.
4. Follow the processing path through:
   - `src/ci_triage/parser.py`
   - `src/ci_triage/redaction.py`
   - `src/ci_triage/classifier.py`
   - `src/ci_triage/report.py`
5. Match the source line to its `E-###` evidence ID.
6. Match that ID to `finding.evidence_refs`.
7. Explain the file-size, evidence-count, and evidence-length limits.
8. Add a synthetic token to a temporary copy of the fixture. Confirm that the report contains a redaction marker instead of the token.
9. Delete the temporary fixture and report.

## Deliverable

A one-page evidence trace showing source field, normalization, redaction, rule match, evidence ID, and report field.

## Completion gate

- [ ] The triggering input can be traced to the finding.
- [ ] The synthetic token does not appear in output.
- [ ] Input bounds can be explained.
- [ ] No real credential was used.

