from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    source: str
    text: str


@dataclass(frozen=True)
class Finding:
    category: str
    confidence: float
    summary: str
    matched_rules: list[str]
    evidence_refs: list[str]
    next_checks: list[str]


@dataclass
class TriageReport:
    schema_version: str
    run: dict[str, Any]
    finding: Finding
    evidence: list[Evidence]
    ai_explanation: dict[str, Any] | None = None
    limitations: list[str] = field(default_factory=list)
    audit: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
