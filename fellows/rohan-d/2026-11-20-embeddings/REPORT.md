# ML explainer: distance versus cosine on toy 2-D word vectors

**Week:** 16–20 Nov 2026 · logged 2026-11-24
**Project:** Brutalist film as code — STEM and AI explainers
**Evidence of commit:** none yet; source is in this folder. [add the commit link once the folder is committed]

- **Drive:** https://drive.google.com/drive/folders/1KsCa1LWmcUZyzRHbTyZt7uj0LILO8NgO?usp=drive_link (week folder `2026-11-20`)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `claude-liam-embeddings.mp4` (16:9, 2:45) · `claude-liam-embeddings-vertical.mp4` (9:16, 2:45)

## What this film was for
Toy vectors cat (4,1), dog (3,2), car (1,4). Distance says a cat is 8.2 from three cats and 4.2 from a car; cosine gives 1.00 for three cats, 0.94 for dog and 0.47 for car. High cosine means near, not the same, and a zero vector has no cosine.

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
| Landscape | 3840×2160, 2:45; frame QC 0 blockers / 0 majors; type check pass |
| Vertical | 2160×3840, 2:45; frame QC 0 blockers / 0 majors; type check pass |
| Footer labels | none seen on the sampled frames (standing rule) |
| Narration | Kokoro `am_onyx`; checked for words only, not for delivery |

## Problems found by running it
- The distance-versus-length story needed a pair of vectors where distance really misleads; Claude picked cat versus cat times three.
- Several scene frames were underfilled and were scaled up; one portrait title touched the right edge, so a shorter on-screen title was used (the outro keeps the full title).
- The portrait labels near arrow tips initially overflowed the margin.

## Evidence
- This folder (source). Renders: Drive link above.

## Next
Listen once with sound on; add the weekly Drive subfolder link and the commit link; add the required opening line if the supervisor wants it.
