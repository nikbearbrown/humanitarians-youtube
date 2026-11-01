# CHECKS-REPORT — *Safer By Not Looking.*

Ep. 15 · `satellite-collision-avoidance` · pre-audio gate run, 2026-10-31

Gates F, L, A, W and B all run **before** GATE P, because they are free and
because a scene that fails them would have to be rebuilt after a human had
already signed off on its content.

---

## Summary

| Gate | What it checks | Result |
|---|---|---|
| **F** | paperwork complete | **PASS** |
| **L** | beat mix / ledger | **PASS** — clean |
| **A** | render-free scene pre-flight | **PASS** — 10/10 after 1 fix |
| **W** | WCAG contrast + safe margins | **PASS** — 10/10 |
| **B** | pixel layout, landscape | **PASS** — 10/10, 0 errors 0 warnings |
| **B** | pixel layout, portrait | **PASS** — 10/10, 0 errors 0 warnings |
| **pre-flight** | 20 frames read by eye | **3 defects found and fixed** |
| **P** | human signature | **PASS** — signed 2026-10-30 |
| **V** | 16:9 master, explicit `--mp4` | **PASS** — 28 frames, 0/0 (after 1 fix) |
| **V** | 9:16 master, explicit `--mp4` | **PASS** — 28 frames, 0/0 (after 1 fix) |
| frame reading | both cuts, B08-B13 extracted separately | clean — see `VISUAL-QC.md` |

> **GATE T and GATE SHARPNESS are not shipped in this toolkit**, despite
> `ai-explainer/SKILL.md` describing GATE T as "ALWAYS RUN". Ninth
> consecutive episode recording this rather than silently skipping it.

---

## GATE F — paperwork

| File | Status |
|---|---|
| `SOURCES.md` | present — verbatim ESA and Balch/Martin/Ferson quotes, the deliberately-unused list, and the two measured-but-unclaimed results |
| `FACTCHECK.md` | present — every on-screen claim, PUBLISHED vs COMPUTED, plus seven refused claims |
| `SHOTLIST.md` | present — 14 beats, lanes, aspect discipline |
| `PROMPTS.md` | present — records that **no image-generation prompts were used** |
| `PEDAGOGY.md` | present — awaiting signature |
| `beat_sheet.json` | 14 beats, 426 words |
| `assets/conj.py`, `assets/gen_conj.py` | the probability, the population, the plates |
| `scenes.py` | 10 aspect-aware scenes |

## GATE L — beat lint

```
[beat-lint] clean — beat mix OK (beat_sheet.json)
```

14 beats: 4 Remotion (B00, B11, B12, B13) + 10 Manim (B01–B10). The ledger
agrees: `[todo] 0/14 filled`.

## GATE A — render-free pre-flight

**10/10 clean, after one fix.**

### The defect it caught

```
WARN  1 coord(s) outside the safe area, e.g. (6.6, 1.4) in move_to
```

`_swatch_row` positioned its label at `left + swatch + lab.width/2`. That is
correct in a real render, and **meaningless under the geometry stub**, where
a `Text` has no width — so the gate computed x = 6.6 on a ±6.15 frame.

The fix is not to suppress the warning but to stop depending on the measured
width at all: the label is already fitted to `w - 0.42`, so centring it in
the space right of the swatch is exact in both the stub and the render.

## GATE W — contrast and margins

10/10 clean against the `claude` palette. `#B9B4A0` (ghost) is **2.0:1 on
cream and fails WCAG**, so it is used for strokes and fills only — including
B07's fading-alert traces and B09's unlit team marks — never for text.

## GATE B — pixel layout, BOTH aspects

**20/20 clean, 0 errors, 0 warnings, on the first pass.**

| Scene | landscape | portrait |
|---|---|---|
| B01_Presenter | 0 / 0 | 0 / 0 |
| B02_OneBreath | 0 / 0 | 0 / 0 |
| B03_TheBenchmark | 0 / 0 | 0 / 0 |
| B04_TheNumber | 0 / 0 | 0 / 0 |
| B05_Dilution | 0 / 0 | 0 / 0 |
| B06_TheFlip | 0 / 0 | 0 / 0 |
| B07_TheTask | 0 / 0 | 0 / 0 |
| B08_TheReversal | 0 / 0 | 0 / 0 |
| B09_NinetySeven | 0 / 0 | 0 / 0 |
| B10_TheTell | 0 / 0 | 0 / 0 |

First-pass green is not luck — it is the Ep. 11–14 lessons written into the
layout before the first render:

- **Every landscape plate beat with a right-hand column puts its plate at
  x = −1.10**, so the plate's right edge is 2.20 and the column (2.52…5.96)
  clears it by 0.32. This is the Ep. 14 defect, now a named constant
  (`PLATE_X`) with the reason in the comment. B04 is the deliberate
  exception: it has no right-hand column, so it centres.
- **Plate-internal label positions are measured, not guessed.** `FLIP_FX`,
  `BARS_PANEL_FX` and `GEOM_PANEL_FX` are derived from each plate's actual
  pixel geometry (Axes insets its box by 18 px on 1560) and are all safely
  inside the plate, which is what makes the `pw * k` form legal here.
- **Band arithmetic was done before writing the scenes**, which caught three
  collisions on paper: B03's and B09's isotype labels sat 0.13 and 0.09 units
  from their fields (floor is 0.15), and B10's right column ran to y = −2.00,
  past the figure band.

### What GATE B structurally cannot check here

Six of ten scenes are plate beats. A plate's **image** is invisible to the
gate; its **frame** is a Rectangle, and therefore a curve — so a label
crossing a plate's *outline* is caught while one in its *interior* is not.
Everything inside was verified by arithmetic and by reading frames.

## Visual pre-flight — 20 frames, read before the signature

All ten scenes rendered at low resolution in both aspects and read as contact
sheets. **It found three defects that every gate passed.**

### 1 · B03 — the thirty could not be found

The beat asks the viewer to find three terracotta marks in a field of 1,532.
At `scale(1.7)` they were measured in a rendered frame and were **invisible**
— the entire point of the isotype did not land. Raised to `scale(2.8)`, where
the mark nearly fills its own cell: unmistakably one mark, unmistakably
visible. No gate tests "can a human find this".

### 2 · B06 portrait — name and value 0.02 units apart

The two legend rows stacked each name above its value at 0.56 spacing, which
left **0.02 units** between one row's value and the next row's name. They
read as a single run-on block. `_swatch_row` now takes an optional value and
puts name and number on one line.

### 3 · B08 portrait — the panel label sat on the legend

"scored on the 124 notified" ended 0.06 units above "the trained model".
Legend rows moved from −0.52/−1.02 to −0.72/−1.18, chip to −1.74.

### What the frames confirmed as correct

- **B04** — the three panels on one density scale read as *spreading and
  thinning*, which is the whole mechanism. The terracotta disk is identical
  and fixed in all three.
- **B05** — the summit, the threshold and both named ends read immediately.
- **B06** — two bars for the same conjunction straddling the dashed rule.
- **B07** — ghost traces fade, terracotta traces climb, the cutoff rule sits
  where the forecast is made.
- **B08** — the reversal is legible at a glance: ink tall then short,
  terracotta short then tall.
- **B09** — 12 lit marks in 97 reads as a proportion without a caption.
- **B10** — the diluting curve crosses the threshold while the flat bound
  does not, and the two dots sit at the same x.
- Every scene carries its footer, citation and wordmark bug.

Re-verified after all three fixes: GATE A, W and B still clean on B03, B06
and B08 in both aspects.

## Pacing and play-count parity

**Solved and verified.** Measured narration totals **158.93 s (2:38.9)**,
+5.2 % against the words-only estimate — the same sign and size as Ep. 14.

Nine of ten scenes hit or neared the RT 1.55 cap with HOLD taking the
remainder. `natboth15.py` then found **seven** scenes whose portrait branch
plays fewer reveals, because every landscape right-hand column becomes
stacked legend rows and B03/B09 drop their chips and notes entirely. All
seven carry `RT_PORTRAIT`. `verify15.py`:

```
worst headroom +0.00 s
PASS: every scene lands UNDER its beat in BOTH aspects
```

All twenty clips land exactly **+0.18 s** under their beat — the `TAIL_TRIM`
— so nothing was centre-cut in either cut.

### What GATE V then found (both cuts failed first time)

- **B04, 16:9** — low-contrast 0.23. The density-shaded plate could not be
  rescued by its display gamma: 0.09 passed the gate but rendered panels 2
  and 3 almost equally dark, reading as the OPPOSITE of dilution. Redrawn as
  1/2/3σ covariance ellipses. Final 0.336.
- **B09, 9:16 only** — low-contrast 0.26. Its 85 ghost-grey marks were the
  dominant ink once portrait dropped the chip and pull-quote that carried
  landscape. Unlit marks → `soft`. Portrait 0.432, landscape 0.389.

**A contrast margin that depends on elements portrait drops is not a
margin.**

## Numerical self-check

`assets/gen_conj.py` **asserts four claims and writes no plate if any fails.**
Re-verified reproducing on seed 1515, 2026-10-31:

```
  Pc peaks at sigma 212.1 m  (d/sqrt(2) = 212.1)   Pc = 1.635e-03
  Pc crosses 1e-04 at sigma 1397.7 m on the dilution branch
  degraded sigma 5000.0 m -> Pc 7.986e-06
  max-Pc (scale-free)     -> 1.635e-03
  final risk >= 1e-4 : 180 of 120,000 (0.15%)
                        all MSE   notified MSE
  persistence            0.0609          1.275
  ridge                  0.0152          4.130
  -> all four hold. writing plates.
```

**Two results are measured and reported but deliberately NOT claimed on
screen as fixes**: the σ/d feature (−2.7 % on the notified error) and tail
reweighting (2.4× better on the tail, 15× worse overall, still loses to
persistence). B10 states the first out loud as a fix that did not work.

## Cost

**$0.00.** Kokoro `af_bella` locally; Manim and Remotion for picture; no
image model; no ElevenLabs; no API keys. Fellow Tier throughout.
