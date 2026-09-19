# Scenario Questions

## The unknown-class rate doubles after a toolchain upgrade. What do you do?

Segment by workflow, job, runner image, and time; sample sanitized unknown reports; identify format or error-signature changes; add regression fixtures; update narrow rules; and monitor whether the rate returns to baseline without increasing false positives.

## A team asks the tool to rerun every timeout automatically. How do you respond?

Separate recommendation from execution. Quantify timeout causes and flakiness first. If reruns are justified, design a different approved service with rate limits, idempotency, attempt caps, environment restrictions, and human approval for consequential workflows.

## A model explanation contradicts the deterministic class.

Retain the deterministic result, flag the explanation, and investigate the prompt, evidence, and validator. The model must not silently override the authoritative class.

## A report contains a customer email address.

Stop distribution, contain and delete generated copies where possible, assess exposure, follow incident policy, strengthen redaction and tests, and rotate any credential if the leaked value was a secret. Do not use the affected report as a public fixture.

## GitHub log download starts returning 403.

Check token expiry, Actions permission, organization SSO, repository visibility, and rate-limit headers. Reproduce against synthetic local data to show that analysis remains healthy while acquisition is impaired.

## A classification rule matches both dependency and test failures.

Examine causal ordering and evidence specificity. Adjust precedence only with regression examples, or refine the patterns so the earliest actionable cause wins. Document ambiguity rather than hiding it with a confidence score.

