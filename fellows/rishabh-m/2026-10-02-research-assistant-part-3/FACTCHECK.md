# FACTCHECK — research-assistant-part-3

All bugs are ones Rishabh logged in `personal/Documentation/Stage 1 - Infrastructure Setup.md`.
Checked 2026-10-02.

| # | Claim (beat) | Verdict | Evidence |
|---|---|---|---|
| 1 | Mock missing a required field → 500 not 422 (B03) | ✓ | §7 ⚠ "Required fields and the mock"; Debugging Techniques bullet 2 |
| 2 | 422 = caller's mistake, 500 = my code (B03) | ✓ | same |
| 3 | DAG Import Error from `say_hello` without `()`; error only names the file; run the file directly (B04) | ✓ | §6.3.5 "(this was the 'Dag Import Error')"; Debugging Techniques bullet 3 |
| 4 | `test_dag.py` excerpt (B04) | ✓ excerpt | verbatim lines 14–18 + 48; `...` marks omitted lines, labelled |
| 5 | Naming-convention change committed, tests passed, live table still `papers_pkey` (B05) | ✓ | Task 3 |
| 6 | create_all never alters existing tables (B05) | ✓ | §5.3; Debugging Techniques |
| 7 | Init script didn't run on existing volume → createdb by hand (B06) | ✓ | §6.3.2 ⚠ |
| 8 | Airflow password changes after any `down`; lives in a container file (B06) | ✓ | Task 4 ⚠ Correction |
| 9 | pytest collected `airflow/dags/test_dag.py`; fixed with `testpaths` (B07) | ✓ | Task 2; `pyproject.toml` verbatim |
| 10 | `--envfile` registered by pytest-dotenv (last release 2020) and pytest-env; crash before tests; removed the old one (B08) | ✓ | Task 2 🔧; error string verbatim |
| 11 | `make reset`: wipe volumes, rebuild, pull model, seed, print password (B09) | ✓ | `Makefile` reset target |
| 12 | Four habits (B10) | ✓ | "Habits that do the rest" 1, 3, 4, 5 |
| 13 | Deadline → take the fix (B11) | ⚑ interpretation | our judgment; bounds the reel's own advice |

Omitted by design: the reference-code comparisons (by request — build framing only),
Airflow 3 vs 2 (Part 2 B06 owns it), httpx `timeout=None` (too small for its own beat).
