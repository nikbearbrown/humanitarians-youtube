# FLOW-REVIEW — What-If Analysis Without AI Guessing

Watch-free projection for an AI reviewer (Codex/Claude) or a human. Ground truth is
`beat_sheet.json`; real code under the Mycroft project root (see `SOURCES.md`).

- **Fellow / narrator:** Adwait Changan · Onyx (`am_onyx`) · @HumanitariansAI · Pragmatist
- **this week** · 14 beats, ~4 min · 16:9
- **Thesis:** give finance teams scenario analysis without letting the agent turn assumptions into
  forecasts or recommendations — the engine calculates; the human decides.

## The flow
| # | Act | Visual | Beat's job |
|---|---|---|---|
| B00 | COLD OPEN | ClaudeComposerAsk | The problem + the answer: bind to baseline, explicit assumptions, stamp every output. |
| B01 | Problem | CwcConceptCard | "Assumptions aren't forecasts." |
| B02 | Problem | MedhavyConceptCard | The failure: an assumption silently reframed as a forecast/recommendation. |
| B03 | Contract | CwcConceptCard | Act title — `scenario.py`. |
| B04 | Contract | ClaudeCodeBeat | Real baseline hash verification (`_load_baseline`). |
| B05 | Contract | ClaudeScienceLayerStack | Two methods only; lineage; illegal inputs rejected; deterministic. |
| B06 | Contract | ClaudeCodeBeat | Real deterministic arithmetic + negative guard (`_scenario_result`). |
| B07 | Exercises | CwcConceptCard | Act title — from baseline $230,000. |
| B08 | Exercises | ClaudeWindow | Three what-ifs: $275,500 / $250,000 / $252,300. |
| B09 | Exercises | ClaudeWindow | Decision pack labels: SIMULATION_NOT_FORECAST / NONE / HUMAN_REQUIRED / PENDING. |
| B10 | Exercises | MedhavyConceptCard | Proven not promised — 32 tests. |
| BVDT | VERDICT | ClaudeVerdictArtifact | Calculate the scenario, don't choose the future + disclosures. |
| BHTF | YOUR TURN | ClaudeComposerAsk | "Should an agent calculate the scenario — or decide which future the business should choose?" |
| BOUT | OUTRO | ClaudeTitleOutro | Title restate. |

## Confirmed facts (must stay exact)
Baseline actual EBITDA $230,000 · +5% revenue → $275,500 (+$45,500) · −$20,000 COGS → $250,000
(+$20,000) · balanced exercise → $252,300 (+$22,300) · AMOUNT / PERCENT_OF_ACTUAL only ·
rejects duplicate/non-finite/negative · deterministic, no external LLM · SIMULATION_NOT_FORECAST ·
Recommendation NONE · Decision HUMAN_REQUIRED · PENDING_HUMAN_REVIEW · **32 project tests this week**.

## Review prompt (paste to Codex / a reviewer)
> Review the flow of this 14-beat explainer (`FLOW-REVIEW.md` + `beat_sheet.json`). You cannot watch
> the video. Check: (1) logical flow problem → contract → exercises; (2) every code excerpt matches
> the real files in `SOURCES.md` verbatim; (3) the three results ($275,500 / $250,000 / $252,300)
> follow from `sample-scenarios.json` + the arithmetic; (4) the "calculate, don't decide" boundary is
> shown, not asserted; (5) the four labels are present and exact; (6) the 32-tests figure; (7) pacing
> for the code beats (B04, B06) and BVDT (~30s). Return: beat | issue | severity | fix. Do not invent
> facts; mark anything needing the repo as VERIFY.
