import json
import tempfile
import unittest
from pathlib import Path

from ci_triage.parser import InputError, load_fixture
from ci_triage.redaction import redact


class ParserTests(unittest.TestCase):
    def write(self, value) -> Path:
        handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False)
        json.dump(value, handle)
        handle.close()
        self.addCleanup(Path(handle.name).unlink, missing_ok=True)
        return Path(handle.name)

    def test_missing_run_is_rejected(self):
        with self.assertRaises(InputError):
            load_fixture(self.write({"jobs": []}))

    def test_non_string_log_line_is_rejected(self):
        value = {
            "run": {"id": 1, "name": "x", "conclusion": "failure", "html_url": "https://example.invalid"},
            "jobs": [{"name": "x", "conclusion": "failure", "log_excerpt": [42]}],
        }
        with self.assertRaises(InputError):
            load_fixture(self.write(value))

    def test_secret_patterns_are_redacted(self):
        text = redact("token=abc123 password=hunter2 ghp_123456789012345678901234")
        self.assertNotIn("abc123", text)
        self.assertNotIn("hunter2", text)
        self.assertNotIn("ghp_", text)


if __name__ == "__main__":
    unittest.main()

