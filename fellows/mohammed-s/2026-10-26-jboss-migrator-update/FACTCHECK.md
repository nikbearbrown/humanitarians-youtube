# FACTCHECK — `hussain-jboss-migrator-update-2026-11-03` · "Batch Mode Lands."

Source: the jboss-migrator repository and its test runs on 2026-11-03. Every number on screen
or in narration was re-checked against git / GitHub / pytest on the build date, not from memory.

| Beat | Claim | Verified by | Status |
|---|---|---|---|
| B00 | The design from the last video is now working code on GitHub | `github.com/mdhussainshariff/jboss-migrator`, `main` at `41d62af` | Correct |
| B00 | Today it gained batch mode | `git log`: `41d62af Add batch mode for migrating a portfolio of apps` (2026-11-03) | Correct |
| B01 | Six stages are Python modules: config.py, baseline.py, analyzer.py, transformers/, verify/, testplan/ | `ls migrator/` | Correct |
| B01 | Five of the six stages have unit tests; baseline does not | `tests/`: config, analyzer (test_planner_analyzer), transformers (test_namespaces, test_server_config), verify (test_diff_guard, test_test_compare), testplan (test_testplan); no test imports `baseline` | Correct — **corrected during fact-check** (first draft said "each one has unit tests") |
| B02 | Repo is public | `gh repo view … --json visibility` → `PUBLIC` | Correct |
| B02 | 49 files · 3,143 lines | `git show --stat 74d01c9` → `49 files changed, 3143 insertions(+)` | Correct (initial commit; lines include YAML, templates, tests) |
| B02 | 18 unit tests passing | `pytest -q` on the initial commit → `18 passed` | Correct |
| B02, B06 | PR #75 into nikbearbrown/mycroft, open | `gh pr view 75 --repo nikbearbrown/mycroft` → `OPEN`, commits `55c4dcb`, `e11825f` | Correct |
| B03 | portfolio.yaml lines shown | `portfolio.yaml` at `41d62af`, trimmed (comments and some keys omitted, no lines altered) | Correct; hostnames illustrative (footnote on screen) |
| B03 | Billing inherits defaults; customer-portal overrides only `source.server` and keeps `java: 8` | `tests/test_batch.py::test_example_portfolio_loads` | Correct |
| B04 | All bad entries reported together, before anything runs | `batch.parse` collects errors; `test_name_defaults_to_repo_and_all_errors_reported` | Correct |
| B04 | One crash is recorded and the rest carry on; each app has its own folder | `batch._run_app` catches per app, `workdir/<app>`; `test_run_isolates_failures_keeps_order_and_writes_summary` | Correct |
| B04 | UI checks take turns | `pipeline._UI_LOCK` around deploy + snapshot | Correct |
| B05 | `23 passed in 11.71s` | pytest run on 2026-11-03 (output captured in session) | Correct |
| B05 | Batch run against a missing repo: clone fails, app marked error, summary written | `jboss-migrator batch` smoke run on 2026-11-03; real output, timestamp and temp paths trimmed | Correct |
| B06 | Commits `41d62af` (main) and `e11825f` (PR #75); 5 new tests; 23 of 23 passing | `git log`; `tests/test_batch.py` has 5 tests; 23 test functions in `tests/` | Correct |
| B07 | Not yet run end to end on a real JBoss app; engines not run together | No such run has happened; only unit tests and the batch smoke run | Correct (stated as a limitation) |

## Labelled as illustrative on screen
- B03 footnote: "Trimmed from portfolio.yaml · hostnames illustrative".

## Not verified
- Presenter has not reviewed the cut yet.
