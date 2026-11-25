# ML explainer: batch normalization and the condition number of the loss

**Week:** 23–27 Nov 2026 · logged 2026-11-24
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-27`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `claude-liam-batch-norm.mp4` (16:9, 3:00) · `claude-liam-batch-norm-vertical.mp4` (9:16, 3:00)

## What this film was for
Two features, [2,4,6,8] and [200,400,600,800], normalize to the same four numbers. On a small regression the raw loss has condition number 3,182,113 and has not converged in 100,000 steps; normalized it is 1.4 and converges in 4 steps. Gamma and beta restore scale, and small batches make noisy statistics.

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
- I accidentally added row rules to the wrong beat with a global text replace, which put lines through the numbers. Claude found it by looking at the audit frame, and removed them.
- The portrait build was blocked by the type check: the typeset equations render too small in the tall frame. Claude wrote the portrait formulas as large text instead and kept the typeset ones in the landscape cut.
- My own build script wrongly marked the vertical master as done when the type gate had blocked it. I caught it from the log and corrected the table.
- Frames were underfilled until the two features were put on wide cards.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
