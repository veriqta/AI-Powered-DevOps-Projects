# Safe Sample Data

These fixtures simulate failed GitHub Actions runs. They use invented repositories, IDs and placeholder values.

| Fixture | Expected primary class |
|---|---|
| `test-failure.json` | `test_failure` |
| `dependency-failure.json` | `dependency_failure` |
| `runner-failure.json` | `runner_infrastructure` |
| `permission-failure.json` | `permission_or_secret` |
| `unknown-failure.json` | `unknown` |

Never replace these files with private workflow logs. Use explicitly authorized exports and review them for secrets before analysis.

