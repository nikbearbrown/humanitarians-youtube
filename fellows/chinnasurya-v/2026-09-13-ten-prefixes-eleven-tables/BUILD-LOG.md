# BUILD-LOG — Ten Prefixes, Eleven Tables

## Output

| | |
|---|---|
| Master | `medhavy-lti-tables.mp4` (also at `$ART_HOME/renders/`) |
| Resolution | 3840 x 2160 · 24 fps |
| Duration | 114.5 s (1:54.5) |
| Audio | AAC 48 kHz stereo, Kokoro `am_onyx`, per-beat timeline |
| Beats | 8, all filled from `media/` |
| Size | 3.6 MB |

## Timeline

Script written 2026-09-13, unchanged since. Built 2026-10-28, in the same session
as `medhavy-canvas-sync`.

## Architecture

Toolkit read-only. Narration via `generate_audio_kokoro.py`, conform via
`./art final`, visuals rendered out of tree by `scenes/render_scenes.py` into
`media/<beat>.mp4`. The core — layout, fonts, `fit()`, `node()`, elastic
allocation, frame assembly — came over verbatim from `medhavy-canvas-sync`,
which had itself taken it from `medhavy-it-requirements`. Only the eight scene
functions and one new `tcard()` helper are new. `git status` on `$ART_HOME` empty
before and after.

## Duration drift

Script estimate 107 s from 357 words at 3.35 words/sec. Measured 114.3 s of
narration, 114.5 s conformed, about 7 percent over. The overshoot is B02 and B06,
both of which read lists of table names, and Kokoro reads an identifier more
slowly than prose. Same cause as the overshoot on `medhavy-it-requirements`. No
holds padded, no narration trimmed.

| Beat | Measured |
|---|---|
| B00 | 10.28 |
| B01 | 10.22 |
| B02 | 17.75 |
| B03 | 16.64 |
| B04 | 15.32 |
| B05 | 10.75 |
| B06 | 20.20 |
| B07 | 13.18 |

## Defects found in QC and fixed

Three, all from the contact sheet. The title cards came out clean first time,
which is the first reel in this series where that is true, because
`title_card()` now derives its geometry from the footer instead of from a
fraction of the frame.

1. **B06's `+ institutions` label collided with the `11` numeral.** It was placed
   at `lx + 0.52 * (rx - lx)`, a guessed midpoint that takes no account of how wide
   the numerals actually render. Fixed by measuring `10` with the display font's own
   metrics, computing the real gap, and passing the label through `fit()` so it can
   never exceed it.
2. **B03's table names sat hard on their arrows.** Drawn at `mid - 1.55 * size`,
   which left the descenders touching the arrow body. Lifted to `1.95 * size`.
3. **B06's captions touched the numerals above them.** `TABLES NAMED lti_*` was at
   `0.98 * nf.size` below the numeral origin, which is inside the numeral's own
   glyph box. Moved to `1.10`.

All three are the same mistake in different clothes, and it is the mistake this
project keeps making: **a position guessed as a fraction of something, when it
could have been measured from the thing it has to clear.** Defect 1 is the clean
example — the fix is not a bigger margin, it is asking the font how wide the text
actually is.

## Lints — reported, not silenced

- `SKIN LINT: NO RENDERABLE BEATS` — expected for this architecture. Same run
  reports `8/8 filled`.
- `'step-reveal' carries 5/8 beats (62%) — over the ~40% cap`. Third reel in a row
  to trip this, and the third different label to be the one over: `step-reveal` on
  the first reel, `hard-snap` on `medhavy-it-requirements` and on
  `medhavy-canvas-sync`, `step-reveal` again here. The labels come from the
  script's own shot lists and were left as written.

## Judgment calls

- B04 states launch audit retention as 1 hour. That is what the schema says, and
  a later audit of the same codebase found the published privacy policy says 12
  months and the purge job is not scheduled. Rather than drop the claim or quietly
  change the number, the discrepancy is written into `FACTCHECK.md` as a note on
  row 4, with the instruction that the figure must be re-measured before any
  rebuild. The reel ships with a known-contested number and says so in its own
  paperwork.
- No connection string, no column contents, no sample rows, no real identifiers.
  B06's numerals are counts, and the arithmetic is in the fact-check.

## Not done

- No 9:16 cut. At 1:54 it fits under the 180 s cap without dropping beats, but it
  needs portrait scene layouts rather than a centre crop.
- No captions or word clock.
- `PEDAGOGY.md` carries `VERDICT: PENDING`. Not self-signed.
