# When Not to Build an Agent

*Agentic AI: From the Loop to MCP* · Friday 2026-10-23
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> Three conditions, and all of them have to hold. A failed condition is a specification for what to build instead, not a rejection.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `WhenNotToBuildAnAgent_AdwaitChangan_2026-10-23.mp4` | 3840×2160 (16:9) | ~3:30 |
| `short/WhenNotToBuildAnAgent_AdwaitChangan_2026-10-23-short.mp4` | 2160×3840 (9:16) | ~2:23 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Proposes three conditions — doing rather than describing, cheap to undo, checkable without reading every step — and then scores six ordinary tasks against them instead of arguing in the abstract. Two pass. Each condition fails exactly twice, so there is no single villain to fix, which is itself the finding. Two of three is named as the dangerous score, because it feels like success while you are building it. The closing move is the useful one: the condition that failed tells you what to build first.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `decide.py` | **Runnable.** Every figure on screen is printed by it. `python3 decide.py` |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
