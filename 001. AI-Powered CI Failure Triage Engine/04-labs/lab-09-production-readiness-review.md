# Lab 09: Production Readiness Review

## Objective

Assess what must change before a team can operate the triage engine as a service.

## Steps

1. Review `architecture/` and `docs/security-model.md`.
2. Create a table covering availability, authorization, privacy, retention, observability, cost, capacity, recovery, ownership, and change management.
3. For each area, record current state, production gap, risk, proposed control, owner, and verification method.
4. Define measurements for triage success, latency, unknown rate, model rejection rate, redaction regressions, and cost.
5. Describe a rollback that disables AI while retaining deterministic triage.
6. Explain how webhook ingestion, queues, idempotency, tenant isolation, and controlled report storage would alter the architecture.
7. Separate implemented controls from roadmap proposals.

## Deliverable

`docs/production-readiness-review.md` in the learner repository.

## Completion gate

- [ ] Current capabilities and future proposals are clearly separated.
- [ ] Residual risks have owners or acceptance decisions.
- [ ] AI can be disabled independently.
- [ ] No write access is introduced without a separate authorization design.

