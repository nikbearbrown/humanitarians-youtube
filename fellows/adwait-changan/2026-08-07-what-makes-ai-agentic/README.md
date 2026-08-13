# What Makes an AI "Agentic"

**Episode 1 of 10** · *Agentic AI: From the Loop to MCP* · Friday 2026-08-07
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> An agent is not a smarter model. It is the same model placed inside a loop that can
> act — and the loop, not the intelligence, is what you pay for.

## Master

`WhatMakesAIAgentic_AdwaitChangan_2026-08-07.mp4` — 1920×1080 review cut and 3840×2160
clean master, ~3 min 20 s, 13 beats, zero slates.
Review cut with beat labels: `WhatMakesAIAgentic_AdwaitChangan_2026-08-07-slate.mp4`.

## What the episode does

Opens on the word *agentic* being useless from overuse, then earns a definition instead of
asserting one. Act 1 strips a language model to its actual contract — prompt, generate,
return, stop — and shows a chatbot handed a real task producing a confident plan and no
action. Act 2 changes exactly one thing: it wraps the same model in a loop with tools,
shown first as an arc that closes on itself and then as eleven real lines of Python. Act 3
charges for it: six failure modes that arrive the instant the loop can act, and a
three-condition test for whether you should reach for one at all.

The episode deliberately never claims agents are better. It claims they are *different*,
and that the difference has a price.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else is derived from it. |
| `agent_loop.py` | **Runnable.** The loop shown verbatim in B06. `python3 agent_loop.py` → `rows in the sales file: 3` |
| `PEDAGOGY.md` | GATE P — the signed narration/structure review |
| `FACTCHECK.md` | Claim-by-claim audit + the anti-dating search |
| `SOURCES.md` | Provenance, toolkit, patterns used |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds this cut end to end |
| `BUILD-LOG.md` | What was actually run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC findings |

## Beat map

| Beat | Act | Pattern | What you watch |
|---|---|---|---|
| B00 | Cold open | ClaudeComposerAsk | The ask, answered in three lines |
| B01 | Act 1 | CwcConceptCard | "The Word Does Too Much" |
| B02 | Act 1 | ClaudeScienceLayerStack | Prompt / Generate / Return — one turn, then nothing |
| B03 | Act 1 | ClaudeWindow | A chatbot asked to book a flight: a plan, no action |
| B04 | Act 2 | CwcConceptCard | "Put It In a Loop" |
| B05 | Act 2 | ClaudeScienceSourceFlow | Think → Act → Observe, the arc closing on itself |
| B06 | Act 2 | ClaudeCodeBeat | `agent_loop.py` — eleven real lines |
| B07 | Act 2 | ClaudeScienceLayerStack | State / Feedback / **A stopping rule** |
| B08 | Act 3 | ClaudeScienceChipGrid | Six failure modes agency brings |
| B09 | Act 3 | MedhavyConceptCard | When to reach for an agent — three conditions |
| BVDT | Verdict | ClaudeVerdictArtifact | A loop, not a brain |
| BHTF | Your turn | ClaudeComposerAsk | The viewer's prompt, read aloud |
| BOUT | Outro | ClaudeTitleOutro | Title restate · Episode 1 of 10 |

## Rebuild

```bash
source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate
cd /Users/adwaitchangan/Study/Brutalist/brutalist.art
REEL=/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-08-07-what-makes-ai-agentic
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 runtime/scripts/compile.py "$REEL" --review
./art final "$REEL"
```

Cost: **$0.00**. No API key is used anywhere in this build.

## Status

Built, visually QC'd, master rendered. **Not published** — publishing is a separate,
explicit human decision and is not authorized by any gate in this folder.

Next: Episode 2, *The Agent Loop* (2026-08-14) — inside one pass, and why the observation
is the part holding it up.
