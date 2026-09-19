# Scenario 04: Malformed Model Response

Review `tests/test_ai_validation.py`, then extend it with a response that has an invalid priority, an extra field, or a nonexistent evidence reference.

The validator must reject the response. The command must retain the deterministic classification and record AI unavailability as a limitation. Passing malformed output through “because it looks useful” fails the exercise.

