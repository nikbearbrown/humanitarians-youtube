# Building a Tool Server

*Agentic AI: From the Loop to MCP* · Friday 2026-10-09
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> Three calls are the whole shape: list what exists, describe one in full, run it. The docstring you wrote for the next developer is what the machine reads.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `BuildingAnMCPServer_AdwaitChangan_2026-10-09.mp4` | 3840×2160 (16:9) | ~3:25 |
| `short/BuildingAnMCPServer_AdwaitChangan_2026-10-09-short.mp4` | 2160×3840 (9:16) | ~2:21 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Builds a working tool server end to end and connects a client that was told nothing in advance. The client asks what exists, gets two tools it had never heard of, asks for one contract in full, and calls it. Nobody wrote the tool list by hand: the names come from the registry and the descriptions come from the functions' own docstrings through `inspect.getdoc`, so the comment written for a human is the thing a machine uses to decide. The refusal is shown too, because discovery only means something if the published list is exhaustive.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `server.py` | **Runnable.** Every figure on screen is printed by it. `python3 server.py` |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
