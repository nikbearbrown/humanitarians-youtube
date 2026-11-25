# ML explainer: momentum in gradient descent on a narrow valley

**Week:** 16–20 Nov 2026 · logged 2026-11-24
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-20`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `claude-liam-momentum.mp4` (16:9, 3:00) · `claude-liam-momentum-vertical.mp4` (9:16, 3:00)

## What this film was for
On the loss 0.5(x^2 + 25y^2) from (4, 1), plain descent bounces across the valley and needs 47 steps to reach loss 0.01; momentum with beta 0.5 needs 20; beta 0.9 needs 53; beta 0.99 does not settle in 200 steps. The film shows why: swings across the valley cancel in the velocity while steady slopes along it add up.

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
| Landscape | 3840×2160, 3:00; frame QC 0 blockers / 0 majors; type check pass |
| Vertical | 2160×3840, 3:00; frame QC 0 blockers / 0 majors; type check pass |
| Footer labels | none seen on the sampled frames (standing rule) |
| Narration | Kokoro `am_onyx`; checked for words only, not for delivery |

## Problems found by running it
- Pale valley contours failed the contrast check (ink-on-background separation below 0.3); I darkened them.
- The slope bars in one beat collided with their header and a legend; Claude resized the bars and re-spaced the labels.
- In the vertical cut the valley is turned on its side so its long axis fits the tall frame.
- A 'start' label sat on a contour line and failed the label-on-line check, so it became a ring around the start point.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
