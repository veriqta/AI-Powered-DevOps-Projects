# System Configuration

## 1. Clone and Enter the Repository

```bash
git clone https://github.com/veriqta/ai-powered-devops-projects.git
cd ai-powered-devops-projects/projects/001-ai-powered-ci-failure-triage-engine
```

If you forked the repository, clone your fork URL instead.

## 2. Create a Branch

```bash
git switch -c project-001-ci-failure-triage
```

## 3. Verify Tools

```bash
python3 --version
git --version
```

Python must be 3.11 or newer.

## 4. Create the Virtual Environment

Linux, macOS or WSL:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 5. Install the Project

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

## 6. Run Local Verification

```bash
chmod +x scripts/*.sh
./scripts/verify-environment.sh
./scripts/validate-samples.sh
python -m unittest discover -s tests -v
ci-failure-triage --input sample-data/test-failure.json
```

## 7. Optional GitHub Configuration

Create a fine-grained token only if you need private repository access. Grant the smallest appropriate repository access and **Actions: read**. Store it only in the current shell or an ignored local secret manager.

```bash
export GITHUB_TOKEN="replace-with-your-token"
ci-failure-triage --repository OWNER/REPO --run-id RUN_ID
```

Public workflow data may be accessible without a token. API limits still apply.

## 8. Optional AI Configuration

Copy the example without adding real values to Git:

```bash
cp .env.example .env
```

Load values through your normal secret-management method:

```bash
export AI_API_KEY="replace-with-approved-key"
export AI_MODEL="approved-model-id"
export AI_BASE_URL="https://api.openai.com/v1"
ci-failure-triage --input sample-data/test-failure.json --enable-ai
```

Never commit `.env`. AI receives only selected, redacted evidence.

## 9. Cleanup

```bash
make clean
deactivate
```

