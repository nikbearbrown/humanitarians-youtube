# The Confused Deputy

*Agentic AI: From the Loop to MCP* · Friday 2026-10-16
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> An agent that acts, plus text nobody controls, is an old security bug with a new surface. The text has no permissions. The agent has yours.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `TheConfusedDeputy_AdwaitChangan_2026-10-16.mp4` | 3840×2160 (16:9) | ~3:31 |
| `short/TheConfusedDeputy_AdwaitChangan_2026-10-16-short.mp4` | 2160×3840 (9:16) | ~2:22 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit: kept beats carry the parent's
narration unchanged and only the outro is new. Masters go to the Drive. They are never
committed here.

## What the video does

Takes two ordinary ingredients and shows that the combination is the problem. An operator instruction and a fetched ticket arrive in the same context as the same kind of thing, and nothing in that context marks which one was authorised. The tool then runs with the agent's permissions rather than the text's. The defences are ranked honestly: none of them detect an injection, all of them limit it, and only a human before the irreversible step holds when detection fails.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `deputy.py` | **Runnable.** Every figure on screen is printed by it. `python3 deputy.py` |
| `PEDAGOGY.md` | GATE P — signed narration and structure review |
| `FACTCHECK.md` | Claim-by-claim audit, including corrections made before shipping |
| `SOURCES.md` | Captured output and provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC. Written locally; `_qc/` is git-ignored repo-wide, so it is not in this checkout. |
| `short/` | The 9:16 derivative — its own beat sheet and its own signed gate |

## Rebuild

See `BUILD-PROMPT.md`. Nothing in this folder publishes, uploads or notifies anyone.
