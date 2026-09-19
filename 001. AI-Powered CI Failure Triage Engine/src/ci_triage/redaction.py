from __future__ import annotations

import re

_PATTERNS = [
    (re.compile(r"(?i)(authorization:\s*bearer\s+)[^\s]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)\b(gh[pousr]_[A-Za-z0-9_]{20,})\b"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"(?i)\b(api[_-]?key|token|password|secret)\s*[=:]\s*[^\s,;]+"), r"\1=[REDACTED]"),
    (re.compile(r"(?i)://([^:/\s]+):([^@/\s]+)@"), r"://\1:[REDACTED]@"),
]


def redact(text: str) -> str:
    result = text
    for pattern, replacement in _PATTERNS:
        result = pattern.sub(replacement, result)
    return result

