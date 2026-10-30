# Grounding and Retrieval

*Agentic AI: From the Loop to MCP* · Friday 2026-09-11
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> Retrieval does not make an agent truthful. A citation you can check does, and only for the part a check can reach.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `GroundingAndRetrieval_AdwaitChangan_2026-09-11.mp4` | 3840×2160 (16:9) | ~3:40 |
| `short/GroundingAndRetrieval_AdwaitChangan_2026-09-11-short.mp4` | 2160×3840 (9:16) | ~2:37 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Four answers, each with a citation, run through the automatic check anyone would write. Two citations check out. One of those two is still false, and that is the whole lesson: the source is real, the quote is real, and the claim does not follow from it. A check can confirm that a quote exists in a named source. It cannot confirm that the quote supports the sentence built on top of it.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `grounding.py` | **Runnable.** Every figure on screen is printed by it. `python3 grounding.py` |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
