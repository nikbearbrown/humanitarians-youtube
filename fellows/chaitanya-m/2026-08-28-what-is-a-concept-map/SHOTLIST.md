# SHOTLIST — What Is a Concept Map

Ten beats. Nine setups from the script's Appendix B, plus B00, the requested
spoken intro. Every shot is type and rule on a fixed frame: no camera moves, no
3D, no particle work, no stock footage.

Durations are **measured from the Kokoro narration**, not planned. The pipeline
is audio-first — duration is an output. See BUILD-LOG for the drift table
against the script's estimates.

## 16:9 master — 3840×2160, 24 fps, 228.86 s (3:48.86)

| Beat | In | Dur | Act | Motion | On screen |
|---|---|---:|---|---|---|
| B00 | 00:00 | 9.75 s | INTRO | hard-snap | Title card. Display `WHAT IS A CONCEPT MAP`, mono `MEDHAVY RESEARCH LOG` / `2026-08-28`, one signal rule |
| B01 | 00:09 | 12.25 s | SCENE 1 — Cold open | step-reveal | TOC (CH 21/22/23) in mono, red strike-through left to right over 6 frames, then `THIS IS NOT A MAP` |
| B02 | 00:22 | 13.03 s | SCENE 2 — The definition | hard-cut | Split frame, 4 px centre rule. `FIG. 01 — SEQUENCE` vs `FIG. 02 — DEPENDENCY`; lower third `NODE = ONE TEACHABLE IDEA` / `EDGE = PREREQUISITE` |
| B03 | 00:35 | 20.29 s | SCENE 3 — Anatomy of a node | step-reveal | `FIG. 03 — NODE RECORD`: 7-row Paclitaxel table, rows 4 frames apart, `canonical_name` and `prerequisite_nodes` in signal. Closes on `THE EDGE IS THE POINT` |
| B04 | 00:55 | 31.78 s | SCENE 4 — Why humans | step-reveal | Bar chart HIGH 9 / MEDIUM 10 / LOW 6, `LOW` bar in signal; hard cut to `THIN_CONTENT: 2`; closes `THE PIPELINE MARKS ITS OWN WEAK SPOTS` |
| B05 | 01:27 | 37.56 s | SCENE 5 — The four stages | hard-cut | Four-panel band `01 GENERATE` → `04 EXPORT`, one active at a time. `ACCEPT` / `EDIT` / `REMOVE` as stacked signal blocks, removal struck. Holds `ZERO PENDING OR NOTHING` |
| B06 | 02:04 | 20.31 s | SCENE 6 — What gets thrown away | step-reveal | Node record returns at **9 rows**; `wikipedia_categories`, `confidence`, `source_url` struck and dropped on a 2-frame step; gap closes to `FIG. 04 — VERIFIED OUTPUT`. Closes `SCAFFOLDING ≠ CONTENT` |
| B07 | 02:24 | 32.83 s | SCENE 7 — The honest finding | draw-on | Hairline pipeline `PIPELINE → IMPORT → REVIEW → EXPORT → S3`, final arrow runs off frame into nothing, 3 s silent hold. `grep: 0 consumers`, then `STORED, NOT SPENT` |
| B08 | 02:57 | 34.23 s | SCENE 8 — The crack | hard-cut | `FIG. 05 — DANGLING EDGE`: three boxes, three independent signal routes into `MICROTUBULE DYNAMICS`; target box hard-cuts out, three edges remain pointing at empty frame, 3 s hold. `18 EDGES · 0 DANGLING · TODAY` |
| B09 | 03:32 | 16.83 s | SCENE 9 — Close | step-reveal | Four-line summary block; `CONSUMERS = 0` held in signal 2 s; hard cut to black |

**Motion mix:** step-reveal 5/10 (50%), hard-cut 3/10, hard-snap 1/10,
draw-on 1/10. This exceeds the toolkit's ~40% step-reveal cap. The labels are
read off the script's own shot list, which specifies step-reveals for exactly
those five scenes; relabelling to satisfy the guard would misdescribe the
motion. See BUILD-LOG.

## 9:16 short — 2160×3840, 24 fps, 160.04 s (2:40.04)

Planned by the toolkit's `shorts.py` against the 3:00 cap. **B05** and **B08**
dropped as the longest unprotected middle beats; B00 and B09 protected.

| Beat | In | Dur | Note |
|---|---|---:|---|
| B00 | 00:00 | 9.75 s | Protected |
| B01 | 00:09 | 12.25 s | |
| B02 | 00:22 | 13.03 s | |
| B03 | 00:35 | 20.29 s | |
| B04 | 00:55 | 31.78 s | |
| B06 | 01:27 | 20.31 s | |
| B07 | 01:47 | 32.83 s | |
| B09 | 02:20 | 15.30 s | Protected. Outro rewritten to name the two dropped beats and point at the long cut |
| — | 02:35 | 4.50 s | Silent brutalist endcard, native 2160×3840 |

Portrait slots are **native re-layouts** from `render_scenes.py`, not centre
cuts. A centre cut of 3840×2160 keeps 1215 px of width and would have destroyed
the bar chart, the split frame, and the four-panel band.

**Known cosmetic mismatch:** the short's B09 keeps the four-line summary visual
while the voice reads the rewritten outro. Step reveals were timed to the
original narration.

## Superseded

An earlier full-length 9:16 (228.86 s, all ten beats) was built by deliberately
bypassing `shorts.py`. That was the wrong call — the 3:00 cap is a real
constraint on the 9:16, and the auto-shorten is the intended behaviour, not an
obstacle. `short/` above supersedes it and is the only 9:16 deliverable; the
superseded cut is not carried in this folder.
