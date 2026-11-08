# CHECKS-REPORT — *Aim Where It's Going.*

Ep. 16 · `predictive-adaptive-optics` · pre-audio gate run, 2026-11-07

Gates F, L, A, W and B all run **before** GATE P, because they are free and
because a scene that fails them would have to be rebuilt after a human had
already signed off on its content.

**A, W and B were then re-run after the pacing solve**, because that solve
rewrites `scenes.py`. The rewrite only touches numeric timing constants, so
layout could not move — but "could not have moved" is an argument, not a
check, and the gates are free. 10/10 · 10/10 · 20/20, all still clean.

---

## Summary

| Gate | What it checks | Result |
|---|---|---|
| **F** | paperwork complete | **PASS** |
| **L** | beat mix / ledger | **PASS** — clean |
| **A** | render-free scene pre-flight | **PASS** — 10/10, first pass |
| **W** | WCAG contrast + safe margins | **PASS** — 10/10, first pass |
| **B** | pixel layout, landscape | **PASS** — 10/10, first pass |
| **B** | pixel layout, portrait | **PASS** — 10/10 after 2 fixes |
| **pre-flight** | 20 frames read by eye | **5 defects found and fixed** |
| **P** | human signature | **SIGNED** — `VERDICT: PASS`, Om Mali |
| **V** | rendered-frame QC on each master | **PASS** — 28 frames, 0 BLOCKER, 0 MAJOR, **each cut** |
| **frames read** | both finished cuts, by eye | **1 defect found that no gate could catch** — see `_qc/VISUAL-QC.md` |

> **GATE T and GATE SHARPNESS are not shipped in this toolkit**, despite
> `ai-explainer/SKILL.md` describing GATE T as "ALWAYS RUN". Tenth
> consecutive episode recording this rather than silently skipping it.

---

## GATE F — paperwork

| File | Status |
|---|---|
| `SOURCES.md` | present — verbatim Keck and Doelman quotes, the deliberately-unused list, the two measured-but-unclaimed results |
| `FACTCHECK.md` | present — every on-screen claim, PUBLISHED vs COMPUTED, plus eight refused claims and six stated limitations |
| `SHOTLIST.md` | present — 14 beats, lanes, aspect discipline, the colour contract |
| `PROMPTS.md` | present — records that **no image-generation prompts were used**, plus every seed |
| `PEDAGOGY.md` | present — awaiting signature |
| `beat_sheet.json` | 14 beats, 428 words |
| `assets/ao.py`, `assets/gen_ao.py` | the atmosphere, the lag, the predictor, the plates |
| `scenes.py` | 10 aspect-aware scenes |

## GATE L — beat lint

```
[beat-lint] clean — beat mix OK (beat_sheet.json)
```

14 beats: 4 Remotion (B00, B11, B12, B13) + 10 Manim (B01–B10).

## GATE A — render-free pre-flight

**10/10 clean, first pass.** No fixes required.

This is the first episode since Ep. 11 to pass GATE A untouched, and the
reason is that the two known stub traps were designed out before writing:
`_swatch_row` positions its label from the **container** rather than from a
measured `Text.width` (the Ep. 15 defect), and no `Line` is ever built from a
`Text.get_left()` (the Ep. 09 defect).

## GATE W — contrast and margins

**10/10 clean, first pass**, against the `claude` palette. `#B9B4A0` (ghost)
is **2.0:1 on cream and fails WCAG**, so it is used for strokes and fills only
— plate frames and the tick rules — never for text.

## GATE B — pixel layout, BOTH aspects

**20/20 clean. Landscape 10/10 on the first pass; portrait 10/10 after two
fixes to one scene.**

| Scene | landscape | portrait |
|---|---|---|
| B01_Presenter | 0 / 0 | 0 / 0 |
| B02_OneBreath | 0 / 0 | 0 / 0 |
| B03_TheDistance | 0 / 0 | 0 / 0 |
| B04_TheLaw | 0 / 0 | 0 / 0 |
| B05_TheFilter | 0 / 0 | **2 errors → 0** |
| B06_BackOrAcross | 0 / 0 | 0 / 0 |
| B07_TheCeiling | 0 / 0 | 0 / 0 |
| B08_TheBudget | 0 / 0 | 0 / 0 |
| B09_OnSky | 0 / 0 | 0 / 0 |
| B10_TheTell | 0 / 0 | 0 / 0 |

### The two portrait errors, both in B05

```
ERROR · off-frame: `theframethathasnotarrived` box=[-0.05, 0.39, 2.57, 0.57]
ERROR · text-on-text (overlap 30%): `OneLinearFilter` ✕ `oneweighteach,fittedonce`
```

1. The slot label was centred on the slot at x = 1.26 and ran to 2.57 on a
   ±1.95 frame. In portrait it now **centres on the frame**, not on the slot.
2. The weight-fan caption sat at y = 2.96 — straight through the title at
   3.14. The whole tick row moved down and the caption with it.

Both are the classic portrait failure: **a position that is comfortable in a
12.3-unit frame is off-frame in a 3.6-unit one.** Portrait remains the
stricter aspect, as it has been since Ep. 08.

### What kept landscape green on the first pass

- **Band arithmetic done on paper before writing**, which is the Ep. 15
  lesson. The plate heights (`ph = pw · ih/iw`) were computed from the actual
  PNG dimensions, not assumed.
- **Every landscape plate with a right-hand column sits at x = −1.10**, so its
  right edge clears the column (2.52…5.96) by at least 0.32.
- **Plate-internal label positions are derived, not guessed.**
  `LAW_TAU2_FX`, `NOISE_REAL_FX`, `DECOMP_GROUP_FX` and `BUDGET_BAR_FX` are
  computed from `gen_ao.py`'s own axis insets (26 px on 1560). B06's and
  B08's group labels land dead under their bar groups because of it.

### What GATE B structurally cannot check here

Five of ten scenes are plate beats. A plate's **image** is invisible to the
gate; its **frame** is a Rectangle and therefore a curve — so a label crossing
a plate's *outline* is caught while one in its *interior* is not. This is why
`slide.png`'s two scale rules were **moved out of the plate** and redrawn as
Manim mobjects: labelling a rule drawn inside the image would have put text
somewhere no gate inspects.

## Visual pre-flight — 20 frames, read before the signature

All ten scenes rendered at low resolution in both aspects and read. **It found
five defects that every gate passed.**

### 1 · B05 landscape — the whole scene sat in the top half

Ticks, weight fan, slot and labels all lived above y = −0.5; everything below
was empty to the closing line. A **FILL-THE-CANVAS defect**, and no gate tests
for it. The tick row dropped to y = −0.55 and the weight fan more than doubled
in height, so the figure now spans the band.

### 2 · B05 portrait — the same defect, after the GATE B fix

Moving the caption off the title left the bottom third empty. The row dropped
again and the bars grew.

### 3 · B09 — a joiner line 0.10 units long

The two result cards sit 0.30 apart, so a line drawn between them with 0.10
of clearance each side rendered as a **stray tick** with "same predictor"
floating beside nothing. The shared fact moved **below both cards**, which
also filled the band they left empty.

### 4 · B09 — three terracotta elements in one beat

With the shared fact accented, the beat carried an accented 2021 result, an
accented shared fact *and* an accented closing line. "One terracotta moment
per beat — if two things are orange, neither is the point." The shared fact
dropped to `soft`.

### 5 · B03 and B04 — dead bottom-right quadrants

Both put their right-hand column in the top half and their figure on the
left, leaving the lower right empty. B03's chip block moved down to y = −0.52
and its scale rules spread from x = −5.20; B04's column now runs to −1.12.

### What the frames confirmed as correct

- **B03** — the two cuts are visibly the *same shape, offset*, and the 1.7 cm
  rule beside the 15 cm rule makes the ratio the picture.
- **B04** — the terracotta connector reads as the subject; the two curves no
  longer read as redundant now that the pure-Kolmogorov line is gone.
- **B05** — the fan growing toward the newest frame, the arrow jumping a
  labelled 2 ms gap into an *empty* slot. The mechanism reads without the
  narration.
- **B06** — the short soft bars say "nothing gained" rather than "nothing
  drawn", which is what the log floor at gain = 1 was for.
- **B08** — the terracotta slice collapses while the bar barely shortens.
  That gap *is* the beat.
- **B10** — struck expectation, then paired counters; the reversal between
  quiet and noisy sensor is legible at a glance.
- Every scene carries its title, hairline, citation and wordmark bug.

Re-verified after all fixes: GATE A, W and B still clean on B03, B04, B05 and
B09 in both aspects.

## Numerical self-check

`assets/gen_ao.py` **asserts eight claims and writes no plate if any fails.**
Reproduced on seed 1616, 2026-11-07:

```
  translation operator is exact                  ok   rel err 2.2e-07
  Kolmogorov lag exponent is 5/3                 ok   1.666667
  sigma^2(tau0) = 1 rad^2                        ok   0.9972 rad^2
  screens reproduce the spectral integral        ok   ratio 1.0205
  in-band lag error goes as tau^2, not tau^(5/3) ok   1.990
  prediction still wins at realistic noise       ok   11.20x (1 layer) 4.82x (3 layers)
  more layers cost the predictor                 ok   11.20 > 5.24 > 4.82
  looking BACK beats looking ACROSS              ok   L1 5.1/1.2  L2 3.7/1.0  L3 3.7/1.1
```

**Two results are measured and reported but deliberately NOT claimed on
screen**: the in-band share of total phase variance (~79%, unstable across
realisations) and the two-layer condition (within 10% of three layers). Both
are in `FACTCHECK.md`.

## Pacing — solved after the signature

428 words predicted **2:38.6**; Kokoro measured **160.82 s = 2:40.8**, 1.4%
long, **19.2 s inside the 3:00 cap**. Across Eps. 06–16 the words-only model
has now erred +10.4%, −0.4%, −5.0%, … , +1.4% — noisy in both directions, which
is why the margin is budgeted rather than trusted.

**Five** scenes — B03, B04, B06, B07, B08 — turn a landscape right-hand column
into stacked rows and so play fewer reveals in portrait. (The pre-audio note
here said six; the measured pass says five. B05 restacks its layout but plays
the same twelve reveals in both aspects.) Each of the five carries its own
`RT_PORTRAIT`, solved to reproduce the landscape body length:

| beat | portrait plays | landscape plays | RT | RT_PORTRAIT |
|---|---|---|---|---|
| B03 | 11 | 13 | 1.550 | 1.798 |
| B04 |  8 | 11 | 1.550 | **2.000 (capped)** |
| B06 | 10 | 12 | 1.550 | 1.759 |
| B07 |  8 | 10 | 1.550 | 1.878 |
| B08 | 10 | 12 | 1.550 | 1.770 |

B04 portrait wanted 2.190 and was capped at 2.000, which leaves it ~0.9 s more
frozen tail than its landscape twin. That is a deliberate trade: past RT ≈ 2 a
reveal stops reading as a reveal, and `hold_to_beat()` absorbs the difference
into a held closing frame, which is invisible.

Every scene lands **under** its beat in both aspects — worst case −0.220 s
(B06), and `frames / 24 == duration` exactly on all twenty clips. The residual
0.15–0.22 s undershoot is frame quantisation inside `play()` and is not
fixable by raising HOLD: a larger HOLD raises `renderer.time` and
`hold_to_beat()` shortens the tail by the same amount. Undershoot is the
correct side to err on — a short clip is padded with a held frame, a long one
is centre-cut and would clip the closing line off both ends.

## Cost

**$0.00.** Kokoro `af_bella` locally; Manim and Remotion for picture; no image
model; no ElevenLabs; no API keys. Fellow Tier throughout.
