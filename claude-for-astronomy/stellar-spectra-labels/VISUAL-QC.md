# VISUAL-QC — *What The Model Would Say.*

Ep. 14 · `stellar-spectra-labels` · both cuts read by eye, 2026-10-23

> CLAUDE.md rule 5: **verify renders by LOOKING at frames, never by the mp4
> probe alone.** On this reel that mattered twice — the pre-flight found two
> defects every gate passed.

---

## GATE V

| Cut | Frames | BLOCKER | MAJOR | Report |
|---|---|---|---|---|
| 16:9 `claude-for-astronomy_OmMali_23_10_2026.mp4` | 28 | 0 | 0 | `_qc/REPORT-16x9.md` |
| 9:16 `stellar-spectra-labels-9x16.mp4` | 28 | 0 | 0 | `_qc/REPORT-9x16.md` |

Both run with an explicit `--mp4`. Contact sheets: `_qc/contact_sheet-16x9.png`,
`_qc/contact_sheet-9x16.png`.

**The contact sheet covers B00–B07 only** (16 of the 28 sampled frames), so
B08–B13 were extracted from each master directly at 85 % of their beats and
read separately. A gate's summary line is not the frame being right.

---

## Read in the 16:9 master

| Beat | What the frame shows | Verdict |
|---|---|---|
| B00 | composer ask, `Ciao, HAI`, three result lines | OK |
| B01 | name, rule, struck row, boxed row, series line | OK |
| B02 | three rows; "SO IT PREDICTS THE MODEL" accented and underlined | OK |
| B03 | 5 terracotta marks against a 560-mark field; chip; "no stellar models / no line list" | OK |
| B04 | three spectra, rows named in the margin, terracotta guide through the deepening line | OK |
| B05 | four boxes, physics model in terracotta, bracket under links 2–4 | OK |
| B06 | tight scatter on the traced diagonal, `0.033 dex` | OK |
| B07 | points off the diagonal, axis reads "what the TRUTH says", `0.128 dex` | OK |
| B08 | three bars; names and values under their own bars; **15× span clear of bar three** | OK |
| B09 | the trend, zero named in the margin, `correlation 0.995`, the slope | OK |
| B10 | terracotta bar tallest, two shorter bars named as the wins | OK |
| B11 | five-line verdict page, heading "Precision is agreement, not accuracy" | OK |
| B12 | handoff prompt with three grading lines | OK |
| B13 | title poster-style with the terracotta period, handle, series line | OK |

## Read in the 9:16 master

| Beat | What portrait does differently | Verdict |
|---|---|---|
| B03 | **PUBLISHED chip dropped**; label, marks, grid, card stack vertically | OK — the chip is the one item the narration does not speak; the citation line still names the paper |
| B04 | row names stack beneath the plate instead of sitting in the margin | OK |
| B05 | chain runs top-to-bottom, bracket on the right | OK |
| B06 / B07 | axis notes and chip stack beneath the plate | OK |
| B08 / B10 | bar names become legend rows with colour swatches; the 15× becomes a chip | OK |
| B09 | **zero named in a note, not the margin** — a 3.40-unit plate in a 3.60-unit frame leaves no margin to put it in | OK |
| B00 / B11 / B12 / B13 | re-rendered from the 916 compositions, not centre-cut | OK — verified 2160 × 3840 at source |

**The portrait reduction rule held: anything the narration speaks stayed on
screen.** The only two things portrait loses are on-screen-only extras, and
both are carried elsewhere in the frame.

---

## Defects found by reading frames, after every gate had passed

### 1 · B08 — the 15× span was invisible

The double-arrow sat on bar three's right edge in the same terracotta as the
bar. The shaft disappeared into it; only the arrowheads showed, as two ears
above the bar top. The `15x` tag floated with nothing connecting it to
anything — **the beat's central comparison did not read at all.**

Same-colour-on-same-colour is not an overlap GATE A, W or B tests, and the
arrow was geometrically exactly where it was asked to be. Moved to x = 1.85,
clear of both the bar and the plate edge. Confirmed in the final master.

### 2 · B07 — the plate frame blinked off

`FadeOut` removed `before`'s frame and `after` had been built without one, so
the border vanished between B06 and B07 — precisely the moment the viewer is
asked to accept that nothing about the model changed. `after` now carries a
frame. Confirmed in the final master.

### Found earlier, in the pre-GATE-P pre-flight

**`spectra.png` was clipping its own point.** A fixed 0.3–1.0 flux window cut
the metal-rich spectrum's deepest lines — the very thing the plate exists to
show. Normalised to the actual range across all three spectra and re-read.

---

## Audio

−21.0 LUFS integrated, LRA 2.8 LU, AAC mono 24 kHz, one mix shared by both
cuts. Kokoro `af_bella`, local, $0.00.

Measured per-beat durations are the master clock; both cuts run 155.07 s with
3721 frames at 24 fps, and every Manim scene lands **+0.18 s under** its beat
in both aspects, so no clip was centre-cut.
