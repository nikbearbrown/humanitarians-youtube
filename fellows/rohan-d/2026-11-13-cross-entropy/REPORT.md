# ML explainer: cross-entropy loss and why confident mistakes cost so much

**Week:** 9–13 Nov 2026 · logged 2026-11-24
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `claude-liam-cross-entropy.mp4` (16:9, 3:06) · `claude-liam-cross-entropy-vertical.mp4` (9:16, 3:06)

## What this film was for
How a classifier turns scores into a loss: softmax shares 66/24/10, loss minus-log of the right answer's share (0.417), why a confident mistake costs 4.6 while a hedge costs 0.7, the slope share-minus-answer, and the clipping floor (27.63).

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
| Landscape | 3840×2160, 3:06; frame QC 0 blockers / 0 majors; type check pass |
| Vertical | 2160×3840, 3:06; frame QC 0 blockers / 0 majors; type check pass |
| Footer labels | none seen on the sampled frames (standing rule) |
| Narration | Kokoro `am_onyx`; checked for words only, not for delivery |

## Problems found by running it
- I first built from the wrong reference videos. After I attached the right ones, Claude re-read them and rebuilt the film on the `ai-explainer` spine instead of the `tldr` spine.
- The writer's correction never fired: the trigger phrase ended in a period and the writer matches phrases without punctuation. Claude found it on a frame at the end of the beat and fixed it.
- Cached clips hid edits more than once (the clip is reused unless deleted); Claude learned to delete the beat's clip after every change.
- Pre-flight needed shapes that change (Transform/GrowFromEdge); Claude restructured the bars so the static check passed.
- I asked for the greeting 'Namaste' to be changed to 'Hi'; Claude re-recorded the first line and rebuilt both masters.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
