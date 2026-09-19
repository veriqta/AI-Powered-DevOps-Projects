# Shared Schemas

Schemas define stable data exchanged across projects.

Rules:

- Use semantic versioning.
- Set `additionalProperties` deliberately.
- Define required fields and bounds.
- Include safe examples.
- Test valid and invalid fixtures.
- Document migrations and consuming projects.

The starter [AI finding schema](ai-finding.schema.json) demonstrates evidence-bound output. Projects may extend it without weakening required evidence.

