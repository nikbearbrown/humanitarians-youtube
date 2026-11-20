# Guardrails and Evals

*Agentic AI: From the Loop to MCP* · Friday 2026-09-18
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> You cannot read every run, so you must be able to score one. Evals are the stopping rule for the builder, not a quality badge.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `GuardrailsAndEvals_AdwaitChangan_2026-09-18.mp4` | 3840×2160 (16:9) | ~3:27 |
| `short/GuardrailsAndEvals_AdwaitChangan_2026-09-18-short.mp4` | 2160×3840 (9:16) | ~2:25 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Opens by pricing the obvious plan. Reviewing one run carefully takes about ninety seconds, and that constant does not shrink with volume, so a thousand runs a day costs twenty five human hours in a twenty four hour day. Sampling is then tested rather than waved away: five percent of a two percent failure rate leaves nineteen failures a day that nobody sees, and the sample still looks clean. Raising the sample buys back failures only by buying back the hours it was supposed to save. The way out is to change the question from *did a human read it* to *would anything have noticed*, because a check costs the same at any volume.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `evals.py` | **Runnable.** Every figure on screen is printed by it. `python3 evals.py` |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
