# VISUAL-QC — *Safer By Not Looking.*

Ep. 15 · `satellite-collision-avoidance` · both cuts read by eye, 2026-10-31

> CLAUDE.md rule 5: **verify renders by LOOKING at frames, never by the mp4
> probe alone.** On this reel it mattered four times — three defects before
> GATE P that every gate passed, and one case where a gate *passed* a frame
> that was actively misleading.

---

## GATE V

| Cut | Frames | BLOCKER | MAJOR | Report |
|---|---|---|---|---|
| 16:9 `claude-for-astronomy_OmMali_30_10_2026.mp4` | 28 | 0 | 0 | `_qc/REPORT-16x9.md` |
| 9:16 `satellite-collision-avoidance-9x16.mp4` | 28 | 0 | 0 | `_qc/REPORT-9x16.md` |

Both run with an explicit `--mp4`. **Both failed on the first pass** — see
below. Contact sheets: `_qc/contact_sheet-16x9.png`,
`_qc/contact_sheet-9x16.png`.

**The contact sheet covers B00–B07 only** (16 of the 28 sampled frames), so
B08–B13 were extracted from each master directly at 85 % of their beats and
read separately.

---

## Read in the 16:9 master

| Beat | What the frame shows | Verdict |
|---|---|---|
| B00 | composer ask, `Ola, HAI`, three result lines | OK |
| B01 | name, rule, struck row, boxed row, series line | OK |
| B02 | three rows; "SO IT IS PARTLY ABOUT YOU" accented and underlined | OK |
| B03 | 1,532 marks with **3 terracotta** findable among them; chip; message note | OK |
| B04 | three panels of 1/2/3σ ellipses; disk outside / between / alone | OK |
| B05 | the summit, the threshold, both named ends | OK |
| B06 | two bars for the same conjunction straddling the dashed rule | OK |
| B07 | ghost traces fade, terracotta traces climb, cutoff rule | OK |
| B08 | two panels, ink tall then short, terracotta short then tall | OK |
| B09 | 12 terracotta of 97; the organisers' pull-quote | OK |
| B10 | diluting curve crosses the threshold, flat bound does not; two dots at the same x | OK |
| B11 | five-line verdict page, "A probability about you" | OK |
| B12 | handoff prompt, three grading lines | OK |
| B13 | title poster-style with the terracotta period | OK |

## Read in the 9:16 master

| Beat | What portrait does differently | Verdict |
|---|---|---|
| B03 | **PUBLISHED chip and message note dropped**; label, field, label stack | OK — neither is spoken; the citation still names the paper |
| B04 | panel names stack beneath the plate | OK |
| B05–B08, B10 | **every right-hand column becomes stacked legend rows** | OK |
| B06 | name and value share one line (see defect 2) | OK |
| B09 | **chip and pull-quote dropped** | OK — but this is what caused the GATE V failure below |
| B00 / B11 / B12 / B13 | re-rendered from the 916 compositions, not centre-cut | OK — verified 2160 × 3840 at source |

**The portrait reduction rule held: anything the narration speaks stayed on
screen.** What portrait loses is on-screen-only extras.

---

## Defects found by reading frames

### Before GATE P — three that every gate passed

**1 · B03 — the thirty could not be found.** The beat asks the viewer to find
three terracotta marks among 1,532. At `scale(1.7)` they were measured in a
rendered frame and were **invisible**; the entire point of the isotype did
not land. Raised to `scale(2.8)`.

**2 · B06 portrait — name and value 0.02 units apart.** The legend stacked
each name above its value and they read as one run-on block. `_swatch_row`
now takes an optional value and puts both on one line.

**3 · B08 portrait — the panel label sat on the legend**, 0.06 units clear.
Rows moved down.

### After GATE V — two failures, one of which taught the real lesson

**4 · B04 failed low-contrast at 0.23, and the obvious fix made it lie.**

The plate shaded the Gaussian as a continuous greyscale across a density
ratio of 1 : 0.056 : 1e-4. Sweeping the display gamma against the gate's own
metric:

| gamma | gate | the picture |
|---|---|---|
| 0.25 | 0.23 FAIL | honest |
| 0.09 | 0.34 pass | panels 2 and 3 almost equally dark — **read as the opposite of dilution** |
| 0.70 | 0.31 marginal | panels 2 and 3 vanished below the ink threshold |

**A gate passing is not the frame being right.** I rendered gamma 0.09, read
it, and rejected it — it would have shipped a frame arguing that more
uncertainty means more density.

The plate was redrawn as **1/2/3σ covariance ellipses**: crisp ink rather
than soft gradient, the standard way conjunction geometry is drawn, saying
the same thing. Contrast then came from removing pale ink rather than adding
dark — ghost outer rings → ink/soft at descending widths, and the three
per-panel borders deleted. Final **0.336**, margin +0.036.

**5 · B09 failed in 9:16 only, at 0.26.** Its 85 unlit team marks were
ghost-grey, just above the ink threshold. Landscape survived because its chip
and pull-quote added dark text; **portrait drops both**. Unlit marks moved to
`soft` — still a fill, so the palette rule is untouched. Portrait 0.432,
landscape 0.389.

> **The general lesson: a contrast margin that depends on elements portrait
> drops is not a margin.** Worth carrying forward.

Both fixes required re-rendering the affected scene at 4K in **both** aspects
and recompiling **both** masters. Re-verified: GATE A, W and B still clean on
B04 and B09 in both aspects, and GATE V clean on both cuts.

---

## Audio

−21.0 LUFS integrated, AAC mono, one mix shared by both cuts. Kokoro
`af_bella`, local, $0.00.

Measured per-beat durations are the master clock; both cuts run 158.93 s with
3814 frames at 24 fps, and every Manim scene lands **+0.18 s under** its beat
in both aspects, so no clip was centre-cut.

Seven scenes carry `RT_PORTRAIT`, because every landscape right-hand column
becomes stacked rows in portrait and those branches play fewer reveals.
