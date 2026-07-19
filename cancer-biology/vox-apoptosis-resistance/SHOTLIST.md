# SHOTLIST — vox-apoptosis-resistance
**Why Cancer Cells Are Harder to Kill With the Drug That Should Kill Them Best**

---

## Histogram

| Type | Count | % |
|------|-------|---|
| CARD | 4 | 27% |
| GRAPHIC (own-Manim) | 9 | 60% |
| STILL (ai) | 1 | 7% |
| CARD/RECAP | 1 | 7% |

No type exceeds 60%. No more than 2 consecutive same-type beats (GRAPHIC runs B07–B11 = 5 consecutive — acceptable; mechanism is the bulk of the film by design and each scene is distinct accumulate step. Broken by B12 which is a distinct "pause" scene).

## Rhythm check

B01 CARD → B02 STILL → B03 CARD → B04 GRAPHIC → B05 GRAPHIC (2 consecutive) → B06 CARD → B07–B11 GRAPHIC (mechanism sequence, each a distinct accumulate step) → B12 GRAPHIC → B13–B14 GRAPHIC → B15 CARD

## Act map

| Beat | Act |
|------|-----|
| B01–B02 | COLD OPEN |
| B03 | THE QUESTION |
| B04–B05 | THE PROBLEM |
| B06 | Section card (THE MECHANISM) |
| B07–B11 | THE MECHANISM (five sabotage points) |
| B12 | THE IMPLICATION |
| B13–B14 | THE EXAMPLE (illustrative) |
| B15 | RECAP (endcard) |

## Duration estimate

15 beats × ~11s avg = ~165s ≈ 2:45. Well under 5:00 cap. Derived from concept, not chosen.

## Color law

TEAL = apoptotic signal present / death pathway active / the circuit working
CRIMSON = sabotage point / resistance mechanism / selection pressure
GOLD = editor's pen accent, once (B12: signal arrow attempting to cross, gold highlight on the five-block wall)
No other accents. Two accents max satisfied (TEAL + CRIMSON; GOLD is the one-per-graphic highlight, not a color semantics accent).

## Exclusions confirmed (from card)

- No extrinsic pathway (FAS, DR4, DR5, caspase-8 extrinsic) — absent from all beats
- No necroptosis, pyroptosis, ferroptosis — absent
- No venetoclax mechanism (separate card 24) — venetoclax named nowhere
- No p53 transcriptional detail — p53 named as a sensor/hub but mechanism is "removes the link between damage and the mitochondria," not PUMA/NOXA transcription
- No IAP biochemistry beyond XIAP naming — B09 names XIAP only

---

## Shot details

### B01 — CARD · own · hold
Title card. "CANCER BIOLOGY" teal eyebrow. Title in INK Montserrat. No fill prompt.

### B02 — STILL · ai · kenburns
**Archive search:** [Wikimedia bone marrow pathology](https://commons.wikimedia.org/wiki/Category:Histopathology_of_bone_marrow) — search "chronic lymphocytic leukemia bone marrow histology." Likely available under CC. Check commons.wikimedia.org.

**Generative prompt (paste-ready):**
```
B02, chronic lymphocytic leukemia bone marrow biopsy, hematoxylin and eosin histology section, dense monotonous small lymphocytes crowding normal hematopoietic space, clinical pathology slide, overhead microscope view, cool clinical light, editorial desaturated treatment, no text, no labels, no annotations
```

### B03 — CARD · own · hold
THE QUESTION beat. Question on screen in SERIF, INK. "Why does the death signal arrive but not execute?" underlined in TEAL.

### B04 — GRAPHIC · own · drawon
Intrinsic pathway circuit, intact: DAMAGE → p53 → BH3-ONLY PROTEINS → BCL-2 BALANCE → MOMP → CASPASES → DEATH. Drawn left-to-right. All elements TEAL. Arrow drawon animation.

### B05 — GRAPHIC · own · drawon
Same circuit. A crimson STOP block slides in at the BCL-2 balance node. Signal arrives (teal arrow flows left) then stops. Reinforces "signal arrives, does not execute."

### B06 — CARD · own · hold
Section card. "FIVE SABOTAGE POINTS" in DISPLAY caps. CRIMSON eyebrow accent.

### B07 — GRAPHIC · own · accumulate
First sabotage block snaps into circuit at MOMP/effector junction. Label: "BCL-2 HIGH." Circuit visible; crimson blocker appears with a short grow animation.

### B08 — GRAPHIC · own · accumulate
Second sabotage block at effector position. Label: "BAX LOST." Circuit now has two crimson blocks.

### B09 — GRAPHIC · own · accumulate
Third sabotage block at caspase node. Label: "XIAP." Three crimson blocks.

### B10 — GRAPHIC · own · accumulate
Fourth sabotage block at BH3-only sensor. Label: "AKT-BAD." Four crimson blocks.

### B11 — GRAPHIC · own · accumulate
Fifth sabotage block at p53/sensor position. Label: "p53 MUT." All five crimson blocks in place. The complete sabotage map.

### B12 — GRAPHIC · own · hold
Full five-block circuit, static. Gold highlight arrow attempts to cross from left; stops at first block. "SIGNAL PRESENT · CANNOT EXECUTE" chip below.

### B13 — GRAPHIC · own · accumulate
Clonal selection staircase, step 1. Multiple teal dots (cells). Exposure 1 arrow (crimson). Most dots disappear. One BCL-2-high dot remains enlarged. Label "BCL-2 HIGH — SELECTED." Illustrative.

### B14 — GRAPHIC · own · accumulate
Staircase continues. Step 2: from BCL-2-high survivor, another selection; "BAX LOST" added. Step 3: "XIAP UP" added. Three-step staircase showing the built resistance. Illustrative.

### B15 — CARD · own · hold
RECAP endcard. Question → Answer. "CANCER BIOLOGY" as topic kicker (not full book title, not chapter number).

---

## Open media slots requiring human fill

| Beat | Slot | Action needed |
|------|------|---------------|
| B02 | STILL · ai | Search Wikimedia (CLL bone marrow histology) or generate with prompt above |

All other beats are own-Manim (no human fill required for slate cut).
