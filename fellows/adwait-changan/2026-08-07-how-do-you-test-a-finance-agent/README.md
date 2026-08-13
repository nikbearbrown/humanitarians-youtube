# How Do You Test a Finance Agent? Break the Books on Purpose

**Fellow:** Adwait Changan · **this week** · **Project:** Mycroft Finance Investigator
**Voice:** Kokoro `am_onyx` ("Onyx, in for Humanitarians AI") · **Channel:** @HumanitariansAI
**Builder:** `cli-explainer` · **Register:** Pragmatist · **Aspect:** 16:9 · **14 beats, ~4 min**

A successful sample run is insufficient evidence — the system also has to prove its controls
**fail safely**. This week's evaluation harness (`evaluation.py`) runs each case in an isolated
temporary copy of the synthetic data and plants defects: four reconciliation breaks
(actuals↔ledger, unmapped account, customer↔revenue, headcount↔payroll) and two behavioral
overreaches (step-limit exceeded, agent self-approval). Each is checked against an explicit
expectation and contrasted with the valid baseline (−$120,000 EBITDA variance, 7 steps, 41
evidence, OPEN gate). The `evaluate` CLI produces a scorecard: **7 of 7 expectations matched**,
and the project suite reaches **24 passing tests**.

**Honesty:** deterministic synthetic adversarial evaluation, **no external LLM**. A pass verifies
**only these committed synthetic cases** — not model confidence, production certification, or human
adequacy approval (`adequacy: PENDING_HUMAN_REVIEW`).

## Files
- `beat_sheet.json` (source of truth) · `FLOW-REVIEW.md` (watch-free flow + Codex prompt)
- `PEDAGOGY.md` · `FACTCHECK.md` (code-bound) · `SOURCES.md` · `BUILD-PROMPT.md` · `BUILD-LOG.md`
- `_qc/REPORT.md`, `qc-sheet.png`

**Git note:** `*.mp4`/`*.mp3` gitignored. Rendered master delivered as
`HowDoYouTestAFinanceAgentBreakTheBooksOnPurpose_AdwaitChangan_2026-08-07.mp4`.
