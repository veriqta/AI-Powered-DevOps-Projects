from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path

from .ai_client import AIError, explain
from .classifier import classify
from .github_client import GitHubActionsClient, GitHubError
from .models import TriageReport
from .parser import InputError, load_fixture
from .report import render_json, render_text


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evidence-linked GitHub Actions failure triage")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--input", type=Path, help="safe local JSON fixture")
    source.add_argument("--repository", help="GitHub repository as OWNER/REPO")
    parser.add_argument("--run-id", type=int, help="workflow run ID for live GitHub mode")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--enable-ai", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.input:
            run, evidence = load_fixture(args.input)
        else:
            if not args.run_id or args.run_id <= 0:
                raise InputError("--run-id is required with --repository")
            payload = GitHubActionsClient(os.getenv("GITHUB_TOKEN")).collect(args.repository, args.run_id)
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json") as handle:
                json.dump(payload, handle)
                handle.flush()
                run, evidence = load_fixture(Path(handle.name))

        finding = classify(evidence)
        report = TriageReport(
            schema_version="1.0",
            run=run,
            finding=finding,
            evidence=evidence,
            limitations=[
                "Classification is based on bounded excerpts, not the complete repository state.",
                "The tool does not rerun jobs, modify code, approve changes or operate production systems.",
                "AI explanation, when enabled, cannot override the deterministic failure class.",
            ],
            audit={
                "generated_at": datetime.now(UTC).isoformat(),
                "source_mode": "fixture" if args.input else "github-actions",
                "deterministic_authority": True,
                "ai_requested": bool(args.enable_ai),
            },
        )
        if args.enable_ai:
            key = os.getenv("AI_API_KEY")
            model = os.getenv("AI_MODEL")
            if not key or not model:
                raise InputError("AI_API_KEY and AI_MODEL are required with --enable-ai")
            try:
                report.ai_explanation = explain(
                    finding,
                    evidence,
                    api_key=key,
                    base_url=os.getenv("AI_BASE_URL", "https://api.openai.com/v1"),
                    model=model,
                    timeout=int(os.getenv("AI_TIMEOUT_SECONDS", "20")),
                )
            except AIError as exc:
                report.limitations.append(f"AI explanation unavailable: {exc}")

        output = render_json(report) if args.format == "json" else render_text(report)
        if args.output:
            if args.output.exists() and not args.output.is_file():
                raise InputError("output path is not a regular file")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(output + "\n", encoding="utf-8")
        else:
            print(output)
        return 0
    except (InputError, GitHubError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
