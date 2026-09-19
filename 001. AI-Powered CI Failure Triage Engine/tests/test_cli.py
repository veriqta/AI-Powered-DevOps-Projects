import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

from ci_triage.cli import main

ROOT = Path(__file__).resolve().parents[1]


class CLITests(unittest.TestCase):
    def test_json_output(self):
        stream = StringIO()
        with redirect_stdout(stream):
            code = main(["--input", str(ROOT / "sample-data/test-failure.json"), "--format", "json"])
        self.assertEqual(0, code)
        payload = json.loads(stream.getvalue())
        self.assertEqual("test_failure", payload["finding"]["category"])
        self.assertIsNone(payload["ai_explanation"])

    def test_missing_file_fails_safely(self):
        error = StringIO()
        with redirect_stderr(error):
            code = main(["--input", "/does/not/exist.json"])
        self.assertEqual(2, code)
        self.assertIn("ERROR:", error.getvalue())

    def test_ai_requires_configuration(self):
        error = StringIO()
        with redirect_stderr(error):
            code = main(["--input", str(ROOT / "sample-data/test-failure.json"), "--enable-ai"])
        self.assertEqual(2, code)
        self.assertIn("AI_API_KEY", error.getvalue())


if __name__ == "__main__":
    unittest.main()

