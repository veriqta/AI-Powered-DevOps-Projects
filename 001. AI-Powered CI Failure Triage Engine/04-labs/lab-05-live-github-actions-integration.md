# Lab 05: Live GitHub Actions Integration

## Objective

Collect one authorized GitHub Actions failure using read-only access.

## Path A: Authorized live repository

1. Select a failed run in a repository the learner may access.
2. Record its `OWNER/REPOSITORY` and numeric run ID.
3. For a private repository, create a fine-grained token limited to that repository with Actions read access. Do not grant write or administration access.
4. Export the token through the current shell or an approved secret manager:

   ```bash
   export GITHUB_TOKEN="read-only-token"
   ```

5. Run:

   ```bash
   ./scripts/run-live-github.sh OWNER/REPOSITORY RUN_ID
   ```

6. Generate JSON with the CLI if a reviewable local report is required.
7. Confirm that the client made read requests only.
8. Sanitize repository names, URLs, commit identifiers, usernames, and logs before preserving evidence.
9. Unset the shell variable:

   ```bash
   unset GITHUB_TOKEN
   ```

## Path B: No authorized repository or token

1. Inspect `src/ci_triage/github_client.py`.
2. List the metadata, jobs, and log endpoints used.
3. Review `tests` and add mocked client tests for a successful response and one HTTP error.
4. Use the supplied fixtures to complete the normalization and reporting portion.
5. Document why local simulation is safer than using an unauthorized token.

## Deliverable

A sanitized acquisition record or mocked integration-test record, plus the minimum-permission explanation.

## Completion gate

- [ ] Only authorized or synthetic data was used.
- [ ] Access remained read-only.
- [ ] No token appears in files, output, screenshots, or Git history.
- [ ] Acquisition failure does not prevent local analysis.

