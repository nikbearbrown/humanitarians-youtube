# SHOTLIST — Week 5 Progress

Typed work order. Nine beats, **no open media slots**. Two are registered Remotion compositions; seven are Manim
scenes in `scenes.py`. Narration is `SCRIPT.md` verbatim: B00 is section 1, B01-B07 are sections 2-8, BOUT is
section 9. Same structure and style as the Week 2 progress video.

**Status: audio approved except B04, regenerated for the reworded line. Both review cuts are built, 16:9 (`week-5-progress-slate.mp4`) and 9:16 (`vertical/week-5-progress-vertical-slate.mp4`, 2160x3840), with Gates F, L, A, W, B, V and T all on and passing on each. Not yet run: `./art final`, which waits for Keya's OK.**

## Rules for every visual

- Simple illustrative graphics only. No photos or recordings of Keya, no person icons, no real company, product or
  tool logos. **No Duolingo logo, owl or branding:** the app is a generic drawn phone with plain text.
- Files, terminals, frames and rulers are drawn, not screenshots. Numbers (12%, 72 px) are the script's own.
- **Fill the frame (Gate V):** content covers at least 55% of the safe area at 50% and at 85% of every beat. Lay out
  the cast early and hold it; scale shapes and type up rather than clustering at the top.
- **Portrait (9:16):** native layouts, not a crop (the same `scenes.py` with `PORTRAIT = True`). Text is at least
  72 px at 2160x3840 (the scene scan flags anything under 30 pt, about 88 px of ink) and sits above 86% of the frame
  height; the bottom 14% stays empty.
- Palette `humanitarians`: ink `#2F2A26`, crimson `#E4572E` (problem or changed, one accent per beat), teal `#1F4E5F`
  (done), slate `#29335C` (structure), ground `#F3EBDD`. Gold and sage are fills only, never text.
- Un-highlighted elements never fade below about 40% opacity.
- No dates on screen or in files Keya writes.

## Library check

`./art scenes` was searched first (forgetting curve, ruler and text size, composer, outro).

| Need | Result |
|---|---|
| Cold open | **Hit:** `ClaudeComposerAsk`, `ClaudeComposerAsk916` (RENDERABLE) |
| Outro | **Hit:** `LogoOutro`, `LogoOutro916` (RENDERABLE) |
| Decay curve, ruler/measure, phone, wave, table | **Weak or no match** (leads were figures for other films). Custom Manim |

## Beats

| Beat | Act | Lane | Asset | What the viewer sees | Length (s) |
|---|---|---|---|---|---|
| B00 | INTRO | remotion | `ClaudeComposerAsk` | Claude composer: "Hi, Keya", the ask types in at the composer's default timing (0.6 s in), three result lines | 12.03 |
| B01 | THIS WEEK'S VIDEO | manim | `B01_ThisWeeksVideo` | Title card (text only); a drawn phone and a year bar; five research cards: forgetting curve, spaced repetition, Leitner boxes, blog posts, research paper | 17.56 |
| B02 | READING THE PAPER | manim | `B02_TheNumber` | A summary with "12%"; the table: two versions of the same model; "mixed" against the older method; the 12% crossed out; "check what it is compared against" | 19.99 |
| B03 | LANDSCAPE AND VERTICAL | manim | `B03_LandscapeVertical` | A landscape and a vertical frame; the same narration as a wave; a squeezed layout crossed out; a vertical layout of three stacked blocks | 16.43 |
| B04 | MEASURE, DON'T ASSUME | manim | `B04_Measure` | A ruler; a terminal with a crossed-out figure; a ruler on a frame; five scene bars all above a dashed 72 px rule | 13.40 |
| B05 | WATCHING AND LISTENING | manim | `B05_EarAndEye` | An eye; three test clips (shimasu, mimasu, Leitner, plain text) ticked; typing and voice tracks out of sync, then in sync | 13.87 |
| B06 | WATCHING BRUTALIST VIDEOS | manim | `B06_Watching` | A grid of drawn players; "what other fellows cover"; one starred "my own" | 7.68 |
| B07 | THE TAKEAWAY | manim | `B07_Takeaway` | Three cards: a number needs its comparison, a vertical video needs its own layout, a claim needs a measurement | 8.34 |
| BOUT | OUTRO | remotion | `LogoOutro` | Humanitarians AI mark and `@HumanitariansAI` handle | 4.25 |

Lengths are the measured narration (total 113.55 s).

## Portrait notes

- 9:16 stacks each scene's cast in one column; B03 draws the vertical design as its own proof (three stacked blocks).
- Romaji only on screen (shimasu, mimasu), so no kana font is needed.
- 9:16 outro keeps the `@HumanitariansAI` line, which the toolkit places below 86% of the frame height (as in Week 2).

## Status of the layouts

Both cuts were built with every gate on. Gate T passes on each (lowest text-run 43 px against the 41 px landscape floor;
84 px against the 72 px portrait floor) and Gate V reports no blocker or major defect. Each Manim phase lays out its
full cast as soon as it starts and fills in the words on their cues, so no phase is empty at 25%, 50% or 85% of a beat.
B03, B04 and B05 were reworked for this (full cast early, larger pieces, no empty gaps between phases).

## B00 typing start

`ClaudeComposerAsk` starts typing at its default 0.6 s (frame 18). No toolkit change was made for this; the
explainer's no-lead-silence timing is not applied to B00.

## Listen for

- "Keya", "shimasu", "mimasu" and "Leitner" (custom pronunciations), and "Brutalist" read aloud.
