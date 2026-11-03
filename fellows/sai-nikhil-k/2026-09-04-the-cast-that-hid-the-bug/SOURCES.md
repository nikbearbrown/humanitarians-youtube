# SOURCES — The Cast That Hid the Bug

Reel: `claude-sai-the-cast-that-hid-the-bug` · Scout · production hardening

## Primary source

| Source | How it is used |
|---|---|
| `github.com/nikhil-kunapareddy/ScoutAI` | The subject. Cloned at `c69c5b2` (merge of PR #1). |
| commit `6aea97e` "Production hardening: bug fixes, OOP restructure, tests, container" | The week being reported. Supplies B02 (the annotations bug), B03 (deployment), B05 (the recap). |
| `scout/tools/registry.py` `_parameter_schema()` | B02. The docstring there states the bug and the fix in the author's own words. |
| `README.md` § Deployment / § Ping-to-wake | B03. The Socket-Mode-has-no-port argument and the three missing pieces. |
| `scout/core/backends/base.py`, `scout/core/agent.py` | B05. `ChatBackend` and `ConversationalAgent` — the two interfaces named in the verdict. |

## Numbers on screen — every one measured locally, not quoted

The README claims "170 tests". It was **verified** rather than repeated:

| Claim on screen | How it was checked | Result |
|---|---|---|
| 170 tests pass in 0.26s | `pytest` in a fresh venv from `requirements*.txt` | `170 passed in 0.26s` |
| no network, no credentials | Suite run with no `.env` present | passed |
| 6 job sources | `ls scout/tools/jobs/` minus `__init__.py` | amazon, google, netflix, greenhouse, northeastern, boston_university = 6 |
| Greenhouse × 8 boards | `len(greenhouse.BOARDS)` imported live | 8 — Databricks, Airbnb, Stripe, Pinterest, Reddit, Coinbase, Dropbox, Robinhood |
| 5 correctness bugs | Counted from the commit message's "Correctness fixes:" list | registry, netflix, agent, settings, slack = 5 |
| "Google — no API" | README operational notes; Google publishes no jobs API, hence no posting dates | stated by the author |

Also verified but not shown: `ruff check .` → `All checks passed!`; 3 model backends
(`anthropic`, `ollama`, `llama`); 3 agent specs (`bigtech`, `resume`, `university`);
~4,100 lines of Python.

## Honesty log

- **No dollar figures on screen.** The README estimates ECS Fargate at ~$6/month and
  a `t4g.nano` at ~$3–5/month. These are the author's estimates, not measured bills,
  so they are kept out of the reel entirely (DOUBLE-CHECK LAW).
- **No "quarter of a second" rounding on screen.** The artifact line says 0.26 seconds,
  the measured figure. The narration says "a quarter of a second", which is a spoken
  approximation of the same measured number, not a second claim.
- **The bug is described, not benchmarked.** The reel says the model was told `days` and
  `limit` were strings. That is what the schema contained; the reel does **not** claim a
  measured behavioural regression (e.g. "the model passed bad values N% of the time"),
  because that was never measured.
- **"Next week, persistence"** is a stated intention, not a shipped feature. Conversation
  history and the parsed profile are in memory today — the README's own Ping-to-wake
  section lists persistence as one of the three things that do not exist yet.
- **Unverified / out of scope:** nothing in the reel depends on the live job endpoints
  actually responding today. The six sources are described by their integration method,
  which is read from the code, not from a live call.
