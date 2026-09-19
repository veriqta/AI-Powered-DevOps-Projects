# ADR 001: Deterministic Classification Remains Authoritative

- Status: Accepted
- Date: 2026-09-19

## Context

CI logs may contain misleading text, and model explanations can be unsupported or inconsistent.

## Decision

Rules select the primary failure class. AI may explain and prioritize the selected evidence but cannot change the class, execute commands or trigger CI actions.

## Consequences

The system remains useful without a model. New classes require explicit rules and tests. Unknown failures remain visible rather than being confidently guessed.

