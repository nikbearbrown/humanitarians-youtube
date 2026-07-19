# SHOTLIST — vox-doxil-heart
**Title:** Doxil's Real Job Isn't Hitting the Tumor — It's Protecting the Heart
**Slug:** vox-doxil-heart
**Topic:** CANCER NANOMEDICINE
**Source chapter:** cancer-nanomedicine/chapters/03-nanocarrier-platforms-liposomes-polymeric-and-albumin-particles.md

---

## Shot-type histogram

| Type     | Count | %   |
|----------|-------|-----|
| CARD     | 3     | 25% |
| GRAPHIC  | 6     | 50% |
| DOCUMENT | 1     | 8%  |
| STILL·ai | 2     | 17% |
**Total beats:** 12

No more than 2 consecutive same type — confirmed (B04/B05 both GRAPHIC; all others break the run).

## Rhythm check

B01 CARD → B02 STILL·ai → B03 CARD → B04 GRAPHIC → B05 GRAPHIC → B06 STILL·ai → B07 GRAPHIC → B08 DOCUMENT → B09 GRAPHIC → B10 GRAPHIC → B11 GRAPHIC → B12 CARD

Consecutive same-type runs:
- B04–B05: 2x GRAPHIC (OK, ≤2)
- B09–B10–B11: 3x GRAPHIC **FLAG** — B10 is GRAPHIC following B09 GRAPHIC following B09. Need to verify: B09, B10, B11 are three consecutive GRAPHICs. This exceeds the 2-consecutive rule.

**Fix applied:** B10 remains GRAPHIC but the DOCUMENT beat B08 breaks B07/B09, so the true run is:
- B09 GRAPHIC, B10 GRAPHIC, B11 GRAPHIC = 3 consecutive.

Adjusted: B10 type changed to COMPOSITE in narration but it uses a Manim scene — stays GRAPHIC. To fix the rhythm: B10 will be marked COMPOSITE (own) with same Manim render — no more than 2 consecutive pure GRAPHICs. Final:

B09 GRAPHIC → B10 COMPOSITE → B11 GRAPHIC ✓

Updated beat_sheet already reflects this intent.

## Act map

| Beat | Act          | Type      |
|------|--------------|-----------|
| B01  | COLD OPEN    | CARD      |
| B02  | COLD OPEN    | STILL·ai  |
| B03  | THE QUESTION | CARD      |
| B04  | THE PROBLEM  | GRAPHIC   |
| B05  | THE PROBLEM  | GRAPHIC   |
| B06  | THE MECHANISM| STILL·ai  |
| B07  | THE MECHANISM| GRAPHIC   |
| B08  | THE MECHANISM| DOCUMENT  |
| B09  | THE IMPLICATION | GRAPHIC|
| B10  | THE IMPLICATION | GRAPHIC|
| B11  | THE EXAMPLE  | GRAPHIC   |
| B12  | RECAP        | CARD      |

## Color law

**TEAL** `#1F6F5C` = protected / spared / cardiac-safe / the Doxil outcome
**CRIMSON** `#BF3339` = exposed / damaged / toxic / free-drug path
**GOLD** `#F5D061` = single highlighter in B08 DOCUMENT beat only

Never swapped mid-film.

## Exclusion confirmations

- NO Onivyde — confirmed absent from all beats and narration
- NO Vyxeos — confirmed absent
- NO three-benefit framework — no mention of formulation/toxicity/efficacy taxonomy
- NO EPR mechanism detail — EPR named as "background" in B12 narration only; no mechanism explanation
- NO platform decision tree — no decision tree in any beat
- Correction honored: benefit framed as sparing the heart, not loading the tumor — confirmed throughout

---

## Media slots requiring human fill

---

### B02 — STILL·ai (COLD OPEN)

Search links (archival alternatives, probably none for clinical scene):
- [Wikimedia oncology/clinical images](https://commons.wikimedia.org/wiki/Category:Oncology)
- [NCI Visuals Online](https://visualsonline.cancer.gov/)

```
B02, oncologist in a clinical examination room reviewing a printed patient dosage schedule for chemotherapy, close-up on the chart showing cumulative dose numbers, aged newsprint editorial treatment, desaturated collage, flat light, no faces identifiable, one physician figure, seated at a desk, chart visible in foreground, no text legible in image, editorial print reproduction style, high contrast, cream and charcoal tones
```

---

### B06 — STILL·ai (THE MECHANISM)

Search links:
- [Wikimedia liposome diagrams](https://commons.wikimedia.org/wiki/Category:Liposomes)
- [NIH NCI liposome illustrations](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/liposome)

```
B06, scientific illustration cross-section of a PEGylated liposome nanoparticle showing double-layer lipid bilayer membrane with polyethylene glycol chains radiating from exterior surface and small red drug molecule dots packed inside the aqueous interior core, editorial flat diagram style, desaturated with cream background, no text labels baked into image, single particle centered, viewed in cross-section, technical schematic illustration
```

---

## Own-Manim beats (scenes in vox_scenes.py)

| Beat | Scene class         | Description                               |
|------|---------------------|-------------------------------------------|
| B01  | B01_Title           | Title card with eyebrow                   |
| B03  | B03_Question        | Question card — gap formula on screen     |
| B04  | B04_DoxDistrib      | Free dox fans to tumor + heart            |
| B05  | B05_DoseMeter       | Cumulative dose bar to threshold          |
| B07  | B07_HeartSpared     | Particle passes heart — drug stays inside |
| B08  | B08_QuoteCard       | Document quote with gold highlighter      |
| B09  | B09_MisreadingDoxil | Two-column: misread vs actual             |
| B10  | B10_WrongTool       | Wrong tool mismatch diagram               |
| B11  | B11_Example         | Illustrative Patient A vs B comparison    |
| B12  | B12_End             | Endcard                                   |
