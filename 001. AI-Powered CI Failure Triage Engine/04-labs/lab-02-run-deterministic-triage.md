# Lab 02: Run Deterministic Triage

## Objective

Generate repeatable reports without GitHub credentials or a model endpoint.

## Steps

1. Activate `.venv`.
2. Generate reports for every fixture:

   ```bash
   ./scripts/run-sample.sh
   ```

3. List the results:

   ```bash
   ls -1 output/*-report.json
   ```

4. Inspect each report and record its category, confidence, matched rule, evidence references, next checks, and limitations.
5. Confirm the expected mapping in [Expected Results](../walkthrough/expected-results.md).
6. Run one text report directly:

   ```bash
   ci-failure-triage --input sample-data/test-failure.json
   ```

7. Run the same fixture twice and confirm the classification and evidence references remain stable. Ignore the generated audit timestamp when comparing reports.

## Validation

Expected classes are `test_failure`, `dependency_failure`, `runner_infrastructure`, `permission_or_secret`, and `unknown`.

## Deliverable

Five generated reports and a short comparison table. Generated reports may stay ignored locally. Publish only sanitized evidence selected for the learner portfolio.

## Completion gate

- [ ] Every fixture produced a valid report.
- [ ] Results match the documented classes.
- [ ] The unknown fixture remains `unknown`.
- [ ] No external service was contacted.

