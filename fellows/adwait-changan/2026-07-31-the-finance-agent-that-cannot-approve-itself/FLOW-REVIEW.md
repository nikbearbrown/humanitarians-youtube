# FLOW-REVIEW — The Finance Agent That Cannot Approve Itself (Week 31)

A watch-free projection of the cut for an AI reviewer (Codex/Claude) or a human. Ground truth
is `beat_sheet.json`; the real code lives under the Mycroft project root (see `SOURCES.md`).

- **Fellow / narrator:** Adwait Changan · Onyx (`am_onyx`) · @HumanitariansAI · Pragmatist
- **Week 31** (July 27–31, 2026) · 15 beats, ~4.5 min · 16:9
- **Thesis:** a finance agent can compute a verified variance and gather evidence, but it
  **cannot approve its own explanation** — approval is a human gate enforced in code.

## The flow

| # | Act | Visual | Beat's job |
|---|---|---|---|
| B00 | COLD OPEN | ClaudeComposerAsk | The sharp question, answered: approval is a human gate (bound to run+SHA-256; agents rejected; append-only; 7 new tests, 19 passing). |
| B01 | Problem | CwcConceptCard | "Computing a number is safe. Blessing it is not." |
| B02 | Problem | ClaudeWindow | The verified run: 43 rows/6 datasets, $350k→$230k, −$120k, 7 steps, 41 evidence — verified, not approved. |
| B03 | Problem | MedhavyConceptCard | The trap: if the agent approves its own explanation, the human-control boundary is gone. |
| B04 | Review Gate | CwcConceptCard | Act title — `review.py`. |
| B05 | Review Gate | ClaudeCodeBeat | Real `build_review_request()`: OPEN, bound to run_id + SHA-256, reviewer blank, "cannot approve itself". |
| B06 | Review Gate | ClaudeScienceLayerStack | The four rules: bound to run; rejects agents + unknown evidence; APPROVE earned; append-only. |
| B07 | Review Gate | ClaudeCodeBeat | Real enforcement: `AGENT_IDENTITIES` rejection + APPROVE requirements. |
| B08 | Review Gate | ClaudeWindow | `review-decision.schema.json` required fields + enums. |
| B09 | Gate Holds | CwcConceptCard | Act title. |
| B10 | Gate Holds | ClaudeWindow | CLI: `review-request` → OPEN; self-approval → rejected; named human + evidence → CLEARED (append-only). |
| B11 | Gate Holds | MedhavyConceptCard | 7 new review-control tests → 19 passing this week. |
| BVDT | VERDICT | ClaudeVerdictArtifact | The boundary + disclosures (local, no LLM, sample OPEN, nothing fabricated). |
| BHTF | YOUR TURN | ClaudeComposerAsk | "What controls would you require before allowing a finance agent to publish its findings?" |
| BOUT | OUTRO | ClaudeTitleOutro | Title restate. |

## Confirmed facts (must stay exact)
43 data rows · 6 synthetic datasets · Budget EBITDA $350,000 · Actual $230,000 · Variance
−$120,000 · 7 tool steps · 41 evidence references · 7 new review-control tests · 19 passing
this week. Local deterministic, **no external LLM in the runtime**. Sample review request
remains **OPEN**; nothing fabricated.

## Review prompt (paste to Codex / a reviewer)
> Review the narrative and logical flow of this 15-beat explainer (`FLOW-REVIEW.md` +
> `beat_sheet.json`). You cannot watch the video. Check: (1) logical flow across problem →
> gate → proof; (2) every code excerpt matches the real files in `SOURCES.md` (verbatim, not
> paraphrased) — flag any drift; (3) the "cannot approve itself" claim is enforced by the code
> shown (AGENT_IDENTITIES, APPROVE requirements, append-only), not just asserted; (4) the
> disclosures (local / no external LLM / sample OPEN / nothing fabricated) are present and
> unambiguous; (5) the test claim (7 new, 19 total) matches `tests/test_review.py`;
> (6) pacing risks for dense beats (B05, B07 code; BVDT ~30s). Return: beat | issue | severity
> (blocker/major/minor) | concrete fix. Do not invent facts; mark anything needing the repo
> to confirm as VERIFY.
