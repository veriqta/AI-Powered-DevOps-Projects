from __future__ import annotations

import re
from dataclasses import dataclass

from .models import Evidence, Finding


@dataclass(frozen=True)
class Rule:
    rule_id: str
    category: str
    pattern: re.Pattern[str]
    weight: int
    next_check: str


RULES = [
    Rule("R-TEST-001", "test_failure", re.compile(r"(?i)(assertionerror|tests? failed|expected .+ (?:but|got)|pytest.+failed)"), 4, "Open the named failing test and reproduce it locally."),
    Rule("R-TEST-002", "test_failure", re.compile(r"(?i)(coverage.+below|snapshot.+failed)"), 3, "Compare the result with the approved test baseline."),
    Rule("R-DEP-001", "dependency_failure", re.compile(r"(?i)(no matching distribution|could not resolve|dependency conflict|package .+ not found)"), 4, "Check the lock file, registry availability and requested version."),
    Rule("R-LINT-001", "quality_gate_failure", re.compile(r"(?i)(lint(?:er)? error|formatting check failed|ruff .+ found|eslint.+error)"), 4, "Run the documented formatter or linter locally."),
    Rule("R-BUILD-001", "build_failure", re.compile(r"(?i)(compilation failed|build failed|syntaxerror|cannot find module)"), 4, "Reproduce the build with the same runtime and dependency versions."),
    Rule("R-TIME-001", "timeout", re.compile(r"(?i)(timed? out|timeout|exceeded the maximum execution time)"), 5, "Inspect the slow step, dependency latency and configured time limit."),
    Rule("R-RUNNER-001", "runner_infrastructure", re.compile(r"(?i)(runner lost communication|hosted runner.+unavailable|no space left on device|connection reset)"), 5, "Check runner health, disk, network and provider status before changing code."),
    Rule("R-AUTH-001", "permission_or_secret", re.compile(r"(?i)(permission denied|resource not accessible by integration|bad credentials|401 unauthorized|403 forbidden)"), 5, "Verify token presence, scope, event restrictions and repository permissions."),
    Rule("R-CACHE-001", "cache_or_artifact", re.compile(r"(?i)(cache.+corrupt|artifact.+not found|failed to restore cache)"), 4, "Retry without the cache and verify artifact names and retention."),
]


def classify(evidence: list[Evidence]) -> Finding:
    scores: dict[str, int] = {}
    matches: dict[str, list[str]] = {}
    refs: dict[str, list[str]] = {}
    checks: dict[str, list[str]] = {}
    for item in evidence:
        for rule in RULES:
            if rule.pattern.search(item.text):
                scores[rule.category] = scores.get(rule.category, 0) + rule.weight
                matches.setdefault(rule.category, []).append(rule.rule_id)
                refs.setdefault(rule.category, []).append(item.evidence_id)
                checks.setdefault(rule.category, []).append(rule.next_check)
    if not scores:
        return Finding(
            category="unknown",
            confidence=0.2,
            summary="The supplied evidence does not match a supported deterministic failure class.",
            matched_rules=[],
            evidence_refs=[e.evidence_id for e in evidence[:3]],
            next_checks=["Inspect the earliest failed step and collect a larger safe log excerpt."],
        )
    category = sorted(scores, key=lambda c: (-scores[c], c))[0]
    score = scores[category]
    confidence = min(0.95, 0.45 + score * 0.08)
    unique_rules = list(dict.fromkeys(matches[category]))
    unique_refs = list(dict.fromkeys(refs[category]))
    unique_checks = list(dict.fromkeys(checks[category]))
    label = category.replace("_", " ")
    return Finding(
        category=category,
        confidence=round(confidence, 2),
        summary=f"Deterministic rules classify the primary failure as {label}.",
        matched_rules=unique_rules,
        evidence_refs=unique_refs,
        next_checks=unique_checks,
    )

