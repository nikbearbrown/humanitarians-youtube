# What Is MCP?

*Agentic AI: From the Loop to MCP* · Friday 2026-10-02
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> MCP turns an M×N integration problem into M+N by standardising the seam, not the model. It fixes the connection, never the content.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `WhatIsMCP_AdwaitChangan_2026-10-02.mp4` | 3840×2160 (16:9) | ~3:33 |
| `short/WhatIsMCP_AdwaitChangan_2026-10-02-short.mp4` | 2160×3840 (9:16) | ~2:24 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Counts connectors rather than describing a protocol. Five apps and ten tools is fifty connectors, each maintained separately; through a shared protocol it is fifteen. The property that matters is the derivative: one more tool costs one connector instead of one per app, and that number never grows. Then the case against is given its due. At small scale the protocol loses outright, and a bad tool description is bad in any protocol, because the seam was never the hard part.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `integrations.py` | **Runnable.** Every figure on screen is printed by it. `python3 integrations.py` |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
