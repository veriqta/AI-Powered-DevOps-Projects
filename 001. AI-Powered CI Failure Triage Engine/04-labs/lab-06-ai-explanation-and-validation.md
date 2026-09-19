# Lab 06: AI Explanation and Validation

## Objective

Test the optional model boundary without allowing model output to control classification or execution.

## Required local path

1. Read `src/ci_triage/ai_client.py` and `tests/test_ai_validation.py`.
2. Run:

   ```bash
   python -m unittest tests.test_ai_validation -v
   ```

3. Add validation cases for invalid priority, missing keys, and an empty evidence list.
4. Complete [Prompt Injection](../failure-scenarios/scenario-03-prompt-injection.md).
5. Complete [Malformed Model Response](../failure-scenarios/scenario-04-malformed-model-response.md).
6. Confirm that rejected output cannot change the deterministic category.

## Optional approved-endpoint path

1. Configure `AI_API_KEY`, `AI_MODEL`, and `AI_BASE_URL` through the environment.
2. Use only a supplied synthetic fixture.
3. Run:

   ```bash
   ci-failure-triage \
     --input sample-data/dependency-failure.json \
     --enable-ai \
     --format json \
     --output output/dependency-ai-report.json
   ```

4. Compare the AI-enabled and deterministic reports.
5. Confirm that the category remains unchanged and every model evidence reference exists.
6. Record latency and usage information when the endpoint provides it.

## Deliverable

Validation test evidence and an AI-boundary assessment. Model access is not required for completion.

## Completion gate

- [ ] Log instructions are treated as untrusted data.
- [ ] Invalid model output is rejected.
- [ ] Deterministic triage survives model failure.
- [ ] No private log was transmitted.

