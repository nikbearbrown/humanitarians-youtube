# Tools: Giving a Model Hands

**Episode 3 of 10** · *Agentic AI: From the Loop to MCP* · Friday 2026-08-21
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> A tool is not a function you expose — it is a contract you write in English. The model
> reads the contract, never the code. So the description *is* the tool.

## Master

`ToolsAndFunctionCalling_AdwaitChangan_2026-08-21.mp4` — 3840×2160 clean master,
~3 min 17 s, 13 beats, zero slates.
Review cut with beat labels: `…-slate.mp4`.

## What the episode does

Episodes 1 and 2 built a loop and made its feedback honest, and both took "it calls a tool"
for granted. This is where that gets paid for — with a fact that lands badly for programmers:
the function is the one part of your tool the model never receives.

Act 1 prints the actual payload and ends on the line `not sent — the function body`. Act 2
shows the fourteen real lines that build that payload, names the three questions a
description has to answer, and then runs a controlled A/B: the same function body with a
13-character docstring and a 292-character one, with `function bodies identical: True` on
screen as the control. Act 3 charges for it — four prices every tool you add will keep
charging — and hands over the rule.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else is derived from it. |
| `tools.py` | **Runnable.** `to_schema()` is shown verbatim in B05; B03 and B07 are its real printed output. `python3 tools.py` |
| `PEDAGOGY.md` | GATE P — the signed narration/structure review |
| `FACTCHECK.md` | 12 claims audited; rows 3–7 verified by execution or count |
| `SOURCES.md` | Captured program output + provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds this cut end to end |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC findings |

## Beat map

| Beat | Act | Pattern | What you watch |
|---|---|---|---|
| B00 | Cold open | ClaudeComposerAsk | The ask, answered in three lines |
| B01 | Act 1 | CwcConceptCard | "You Are Writing Documentation" |
| B02 | Act 1 | ClaudeScienceSourceFlow | The three things that cross the wire |
| B03 | Act 1 | ClaudeWindow | **The real payload** — ending on `not sent — the function body` |
| B04 | Act 2 | CwcConceptCard | "The Description Is the Tool" |
| B05 | Act 2 | ClaudeCodeBeat | `to_schema()` — fourteen real lines |
| B06 | Act 2 | ClaudeScienceLayerStack | What it returns / when to use it / **when NOT to** |
| B07 | Act 2 | ClaudeWindow | **The A/B** — 13 chars vs 292, identical bodies |
| B08 | Act 3 | ClaudeScienceChipGrid | Four prices every tool charges |
| B09 | Act 3 | ClaudeScienceLayerStack | The rule for writing one |
| BVDT | Verdict | ClaudeVerdictArtifact | A tool is a contract, not a function |
| BHTF | Your turn | ClaudeComposerAsk | The viewer's prompt, read aloud |
| BOUT | Outro | ClaudeTitleOutro | Title restate · Episode 3 of 10 |

Nine distinct patterns across 13 beats — the widest spread in the series so far.

## Continuity

`tools.py` carries forward the *same* `read_file` and `count_rows` the earlier episodes
call. The functions are unchanged; only what is written above them changes — which is the
episode's whole argument. It also pays a debt: Episode 2 established that the error is the
observation, and `read_file`'s docstring now says so to the model.

This episode is also the setup for Episode 9. MCP standardises exactly this seam.

## Rebuild

```bash
source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate
cd /Users/adwaitchangan/Study/Brutalist/brutalist.art
REEL=/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-08-21-tools-and-function-calling
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 runtime/scripts/compile.py "$REEL" --review
./art final "$REEL"
```

Cost: **$0.00**.

## Status

Built, visually QC'd, master rendered. **Not published.**

Next: Episode 4, *Memory and Context* (2026-08-28) — agents don't forget, they overflow.
