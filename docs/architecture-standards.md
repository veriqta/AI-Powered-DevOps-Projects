# Architecture Standards

Architecture documentation must help another engineer understand behavior, risk and ownership.

## Required Views

### System Context

Show users, the project system and external dependencies.

### Component View

Show the main services, modules, stores, queues, policy engines and interfaces.

### Data Flow

Show important inputs, transformations, storage, outputs and external transfers. Label sensitive data and trust boundaries.

### Runtime or Deployment View

Show where components run, how they communicate and which permissions they require.

## Required Written Decisions

Document:

- operational problem and users;
- component responsibilities;
- authoritative deterministic controls;
- AI responsibility and boundary;
- data classification and retention;
- authentication and authorization;
- time, size, retry and cost limits;
- degraded behavior;
- observability;
- cleanup and recovery.

## Diagram Rules

- Use stable component names.
- Keep a diagram focused on one relationship.
- Label directional flows.
- Distinguish required from optional paths.
- Mark external services and human approval.
- Keep diagrams in editable, version-controlled form.
- Update diagrams when implementation behavior changes.

## Decision Records

Use short architecture decision records for consequential choices. Each record should state context, decision, alternatives, consequences and review trigger.

