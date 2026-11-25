# ML explainer: dropout and inverted scaling on eight activations

**Week:** 23–27 Nov 2026 · logged 2026-11-24
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `claude-liam-dropout.mp4` (16:9, 2:46) · `claude-liam-dropout-vertical.mp4` (9:16, 2:46)

## What this film was for
Eight activations 1 to 8 sum to 36. A random mask keeps 1, 5, 6, 7 (sum 19, scaled 38). Ten thousand masks average 35.98, unscaled they average 18; 256 masks average exactly 36 for a plain sum; noise grows with p (4.8, 14.3, 42.9).

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
| Landscape | 3840×2160, 2:46; frame QC 0 blockers / 0 majors; type check pass |
| Vertical | 2160×3840, 2:46; frame QC 0 blockers / 0 majors; type check pass |
| Footer labels | none seen on the sampled frames (standing rule) |
| Narration | Kokoro `am_onyx`; checked for words only, not for delivery |

## Problems found by running it
- Two headings stacked on top of each other because I faded the new heading in without removing the old one; the layout check flagged it and Claude replaced it with a cross-fade.
- The type check said it could not find dark text in one beat that used only grey labels, so those labels became ink.
- A pale grid failed the contrast check in the portrait cut and was darkened.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
