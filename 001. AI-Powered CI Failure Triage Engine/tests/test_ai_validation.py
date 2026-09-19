import unittest

from ci_triage.ai_client import AIError, _validate


class AIValidationTests(unittest.TestCase):
    def test_valid_output(self):
        value = {
            "explanation": "The test assertion failed.",
            "priority": "medium",
            "evidence_refs": ["E-002"],
            "limitations": ["Only an excerpt was supplied."],
        }
        self.assertEqual("medium", _validate(value, {"E-002"})["priority"])

    def test_invented_reference_is_rejected(self):
        value = {
            "explanation": "Unsupported.",
            "priority": "high",
            "evidence_refs": ["E-999"],
            "limitations": [],
        }
        with self.assertRaises(AIError):
            _validate(value, {"E-001"})

    def test_extra_field_is_rejected(self):
        value = {
            "explanation": "Unsafe.",
            "priority": "high",
            "evidence_refs": ["E-001"],
            "limitations": [],
            "command": "deploy",
        }
        with self.assertRaises(AIError):
            _validate(value, {"E-001"})


if __name__ == "__main__":
    unittest.main()

