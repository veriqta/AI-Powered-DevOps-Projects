# Completion Checklist

## Environment

- [ ] Python 3.11 or newer is active.
- [ ] The project is installed in an isolated virtual environment.
- [ ] `ci-failure-triage --help` succeeds.
- [ ] No secret is stored in a tracked file.

## Functional result

- [ ] All supplied fixtures validate.
- [ ] Every fixture produces the expected class.
- [ ] Unknown evidence remains `unknown`.
- [ ] Output contains traceable evidence references.
- [ ] Redaction is verified with tests.
- [ ] AI failure does not prevent deterministic reporting.

## Engineering quality

- [ ] Unit and integration tests pass.
- [ ] CI checks pass in the learner repository.
- [ ] Read-only permissions are documented.
- [ ] Architecture and trust boundaries can be explained.
- [ ] At least three failure exercises are completed.
- [ ] Limitations and future improvements are documented.

## Portfolio readiness

- [ ] Published examples contain only synthetic or authorized data.
- [ ] The project can be explained in two minutes without reading notes.
- [ ] Screenshots and claims match results actually produced.
- [ ] The repository links to evidence, tests, architecture, and the demonstration.

