# Scenario 05: Redaction Regression

Add a synthetic credential format to a local fixture and confirm whether it is redacted. If not:

1. stop before model transmission or publication;
2. add a failing redaction unit test;
3. implement the narrowest safe pattern;
4. rerun the full suite;
5. assess false positives and document limitations.

Never test with a real credential. The evidence should show the test failing before the fix and passing afterward.

