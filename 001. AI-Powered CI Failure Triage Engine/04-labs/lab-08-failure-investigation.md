# Lab 08: Failure Investigation

## Objective

Practice evidence-first troubleshooting and safe recovery.

## Steps

1. Select three exercises from `failure-scenarios/`.
2. Include at least one security scenario and one dependency or integration scenario.
3. For each exercise, record:
   - expected behavior;
   - observed symptom and exit code;
   - evidence collected before making a change;
   - hypothesis;
   - smallest diagnostic action;
   - recovery action;
   - verification result;
   - prevention or detection improvement.
4. Use the documents in `troubleshooting/` when blocked.
5. Run the full test suite after every code change.
6. Rehearse cleanup:

   ```bash
   ./scripts/cleanup.sh
   ```

## Deliverable

Three completed lab records containing sanitized evidence and verified recovery steps.

## Completion gate

- [ ] Three scenarios were completed.
- [ ] Evidence was collected before remediation.
- [ ] Recovery was verified, not assumed.
- [ ] At least one lasting control improvement was proposed.

