# Security Policy

## Reporting a vulnerability

Do not disclose suspected vulnerabilities in public issues, discussions, pull requests, screenshots, or demonstration videos.

Use GitHub private vulnerability reporting when it is enabled for this repository. Include:

- The affected project and file
- The observed behavior
- Reproduction steps using safe data
- The possible impact
- Suggested mitigation, if known
- Whether credentials or sensitive information may have been exposed

Do not test against systems, accounts, repositories, or data without explicit authorization.

## Supported content

Security fixes are prioritized for projects marked **Ready** or **Maintenance**. Planned and in-development projects may change significantly before release.

## Sensitive information

Never submit:

- API keys, passwords, tokens, or private keys
- Real customer or employee data
- Private infrastructure addresses or account identifiers
- Unredacted production logs
- Proprietary source code
- Exploit material that creates unnecessary public risk

If a secret is accidentally committed, revoke or rotate it immediately. Removing it from the latest commit is not sufficient because it may remain in Git history.

## Safe research

Use synthetic fixtures and isolated environments. Follow project cleanup instructions and verify that cloud resources have been removed. AI-generated commands must be reviewed before execution and must never receive broader permissions than the project requires.

