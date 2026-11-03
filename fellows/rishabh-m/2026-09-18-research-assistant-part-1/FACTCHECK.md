# FACTCHECK — research-assistant-part-1

Every claim spoken or shown, checked against the project repo
(`/Users/rishabh_hm/Documents/Projects/AI-Research-Assistant`) and its Stage 1
write-up. Checked 2026-09-18.

| # | Claim (beat) | Verdict | Evidence |
|---|---|---|---|
| 1 | Hundreds of new AI papers a week on arXiv (B02) | ✓ conservative | README "The Problem"; real volume is higher — "hundreds" is a floor, not a count |
| 2 | Keyword search misses same-meaning papers; chatbots may lack recent work (B02) | ✓ | README "The Problem" |
| 3 | RAG = retrieve relevant passages, give them to the model with the question (B03) | ✓ | standard definition; README summary |
| 4 | Target: daily arXiv fetch → PDF text → chunk/embed → store → hybrid search → local model → answer + sources (B04) | ✓ | README "End goal" + Stack table; `personal/assets/overview.png` |
| 5 | Ten boxes, the model is one (B04) | ✓ | count of the B04 diagram as drawn — a framing, not a metric |
| 6 | Five services: API, Postgres, Ollama, OpenSearch, Airflow (B01, B05) | ✓ | `compose.yaml`; Stage 1 doc goal line. (Dashboards + CloudBeaver are UIs, not counted) |
| 7 | All five health-checked (B01, B05) | ✓ | every one has a `healthcheck:` in `compose.yaml` |
| 8 | API `/health` checks database, model, search (B05, B08) | ✓ | `src/routers/ping.py` — `_check_database`, `_check_ollama`, `_check_opensearch` |
| 9 | One sample paper; search empty; small model pulled; test DAG only (B05) | ✓ | `scripts/seed_paper.py`; wrap-up diagram "(no indices yet)"; `llama3.2:1b`; `airflow/dags/test_dag.py` |
| 10 | `/ask` returns a mock answer (B05, B09) | ✓ | `src/routers/ask.py`; commit `2d81919` |
| 11 | Build order config → database → models → repository → routers (B06) | ✓ | Stage 1 doc, Guiding Principle 1 |
| 12 | One service at a time, one working commit per step (B07) | ✓ | Guiding Principles 2–3; the git log shown is verbatim `git log --oneline --reverse`, excerpted (7 of 19 commits omitted, emoji stripped) |
| 13 | Missing `opensearch` key in /health meant old code in the container (B07) | ✓ | Stage 1 wrap-up, "Debugging Techniques Learned" bullet 1 |
| 14 | No DB → API refuses to start; no search/model → starts, "degraded" (B08) | ✓ | README Key Learnings; `ping.py` `overall = "ok" if all(...) else "degraded"` |
| 15 | Health check asks whether the model is pulled (B08) | ✓ | `_check_ollama`: `if ollama.default_model not in models` |
| 16 | Adding fields later is safe; removing breaks clients (B09) | ✓ | README Key Learnings, "Contracts first" |
| 17 | `ask.py` on screen (B09) | ✓ trimmed | verbatim minus docstrings, `Field(description=…)` and one blank line per gap; labelled "(docstrings trimmed)" |
| 18 | Notebook is faster for testing whether RAG helps (B10) | ✓ interpretation | our judgment; flagged — the doc argues infra-first, this beat bounds it |

## Editorial decisions

- **Framed as "I'm building"** — true of the repo. The narration makes no claim that
  the architecture was invented from nothing; it describes what was built and why.
