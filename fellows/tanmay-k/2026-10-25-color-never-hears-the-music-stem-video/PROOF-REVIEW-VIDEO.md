# Feedback: "Color Never Hears the Music" — long film (16:9), video review 4

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2 each, /12) plus the binary production gate.
**Reviewed:** the compiled video `color-never-hears-the-music.mp4` (3840×2160, 30 fps, 285.6 s, narration `am_onyx`), the 13 beat clips (`_beats/`), the measured gate (`VIDEO-GATE-LONG.md`, `measure_long_video.py`), frames I extracted from the beats (B01 mid-clip, B10 mid-countdown, and the last 1.5–3 s of B04, B07, B09, B11, B12, B13), and Tanmay's watch of the beats and the Short (2026-10-25, no changes requested).
**Prior reviews:** `PROOF-REVIEW.md` (script, 12/12), `PROOF-REVIEW-RENDERED.md` (stills, 12/12, gate fixed).
**Verdict: clear-for-public.** Teaching **12/12**. Production gate **PASS, measured on the video**. The film passes its own standard (every claim carries a visible source or a visible artifact). Conditions are listed under Do next; none blocks.
One line: this film attempts to teach a two-scale method for predicting colour–music matches and delivers it, with a task whose answer the paper's own chart can contradict.

## Where it improved vs the stills review

| Item | Stills review | Video |
|---|---|---|
| Source lines near the bottom edge | fixed on stills | still inside the safe area on the last frame of every beat (measured) |
| Holds ≥ 2–3 s | not measurable | **measured**: B01, B04, B07, B08, B09, B11, B12 keep every key element fully visible for the last 2.5–3 s (7 samples each) |
| Fades, black frames | not measurable | none: lowest frame luminance 212.7 (page = 249) |
| Loudness, sync | stage-1 only | master −14.5 LUFS / −1.9 dBFS; video vs audio differ by ≤ 0.001 s per beat, 0.000 s on the master |

## Rubric (on the video)

| Criterion | Score | Reason |
|---|---|---|
| Explicit framework | 2 | The strip is on screen from B01's first frame (clearly visible at 300 px in the video, with SAD / HAPPY / STRONG / WEAK labels), is outlined and named in B02, and is explained in B04 before the worked example. |
| Reusable rubric | 2 | The three-step card (B05) and the four-step card (B10) are on screen long enough to read, and the strip is the same tool in every beat. |
| Worked example | 2 | B05 moves the dots to the HAPPY and SAD ends for Bach and Brahms while the swatches land and the sky changes. |
| Falsifiability / edge case | 2 | B07 states "nonwestern scales: untested" beside the US↔Mexico row; B10→B11 asks for a prediction (answer slots, a 6-s countdown), then shows the paper's chart with slow-minor, fast-minor and fast-major and ticks the viewer's answers "between". |
| Active task | 2 | B10: the FAST-MINOR cell highlighted, two answer slots (lighter/darker, more/less saturated), a countdown ring from 6, then the card. |
| Friction | 2 | B01 shows the skies in an order that does not match the order the tunes played; B10 shows two opposite pulls. |
| **Total** | **12/12** | |

## Production gate (measured)

| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | **PASS.** Last frame of every beat extracted from the video passes the ink-margin and source-band checks; contrast ≥ 4.5 for every text colour (INK 10.98, INK_SOFT 4.73, SPARK_TEXT 4.70); type ≥ 28 px logical on sans captions. |
| Sources on screen, not just voiced | **PASS.** Every beat has a source line; the three essay-derived claims (B06 infants, B07 symbolism, B08 scene lengths) carry "from an essay we read" on screen. |
| Side-by-side at the moment of comparison, held ≥ 2 s | **PASS (measured).** B01 skies, B04 rows, B07 contexts + r table, B08 two strips, B09 three columns, B11 three points + answers, B12 swapped skies: all present together for the last 2.5–3 s of their beats. |
| Technical | 3840×2160, 30 fps, H.264, yuv420p, AAC 48 kHz mono, 285.6 s; no black frames; no static run over 6 s (longest 5.77 s in B09, 5.70 s in B04, both holds); frames of the last 1–3 s sampled and viewed. |

## The problem

None that blocks release. The weakest point is **the sourcing of three details, not production**: B06 (infant timeline), B07's colour symbolism and B08's scene lengths are attributed to the essay we read and have no separate source on screen. The film says so on screen ("from an essay we read") and states them as the essay's, not as findings.

## Findings

1. **[EDIT] No captions file for the long film yet** (the Short has `.srt` and `.vtt`). Generate them from `timings.json` before upload; the on-screen figures ("1752" style written forms) should appear as written, as in Week 26.
2. **[NEW SOURCE, optional] B06 / B07 symbolism / B08.** A primary source for each would upgrade "from an essay we read" to a finding. Not required to publish.
3. **[EDIT] B11's three points per axis are approximate** (read off the paper's Figure 2). They are labelled "approximate, read from chart" on screen; keep the label.
4. **Note:** the long film's `.srt`, YouTube title, description, chapters and tags are not built yet; the synthetic-voice disclosure and the tune disclosure ("synthesized for the film") belong in the description.
5. **Housekeeping:** about 2.3 GB of temporary frames (`_frames/`, `_silent/`) can be deleted after sign-off.

## What works

- The film's form is its argument: the skies, the two tunes and the strip carry the idea from the first beat to the swapped ending in B12.
- Every spoken figure is on screen at its moment, and the limits (correlation, two countries, Western classical music, pacing not colour) are stated, not buried.
- B10→B11 gives the viewer a way to be wrong, and the film shows the answer.

## Do next

1. [EDIT] Captions (`.srt`, `.vtt`) and the YouTube metadata file for the long film.
2. [EDIT] Delete the temporary frames once you confirm both videos.
3. Optional: primaries for B06–B08.
