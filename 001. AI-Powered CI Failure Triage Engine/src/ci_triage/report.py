from __future__ import annotations

import json

from .models import TriageReport


def render_json(report: TriageReport) -> str:
    return json.dumps(report.to_dict(), indent=2, sort_keys=True)


def render_text(report: TriageReport) -> str:
    finding = report.finding
    lines = [
        "CI FAILURE TRIAGE REPORT",
        f"Run: {report.run.get('name')} ({report.run.get('id')})",
        f"Conclusion: {report.run.get('conclusion')}",
        f"Primary class: {finding.category}",
        f"Confidence: {finding.confidence:.2f}",
        f"Summary: {finding.summary}",
        "Evidence: " + ", ".join(finding.evidence_refs),
        "Matched rules: " + (", ".join(finding.matched_rules) or "none"),
        "Next checks:",
        *[f"- {item}" for item in finding.next_checks],
    ]
    if report.ai_explanation:
        lines.extend([
            "AI explanation (untrusted, validated):",
            f"- {report.ai_explanation['explanation']}",
            f"- Priority: {report.ai_explanation['priority']}",
            "- Evidence: " + ", ".join(report.ai_explanation["evidence_refs"]),
        ])
    lines.append("Limitations:")
    lines.extend(f"- {item}" for item in report.limitations)
    return "\n".join(lines)

