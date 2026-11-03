# BUILD-LOG — Episode 2, "The Agent Loop"

Built 2026-08-13 (episode dated Friday 2026-08-14). Toolkit: `brutalist.art` pared-down
edition, skill `ai-explainer`. **Total cost: $0.00.**

## Environment

Same as Episode 1 — Python 3.12.6 via `brutalist.art/.venv`, ffmpeg 8.1.2, Node v22.23.1,
Kokoro `am_onyx` local.

## Sequence

| Step | Result |
|---|---|
| Wrote + ran `trace_loop.py` | Real printed output captured for B03. Extends Episode 1's `agent_loop.py` — same loop, same tools, same `max_steps = 8` |
| Authored `beat_sheet.json` | 13 beats, 3 acts, zero slates expected |
| Gate P (`PEDAGOGY.md`) | Signed; audio unlocked |
| Audio | 13 MP3s, 204.8 s total |
| Remotion render | 13/13 beats |
| Review cut | 204.8 s, 13/13 filled, **0 slates** |
| **Visual QC** | 3 defects found (3 MAJOR) — see `_qc/REPORT.md` |
| Extended `trace_loop.py` with `run_lazy()` + re-ran | Produced the real eight-pass log now shown in B07 |
| Fixes + re-render | B03, B07 re-rendered |
| Clean master | `./art final` → 3840×2160, 204.8 s |

## Verification actually performed

- **The source runs.** `python3 trace_loop.py` executed; all three printed blocks captured
  into `SOURCES.md`. B03 and B07 show that output; B06 shows `record()` verbatim.
- **"The comment on line five" was counted, not estimated** — against the rendered frame,
  not just the file. An earlier narration draft said "nine lines"; the shipped line says
  "seven", which is what the code block actually contains.
- **The frames were read.** All three defects came from reading PNGs; the mp4 probe
  reported a healthy 204.8 s file throughout.

## The mistake worth recording

The first patch to `beat_sheet.json` for B03 was **silently reverted**. The background
`remotion_scenes.py` run re-dumps the sheet when it exits, and the patch landed after the
last `media/*.mp4` file appeared but before that final dump. The beat then re-rendered with
the *old* props, and the render reported success.

It was caught only because the verification frame was opened and read — the numbering was
still there. Fixed by re-patching once the process had genuinely exited, and confirming the
write survived by re-reading the JSON before re-rendering.

*Rule for the next episode:* wait on the process, not on its output files; and after
patching a beat sheet, read it back before you trust it.

## Content change during QC

B07 was originally a `MedhavyConceptCard` asserting "one guess, repeated eight times."
That is the episode's central claim and it was being *told*. `trace_loop.py` gained
`run_lazy()`, which drives the real loop with the lazy recorder; because a lazy observation
carries no tool name, the decision function cannot tell what has been tried and picks the
same call every pass. The eight identical lines on screen are that program's real output.
FACTCHECK rows 8 and 9 were upgraded from "accurate" to **verified by execution**.

The repetition is not hard-coded. It falls out of the mechanism — which is the point.

## Toolkit change

Added an optional `numbered` prop (default `true`) to
`runtime/remotion/src/scenes/ClaudeWindow.tsx`, alongside the `width`/`fontSize` wiring done
during Episode 1. With `numbered: false` the lines render unnumbered, in mono, with
`whiteSpace: 'pre'` so column alignment survives — required for B03 and B07, which are
terminal output and were being rendered as numbered prose lists. Defaults unchanged.

## Status

Master rendered, QC clean, gates signed. **Not published.**
