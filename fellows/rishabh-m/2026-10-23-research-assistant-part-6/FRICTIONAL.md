# Frictional log — AI Research Assistant, Stage 2C

## 2026-10-23 — a daily pipeline with no gaps, and an API that shows it

- **Drive:** https://drive.google.com/drive/folders/1L6V_ArnaUhA5H21NCZkvHcUROG6IgxBY
- **Evidence of commit:** [`cc5cdd3`](https://github.com/RishabhHM/AI-Research-Assistant/commit/cc5cdd3ac3470e7f8467be413099bec5e627f340)

**What I was working on.** Turning the manual DAG into a daily pipeline that misses no papers, retries itself, cleans its cache and reports honestly. Then showing each paper's status, sections and overall stats in the API.

**What I tried, and what I expected.**
- I expected Airflow's data interval to give each daily run a day of papers to fetch.
- I expected "fetch yesterday's papers" to be enough to miss nothing.
- I expected a final report task to just summarise the run.
- I expected mypy and the tests to catch mistakes in the DAG.

**Where it resisted, and what I did next.**
- **Airflow 3's data interval is zero-length**, and CLI runs get `logical_date = None`. I wrote `resolve_window`: the last 5 days, anchored on the logical date or on now (`b885747`).
- **arXiv's announcement delay** meant "yesterday" would miss late-announced papers forever. I made the overlapping window re-fetch every run, daily, weekends included (`e1ebbb5`).
- **A hidden `batch_size` bug:** the DAG still had `Param(5)`, and there was no `batch_size` setting. With `None`, every scheduled run would have crashed with `AttributeError`, and mypy only checked `src/`. I added mypy on `airflow/dags/` and `make check-dags` (`cf79650`).
- **An "always run" report could turn failed runs green.** It now raises when an upstream XCom is missing, so the run stays red (`830b725`).
- **My first failure test would have passed for the wrong reason.** The lookback window repaired the broken URL. I re-ran it on a paper outside the window.
- **`response_model` silently dropped the sections** from the detail endpoint. Only a live `curl` showed it (`8cf4a2c`).

**What Claude contributed, and what I did with it.**
- **Roadmap:** I used Claude to break the week's goal into tasks across Oct 19, 21 and 23.
- **Design and refactoring:** Claude helped with the production-grade design: the lookback window, retries and timeouts, cleanup with `all_done`, a report that keeps failures red, and additive-only API changes.
- **Reviews:** before each commit, Claude checked lint, tests and live runs. It pointed me to the `Param(5)` line that needed to become `Param(None, type=["null", "integer"])`.
- **Code and docs:** Claude added the `check-dags` target to the `Makefile` at my request, and wrote the Stage 2 wrap-up in the README and the Stage 2 doc.
- Accepted:
  - **Daily runs including weekends.** Extra runs only refresh the overlap, and the upsert is idempotent.
  - **`trigger_rule="all_done"` for cache cleanup**, so it also runs on the days something failed.
  - **No `pipeline_runs` table.** Airflow's run history and the paper statuses already hold that state.
- Rejected:
  - **A DAG import test as the fix for the `batch_size` bug.** The bug sits inside a task body, so an import test never runs that line. mypy on the DAGs caught it in a test. I also asked for `make check-dags` to catch import errors.

**What I understand now, and what I still do not.**
- Understood:
  - **Reversed:** in Airflow 3, "fetch the data interval" fetches an empty window.
  - Gaps came from arXiv's real-world timing, not from the scheduler.
  - A leaf task that succeeds hides upstream failures unless it raises.
  - Each check covers something different: mypy, `check-dags`, tests and a live `curl` each caught something the others couldn't. 22 tests now pass.
- Not understood / not verified:
  - The `batch_size` fallback is still unconfirmed until the first scheduled run (2026-10-25 06:00 UTC: parsed + failed + skipped should be 25).
  - The SQL (`upsert_many`, `stats`, `get_pending_pdfs`) has no tests against real Postgres, and the 2A client tests are still deferred.
  - A batch of 25 on a laptop doesn't keep up with ~250 new papers a day, so the queue grows.
