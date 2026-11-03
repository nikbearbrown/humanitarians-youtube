# The Finance Agent That Cannot Approve Itself

**Fellow:** Adwait Changan · **this week** · **Project:** Mycroft Finance Investigator
**Voice:** Kokoro `am_onyx` ("Onyx, in for Humanitarians AI") · **Channel:** @HumanitariansAI
**Builder:** `cli-explainer` · **Register:** Pragmatist · **Aspect:** 16:9 · **15 beats, ~4.5 min**

This week adds the **human review gate**. The investigator can compute a verified EBITDA
variance and collect evidence — but it cannot approve its own explanation. In real
`review.py`, it may only *open* a review request (bound to the exact run by ID + SHA-256,
reviewer blank); clearing it requires a named human, an approved/replaced materiality
threshold, and an evidence-backed causal explanation. Agent identities are rejected, unknown
evidence is rejected, and recorded decisions are append-only. Demonstrated end to end (the
self-approval attempt fails; the human gate clears) and proven by **7 new review-control
tests — 19 passing this week**.

**Honesty:** local deterministic workflow, **no external LLM in the runtime**; the committed
sample review request remains **OPEN**; no human approval or causal explanation was fabricated.

## Files
- `beat_sheet.json` — the plan (source of truth) · `FLOW-REVIEW.md` — watch-free flow + Codex review prompt
- `PEDAGOGY.md` (Gate P) · `FACTCHECK.md` (code-bound) · `SOURCES.md` · `BUILD-PROMPT.md` · `BUILD-LOG.md`
- `_qc/REPORT.md`, `qc-sheet.png` — visual QC

**Git note:** `*.mp4`/`*.mp3` are gitignored — the source package rebuilds the video for free
with brutalist.art. Rendered master delivered separately as
`TheFinanceAgentThatCannotApproveItself_AdwaitChangan_2026-07-31.mp4`.
