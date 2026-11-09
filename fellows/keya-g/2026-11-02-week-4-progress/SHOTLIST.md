# SHOTLIST — Week 4 Progress

Typed work order. Seven beats, **no open media slots**. Two are registered Remotion compositions; five are Manim
scenes in `scenes.py` (16:9) and `vertical/scenes.py` (9:16, native layouts, not a crop). Narration is `SCRIPT.md`
verbatim: B00 is section 1, B01–B05 are sections 2–6, BOUT is section 7. Same structure and style as the Week 1
progress video.

**Status: audio approved. All five Manim scenes written in `scenes.py` (16:9) and `vertical/scenes.py` (9:16, native layouts); Gates A, W and B clean on all ten scene-aspect pairs. Both bookends rendered in both aspects. Low-quality previews with audio built for Keya to review. Not yet run: `./art run`, the review cuts, `./art final`.**

## Rules for every visual

- Simple illustrative graphics only. No photos or recordings of Keya, no person icons, no real company, product or
  tool logos. Claude Code, Drive and Humanitarians AI appear as generic drawn shapes or plain text, never as marks.
- Files, folders, video frames and the terminal are drawn, not screenshots.
- The checksum in B04 is a drawn fingerprint pattern. No hash string is shown, because none is real until a final exists.
- Only B01 shows Japanese (はし and three kanji). Every Manim `Text` with kana or kanji sets `font="Hiragino Sans"`
  explicitly; check the rendered frame for tofu boxes.
- **Fill the frame (Gate V):** content covers at least 55% of the safe area at 50% and at 85% of every beat. Lay out the
  full cast early and hold it; scale shapes and type up rather than clustering at the top.
- **Portrait (9:16):** all text above 86% of the frame height; the bottom 14% stays empty. Large, readable type with
  short labels. 9:16 gets its own native layouts.
- Palette `humanitarians`: ink `#2F2A26`, crimson `#E4572E` (problem or blocked, one accent per beat), teal `#1F4E5F`
  (done), slate `#29335C` (structure), ground `#F3EBDD`. Gold and sage are fills only, never text.
- Un-highlighted elements never fade below about 40% opacity.
- No dates on screen or in files, and no counts such as "second" on screen.

## Library check

`./art scenes` was searched first (reel logged) for: quality-check lists, file checksum, folder of files, scene-by-scene review.

| Need | Result |
|---|---|
| Cold open | **Hit:** `ClaudeComposerAsk`, `ClaudeComposerAsk916` |
| Outro | **Hit:** `LogoOutro`, `LogoOutro916` (same as the Week 1 progress video) |
| Gates, checksum, folder, review illustrations | **Miss** (only reel-specific eval and figure scenes came back). Custom Manim. |

## Beats

| Beat | Act | Lane | Asset | What the viewer sees | Length (s) |
|---|---|---|---|---|---|
| B00 | INTRO | remotion | `ClaudeComposerAsk` | Claude composer: "Hi, Keya", the ask types in, three result lines | 10.94 |
| B01 | THIS WEEK'S VIDEO | manim | `B01_ThisWeeksVideo` | Title card; a drawn keyboard types "hashi" and offers kanji candidates; research, script, build chained | 11.84 |
| B02 | WATCHING VIDEOS | manim | `B02_Watching` | A drawn video player; claims matched to sources with checks; scene frames matched to narration waveforms | 10.43 |
| B03 | GATES AND RE-RENDERING | manim | `B03_Gates` | A scene token at four gates, one fails, fix and render again, passes; an off-switch crossed out | 13.27 |
| B04 | FILE INTEGRITY | manim | `B04_Checksum` | A video file with a drawn fingerprint; its copy on a drive shows the same fingerprint; "same file" | 10.41 |
| B05 | WHAT I LEARNED | manim | `B05_WhatILearned` | A folder fills with five parts; a terminal skill bar grows; a plain badge "helps" | 15.36 |
| BOUT | OUTRO | remotion | `LogoOutro` | Humanitarians AI mark and `@HumanitariansAI` handle | 4.22 |

Lengths are the measured narration (total 76.5 s).

## Portrait notes

- 9:16 B01 shows the keyboard guess first, then clears so the three steps stack in reading order.
- 9:16 B03 stacks the four gates down a track, then shows the failed gate, "fix the scene" and "render it again" as a cycle.
- 9:16 outro: keeps the `@HumanitariansAI` line, as in the Japanese video. The toolkit places it at 94% of the frame height, below Keya's 86% text rule; Keya accepted this and Gate T passes it.
