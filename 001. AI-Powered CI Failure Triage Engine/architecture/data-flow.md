# Data Flow

| Flow | Source | Destination | Data | Control |
|---|---|---|---|---|
| DF-001 | Learner | CLI | Fixture path or run ID | Argument validation |
| DF-002 | GitHub API | Collector | Run, jobs and bounded ZIP logs | Read-only token, size and timeout limit |
| DF-003 | Parser | Redactor | Job metadata and excerpts | File, type, record and character limits |
| DF-004 | Redactor | Classifier | Sanitized evidence | Pattern redaction |
| DF-005 | Classifier | Reporter | Finding, rules and evidence IDs | Deterministic schema |
| DF-006 | Classifier | AI endpoint | Selected sanitized evidence | Explicit opt-in, timeout, size limit |
| DF-007 | AI endpoint | Validator | Structured explanation | Exact fields and evidence-reference validation |
| DF-008 | Reporter | User | Text or JSON report | No actions executed |

