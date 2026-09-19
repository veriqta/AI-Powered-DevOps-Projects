# Security Boundaries

## Local Input Boundary

Fixture paths and JSON are untrusted. The parser rejects missing files, oversized data, invalid encoding, invalid structure and unsupported value types.

## GitHub Boundary

Live mode performs read-only requests. Private repositories require an explicitly configured token. The token is never written to reports.

## AI Boundary

AI mode is disabled by default. Only selected redacted evidence crosses the boundary. The response is untrusted, schema-checked and restricted to existing evidence IDs.

## Output Boundary

Reports may still contain operational information. Review classification and sharing requirements before publishing them.

