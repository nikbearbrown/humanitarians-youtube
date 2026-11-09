# SHOTLIST — Week 2 Progress

Typed work order. Nine beats, **no open media slots**. Two are registered Remotion compositions; seven are Manim
scenes in `scenes.py`. Narration is `SCRIPT.md` verbatim: B00 is section 1, B01–B07 are sections 2–8, BOUT is
section 9. Same structure and style as the Week 4 progress video.

**Status: audio approved. Both review cuts are built, 16:9 (`week-2-progress-slate.mp4`) and 9:16 (`vertical/week-2-progress-vertical-slate.mp4`), with Gates F, L, A, W, B, V and T all on and passing on each. Not yet run: `./art final`, which waits for Keya's OK.**

## Rules for every visual

- Simple illustrative graphics only. No photos or recordings of Keya, no person icons, no real company, product or
  tool logos. Claude Code, Selenium, Remotion and Manim appear as plain text or generic drawn shapes, never as marks.
- Files, terminals, browsers and video frames are drawn, not screenshots.
- **Fill the frame (Gate V):** content covers at least 55% of the safe area at 50% and at 85% of every beat. Lay out
  the full cast early and hold it; scale shapes and type up rather than clustering at the top.
- **Portrait (9:16):** all text above 86% of the frame height; the bottom 14% stays empty. Large, readable type with
  short labels. 9:16 gets its own native layouts (the same `scenes.py` with `PORTRAIT = True`), not a crop.
- Palette `humanitarians`: ink `#2F2A26`, crimson `#E4572E` (problem or blocked, one accent per beat), teal `#1F4E5F`
  (done), slate `#29335C` (structure), ground `#F3EBDD`. Gold and sage are fills only, never text.
- Un-highlighted elements never fade below about 40% opacity.
- No dates on screen or in files.

## Library check

`./art scenes` was searched first for: a frozen render with a clock, done versus pass in a terminal, and the
check/file/timeline illustrations.

| Need | Result |
|---|---|
| Cold open | **Hit:** `ClaudeComposerAsk`, `ClaudeComposerAsk916` |
| Outro | **Hit:** `LogoOutro`, `LogoOutro916` (same as the Week 4 progress video) |
| Failing checks, frozen render, folder files, done vs pass, beat timeline, terminal prompt | **Weak or no match** (only figure scenes for other films, such as `CadencesFig1Clock` and `HowWeCode-Phase3`). Custom Manim. |

## Beats

| Beat | Act | Lane | Asset | What the viewer sees | Length (s) |
|---|---|---|---|---|---|
| B00 | INTRO | remotion | `ClaudeComposerAsk` | Claude composer: "Hi, Keya", the ask types in, three result lines | 11.99 |
| B01 | THIS WEEK'S VIDEO | manim | `B01_ThisWeeksVideo` | Explainer title card; "my own work / Selenium tests"; self-healing locators and AI testing agents; wrote the script, built with Claude Code; a video checked; three topic cards, two starred | 21.23 |
| B02 | THE CHECKS | manim | `B02_ManimRemotion` | Three failing-check cards (code, safe area, empty frame); a Remotion render frozen beside a clock; each scene fixed, checks left on; a different browser; a time limit | 19.22 |
| B03 | THE FILES | manim | `B03_Files` | Four dashed slots fill with script, beat sheet, fact check, build state, then a tick | 13.91 |
| B04 | DONE IS NOT PASSED | manim | `B04_DoneNotPassed` | Terminal shows "done" then "pass", marked "not proof"; old frames with a PASS stamp; `build-state.json` with an eye and "real result" | 12.71 |
| B05 | A LATE CHANGE | manim | `B05_LateChange` | An intro line is edited; "the narration is the clock"; one beat block gets new audio and a new render, the rest tick as unchanged | 11.01 |
| B06 | WHAT WAS HARD | manim | `B06_WhatWasHard` | Terminal prompt with "what I expect"; steps ticked with an eye; an Approve button crossed at its corner; "week two: still learning" bar | 12.63 |
| B07 | THE TAKEAWAY | manim | `B07_Takeaway` | Three cards: testing agents (look, act, check), Claude Code does the work, I decide what correct looks like | 6.34 |
| BOUT | OUTRO | remotion | `LogoOutro` | Humanitarians AI mark and `@HumanitariansAI` handle | 4.14 |

Lengths are the measured narration (total 113.2 s).

## Portrait notes

- 9:16 stacks each scene's cast in one column and swaps cards in place where a row would not fit (B02 problem cards show one at a time).
- 9:16 outro: keeps the `@HumanitariansAI` line, as in the Week 4 film; the toolkit places it below 86% of the frame height.

## Listen for

- "Keya" (custom pronunciation), "Manim", "Remotion", "Brutalist", and "build-state.json" read aloud.
