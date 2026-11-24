# ML explainer: k-means on seven points and a bad start

**Week:** 23–27 Nov 2026 · logged 2026-11-24
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `claude-liam-kmeans.mp4` (16:9, 2:59) · `claude-liam-kmeans-vertical.mp4` (9:16, 2:59)

## What this film was for
Seven points, two centers starting at (1,1) and (5,6) settle at (1.25,1.5) and (3.9,5.1) in two rounds; inertia falls from 19.25 to 8.53 and never rises. Four rectangle corners show two stable answers, inertia 4 and 16, depending on the start.

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
| Landscape | 3840×2160, 2:59; frame QC 0 blockers / 0 majors; type check pass |
| Vertical | 2160×3840, 2:59; frame QC 0 blockers / 0 majors; type check pass |
| Footer labels | none seen on the sampled frames (standing rule) |
| Narration | Kokoro `am_onyx`; checked for words only, not for delivery |

## Problems found by running it
- My first starting centers left one point exactly equidistant from both, so the example depended on a tie-break. Claude moved the second center to (5,6) to remove the tie.
- The master was blocked by the type check on one beat with 38 px text. Enlarging the readouts did not fix it; making the half-drawn lines static did, which suggests partially drawn lines were being read as small text.
- Scatter frames were underfilled until the plane was enlarged and outlined.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
