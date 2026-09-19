import unittest
from pathlib import Path

from ci_triage.classifier import classify
from ci_triage.parser import load_fixture

ROOT = Path(__file__).resolve().parents[1]


class ClassifierTests(unittest.TestCase):
    def expected(self, fixture: str, category: str) -> None:
        _, evidence = load_fixture(ROOT / "sample-data" / fixture)
        finding = classify(evidence)
        self.assertEqual(category, finding.category)
        self.assertTrue(finding.evidence_refs)

    def test_test_failure(self):
        self.expected("test-failure.json", "test_failure")

    def test_dependency_failure(self):
        self.expected("dependency-failure.json", "dependency_failure")

    def test_runner_failure_wins(self):
        self.expected("runner-failure.json", "runner_infrastructure")

    def test_permission_failure(self):
        self.expected("permission-failure.json", "permission_or_secret")

    def test_unknown_failure(self):
        self.expected("unknown-failure.json", "unknown")


if __name__ == "__main__":
    unittest.main()

