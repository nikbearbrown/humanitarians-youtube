# TL;DR on a paper: why attention divides by the square root of the key length

**Week:** 9–13 Nov 2026 · logged 2026-11-23
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-13`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `tldr-attention-scaling.mp4` (16:9, 3:41) · `tldr-attention-scaling-vertical.mp4` (9:16, 3:41)

## What this film was for
The Transformer's scaled dot-product attention divides scores by the square root of the key length. The film shows why: longer vectors give wider scores, wide scores make softmax pick one winner and starve the gradient, a fixed divisor fits one length only, and dividing by the square root keeps the spread constant.

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
| Landscape | 3840×2160, 3:41; frame QC 0 blockers / 0 majors; type check pass |
| Vertical | 2160×3840, 3:41; frame QC 0 blockers / 0 majors; type check pass |
| Footer labels | none seen on the sampled frames (standing rule) |
| Narration | Kokoro `am_onyx`; checked for words only, not for delivery |

## Problems found by running it
- Manim's `MathTex` needs `dvisvgm`, which was not installable here. I switched every equation to the toolkit's MathText SVG route.
- The review cut kept showing 'B0x' footers and timecodes. I told Claude it must never appear in any video; the labels now only render with `ART_REVIEW_LABELS=1`, including on contact sheets.
- Gate T (type) failed on the TL;DR cards; Claude patched the card components' font sizes and kept the originals.
- Several Gate B/V defects (a caption off the safe area, underfilled frames, a label sitting on the axis line) were fixed scene by scene.
- The outro's 1.0 s silent tail silently did not apply at first. Claude claimed the rebuild had fixed it before measuring; measuring showed it had not. The final masters measure about 1.04 s of silence.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
