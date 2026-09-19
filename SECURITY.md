# Security Policy

## Supported Content

Security fixes are accepted for the current default branch and active project releases listed in the project catalogue.

## Reporting a Vulnerability

Do not publish an exploitable vulnerability, credential or sensitive dataset in a public issue.

Use GitHub private vulnerability reporting when enabled. Otherwise, contact the maintainers through the private security contact listed in the repository profile.

Include:

- affected path and version;
- clear reproduction steps using safe data;
- potential impact;
- suggested mitigation, if known;
- whether public disclosure has occurred.

Do not access systems or data you do not own or have permission to test.

## Repository Data Rules

Never commit:

- API keys, tokens, passwords or private keys;
- production logs or customer data;
- personal information;
- confidential prompts or proprietary runbooks;
- live cloud account identifiers;
- unlicensed datasets or model outputs.

Use synthetic fixtures and documentation-only network addresses. If a real secret is exposed, stop using it, rotate it and follow the affected provider's incident procedure.

## AI-Specific Security

Projects must treat model responses as untrusted. They must validate output before it reaches automation, keep high-impact actions behind approval and document external data processing.

Prompt injection discovered in a fixture should be reported as a project test case. Prompt injection affecting a working integration or exposing data should be reported privately.

## Safe Research

Good-faith research must remain within authorized environments, minimize data access and avoid service disruption. This policy does not authorize testing of third-party systems.

