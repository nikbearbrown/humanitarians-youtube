# ML explainer: a 3 by 3 edge kernel on a 6 by 6 image

**Week:** 16–20 Nov 2026 · logged 2026-11-24
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-20`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `claude-liam-convolution.mp4` (16:9, 2:43) · `claude-liam-convolution-vertical.mp4` (9:16, 2:43)

## What this film was for
A 3 by 3 kernel with columns -1, 0, 1 slides over a 6 by 6 image whose rows are 0 0 0 9 9 9. The output rows read 0, 27, 27, 0. One kernel of 9 weights replaces 576 in a fully connected layer, and each unpadded layer shrinks the map by 2.

## What was built

| File | What it does |
|---|---|
| `beat_sheet.json` | The film as data: narration, timing, persona and the beat-by-beat scene routing. |
| `make_sheet.py` | Writes `beat_sheet.json` (carries the measured audio durations forward). |
| `scenes.py` | The Manim scenes for the body beats (landscape). |
| `vertical/` | The vertical beat sheet and the native 9:16 scenes. |
| `experiment.py` · `experiment_output.txt` | Every number on screen, recomputed. |
| `FACTCHECK.md` · `SHOTLIST.md` · `PROMPTS.md` · `SOURCES.md` | The claim table, the lane choice per beat, the prompts (none generated) and the sources. |
| `TYPECHECK.md` | The type-size check. |

## Results

| Measure | Value |
|---|---|
| Landscape | 3840×2160, 2:43; frame QC 0 blockers / 0 majors; type check pass |
| Vertical | 2160×3840, 2:43; frame QC 0 blockers / 0 majors; type check pass |
| Footer labels | none seen on the sampled frames (standing rule) |
| Narration | Kokoro `am_onyx`; checked for words only, not for delivery |

## Problems found by running it
- Several beats were underfilled in the frame check (too much empty space), so elements were enlarged or brought in earlier.
- A stray panel edge and a label crossed each other; Claude moved the labels in and narrowed the highlight box.
- The narration for the overview came out under the 9 s minimum, so Claude added one sentence and regenerated that line.
- Portrait layout: the sum readout sat on the right margin, and a shortened label fixed another overflow.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
