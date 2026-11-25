# ML explainer: overfitting with eight noisy points and polynomial fits

**Week:** 9–13 Nov 2026 · logged 2026-11-24
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `claude-liam-overfitting.mp4` (16:9, 2:48) · `claude-liam-overfitting-vertical.mp4` (9:16, 2:48)

## What this film was for
Eight noisy points around y = 2x. A straight line has train error 0.099 and test error 0.074. A degree-7 curve passes through every point (train 0.000) but its test error is 0.221. Test error turns around while training error keeps falling; more data (8 to 40 points) closes the gap; noise sets a floor of about 0.0625.

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
| Landscape | 3840×2160, 2:48; frame QC 0 blockers / 0 majors; type check pass |
| Vertical | 2160×3840, 2:48; frame QC 0 blockers / 0 majors; type check pass |
| Footer labels | none seen on the sampled frames (standing rule) |
| Narration | Kokoro `am_onyx`; checked for words only, not for delivery |

## Problems found by running it
- The degree-7 curve was clipped flat at the bottom of my first plot because its true minimum (-0.89) was below my axis range. Claude widened the range after the frame showed a suspicious flat segment.
- The overview text at first looked tiny; making it big then bled past the edge on the corrected sentence, so the size was reduced to fit.
- In the vertical cut a title ran into the right edge; Claude forced it to wrap at the right word.
- Two labels overlapped bar values in the portrait layout; I changed the layout to rows.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
