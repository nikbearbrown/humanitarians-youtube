# FLOW-REVIEW — Building the Mycroft Finance Investigator

A self-contained description of the video's flow for an AI reviewer (Codex/Claude) or a
human to critique **without watching the video**. Ground truth is `beat_sheet.json` in this
folder; this file is a readable projection of it plus a review prompt. If they disagree,
`beat_sheet.json` wins.

- **Format:** Humanitarians AI Fellows — Weekly Research Report
- **Fellow / narrator of record:** Adwait Changan · **Voice:** Onyx (`am_onyx`), "in for Humanitarians AI"
- **Runtime:** 13 beats, ~3.3 min · **Aspect:** 16:9 · **Register:** Pragmatist
- **Thesis:** an agent can turn raw financial data into an *evidence-backed* variance
  analysis — and its value is as much in **where it stops** (business causation + sign-off
  stay with a human) as in the math it does.
- **Structure:** cold open → 3 acts (three weeks of work) → verdict → your-turn → outro.

## The flow, beat by beat

| # | Act | Visual (Remotion pattern) | ~sec | Beat's job |
|---|---|---|---:|---|
| B00 | COLD OPEN | ClaudeComposerAsk | 21 | Ask "walk me through it," answered in 3 lines: the whole arc (data → engine → agent). Names it a **local, evidence-driven agent**. |
| B01 | Act 1 — Synthetic Ledger | CwcConceptCard | 8 | Act title. "Before an engine can find a variance, it needs books to read." |
| B02 | Act 1 | ClaudeScienceChipGrid | 15 | The six synthetic datasets as a 3×2 chip grid: Budgets, Actuals, Ledger transactions, Customers, Headcount, Account mappings. |
| B03 | Act 1 | ClaudeScienceLayerStack | 17 | What makes it a dataset not a spreadsheet: Schema → Provenance → **Validation rules** (accent). 43 data rows validated across 6 synthetic datasets. |
| B04 | Act 2 — Deterministic Engine | CwcConceptCard | 8 | Act title. "Same inputs, same answer, every time. No model guessing in the middle." |
| B05 | Act 2 | ClaudeCodeBeat | 18 | **Real code** — `finance.py:162 ebitda_variance()`: revenue − costs, `variance = actual − budget`. |
| B06 | Act 2 | ClaudeWindow (artifact) | 18 | The sample number: Budget EBITDA $350,000; Actual $230,000; **Variance (actual − budget) −$120,000**. |
| B07 | Act 3 — The Investigator | CwcConceptCard | 8 | Act title. "A local, evidence-driven agent that decides what to look at — and writes down why." |
| B08 | Act 3 | ClaudeScienceSourceFlow | 19 | The loop: validated books → conditional tool selection → Mycroft Investigator; retains evidence + execution trace; writes **two reports (machine + human)**. Narration states **no external model in the loop**. |
| B09 | Act 3 | MedhavyConceptCard | 14 | The receipt: **7 tool steps, 41 unique evidence references, 12 tests passing**. Every claim traces to a record. |
| BVDT | VERDICT | ClaudeVerdictArtifact | 35 | "Evidence engine, not an oracle." 5 lines incl. the boundary + the **synthetic/DRAFT disclosure**. |
| BHTF | YOUR TURN | ClaudeComposerAsk | 21 | A build prompt centered on the boundary (design an engine that never states a cause it cannot trace). |
| BOUT | OUTRO | ClaudeTitleOutro | 9 | Title restate + @HumanitariansAI + "Onyx, in for Humanitarians AI." |

## Confirmed facts (must stay exact)

43 data rows · 6 synthetic CSV datasets · Budget EBITDA $350,000 · Actual EBITDA $230,000 ·
Variance −$120,000 (actual − budget) · 7 tool steps · 41 evidence references · 12 tests passing.
The agent is **local and evidence-driven, with no external LLM.** The report is a **synthetic
sample of a DRAFT workflow**; materiality, causal explanations, and distribution require a
named human finance reviewer.

## Review prompt (paste to Codex / a reviewer)

> You are reviewing the *narrative and logical flow* of a 13-beat explainer described in
> `FLOW-REVIEW.md` and defined in `beat_sheet.json` (same folder). You cannot watch the
> video; judge structure, logic, and copy only. Check and report, per beat where relevant:
> 1. **Logical flow** — does each beat set up the next? Any gap between data (Act 1),
>    engine (Act 2), and agent (Act 3)? Is the cold-open promise paid off by the verdict?
> 2. **Claim ↔ evidence** — every number in narration/visuals must match "Confirmed facts"
>    above and `SOURCES.md`/`FACTCHECK.md`. Flag any drift, rounding, or unstated sign.
> 3. **The boundary** — is "explains the math bridge, leaves causation + sign-off to a human"
>    stated clearly and not contradicted anywhere? Is the synthetic/DRAFT disclosure present
>    and unambiguous?
> 4. **No-external-LLM framing** — confirm nothing implies the agent uses an external model.
> 5. **B05 code fidelity** — does the shown `ebitda_variance()` excerpt teach the point
>    (variance = actual − budget) without implying capabilities it doesn't show? Is anything
>    in the narration (materiality, reconciliation, tracing) unsupported by the visible code
>    or by `SOURCES.md`?
> 6. **Pacing risks** — flag beats whose narration is too dense for the listed seconds
>    (esp. B05 ~18s of code talk, BVDT ~35s). Suggest cuts, not rewrites.
> 7. **Redundancy / gaps** — any two beats doing the same job; anything a first-time viewer
>    would still not understand after the outro.
> Return a table: beat | issue | severity (blocker/major/minor) | concrete fix. Do not
> invent facts; if something needs source confirmation, mark it VERIFY.
