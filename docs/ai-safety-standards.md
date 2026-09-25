# AI Safety Standards

AI is a fallible dependency. Every AI-enabled project must define what the model can see, what it can produce, what it can request, and what it can never do.

## Minimum controls

- Classify and redact input data
- Treat logs, tickets, repository content, and retrieved documents as untrusted
- Defend against prompt injection
- Use explicit system boundaries and tool allowlists
- Validate structured output against schemas
- Verify citations and evidence references
- Enforce timeouts, rate limits, and cost limits
- Provide safe behavior when the model fails
- Require human approval for high-impact actions
- Record model, prompt, policy, tool call, decision, and result metadata

Evaluation must cover unsupported claims, unsafe instructions, malformed output, sensitive-data leakage, prompt injection, excessive agency, dependency outages, and adversarial input.

