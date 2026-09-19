# Runtime Problems

## The input file is rejected

Validate its syntax and required structure:

```bash
python -m json.tool path/to/input.json
```

The input must describe a run and contain a `jobs` list. Start with a supplied fixture when diagnosing a custom exporter.

## GitHub returns `401 Unauthorized`

The token is missing, expired, malformed, or revoked. Confirm that `GITHUB_TOKEN` is present without printing it:

```bash
test -n "${GITHUB_TOKEN:-}" && echo configured || echo missing
```

Create a replacement with the minimum read-only access and revoke the old token if exposure is suspected.

## GitHub returns `403 Forbidden`

Check repository access, Actions read permission, organization SSO authorization, and API rate limits. A token that can read public metadata may still be unable to download private run logs.

## GitHub returns `404 Not Found`

Verify `OWNER/REPOSITORY`, the run ID, and token access. GitHub may return 404 when a private resource is not visible to the caller.

## Logs cannot be downloaded or opened

Logs may have expired, been deleted, or be unavailable while a run is active. Confirm the run in GitHub, try a completed failed run, and use the local fixture workflow if live acquisition is temporarily unavailable.

## The classification is `unknown`

This is not automatically an error. Inspect the evidence retained in the report. If a recurring failure has stable, distinctive signals, add a narrowly scoped deterministic rule and tests. Do not force a class from weak evidence.

## A secret appears unredacted

Stop. Do not publish or submit the report to a model. Delete generated copies, rotate the exposed credential when applicable, add a redaction regression test, and rerun only with synthetic input until the test passes.

## AI explanation is unavailable

The deterministic report remains valid. Check endpoint approval, `AI_BASE_URL`, model name, API key, timeout, and response shape. Do not weaken schema or evidence validation to accept malformed output.

## AI output references nonexistent evidence

The validator should reject it and record a limitation. Keep the deterministic result, preserve the sanitized response only when policy permits, and investigate the prompt or endpoint behavior.

