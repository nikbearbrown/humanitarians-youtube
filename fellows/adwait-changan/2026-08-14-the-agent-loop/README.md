# The Agent Loop

**Episode 2 of 10** · *Agentic AI: From the Loop to MCP* · Friday 2026-08-14
Humanitarians AI Fellows · Adwait Changan · @HumanitariansAI

> The loop only works because the observation is real. Take the honest observation away and
> you do not have an agent iterating — you have one guess, repeated at full price.

## Master

`TheAgentLoop_AdwaitChangan_2026-08-14.mp4` — 3840×2160 clean master, ~3 min 25 s,
13 beats, zero slates.
Review cut with beat labels: `TheAgentLoop_AdwaitChangan_2026-08-14-slate.mp4`.

## What the episode does

Episode 1 defined the loop from outside. This one goes inside a single pass and asks which
part is actually doing the work — and the answer is deliberately not the reasoning. Act 1
stops drawing the loop and *runs* it, printing one real pass where the same failed call is
recorded two ways: once as `ok`, once carrying `FileNotFoundError` verbatim. Act 2 makes the
case that the observation is load-bearing, shows the seven real lines that produce a good
one, and then runs the lazy version to its step budget — eight identical passes, learning
nothing, on screen. Act 3 names the four ways a loop dies and hands the three stopping rules
back to the builder, where they belong.

## Files

| File | What it is |
|---|---|
| `beat_sheet.json` | The reel. Everything else is derived from it. |
| `trace_loop.py` | **Runnable.** `record()` is shown verbatim in B06; B03 and B07 show this file's real printed output. `python3 trace_loop.py` |
| `PEDAGOGY.md` | GATE P — the signed narration/structure review |
| `FACTCHECK.md` | Claim-by-claim audit; rows 3, 5, 8, 9 verified by execution |
| `SOURCES.md` | Captured program output + provenance |
| `BUILD-PROMPT.md` | Paste-ready prompt that rebuilds this cut end to end |
| `BUILD-LOG.md` | What was run, and what QC found |
| `_qc/REPORT.md` | Frame-level visual QC findings |

## Beat map

| Beat | Act | Pattern | What you watch |
|---|---|---|---|
| B00 | Cold open | ClaudeComposerAsk | The ask, answered in three lines |
| B01 | Act 1 | CwcConceptCard | "One Turn, Slowed Down" |
| B02 | Act 1 | ClaudeScienceSourceFlow | Thought / Action / Observation — only one is reality |
| B03 | Act 1 | ClaudeWindow | **A real trace**: the same failed call, recorded two ways |
| B04 | Act 2 | CwcConceptCard | "The Observation Is Load-Bearing" |
| B05 | Act 2 | ClaudeScienceLayerStack | What was called / what came back / **what went wrong** |
| B06 | Act 2 | ClaudeCodeBeat | `record()` — seven real lines |
| B07 | Act 2 | ClaudeWindow | **The lazy loop run to its budget** — eight identical passes |
| B08 | Act 3 | ClaudeScienceChipGrid | Four ways a loop dies |
| B09 | Act 3 | ClaudeScienceLayerStack | The three stopping rules you write yourself |
| BVDT | Verdict | ClaudeVerdictArtifact | The observation is the load-bearing part |
| BHTF | Your turn | ClaudeComposerAsk | The viewer's prompt, read aloud |
| BOUT | Outro | ClaudeTitleOutro | Title restate · Episode 2 of 10 |

## Continuity

`trace_loop.py` extends Episode 1's `agent_loop.py` — same loop, same tools, same
`max_steps = 8` (which is where "eight times" comes from). Only the recording of the
observation changes. That is the playlist's rule: one running artifact, extended weekly,
never rewritten.

## Rebuild

```bash
source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate
cd /Users/adwaitchangan/Study/Brutalist/brutalist.art
REEL=/Users/adwaitchangan/Study/Brutalist/humanitarians-youtube/fellows/adwait-changan/2026-08-14-the-agent-loop
python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
python3 runtime/scripts/remotion_scenes.py "$REEL"
python3 runtime/scripts/compile.py "$REEL" --review
./art final "$REEL"
```

Cost: **$0.00**.

## Status

Built, visually QC'd, master rendered. **Not published.**

Next: Episode 3, *Tools: Giving a Model Hands* (2026-08-21) — why the description you write
matters more than the code you write.
