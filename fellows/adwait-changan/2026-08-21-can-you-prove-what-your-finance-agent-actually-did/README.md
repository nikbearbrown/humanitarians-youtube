# Can You Prove What Your Finance Agent Actually Did?

**Fellow:** Adwait Changan · **this week** · **Project:** Mycroft Finance Investigator
**Voice:** Kokoro `am_onyx` ("Onyx, in for Humanitarians AI") · **Channel:** @HumanitariansAI
**Builder:** `cli-explainer` · **Register:** Pragmatist · **Aspect:** 16:9 · **15 beats, ~4.5 min**

The investigator's evidence — validated data, deterministic math, adversarial evaluations,
scenario analysis, an open review gate — was spread across dozens of files. This week's
`bundle.py` turns it into one reproducible, auditable package. Before copying a single file it
hash-validates the whole chain (run ID, validation result, review-request hash, evaluation-case
hash, scenario-plan hash, raw + verified data hashes). It then packages **54 artifacts** with
`manifest.json`, `manifest.sha256`, and `REVIEW.md`. An independent `verify-bundle` recomputes
every hash → `INTEGRITY_MATCHED_HUMAN_REVIEW_OPEN`, and seven tamper cases are rejected. **9 bundle
tests; 41 passing total; both GitHub CI checks green** (PR #17).

**Honesty:** SHA-256 proves file integrity — not identity, adequacy, or human approval. Recipe stays
`DRAFT`; release stays `BLOCKED_PENDING_HUMAN_REVIEW`; five human gates stay open (materiality,
causal explanation, evaluation adequacy, scenario approval, distribution).

## Files
- `beat_sheet.json` (source of truth) · `FLOW-REVIEW.md` (watch-free flow + Codex prompt)
- `PEDAGOGY.md` · `FACTCHECK.md` · `SOURCES.md` · `BUILD-PROMPT.md` · `BUILD-LOG.md` · `_qc/REPORT.md`, `qc-sheet.png`

**Git note:** `*.mp4`/`*.mp3` gitignored. Rendered master delivered as
`CanYouProveWhatYourFinanceAgentActuallyDid_AdwaitChangan_2026-08-21.mp4`.
