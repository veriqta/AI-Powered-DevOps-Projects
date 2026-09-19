# Lab 10: Final Demonstration

## Objective

Present a reproducible engineering project with evidence, limitations, and operational reasoning.

## Preparation

1. Start from a clean checkout or clean virtual environment.
2. Follow the [walkthrough](../walkthrough/implementation-guide.md) without undocumented steps.
3. Run:

   ```bash
   make verify
   make sample
   ```

4. If `make sample` is not defined in a learner-modified Makefile, run `./scripts/run-sample.sh` and document the correction before recording.
5. Select two contrasting fixtures and one degraded case.

## Demonstration order

1. Explain the operational problem and users.
2. Show the architecture and trust boundaries.
3. Process a test failure and a runner or permission failure.
4. Trace one evidence ID from input to report.
5. Show redaction using synthetic data.
6. Demonstrate `unknown` or rejected malformed AI output.
7. Show the tests and CI result.
8. Explain permissions, limitations, cost, and the next production improvement.

## Deliverable

A five-to-ten-minute demonstration or annotated screenshot sequence, a project explanation, and links to sanitized engineering evidence.

## Completion gate

- [ ] Another engineer can reproduce the local workflow.
- [ ] Every claim is supported by implementation or evidence.
- [ ] Roadmap items are not presented as completed features.
- [ ] No proprietary data or secret is visible.

