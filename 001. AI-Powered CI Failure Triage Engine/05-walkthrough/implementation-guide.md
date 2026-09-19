# Implementation Guide

## 1. Enter the project

From the repository root:

```bash
cd projects/001-ai-powered-ci-failure-triage-engine
```

All remaining commands assume this directory is the current working directory.

## 2. Verify the workstation

```bash
./scripts/verify-environment.sh
```

Resolve every reported failure before continuing. Python 3.11 or newer and Git are required. Docker and a GitHub token are not required for the local workflow.

## 3. Create the isolated environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

On Windows PowerShell with a native Python installation, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

Confirm that the command is installed:

```bash
ci-failure-triage --help
```

## 4. Validate the supplied evidence

```bash
./scripts/validate-samples.sh
```

The script validates every JSON fixture without sending data to an external service.

## 5. Triage the first failed run

```bash
ci-failure-triage \
  --input sample-data/test-failure.json \
  --output output/test-failure-report.json
```

Inspect the terminal summary, then open the JSON report. Confirm that:

- the classification is `test_failure`;
- evidence references point to supplied job-log lines;
- sensitive values are redacted;
- the report states that the result came from deterministic rules;
- AI analysis is absent.

## 6. Compare distinct failure classes

```bash
./scripts/run-sample.sh
```

Then examine the generated reports:

```bash
ls -la output
```

Compare the evidence and recommended next action for dependency, runner, permission, and unknown failures. An unknown classification is a safe result when the evidence does not support a stronger conclusion.

## 7. Run the automated tests

```bash
python -m unittest discover -s tests -v
```

The suite covers parsing, classification, redaction, AI-response validation, and command-line behavior.

## 8. Use a live GitHub Actions run

This step is optional. Create a fine-grained token with read-only access to Actions metadata and logs for the intended repository. Do not use an administrator token.

```bash
cp .env.example .env
```

Set `GITHUB_TOKEN` in the current shell or load it with an approved secret-management method. Do not commit `.env`.

```bash
export GITHUB_TOKEN="your-read-only-token"
ci-failure-triage \
  --repository OWNER/REPOSITORY \
  --run-id RUN_ID \
  --output output/live-run-report.json
```

The application performs read-only requests. It does not rerun jobs, modify workflows, create issues, or change repository content.

## 9. Enable the optional AI explanation

Do this only after the deterministic workflow and redaction tests pass. Configure an approved OpenAI-compatible endpoint:

```bash
export AI_API_KEY="your-api-key"
export AI_MODEL="approved-model-name"
export AI_BASE_URL="https://approved-endpoint.example/v1"
```

Run against synthetic data first:

```bash
ci-failure-triage \
  --input sample-data/dependency-failure.json \
  --enable-ai \
  --output output/dependency-ai-report.json
```

The model receives redacted evidence and the deterministic result. Its explanation cannot replace the classification, add nonexistent evidence references, or execute an action.

## 10. Exercise safe degradation

Run the unknown fixture:

```bash
ci-failure-triage \
  --input sample-data/unknown-failure.json \
  --output output/unknown-report.json
```

Then run the relevant failure exercises in `failure-scenarios/`. Record observations, evidence, and recovery steps in the learner project journal described by the Project Guide.

## 11. Produce final evidence

```bash
make verify
make sample
```

Preserve the following in a personal portfolio repository:

- passing test output;
- one report from each deterministic class exercised;
- one sanitized live-run report, if authorized;
- an architecture explanation;
- security and AI-safety decisions;
- a limitation discovered during testing;
- a short demonstration or annotated screenshots.

Do not publish tokens, private repository names, proprietary logs, personal data, or unredacted output.
