# SHOTLIST — Week 3 Progress

Typed work order. Eight beats, **no open media slots**. Two are registered Remotion compositions; six are Manim
scenes in `scenes.py`. Narration is `SCRIPT.md` verbatim: B00 is section 1, B01-B06 are sections 2-7, BOUT is
section 8. Same structure and style as the Week 5 progress video.

**Status: audio approved. Both review cuts are built, 16:9 (`week-3-progress-slate.mp4`) and 9:16 (`vertical/week-3-progress-vertical-slate.mp4`, 2160x3840), with Gates A, W, B, V and T all on and passing on each. Not yet run: `./art final`, which waits for Keya's OK.**

## Rules for every visual

- Simple illustrative graphics only. No photos or recordings of Keya, no person icons, no real company, product or
  tool logos. **No Google logo, Docs screenshots or branding:** a shared document is a generic drawn page of plain
  lines with two cursors. The explainer's title appears as plain text only.
- Files, frames, boxes and arrows are drawn, not screenshots. Nothing on screen is data.
- **Fill the frame (Gate V):** content covers at least 55% of the safe area at 50% and at 85% of every beat. Lay out
  the cast early and hold it; scale shapes and type up rather than clustering at the top.
- **Portrait (9:16):** native layouts, not a crop (the same `scenes.py` with `PORTRAIT = True`). Text is at least
  72 px at 2160x3840 (the scene scan flags anything under 30 pt, about 88 px of ink) and sits above 86% of the frame
  height; the bottom 14% stays empty. Every scene stacks its cast in one column.
- Palette `humanitarians`: ink `#2F2A26`, crimson `#E4572E` (problem or changed, one accent per beat), teal `#1F4E5F`
  (done), slate `#29335C` (structure), ground `#F3EBDD`. Gold and sage are fills only, never text.
- Un-highlighted elements never fade below about 40% opacity.
- BOUT is the only beat marked `sparse_by_design` (same reason as Keya's other progress videos). No other exemptions.
- No dates on screen or in files Keya writes.

## Library check

`./art scenes` was searched first (shared document, cursors, backend, script, fact check, composer, outro).

| Need | Result |
|---|---|
| Cold open | **Hit:** `ClaudeComposerAsk`, `ClaudeComposerAsk916` (RENDERABLE) |
| Outro | **Hit:** `LogoOutro`, `LogoOutro916` (RENDERABLE) |
| Generic document with cursors, backend boxes, script and source tags, claim-to-source checks, topic cards, Venn | **No match** (leads were figures for other films). Custom Manim |

## Beats

| Beat | Act | Lane | Asset | What the viewer sees | Length (s) |
|---|---|---|---|---|---|
| B00 | INTRO | remotion | `ClaudeComposerAsk` | Claude composer: "Hi, Keya", the ask types in at the composer's default timing, three result lines | 11.26 |
| B01 | THIS WEEK'S VIDEO | manim | `B01_ThisWeeksVideo` | Title card (text only); a generic document with two cursors and a seven-day row; the page gives way to drawn copy, server, copy boxes, "the most interesting part" with a star | 14.68 |
| B02 | LEARNING FILM AS CODE | manim | `B02_FilmAsCode` | Angle brackets to a film frame, one part at a time (three of four blocks filled); a grid of drawn players over a few days; script, audio, scenes, video linked | 11.07 |
| B03 | CHOOSING TOPICS | manim | `B03_ChoosingTopics` | Six topic cards, some ticked and some crossed out; a grid of drawn players for other fellows' work; two overlapping circles, AI or STEM and my interests, with a star | 12.78 |
| B04 | SCRIPTS AND FACT CHECKS | manim | `B04_ScriptAndChecks` | A drawn script, beat by beat, then each line gets a source tag; claim to source pairs ticked; "quality gates" | 15.08 |
| B05 | WHAT I LEARNED | manim | `B05_BehindTheTool` | A document and a smooth path to a tick (understanding the topic was not hard); the same page with shifted, ordered, shared beneath it; the page again with "feels new" and a star | 13.80 |
| B06 | THE TAKEAWAY | manim | `B06_Takeaway` | Three drawn everyday tools; drawn boxes and arrows revealed behind each; "learn to look behind them" | 6.85 |
| BOUT | OUTRO | remotion | `LogoOutro` | Humanitarians AI mark and `@HumanitariansAI` handle | 4.20 |

Lengths are the measured narration (total 89.72 s).

## Portrait notes

- 9:16 stacks each scene's cast in one column; B06 puts each tool's hidden boxes beside it so three tools still fill the height.
- B05's "underneath" step cards (shifted, ordered, shared) stack as three rows under a small page.
- 9:16 outro keeps the `@HumanitariansAI` line, which the toolkit places below 86% of the frame height (as in Week 2 and Week 5).

## Cue times

Scene cues come from word timings measured on the generated audio (faster-whisper). If any beat's audio is regenerated,
re-measure and update the `go()` times in `scenes.py`.

## Listen for

- "Keya" (custom pronunciation), "Brutalist", "Google Docs", and the pacing of "shifted, ordered and shared".
