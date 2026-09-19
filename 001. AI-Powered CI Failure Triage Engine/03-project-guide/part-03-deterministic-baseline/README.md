# Part 03: Deterministic Baseline

## Purpose

Create a useful offline system before adding an external model.

## Learning outcomes

- extract bounded evidence from heterogeneous job records;
- redact common sensitive values;
- design rule precedence and confidence honestly;
- preserve `unknown` when evidence is insufficient;
- produce recommendations that remain advisory.

## Build tasks

1. Inspect `redaction.py`, `parser.py`, and `classifier.py`.
2. Run every supplied fixture and compare expected classes.
3. Add one new synthetic failure signature.
4. Write a positive test and a nearby negative test.
5. Explain why the selected rule order represents the earliest actionable cause.
6. Generate JSON and verify every evidence reference.

## Validation

```bash
./scripts/validate-samples.sh
./scripts/run-sample.sh
python -m unittest tests.test_classifier tests.test_parser -v
```

## Failure exercise

Process `unknown-failure.json`. List the missing evidence required for a supported class. Do not add a broad keyword rule solely to eliminate `unknown`.

## Completion gate

- [ ] The engine works offline.
- [ ] Redaction occurs before optional model use.
- [ ] Rules are traceable and regression-tested.
- [ ] Unknown evidence remains unknown.

Next: [Part 04](../part-04-platform-integration/README.md)

