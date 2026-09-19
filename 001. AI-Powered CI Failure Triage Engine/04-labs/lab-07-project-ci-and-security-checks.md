# Lab 07: Project CI and Security Checks

## Objective

Run project verification automatically on proposed changes without production secrets.

## Steps

1. Inspect `.github/workflows/ci.yml`.
2. Explain the event triggers, path filters, Python matrix, working directory, and `contents: read` permission.
3. Push the learner branch and open a pull request.
4. Confirm that fixture validation, tests, and the local CLI exercise run.
5. Introduce a temporary failing assertion on the branch and observe the failed check.
6. Restore the correct assertion and confirm the check passes.
7. Verify that the workflow does not require `GITHUB_TOKEN` with elevated permission or an AI key.
8. Enable available secret scanning and dependency review controls where appropriate.
9. Preserve the passing check URL or a sanitized screenshot.

## Deliverable

A short CI control review and evidence of one intentional failure followed by a passing correction.

## Completion gate

- [ ] The workflow passes on supported Python versions.
- [ ] A broken test blocks the expected check.
- [ ] Workflow permissions remain read-only.
- [ ] Synthetic fixtures are used in CI.

