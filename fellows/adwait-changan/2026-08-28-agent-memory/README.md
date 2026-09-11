# Memory and Context

*Agentic AI: From the Loop to MCP* · Friday 2026-08-28
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> An agent has no memory. It has a context budget it re-pays every single turn — so what
> looks like forgetting is overflow, and eviction is a design decision you either make or
> inherit.

## Deliverables

| File | Format | Runtime |
|---|---|---|
| `AgentMemory_AdwaitChangan_2026-08-28.mp4` | 3840×2160 (16:9) | ~3:31 |
| `short/AgentMemory_AdwaitChangan_2026-08-28-short.mp4` | 2160×3840 (9:16) | ~2:47 |

Both 4K. The 9:16 is a **derivative cut**, not a re-edit — kept beats reuse the parent's
audio unchanged; only the outro is new. Masters live on the Drive, never in this repo.

## What the video does

Opens by counting what an agent actually re-sends. Two tools plus one system prompt is 903
characters of instructions **before it has done anything**, and every observation adds 88 more.
The framework lands before any example: three things compete for one budget — fixed
instructions, growing history, and whatever room is left to answer in.

Then the objection everyone raises — *just use a bigger window* — gets tested rather than
waved away. Doubling the budget moves first overflow from turn 13 to 36 to 81, and never
removes it. History grows linearly, the budget does not.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else derives from it. |
| `context.py` | **Runnable.** Imports the previous video's `tools.py` unchanged, so the 903-char figure is a real measurement. `python3 context.py` |
| `PEDAGOGY.md` | GATE P — signed narration/structure review |
| `FACTCHECK.md` | Claim audit; every figure verified by execution |
| `SOURCES.md` | Captured program output + provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds both cuts |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC |
| `short/` | The 9:16 derivative — its own beat sheet and signed gate |

## Rebuild

```bash
source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate
cd /Users/adwaitchangan/Study/Brutalist/brutalist.art
REEL=.../fellows/adwait-changan/2026-08-28-agent-memory
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 runtime/scripts/compile.py "$REEL" --height 2160
python3 runtime/scripts/shorts.py "$REEL" --drop B04 B05 B06 B09 --handle "@HumanitariansAI"
python3 runtime/scripts/generate_audio_kokoro.py "$REEL/short"
python3 runtime/scripts/remotion_scenes.py "$REEL/short"
python3 runtime/scripts/compile.py "$REEL/short" --height 3840
```

Cost: **$0.00** — no API key at any step.

## Status

Both cuts rendered, QC clean, gates signed. **Not published, not uploaded.**
