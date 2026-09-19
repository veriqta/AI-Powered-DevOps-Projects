# Portfolio Guidance

A strong portfolio explains engineering decisions and evidence, not only the final interface.

## Project Story

Your README should answer:

1. What production problem exists?
2. Who experiences it?
3. What evidence enters the system?
4. Why is AI useful?
5. What remains deterministic?
6. How does the system fail safely?
7. What did testing reveal?
8. What would change before real deployment?

## Evidence to Show

- concise architecture diagram;
- representative code and test structure;
- CI result;
- normal and degraded outputs;
- controlled failure investigation;
- security and data-handling controls;
- measurable performance or cost result;
- limitations and next step.

## Demonstration

A five-to-ten-minute demonstration should:

1. state the operational problem;
2. show the architecture;
3. run the normal workflow;
4. introduce one controlled failure;
5. show detection and recovery;
6. disable or break the model;
7. show safe fallback;
8. explain one important trade-off.

## Interview Discussion

Be ready to explain:

- why AI was used;
- how hallucinations are constrained;
- what happens during dependency failure;
- how secrets and permissions are handled;
- how cost and latency are bounded;
- which signals indicate unhealthy behavior;
- what you would redesign at larger scale.

Never claim production deployment, savings or accuracy that you did not measure.

