# Lab 04: Add a Deterministic Rule

## Objective

Extend the classifier without creating broad false positives.

## Task

Add a synthetic cache or artifact failure case. Use evidence such as an artifact upload failure or a missing cache archive. Do not use a vague word such as `failed` as the only signal.

## Steps

1. Read `src/ci_triage/classifier.py` and `tests/test_classifier.py`.
2. Create a safe fixture named `sample-data/cache-artifact-failure.json` in the learner repository.
3. Run it before changing the classifier and record the baseline result.
4. Add the narrowest rule required for `cache_or_artifact`.
5. Add a positive unit test using the new signal.
6. Add a negative test where the same general words appear but the failure has another cause.
7. Decide where the rule belongs in precedence and document why.
8. Run:

   ```bash
   python -m unittest discover -s tests -v
   ci-failure-triage --input sample-data/cache-artifact-failure.json
   ```

9. Review all earlier fixture classifications for regressions.

## Deliverable

The fixture, rule, positive test, negative test, and a short rule-decision note.

## Completion gate

- [ ] The new fixture is classified correctly.
- [ ] The negative case does not match incorrectly.
- [ ] All existing tests still pass.
- [ ] Rule precedence is justified with evidence.

