# Scenario 01: Permission Failure

## Objective

Differentiate invalid authentication, insufficient authorization, hidden private resources, and rate limiting without increasing permissions blindly.

## Exercise

1. Run `sample-data/permission-failure.json` locally and inspect the rule evidence.
2. In an authorized test repository, attempt live acquisition with no token and capture the sanitized failure.
3. Configure a read-only token with Actions access and retry.
4. Explain why write access is unnecessary.

## Success criteria

- Local evidence is classified `permission_or_secret`.
- No token is printed or committed.
- The final permission set is documented and read-only.
- The recovery notes distinguish 401, 403, and 404 behavior.

