# Technical Questions

## Why use deterministic rules before an LLM?

Rules provide repeatability, traceable evidence, offline operation, predictable cost, and a reliable fallback. The model explains bounded evidence; it is not the authority for classification.

## How is prompt injection handled?

Logs are treated as untrusted data, redacted before model use, clearly delimited in the prompt, bounded in size, and never granted tool execution. Model output is schema-validated and may reference only supplied evidence IDs.

## Why can the CLI return success when the CI run failed?

The failed CI state is the input being analyzed. Exit status `0` means triage completed and produced a valid report. Input, acquisition, or report-generation failures use a nonzero exit status.

## How are false positives controlled?

Rules use narrow signals and explicit precedence. Regression fixtures include positive and nearby negative cases. Weak evidence results in `unknown`, not an invented diagnosis.

## What makes live integration safe?

The token is read from the environment, scoped to a selected repository, and granted read-only Actions access. The client uses GET requests only and the application has no rerun, commit, issue, deployment, or remediation capability.

## How would this scale?

Separate acquisition from analysis, enqueue normalized run records, deduplicate by run and attempt, store reports with retention controls, measure rule coverage and latency, and add provider adapters behind a stable internal schema. Preserve per-tenant authorization and auditability.

## What would you monitor?

Acquisition success, triage latency, unknown-class rate, rule distribution, redaction failures, model availability, validation rejection rate, tokens or estimated cost, and report-generation errors. Avoid high-cardinality sensitive labels.

## How is model failure handled?

Timeout, endpoint error, invalid JSON, invalid schema, and unsupported evidence references all degrade to the deterministic report with a recorded limitation.

## Why not automatically rerun failed jobs?

Triage and remediation carry different risk. Automatic reruns can hide flaky tests, consume capacity, repeat unsafe deployments, or amplify an incident. Remediation requires separate policy, authorization, approval, and audit controls.

## What are the principal limitations?

Rule coverage is finite, provider formats evolve, log retention can prevent acquisition, regex redaction cannot guarantee detection of every sensitive value, and root-cause conclusions remain constrained by the evidence available in CI logs.

