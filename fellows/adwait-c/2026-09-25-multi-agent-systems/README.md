# Multi-Agent Systems

*Agentic AI: From the Loop to MCP* · Friday 2026-09-25
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> More agents buys parallelism and specialisation, and charges coordination and reliability. Most multi-agent wins are one agent with better tools.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `MultiAgentSystems_AdwaitChangan_2026-09-25.mp4` | 3840×2160 (16:9) | ~3:34 |
| `short/MultiAgentSystems_AdwaitChangan_2026-09-25-short.mp4` | 2160×3840 (9:16) | ~2:30 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Prices the second agent instead of assuming it helps. Coordination links grow with topology, and reliability compounds downward whenever every step must succeed: eight agents at ninety five percent each finish the chain sixty six percent of the time, and nobody failed individually. To merely match one agent at ninety five percent, eight agents must each hit 99.36 percent. The honest exception is named: if the work genuinely parallelises, or the agents vote, the arithmetic inverts.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `agents.py` | **Runnable.** Every figure on screen is printed by it. `python3 agents.py` |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
