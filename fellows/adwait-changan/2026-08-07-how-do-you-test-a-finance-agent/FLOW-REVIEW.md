# FLOW-REVIEW — How Do You Test a Finance Agent? Break the Books on Purpose

Watch-free projection of the cut for an AI reviewer (Codex/Claude) or a human. Ground truth is
`beat_sheet.json`; the real code lives under the Mycroft project root (see `SOURCES.md`).

- **Fellow / narrator:** Adwait Changan · Onyx (`am_onyx`) · @HumanitariansAI · Pragmatist
- **this week** · 14 beats, ~4 min · 16:9
- **Thesis:** a successful run is insufficient evidence — you must prove the controls **fail safely**,
  by breaking the books on purpose in isolated copies of the data.

## The flow
| # | Act | Visual | Beat's job |
|---|---|---|---|
| B00 | COLD OPEN | ClaudeComposerAsk | The question + the answer: plant defects, match expectations, 7/7, 24 tests. |
| B01 | Problem | CwcConceptCard | "A green run isn't proof." |
| B02 | Problem | MedhavyConceptCard | A control you never trip is a control you never tested. |
| B03 | Break the Books | CwcConceptCard | Act title — `evaluation.py`, isolated copies. |
| B04 | Break the Books | ClaudeCodeBeat | Real `run_evaluation()`: temp copy, `_apply_mutation`, observe, `_matches`. |
| B05 | Break the Books | ClaudeScienceChipGrid | The four reconciliation defects. |
| B06 | Break the Books | ClaudeCodeBeat | Real `_apply_mutation()` — one-row/one-dollar breaks. |
| B07 | Break the Books | ClaudeWindow | Two behaviors REJECTED (step-limit, self-approval) + valid baseline. |
| B08 | Scorecard | CwcConceptCard | Act title. |
| B09 | Scorecard | ClaudeWindow | `evaluate` → 7/7 matched, PASS, 24 tests. |
| B10 | Scorecard | MedhavyConceptCard | What it does NOT prove (confidence / certification / adequacy). |
| BVDT | VERDICT | ClaudeVerdictArtifact | Prove it fails safely + disclosures. |
| BHTF | YOUR TURN | ClaudeComposerAsk | "If your finance agent only works when the data is clean, have you really tested it?" |
| BOUT | OUTRO | ClaudeTitleOutro | Title restate. |

## Confirmed facts (must stay exact)
7 cases (1 baseline + 4 reconciliation defects + 2 behavioral) · 7/7 expectations matched ·
baseline −$120,000, 7 steps, 41 evidence, gate OPEN · SYNTHETIC_ADVERSARIAL_EVALUATION ·
**24 project tests this week** · adequacy PENDING_HUMAN_REVIEW · no external LLM.

## Review prompt (paste to Codex / a reviewer)
> Review the flow of this 14-beat explainer (`FLOW-REVIEW.md` + `beat_sheet.json`). You cannot
> watch the video. Check: (1) logical flow problem → harness → scorecard; (2) every code excerpt
> matches the real files in `SOURCES.md` verbatim — flag drift; (3) the 7 cases and their
> expectations match `evaluations/cases.json`; (4) the "fails safely" claim is demonstrated, not
> asserted; (5) the honesty disclaimer (only these synthetic cases; not confidence/certification/
> adequacy) is present; (6) the 24-tests figure and the −$120,000 baseline are correct; (7) pacing
> risks for the two code beats (B04, B06) and BVDT (~30s). Return: beat | issue | severity | fix.
> Do not invent facts; mark anything needing the repo as VERIFY.
