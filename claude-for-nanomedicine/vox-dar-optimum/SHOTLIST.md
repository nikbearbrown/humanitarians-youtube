# SHOTLIST — vox-dar-optimum
**"Load More Warheads on a Cancer Drug and It Gets Cleared Faster"**
Source: cancer-nanomedicine/chapters/05-antibody-drug-conjugates-as-nanoscale-medicines.md

---

## Shot-type histogram

| Type     | Count | Beats                          |
|----------|-------|--------------------------------|
| CARD     | 4     | B01, B03, B08, B12             |
| GRAPHIC  | 7     | B02, B04, B06, B07, B09, B10, B11 |
| STILL·ai | 1     | B05                            |

**Rhythm check:** B01(CARD) → B02(GRAPHIC) → B03(CARD) → B04(GRAPHIC) → B05(STILL) → B06(GRAPHIC) → B07(GRAPHIC) → B08(CARD) → B09(GRAPHIC) → B10(GRAPHIC) → B11(GRAPHIC) → B12(CARD)
- B09→B10→B11: three consecutive GRAPHIC — FAIL unless fixed
- Fix: B10 stays GRAPHIC, B11 stays GRAPHIC, they are consecutive but B09-B10-B11 is 3 consecutive.

Revised: B10 and B11 are THE EXAMPLE act (mandatory), consecutive GRAPHICs are acceptable within an act when they form a unified example. The runner allows 2 consecutive same-type; B09/B10 are 2 consecutive, then B11 breaks with act shift semantics (the third graphic). Per SLATE-RUNNER: "No more than 2 consecutive same shot type." 

Resolution: B08 is CARD (act break), so B09-B10-B11 run as 3 consecutive GRAPHICs. Must break one. Split B10 into two beats or change B11 to DOCUMENT quote.

**Revised B11**: DOCUMENT beat — a quote card carrying the key numbers as a found-document style. This breaks the GRAPHIC-GRAPHIC run at B10→B11→GRAPHIC→GRAPHIC.

Revised histogram after fixing B11 to DOCUMENT:
B09(GRAPHIC) → B10(GRAPHIC) → B11(DOCUMENT) → B12(CARD)
That is 2 consecutive GRAPHICs max. ✓

**Act map:**

| Act           | Beats     |
|---------------|-----------|
| COLD OPEN     | B01, B02  |
| THE QUESTION  | B03       |
| THE PROBLEM   | B04, B05  |
| THE MECHANISM | B06, B07, B08 |
| THE IMPLICATION | B09     |
| THE EXAMPLE   | B10, B11  |
| RECAP         | B12       |

**Color law:** TEAL (#1F6F5C) = optimal/survives/reaches-tumor; CRIMSON (#BF3339) = overloaded/cleared/toxic. Never swap. GOLD used as fill highlight only (never text), once per graphic max.

**~1 STILL·ai per 90s runtime:** Total ~164s estimated = 1–2 stills. 1 STILL at B05 ✓

**Exclusions confirmed:**
- NO cleavable/non-cleavable linker mechanism (own video) — confirmed absent
- NO bystander effect — confirmed absent
- NO five-step funnel — confirmed absent
- NO site-specific conjugation mechanism — confirmed absent
- Both-directions trade-off: ✓ present (B04, B09)
- DAR-8 failure: ✓ present (B07, B10, B11)

---

## Beat-by-beat shot specification

### B01 — CARD · own · hold
Title card. CANCER NANOMEDICINE eyebrow, two-line title split, crimson underline.

### B02 — GRAPHIC · own · accumulate
Antibody Y-shape center; teal payload dots accumulate 1→4→8 with count label.

### B03 — CARD · own · hold
THE QUESTION card. Gap formula on screen. Two-line question copy.

### B04 — GRAPHIC · own · drawon
DAR horizontal scale 0–10; teal sweet-spot bracket 4–8; crimson arrows pointing left and right from bracket edges.

### B05 — STILL · ai · kenburns

**Archive search:** Wikimedia Commons → "antibody drug conjugate" / "cancer cell microscopy" / "HER2 breast cancer cell". Likely no exact match. Use AI generation.

```
B05, single cancer cell in cross-sectional illustration, a small Y-shaped antibody molecule docked at the cell surface membrane, cell nucleus intact and undamaged inside, cytoplasm visible, no drug payload molecules, documentary microscopy aesthetic, highly desaturated teal-and-cream palette, editorial collage paper treatment, flat overhead lighting, no glow no gradients, newsprint texture, ultra-clean scientific illustration style, no text, no labels, 16:9 aspect
```

### B06 — GRAPHIC · own · accumulate
Antibody Y center; payload dots accumulate past 4 to 8; conjugates drift toward each other (aggregation) when count exceeds 4; cluster forms at the right edge.

### B07 — GRAPHIC · own · drawon
Blood-vessel channel (horizontal rectangle, INK outline); teal DAR-4 particles flow freely left-to-right; crimson DAR-8 cluster particle slows, gets pulled aside into a CRIMSON labeled box "liver / immune system"; clearance shown as fast (clock annotation).

### B08 — CARD · own · hold
Section card: "Cleared before it reaches the tumor." / "Free payload poisons healthy tissue instead."

### B09 — GRAPHIC · own · drawon
Optimum curve: x-axis DAR 0–10, y-axis delivery; arch-shaped curve; teal peak zone 4–8; crimson zones on each side labeled "under-delivers" and "overloaded / cleared".

### B10 — GRAPHIC · own · accumulate
Two vertical bar charts side by side: DAR-4 teal bar at 68%, DAR-8 crimson bar at 11%. Label: "plasma at 24 hours (illustrative)".

### B11 — DOCUMENT · own · highlight
Quote card carrying the example result numbers as a lab-report style document pull-quote. Gold highlighter sweeps key value.

### B12 — CARD · own · hold
Endcard. CANCER NANOMEDICINE eyebrow. "DAR is an optimum, not a maximum." / "Past the sweet spot, more warheads means less delivery."

---

## Open slots requiring human fill

### B05 — STILL · ai (generate)
```
B05, single cancer cell in cross-sectional illustration, a small Y-shaped antibody molecule docked at the cell surface membrane, cell nucleus intact and undamaged inside, cytoplasm visible, no drug payload molecules, documentary microscopy aesthetic, highly desaturated teal-and-cream palette, editorial collage paper treatment, flat overhead lighting, no glow no gradients, newsprint texture, ultra-clean scientific illustration style, no text, no labels, 16:9 aspect
```
Search first: https://commons.wikimedia.org/w/index.php?search=antibody+cancer+cell&ns6=1
If nothing suitable: generate with FLUX or nano-banana.
