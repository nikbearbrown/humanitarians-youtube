# Planning and Decomposition

*Agentic AI: From the Loop to MCP* · Friday 2026-09-04
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> Planning helps when steps are expensive and helps nothing when they are cheap. The plan is only worth its call if the world holds still.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `PlanningAndDecomposition_AdwaitChangan_2026-09-04.mp4` | 3840×2160 (16:9) | ~3:41 |
| `short/PlanningAndDecomposition_AdwaitChangan_2026-09-04-short.mp4` | 2160×3840 (9:16) | ~2:35 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Prices a plan instead of assuming it is good practice. When nothing goes wrong, planning first costs nine calls against sixteen, so it saves seven. Then the world moves: if something changes at step one the plan is discarded and the advantage is gone entirely, and the later the change lands the more of the plan survives. Three conditions have to hold together for a plan to pay, and the truth table shows only one of the four rows reaching PLAN.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `planner.py` | **Runnable.** Every figure on screen is printed by it. `python3 planner.py` |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
