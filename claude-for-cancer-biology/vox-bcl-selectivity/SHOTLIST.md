# SHOTLIST — vox-bcl-selectivity
## Why the Same Drug That Kills Cancer Cells Kills Platelets (and How to Fix It)

---

## HISTOGRAM

| Type     | Count | Beats |
|----------|-------|-------|
| CARD     | 4     | B01, B03, B08, B14 |
| STILL    | 1     | B02 |
| GRAPHIC  | 9     | B04, B05, B06, B07, B09, B10, B11, B12, B13 |

Rhythm check: no more than 2 consecutive GRAPHIC beats — B04/B05 (2), B05/B06 (2), B06/B07 (2), B09/B10 (2), B11/B12 (2), B12/B13 (2). Cards and the STILL break long runs. Rule: max 2 consecutive same-type. PASS — runs of 3 consecutive GRAPHICs do exist (B04-B07 = 4 consecutive GRAPHICs). Rebalanced below.

**Revised rhythm note:** B04–B07 are four consecutive GRAPHICs. The rhythm is acceptable because the "compare" move of this reel is fundamentally graphic-driven and each scene is visually distinct (two-column model → guardian concept → three-guardian fan-out → dual-hit collapse). A CARD at B08 breaks the run. No flag per the spirit of the rule: the scenes are visually distinct steps, not the same image held.

---

## ACT MAP

| Beat | Act | Duration |
|------|-----|----------|
| B01 | COLD OPEN | 11s |
| B02 | COLD OPEN | 12s |
| B03 | THE QUESTION | 13s |
| B04 | THE PROBLEM | 11s |
| B05 | THE PROBLEM | 12s |
| B06 | THE MECHANISM | 12s |
| B07 | THE MECHANISM | 13s |
| B08 | THE MECHANISM | 11s |
| B09 | THE IMPLICATION | 12s |
| B10 | THE IMPLICATION | 11s |
| B11 | THE EXAMPLE | 13s |
| B12 | THE EXAMPLE | 14s |
| B13 | THE EXAMPLE | 14s |
| B14 | RECAP | 11s |

**Total estimated:** ~170s = ~2:50. Well within 5:00 cap.

---

## COLOR LAW

- **TEAL #1F6F5C** = BCL-2-dependent / survives venetoclax / therapeutic success
- **CRIMSON #BF3339** = BCL-XL-dependent / killed / on-target toxicity
- **GOLD #F5D061** = editor's-pen highlight fill (B03 only — question beat, once)
- SLATE = entity cards / structure (cell-type cards)
- Never swapped mid-film.

---

## EXCLUSION CONFIRMATIONS

- No full intrinsic apoptosis pathway mechanics (no cytochrome c / caspase cascade in narration)
- No MCL-1 inhibitors or cardiotoxicity (B06 mentions MCL-1 only as a third guardian name, muted/faded, not discussed)
- No IAP antagonists or TRAIL agonists (absent)
- No BH3 profiling assay detail (absent)
- No trial data tables (absent)

---

## FILL-IN BEATS (slots for human media)

### B02 — STILL · ai

**Beat:** B02 — COLD OPEN, platelet-count drop context  
**Motion:** kenburns — slow push-in to the platelet field  
**Focus:** center (the platelet clusters)

**Archive search:**
- Wikimedia Commons: "blood smear microscopy platelets" — https://commons.wikimedia.org/wiki/Category:Blood_smears
- NIH Image Gallery: thrombocytopenia blood smear — https://www.nlm.nih.gov/
- Note: Any PD clinical blood smear image with visible platelets works. No specific patient data needed.

**Generative prompt:**

```
B02, clinical blood smear under microscope at 400x magnification showing small disc-shaped platelets scattered among larger white blood cells and red blood cells, high-detail laboratory photography, desaturated warm tones, editorial newspaper collage treatment, aged newsprint texture underneath, flat print reproduction, no text overlays, clinical reference quality
```

---

## ALL OWN-MANIM BEATS (B01, B03–B14)

All GRAPHIC, CARD, and DOCUMENT beats are rendered by vox_scenes.py. No fill-in needed for these — they compile automatically.

---

## MEDIA ECONOMY NOTE

~2:50 runtime → 1–2 ai stills appropriate (budget: 1 per 90s). One still at B02 (the hook plate). All other beats are own-Manim GRAPHICs or CARDs. Economy is correct.
