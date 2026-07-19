# SHOTLIST — vox-delivery-diagnosis
## Same Non-Response, Two Opposite Fixes: Did the Drug Fail, or Never Arrive?

---

## Shot-type histogram

| Type     | Count | Beats                          |
|----------|-------|-------------------------------|
| CARD     | 3     | B01, B03, B12                 |
| STILL·ai | 1     | B02                           |
| DOCUMENT | 1     | B06                           |
| GRAPHIC  | 7     | B04, B05, B07, B08, B09, B10, B11 |

Total beats: 12. Rhythm check: no more than 2 consecutive same-type — PASS (CARD→STILL→CARD→GRAPHIC→GRAPHIC→DOC→GRAPHIC→GRAPHIC→GRAPHIC→GRAPHIC→GRAPHIC→CARD — B09/B10 are 2 consecutive GRAPHIC, B10/B11 are 2 consecutive GRAPHIC, B11 is followed by CARD. Max run = 4 consecutive GRAPHICs B07–B10 — VIOLATION. Fix: B08 upgraded to STILL·ai or DOCUMENT boundary. See revised histogram below.)

### Revised histogram (rhythm-corrected)

B01 CARD → B02 STILL·ai → B03 CARD → B04 GRAPHIC → B05 GRAPHIC → B06 DOCUMENT → B07 GRAPHIC → B08 GRAPHIC → B09 GRAPHIC → B10 GRAPHIC → B11 GRAPHIC → B12 CARD

Runs: B04-B05 = 2 GRAPHIC (ok). B07-B11 = 5 consecutive GRAPHIC (VIOLATION). 

Resolution: Insert B08.5 as a STILL·ai beat "the scan result" between B08 and B09, splitting the GRAPHIC run. OR promote B08 to STILL·ai. 

**Applied fix:** B08 becomes STILL·ai (the body-scan result image — placeholder slate, ai prompt below). B07 is GRAPHIC. The run becomes: B07 GRAPHIC → B08 STILL·ai → B09 GRAPHIC → B10 GRAPHIC → B11 GRAPHIC. B09-B11 = 3 consecutive GRAPHIC (VIOLATION still).

**Final fix:** B10 becomes DOCUMENT (a principle stated as a quote). Final sequence:

| Beat | Type     | Act            |
|------|----------|----------------|
| B01  | CARD     | COLD OPEN      |
| B02  | STILL·ai | COLD OPEN      |
| B03  | CARD     | THE QUESTION   |
| B04  | GRAPHIC  | THE PROBLEM    |
| B05  | GRAPHIC  | THE PROBLEM    |
| B06  | DOCUMENT | THE PROBLEM    |
| B07  | GRAPHIC  | THE MECHANISM  |
| B08  | STILL·ai | THE MECHANISM  |
| B09  | GRAPHIC  | THE IMPLICATION|
| B10  | DOCUMENT | THE IMPLICATION|
| B11  | GRAPHIC  | THE EXAMPLE    |
| B12  | CARD     | RECAP          |

Max consecutive same-type: B04-B05 = 2 GRAPHIC (ok). B01 and B03 are CARD separated by STILL·ai (ok). PASS.

---

## Act map

| Act            | Beats    | Purpose                                                |
|----------------|----------|--------------------------------------------------------|
| COLD OPEN      | B01-B02  | Concrete situation: drug fails, swap proposed          |
| THE QUESTION   | B03      | Gap formula on screen + in narration                   |
| THE PROBLEM    | B04-B06  | Two causes, opposite fixes, the danger of wrong move   |
| THE MECHANISM  | B07-B08  | Biodistribution imaging as the diagnostic instrument   |
| THE IMPLICATION| B09-B10  | What each outcome means for the engineering response   |
| THE EXAMPLE    | B11      | Illustrative two-program comparison with numbers       |
| RECAP          | B12      | Endcard: question -> answer in one line                |

---

## Color law

- **TEAL (#1F6F5C)**: delivery confirmed / particle in tumor / the good outcome / the correct engineering branch
- **CRIMSON (#BF3339)**: delivery failed / particle in liver-spleen / the wrong move / the bad outcome
- GOLD (#F5D061): editor's-pen highlighter — used once, in B06 DOCUMENT beat only
- SLATE (#3E5559): entity/structure chips (imaging labels in B07)
- Never swap the TEAL/CRIMSON roles mid-film

---

## Exclusion confirmations

- NO what-each-modality-reads detail (MRI vs CT vs PET specifics excluded) — B07 labels modalities as chip text only, zero physics
- NO FDG proxy lesson — FDG never mentioned
- NO activatable probes — excluded, confirmed absent
- NO release-vs-target-engagement caveat — explicitly excluded; the binary delivery/biology is the only distinction shown
- Illustrative numbers in B11 labeled "illustrative" in FACTCHECK

---

## Per-slot sections (fill-in beats)

---

### B02 — STILL·ai

**Beat:** B02 — COLD OPEN, 14s  
**Required:** fluorescence biodistribution scan image — liver bright, tumor dim

**Archive search:**
- Wikimedia Commons: "fluorescence mouse biodistribution" — check for CC-licensed imaging figures
- NIH/NCI image gallery: nanoparticle biodistribution
- Likely no clean public-domain match; proceed to AI generation

**Generative prompt:**
```
B02, stylized fluorescence biodistribution schematic of a mouse silhouette, large bright false-color hotspot concentrated in the liver and spleen, a small tumor mass outlined on the flank with minimal signal, caption-style labels LIVER (bright) and TUMOR (dim), desaturated editorial newsprint reproduction flat print style, warm cream background, no digital glow, no gradients, biomedical diagram aesthetic, isolated on a cream newsprint-texture ground
```

**Focus:** `[0.5, 0.45]` — center on the mouse, liver region

---

### B08 — STILL·ai

**Beat:** B08 — THE MECHANISM, 18s  
**Required:** biodistribution result map showing two outcome panels

**Archive search:**
- Wikimedia: "nanoparticle biodistribution PET scan" — check CC license
- NIH image library: tumor accumulation imaging
- Likely slate; use AI generation

**Generative prompt:**
```
B08, editorial biomedical schematic showing two side-by-side body silhouette panels on aged newsprint background. Left panel: mouse or human torso outline with bright false-color accumulation in liver and spleen, labeled LIVER/SPLEEN in bold, overall crimson-toned. Right panel: identical outline with bright signal in tumor mass on flank, labeled TUMOR in bold, overall teal-green-toned. Both panels clearly separated, flat editorial print style, desaturated, no digital effects, documentary diagram aesthetic
```

**Focus:** `[0.5, 0.5]` — center both panels equally

---
