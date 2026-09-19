# Lab 01: Inspect CI Failure Evidence

## Objective

Understand the supplied CI run format before relying on the classifier.

## Follow first

[Project Guide Part 01](../project-guide/part-01-operational-problem-and-context/README.md) and [Part 02](../project-guide/part-02-architecture-and-data-design/README.md).

## Steps

1. List the fixtures:

   ```bash
   ls -1 sample-data/*.json
   ```

2. Validate their JSON syntax:

   ```bash
   ./scripts/validate-samples.sh
   ```

3. Open `sample-data/test-failure.json`.
4. Identify the run ID, workflow name, conclusion, jobs, job conclusions, and log excerpts.
5. Repeat the inspection for the dependency, runner, permission, and unknown fixtures.
6. Create an evidence inventory with these columns: fixture, failed job, strongest signal, sensitive-data risk, expected class, and missing context.
7. Explain why a failed job name alone is not enough to establish the cause.

## Validation

The inventory must distinguish observed evidence from assumptions. The unknown fixture must not receive a guessed class.

## Deliverable

`docs/lab-evidence/lab-01-evidence-inventory.md` in the learner repository.

## Completion gate

- [ ] All five fixtures were inspected.
- [ ] Evidence and assumptions are separated.
- [ ] Sensitive fields that would require redaction are identified.
- [ ] Unknown evidence remains unresolved.

