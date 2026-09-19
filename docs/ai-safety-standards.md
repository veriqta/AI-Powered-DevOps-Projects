# AI Safety Standards

These rules apply to every project using a model.

## Model Authority

Model output is an untrusted proposal, classification or explanation. Deterministic controls, policies, source evidence and authorized humans remain authoritative.

## Input Safety

- Accept only authorized inputs.
- Enforce file, record, request and context limits.
- Minimize data before model access.
- Redact or remove secrets and sensitive fields.
- Treat retrieved documents, logs, tickets and code comments as untrusted data.
- Preserve source references for important claims.

## Prompt-Injection Resistance

Projects must not obey instructions found in untrusted operational data. Separate trusted instructions from evidence, restrict tools, validate requested actions and test injection fixtures.

## Output Validation

- Prefer a strict schema.
- Reject unexpected fields and invalid values.
- Verify evidence references.
- Bound length and resource use.
- Prevent output from becoming a shell command, policy decision or deployment action without independent validation and approval.

## Actions and Approval

High-impact actions require explicit human approval. Examples include deployment, rollback, credential change, resource deletion, network change and access modification.

Projects must define allowed actions, prohibited actions, approval identity, audit evidence and recovery.

## Resilience

Provide safe behavior for:

- timeout;
- unavailable endpoint;
- malformed response;
- rate limit;
- excessive cost;
- partial context;
- unsupported conclusion.

A project should retain deterministic output or fail closed.

## Provider and Model Documentation

Record provider assumptions, model identifier, data retention, training use, region, authentication, rate limits and cost controls. Never require learners to send real organizational data.

## Evaluation

Test correctness, unsupported claims, injection resistance, sensitive-data handling, malformed output and model-disabled behavior. Record limitations. A successful demonstration is not proof of general reliability.

