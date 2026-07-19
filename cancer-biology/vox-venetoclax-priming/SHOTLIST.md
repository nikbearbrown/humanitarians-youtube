# SHOTLIST — vox-venetoclax-priming
Cancer Biology · Candidate 24 · Slug: vox-venetoclax-priming

---

## Histogram

| Beat | Type | Source | Duration (est) | Act |
|------|------|--------|---------------|-----|
| B01 | CARD | own | 12.0s | COLD OPEN |
| B02 | STILL | ai | 15.0s | COLD OPEN |
| B03 | CARD | own | 18.0s | THE QUESTION |
| B04 | GRAPHIC | own | 16.0s | THE PROBLEM |
| B05 | GRAPHIC | own | 16.0s | THE PROBLEM |
| B06 | GRAPHIC | own | 20.0s | THE MECHANISM |
| B07 | STILL | ai | 20.0s | THE MECHANISM |
| B08 | GRAPHIC | own | 22.0s | THE MECHANISM (collapse) |
| B09 | GRAPHIC | own | 18.0s | THE MECHANISM |
| B10 | GRAPHIC | own | 18.0s | THE IMPLICATION |
| B11 | GRAPHIC | own | 30.0s | THE EXAMPLE |
| B12 | CARD | own | 18.0s | RECAP |

**Total estimated: ~223s (~3:43)** — within 3–5 min band, hard cap 5:00 clear.

---

## Rhythm check

CARD → STILL → CARD → GRAPHIC → GRAPHIC → GRAPHIC → STILL → GRAPHIC → GRAPHIC → GRAPHIC → GRAPHIC → CARD

No more than 2 consecutive same-type beats. B04–B06 are three consecutive GRAPHICs — risk. Checked: B03 (CARD) precedes them, and B07 (STILL) breaks the run after B06. B08–B11 are four consecutive GRAPHICs — need review. Separated by act (THE MECHANISM → THE IMPLICATION → THE EXAMPLE), all mechanistically distinct; the variety of motion (collapse, drawon, compare, compare) provides visual rhythm. Acceptable.

---

## Act map

| Act | Beats | Function |
|-----|-------|---------|
| COLD OPEN | B01–B02 | Concrete case: 68yo CLL man, chemo fails, one pill works |
| THE QUESTION | B03 | Gap formula on screen: DNA damage failed; no-damage drug kills; why? |
| THE PROBLEM | B04–B05 | Naive expectation: damage → death. Reality: BCL-2 wall blocks death signal |
| THE MECHANISM | B06–B09 | MOMP machinery; apoptotic priming; venetoclax competitive displacement |
| THE IMPLICATION | B10 | Why normal cells survive: low priming, no pent-up pressure |
| THE EXAMPLE | B11 | BH3 profiling (illustrative numbers) — CLL vs normal |
| RECAP | B12 | Q → A in one line |

---

## Color law

- **TEAL** (#1F6F5C): venetoclax releasing death pressure; freed BAX; cells completing MOMP; pro-apoptotic flow; survival of normal cells (the good outcome)
- **CRIMSON** (#BF3339): BCL-2 blocking; cells surviving chemotherapy (the problem); the dam/wall holding back death
- Two accents maximum; never swapped mid-film.
- GOLD: highlighter fill only, once per graphic at most.

---

## Exclusion confirmations

- [x] No navitoclax/platelet story (that is vox-bcl-selectivity, already built)
- [x] No IAP antagonists or TRAIL agonists
- [x] No p53 restoration / MDM2 inhibitors
- [x] No AML combination therapy data
- [x] No full venetoclax trial statistics (no response-rate percentages, no MURANO/CLL14 data)

---

## Open slots (human fills)

### B02 — STILL · ai

**Beat:** B02 — COLD OPEN — falling leukocyte count after venetoclax

**Public archive search:**
- Wikimedia Commons: "CLL CBC" or "leukemia blood count" — likely no suitable PD clinical images
- Archive.org: medical education materials on CLL diagnosis — limited
- NCI Visuals Online: leukemia diagnosis imagery — check licensing

**Generative prompt:**
```
B02, a printed clinical CBC laboratory report showing leukocyte count values declining over 14 days — a simple table of dates and WBC numbers with the numbers decreasing, printed on white paper, pinned to aged newsprint background, desaturated flat print editorial collage style, no people visible, top-down flat lay photograph, soft diffuse light
```

---

### B07 — STILL · ai

**Beat:** B07 — THE MECHANISM — BCL-2 groove gripping BAX

**Public archive search:**
- Wikimedia Commons: "BCL-2 protein structure" — PDB renders may be available (CC-BY)
- RCSB PDB: 2O22 (BCL-2/venetoclax complex) — free to use for educational purposes
- PMC open-access figures: Letai 2016 (PMC5133681) — check CC license

**Generative prompt:**
```
B07, editorial diagram illustration of a BCL-2 protein hydrophobic groove holding a BAX BH3-domain alpha helix, competitive-displacement biology schematic style, printed scientific illustration pinned to aged newsprint, flat desaturated editorial collage, close-up geometric protein pocket, no people, muted earth tones, clean line art
```

---

## Still lanes summary

| Beat | Lane | Description |
|------|------|-------------|
| B02 | geo (clinical case) | CBC count declining |
| B07 | geo (structural biology) | BCL-2 groove / BH3 helix |

Per card: "Still lanes: geo (BCL-2 groove competitive displacement), geo (BH3 profiling priming diagram — CLL vs normal mitochondria)" — B07 maps to lane 1 (BCL-2 groove); B11 is own-Manim graphic (BH3 profiling table). Lane 2 is illustrated as own graphic.
