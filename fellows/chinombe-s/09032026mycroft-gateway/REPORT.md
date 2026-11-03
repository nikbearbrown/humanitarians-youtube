# Sprint 2 — Connecting the three model tiers

- **Week:** 31 Aug – 4 Sep 2026 · 
- **Project:** Mycroft — Adaptive Model Routing & Inference Gateway
- **Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/f8c80ee081c0cf1411b0dcc0592a06ec4d79a384

- **Video:** 
- **Drive:** https://drive.google.com/drive/folders/1pHXg01GKXl1-iEPKqCr3O4BUJwsPSCBk?usp=sharing
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [KV Cache](../09032026how-kv-cache-works/)

## What this sprint was for

Sprint 1 built a logbook with nothing to log. This sprint connects real models to
it: one client that talks to every tier the same way, so cost, latency and tier
are recorded automatically rather than by a caller who remembers to. It also made
this repository's first live API calls  one per tier, each watched by a human as
a gate.

## What was built

| File | What it does |
|---|---|
| `adapters/base.py` | The adapter contract, plus the failure taxonomy: which provider errors are worth retrying and which are not. |
| `adapters/fake.py` | A scriptable adapter that never touches the network  every later test of the client, router and retry logic runs against it. |
| `adapters/groq.py` | The live adapter. Imports the provider SDK lazily and strips inline reasoning from responses. |
| `client.py` | The one door. No public method returns a response without having written a logbook row first  including for failures. |
| `tiers.py` + `tiers.json` | The tier ladder: cheap, mid, strong, as names. Policy refers to tier names, never to models, so a model can be replaced without touching routing. |
| `first_live_call.py` | The gate script: one live call per tier, with the answer checked and the cost recomputed independently. |

Tiers gated live on Groq: `openai/gpt-oss-20b` (cheap), `openai/gpt-oss-120b`
(mid), `qwen/qwen3.6-27b` (strong).

## Results

**Six live calls, $0.00138 total.** Every successful call's cost was recomputed
from the price table and matched the logged row exactly — the first evidence that
Sprint 1's accounting is right and not merely self-consistent.

**A real authentication failure produced a logged row and no crash.** Tested
deliberately, not hoped for.

**Sticker prices do not predict real tier costs.** Published ratios are 2x
(cheap→mid) and 10x (cheap→strong). Observed: **1.4x and 19–26x**. These models
decide how much to say, so cost follows output length, not the rate card.

**The same prompt produces different amounts of work.** The strong model's
reasoning length varied **35% run to run** on an identical prompt, and it used
245 of its 256-token budget — eleven tokens from being truncated silently.

**Input token counts differ per model** (78 versus 17 for the same prompt), which
is why the router later measures input length in characters.

**`outcome: ok` does not mean the answer is usable.** The strong model returned
its reasoning inline in `<think>` tags ahead of the answer and passed every check
in the gate script. Fixed with `strip_reasoning()` in the adapter plus a real
answer check; the gate script, which had exited 0 while printing problems, now
exits 1.

## What this sprint does *not* do

- No routing decision is made anywhere. The caller still names a tier.
- No quality measurement: a call that returns text is recorded as `ok`.
- The price table now holds published rates for the models in use, but the repo's
  previously evidenced Llama models had **no published per-token rate**, so the
  ladder moved to models that could be priced honestly rather than estimated.

## Evidence

- `logs/gateway/first-live-call.jsonl` — 6 rows, every field populated
- `scripts/gateway/FINDINGS.md` section 5 — what the first live calls showed
- `logs/RUN_LOG.md`, entry dated 2026-09-10 (calls 1–3 backfilled and labelled)
- Commit `f8c80ee`

## Limits and open items

- **No progress video was recorded for this week.** The Drive folder holds the
  week's source material; the video is missing, not misplaced.
- Provider console usage was not reconciled against the logged costs — the one
  check this code cannot perform on itself.
- All three tiers sit behind one provider and one credential: a rate limit or an
  auth failure takes out the whole ladder rather than degrading it.
- A credential used in this sprint needs rotating (recorded in the project's
  internal run log, not here).
- `f8c80ee` committed a runtime `.lock` sidecar that should be ignored, and again
  carried no RUN_LOG entry at the time.
