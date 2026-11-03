# FACTCHECK — research-assistant-part-2

Checked 2026-09-25 against the AI-Research-Assistant repo and its Stage 1 write-up.

| # | Claim (beat) | Verdict | Evidence |
|---|---|---|---|
| 1 | Engine created once at startup (B03) | ✓ | `src/main.py` lifespan |
| 2 | First Dockerfile ran 5 workers; later removed (B03) | ✓ | git: `e0e1dbf` `--workers 5` → `c8f492b` 3 → `86c2d72` none |
| 3 | Each worker runs lifespan → own pool; 5 × 20 = 100 = Postgres default (B03) | ✓ arithmetic | Stage 1 doc §4.6 note; `postgres_pool_size=20`. Presented as arithmetic, not an outage |
| 4 | FastAPI closes the session after `yield` (B04) | ✓ | `src/dependencies.py`; doc §4.4 |
| 5 | Unclosed sessions: pool empties ~20 requests in, requests hang (B04) | ✓ | doc §4.4, "pool_size=20 and max_overflow=0 … hanging after about 20 calls" |
| 6 | `dependencies.py` shown with signature wrapped (B04) | ✓ labelled | tokens verbatim; one signature line wrapped to fit, labelled on screen |
| 7 | Compose reads .env and supplies values at start; image holds no secrets (B05) | ✓ | doc §4.6 credentials table; `.dockerignore` |
| 8 | Shared code never imports FastAPI; Airflow reuses it (B06) | ✓ | README Key Learnings; `test_dag.py` imports `src.config`, `src.db` |
| 9 | Airflow 2 pins SQLAlchemy <2.0, couldn't import src/ (B06) | ✓ | doc §6.3 decisions table |
| 10 | /health catches; DAG task raises on degraded (B07) | ✓ | `ping.py` try/except; `test_dag.py` `raise RuntimeError` |
| 11 | Settings default to localhost; compose overrides to service name (B08) | ✓ | `config.py`; `compose.yaml` api env + comment |
| 12 | "9200:9200" = all interfaces; café/campus reachable; search has no password locally (B09) | ✓ | doc Task 1; OpenSearch security off (doc §6.2.1) |
| 13 | Every published port now 127.0.0.1 (B09) | ✓ | real `grep -n` output, all 7 lines |
| 14 | arXiv fetcher answers (B10) | ⚑ PLAN | Stage 2 not built. Framed as "next stage, I'm writing…" |
| 16 | OllamaClient on screen (B14) | ✓ excerpt | verbatim minus `import logging`, `from typing import Any`, `logger`, docstring; the `AsyncClient(...)` line wrapped. Unhighlighted by design — the viewer evaluates it |
| 15 | Title "Sixty Patterns" | ⚑ rhetorical | not a count; contrast device only |
