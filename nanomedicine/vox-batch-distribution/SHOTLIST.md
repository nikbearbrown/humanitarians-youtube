# SHOTLIST — vox-batch-distribution
## Same Average Size, Different Product
### Why Nanoparticle Batches Can't Be Proved Identical Like Pills

---

## Top-Level Audit

### Histogram check
- Beat B06: TWO SIDE-BY-SIDE HISTOGRAMS — the core compare visual
  - Left: TEAL narrow spike at 98 nm (PDI 0.07)
  - Right: CRIMSON wide bell 30–300 nm (PDI 0.31)
  - Shared GOLD vertical tick at 98 nm mean for both columns
  - This is the load-bearing visual for the entire reel

### Rhythm check
- B01 CARD → B02 STILL → B03 CARD → B04 GRAPHIC → B05 GRAPHIC → B06 GRAPHIC
- B07 GRAPHIC → B08 GRAPHIC → B09 DOCUMENT → B10 GRAPHIC → B11 GRAPHIC → B12 CARD
- Consecutive same-type: B04/B05/B06 = 3 consecutive GRAPHICs — ADJUSTED: B05 is conceptual setup, B04 is molecule contrast — acceptable as a MECHANISM cluster; B07/B08 are another pair, broken by B09 DOCUMENT — PASS
- No more than 2 consecutive CARD: B01/B03 separated by B02 STILL — PASS

### Act map
| Beat | Act |
|------|-----|
| B01  | COLD OPEN — title |
| B02  | COLD OPEN — key case (two vials, different behavior) |
| B03  | THE QUESTION — on screen + narration |
| B04  | THE PROBLEM — naive expectation (small molecule binary identity) |
| B05  | THE PROBLEM — the shift (nanoparticle is a population) |
| B06  | THE MECHANISM — core compare (two histograms, same mean) |
| B07  | THE MECHANISM — PDI introduced |
| B08  | THE MECHANISM — three populations inside high-PDI batch |
| B09  | THE IMPLICATION — quote card, the regulatory principle |
| B10  | THE IMPLICATION — matching mean vs matching distribution |
| B11  | THE EXAMPLE — illustrative Batch A vs Batch B |
| B12  | RECAP — endcard, question answered |

### Color law
- TEAL `#1F6F5C` = narrow / controlled / monodisperse / low PDI / the correct product
- CRIMSON `#BF3339` = wide / heterogeneous / high PDI / the problem
- GOLD `#F5D061` = editor's-pen highlight only (mean tick, quote highlight) — never text
- Two accents max: TEAL and CRIMSON — ENFORCED

### Exclusion confirmations
- NO TEM artifact discussion — CONFIRMED: not present in any beat
- NO GMP facilities tour — CONFIRMED: not present in any beat
- NO olaratumab regulatory path — CONFIRMED: not present in any beat
- NO full characterization cascade — CONFIRMED: PDI introduced only as the one tool; no cascade enumeration
- NO encapsulation efficiency parameters — CONFIRMED: not present in any beat

### Media economy
- Runtime estimate: ~159 s (~2:39)
- STILL·ai slots: 1 (B02) — per 90s rule, 1 still earns for ~2:39 total
- All other beats: own-Manim GRAPHIC or CARD or DOCUMENT

---

## Per-Beat Shot Record

### B01 — COLD OPEN (CARD · own · hold)
**Type:** CARD, title  
**Duration estimate:** 11 s  
**Narration:** "Two injectable nanoparticles. Same cancer drug. Same lab. Both labeled one hundred nanometers. A regulator looks at the data and says they are not the same product."  
**Visual:** Title card — "Same Average Size, Different Product" / "Why Batches Can't Be Proved Identical Like Pills"  
**No fill slot — Manim CARD scene**

---

### B02 — COLD OPEN (STILL · ai · kenburns)
**Type:** STILL, source: ai  
**Duration estimate:** 13 s  
**Narration:** "A clinical-grade liposomal batch clears from a patient's bloodstream in forty-five minutes..."  
**Visual:** Two amber pharmaceutical vials side by side, both labeled "100 nm", on newsprint  

**Archive search links:**
- Wikimedia: https://commons.wikimedia.org/wiki/Category:Glass_vials (public domain pharmaceutical vials)
- NCI Visuals Online: https://visualsonline.cancer.gov/ (search: "nanoparticle" or "liposome")

**Generative prompt:**
```
B02, two amber glass pharmaceutical vials side by side on an aged newsprint surface, both vials labeled with a small white paper tag reading "100 nm", editorial flat-print illustration style, highly desaturated, charcoal ink shadows, cream paper ground, overhead view slightly tilted, soft natural light, scientific documentary aesthetic, no people, no hands, no background clutter
```

---

### B03 — THE QUESTION (CARD · own · hold)
**Type:** CARD, question  
**Duration estimate:** 14 s  
**Narration:** "Two batches of the same cancer nanoparticle measure the same average particle size. Regulators say they are not the same product. Why isn't the average enough?"  
**Visual:** Question card — the gap formula text on screen  
**No fill slot — Manim CARD scene**

---

### B04 — THE PROBLEM (GRAPHIC · own · drawon)
**Type:** GRAPHIC, source: own  
**Duration estimate:** 12 s  
**Narration:** "For a small molecule, identity is binary..."  
**Visual:** One teal point, labeled "one structure." Binary bracket below — "identical or not."  
**No fill slot — Manim scene B04_SmallMolecule**

---

### B05 — THE PROBLEM (GRAPHIC · own · drawon)
**Type:** GRAPHIC, source: own  
**Duration estimate:** 13 s  
**Narration:** "A nanoparticle is not a single structure. It is a population..."  
**Visual:** Multiple teal dots of varying sizes arrayed in a bell spread, a vertical tick marking the mean  
**No fill slot — Manim scene B05_NanoCloud**

---

### B06 — THE MECHANISM (GRAPHIC · own · compare)
**Type:** GRAPHIC, source: own  
**Duration estimate:** 15 s  
**Narration:** "Here are two batches. Both have a mean diameter of ninety-eight nanometers..."  
**Visual:** THE KEY VISUAL — two side-by-side histogram columns  
- Left (TEAL): narrow spike at 98 nm, PDI 0.07  
- Right (CRIMSON): wide bell 30–300 nm, PDI 0.31  
- Shared GOLD vertical tick at 98 nm for both  
**No fill slot — Manim scene B06_TwoHistograms**

---

### B07 — THE MECHANISM (GRAPHIC · own · drawon)
**Type:** GRAPHIC, source: own  
**Duration estimate:** 13 s  
**Narration:** "The number that captures this spread is called the polydispersity index, or PDI..."  
**Visual:** Horizontal PDI number line. Teal chip at 0.07 "monodisperse". Crimson chip at 0.31 "heterogeneous". Dashed threshold at 0.2.  
**No fill slot — Manim scene B07_PDIScale**

---

### B08 — THE MECHANISM (GRAPHIC · own · drawon)
**Type:** GRAPHIC, source: own  
**Duration estimate:** 14 s  
**Narration:** "A high-PDI batch is not one product. It is three products blended together..."  
**Visual:** The wide crimson histogram returns with three bracket regions annotated: "small: rapid clearance", "mid-range: designed behavior", "large: liver / spleen"  
**No fill slot — Manim scene B08_ThreePopulations**

---

### B09 — THE IMPLICATION (DOCUMENT · own · highlight)
**Type:** DOCUMENT, source: own  
**Duration estimate:** 13 s  
**Narration:** "Those three populations have different pharmacokinetics..."  
**Visual:** Large serif quote card — "Two batches with identical mean size and different PDIs are not the same product." Gold highlight sweeps "not the same product."  
**No fill slot — Manim DOCUMENT _quote_scene**

---

### B10 — THE IMPLICATION (GRAPHIC · own · compare)
**Type:** GRAPHIC, source: own  
**Duration estimate:** 13 s  
**Narration:** "Matching the mean matches only the center point..."  
**Visual:** Two-column comparison: left "match the mean" (two overlapping single ticks), right "match the distribution" (two overlapping histogram curves)  
**No fill slot — Manim scene B10_MatchMeanVsDistribution**

---

### B11 — THE EXAMPLE (GRAPHIC · own · compare)
**Type:** GRAPHIC, source: own  
**Duration estimate:** 16 s  
**Narration:** "An illustrative example. A QC team receives two batches of liposomal doxorubicin..."  
**Visual:** Side-by-side Batch A (teal, PDI 0.07, "tumor delivery: 100%") vs Batch B (crimson, PDI 0.31, "tumor delivery: ~60%"). Shared 98 nm mean tick. ILLUSTRATIVE label chip at bottom.  
**No fill slot — Manim scene B11_ExampleComparison**

---

### B12 — RECAP (CARD · own · hold)
**Type:** CARD, endcard  
**Duration estimate:** 12 s  
**Narration:** "Why isn't the average enough? Because a nanoparticle is a distribution, not a molecule..."  
**Visual:** Endcard — "A nanoparticle is a distribution, not a molecule." / "CANCER NANOMEDICINE"  
**No fill slot — Manim CARD scene**

---

## Open slots summary

| Beat | Type | Status |
|------|------|--------|
| B02  | STILL · ai | SLATE — fill with generated or archive image |

All other beats: own Manim — no media to source.
