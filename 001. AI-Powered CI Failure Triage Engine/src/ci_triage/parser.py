from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import Evidence
from .redaction import redact

MAX_FILE_BYTES = 2_000_000
MAX_EVIDENCE_ITEMS = 200
MAX_EVIDENCE_CHARS = 4_000


class InputError(ValueError):
    pass


def load_fixture(path: Path) -> tuple[dict[str, Any], list[Evidence]]:
    if not path.exists() or not path.is_file():
        raise InputError(f"input is not a regular file: {path}")
    if path.stat().st_size > MAX_FILE_BYTES:
        raise InputError(f"input exceeds {MAX_FILE_BYTES} bytes")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise InputError(f"invalid UTF-8 JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise InputError("input root must be an object")
    run = payload.get("run")
    jobs = payload.get("jobs")
    if not isinstance(run, dict) or not isinstance(jobs, list):
        raise InputError("input requires object 'run' and array 'jobs'")
    required = {"id", "name", "conclusion", "html_url"}
    missing = sorted(required - run.keys())
    if missing:
        raise InputError("run missing fields: " + ", ".join(missing))

    evidence: list[Evidence] = []
    for job_index, job in enumerate(jobs, 1):
        if not isinstance(job, dict):
            raise InputError(f"job {job_index} must be an object")
        job_name = str(job.get("name", f"job-{job_index}"))
        conclusion = str(job.get("conclusion", "unknown"))
        lines = job.get("log_excerpt", [])
        if isinstance(lines, str):
            lines = lines.splitlines()
        if not isinstance(lines, list):
            raise InputError(f"job {job_index} log_excerpt must be text or array")
        evidence.append(Evidence(
            evidence_id=f"E-{len(evidence)+1:03d}",
            source=f"job:{job_name}",
            text=redact(f"job={job_name} conclusion={conclusion}")[:MAX_EVIDENCE_CHARS],
        ))
        for line in lines:
            if len(evidence) >= MAX_EVIDENCE_ITEMS:
                break
            if not isinstance(line, str):
                raise InputError(f"job {job_index} log lines must be strings")
            cleaned = redact(line.strip())
            if cleaned:
                evidence.append(Evidence(
                    evidence_id=f"E-{len(evidence)+1:03d}",
                    source=f"job:{job_name}",
                    text=cleaned[:MAX_EVIDENCE_CHARS],
                ))
    if not evidence:
        raise InputError("no job evidence found")
    return run, evidence

