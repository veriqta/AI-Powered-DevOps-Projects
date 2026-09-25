# Project Standards

Every published project must be useful, reproducible, safe, and honest about its limitations.

## Required learning experience

Each project must explain:

- The problem being solved
- The intended users
- The system being built
- The final expected result
- The prerequisites and expected cost
- The implementation sequence
- How to verify each milestone
- How to troubleshoot common failures
- How to clean up local and cloud resources

## Required project resources

A complete project includes, where applicable:

- Project overview and requirements
- Project-specific prerequisites
- System configuration and verification
- Numbered follow-along labs
- Starter code
- Working reference implementation
- Infrastructure as code
- Automated tests
- Safe sample data
- Architecture and data-flow diagrams
- Security and threat analysis
- CI/CD configuration
- Observability configuration
- Failure scenarios and recovery exercises
- Expected terminal and report output
- Production-readiness review
- Interview and portfolio preparation

## Implementation rules

- Pin or constrain important dependencies.
- Keep secrets out of code, fixtures, images, and Git history.
- Prefer deterministic logic for decisions that can be expressed as rules.
- Treat model responses as untrusted input.
- Validate structured model output against an explicit schema.
- Add timeouts, bounded retries, input limits, and failure fallbacks.
- Require approval before destructive, privileged, or costly actions.
- Use least-privilege identities for applications, pipelines, and agents.
- Include idempotent cleanup where practical.
- Never claim that code was tested unless it was executed.

## Testing standard

Projects must test normal behavior, invalid input, dependency failure, model failure, security controls, and cleanup. Acceptance criteria must be measurable. Tests must not require access to private production systems.

## Documentation standard

Write for a global public audience. Address the participant directly where natural. Define unfamiliar terms before using them. Show commands, file locations, expected results, verification, and recovery. Avoid unexplained placeholders and fabricated output.

## Completion gate

A project is marked **Ready** only when:

- A clean environment can follow the documented setup
- The complete build works from beginning to end
- Tests pass
- Failure exercises can be reproduced safely
- Cleanup is verified
- Security and AI safety reviews are complete
- Expected results match actual results
- Links, commands, and file paths have been checked

