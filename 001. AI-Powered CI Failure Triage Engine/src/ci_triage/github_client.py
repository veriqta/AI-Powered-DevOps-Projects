from __future__ import annotations

import io
import json
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from typing import Any

from .redaction import redact

API_VERSION = "2022-11-28"
MAX_DOWNLOAD_BYTES = 10_000_000
MAX_LOG_LINES_PER_JOB = 200


class GitHubError(RuntimeError):
    pass


class _SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Do not forward an API token to GitHub's external log-storage host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected is not None:
            old_host = urllib.parse.urlparse(req.full_url).netloc
            new_host = urllib.parse.urlparse(newurl).netloc
            if old_host.casefold() != new_host.casefold():
                redirected.remove_header("Authorization")
        return redirected


class GitHubActionsClient:
    def __init__(self, token: str | None, timeout: int = 20) -> None:
        self.token = token
        self.timeout = timeout

    def _request(self, url: str) -> bytes:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "veriqta-ci-failure-triage/0.1",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(url, headers=headers)
        try:
            opener = urllib.request.build_opener(_SafeRedirectHandler())
            with opener.open(request, timeout=self.timeout) as response:
                data = response.read(MAX_DOWNLOAD_BYTES + 1)
        except urllib.error.HTTPError as exc:
            raise GitHubError(f"GitHub API returned HTTP {exc.code}") from exc
        except urllib.error.URLError as exc:
            raise GitHubError(f"GitHub API unavailable: {exc.reason}") from exc
        if len(data) > MAX_DOWNLOAD_BYTES:
            raise GitHubError("GitHub response exceeded download limit")
        return data

    def _json(self, url: str) -> dict[str, Any]:
        try:
            value = json.loads(self._request(url))
        except json.JSONDecodeError as exc:
            raise GitHubError("GitHub API returned invalid JSON") from exc
        if not isinstance(value, dict):
            raise GitHubError("GitHub API response must be an object")
        return value

    def collect(self, repository: str, run_id: int) -> dict[str, Any]:
        if repository.count("/") != 1:
            raise GitHubError("repository must be OWNER/REPO")
        base = f"https://api.github.com/repos/{repository}/actions/runs/{run_id}"
        run = self._json(base)
        jobs_payload = self._json(base + "/jobs?per_page=100")
        jobs = jobs_payload.get("jobs", [])
        if not isinstance(jobs, list):
            raise GitHubError("jobs response does not contain an array")
        excerpts = self._download_logs(base + "/logs")
        unassigned_logs = [line for lines in excerpts.values() for line in lines]
        normalized_jobs = []
        for job in jobs:
            if not isinstance(job, dict):
                continue
            name = str(job.get("name", "unknown"))
            normalized_jobs.append({
                "id": job.get("id"),
                "name": name,
                "conclusion": job.get("conclusion"),
                # GitHub's archive entry names are not guaranteed to match the
                # display name exactly. Preserve bounded evidence when there is
                # only one job instead of silently returning an empty record.
                "log_excerpt": excerpts.get(name, unassigned_logs if len(jobs) == 1 else []),
            })
        return {
            "run": {
                "id": run.get("id", run_id),
                "name": run.get("name", "unknown"),
                "conclusion": run.get("conclusion", "unknown"),
                "html_url": run.get("html_url", ""),
                "head_sha": run.get("head_sha"),
                "event": run.get("event"),
            },
            "jobs": normalized_jobs,
        }

    def _download_logs(self, url: str) -> dict[str, list[str]]:
        raw = self._request(url)
        result: dict[str, list[str]] = {}
        try:
            with zipfile.ZipFile(io.BytesIO(raw)) as archive:
                for info in archive.infolist():
                    if info.is_dir() or info.file_size > MAX_DOWNLOAD_BYTES:
                        continue
                    name = info.filename.rsplit("/", 1)[-1].removesuffix(".txt")
                    text = archive.read(info).decode("utf-8", errors="replace")
                    result[name] = [redact(line) for line in text.splitlines()[-MAX_LOG_LINES_PER_JOB:]]
        except zipfile.BadZipFile as exc:
            raise GitHubError("workflow logs were not a valid ZIP archive") from exc
        return result
