# SHOTLIST — vox-fluency-trap-ai
## Why AI Output That Sounds Right Can Be Completely Wrong

---

### HISTOGRAM
| Type | Beats | % |
|---|---|---|
| STILL · ai | B01, B11 | 12.5% |
| GRAPHIC · own | B02, B03, B05, B06, B07, B09, B12, B13, B14 | 56% |
| CARD · own | B04, B08, B10, B15, B16 | 31% |

No consecutive same-type violations. STILL beats at B01 (hook) and B11 (act boundary). Rhythm: STILL, GRAPHIC, GRAPHIC, CARD, GRAPHIC, GRAPHIC, GRAPHIC, CARD, GRAPHIC, CARD, STILL, GRAPHIC, GRAPHIC, GRAPHIC, CARD, CARD.

### ACT MAP
- **COLD OPEN** B01–B02: analyst receives polished summary; clicks citation → nothing
- **THE QUESTION** B03–B04: two identical citations; which is real? Named on screen.
- **THE PROBLEM** B05: naive expectation — confident text signals real source
- **THE MECHANISM** B06–B10: model optimizes plausibility not groundedness → same process → same surface; structural, not a bug
- **THE IMPLICATION** B11: fluency suppresses verification impulse
- **THE EXAMPLE** B09 (inline), B14: Mia's six citations — four clean, two failures
- **THE PRACTICE** B12–B13, B15: verification gate; four-item check; the one rule
- **RECAP** B16: endcard — question to answer

### COLOR LAW
TEAL (#1F6F5C) = real / verified / grounded  
CRIMSON (#BF3339) = hallucinated / fabricated / empty  
GOLD = highlighter fill only, once per graphic at most  
Never swap mid-film.

### EXCLUSIONS CONFIRMED
- NO transformer architecture explanation
- NO Bayesian probability formalism
- NO retrieval-augmented generation as a solution
- NO semantic entropy math
- No mention of specific model versions or benchmarks

---

## STILL SLOTS (fill after slate review)

### B01 — STILL · ai — hook plate
**Beat:** B01 | Duration: ~11s | Motion: kenburns — slow push-in toward citation list

**Archive search:**
- Wikimedia: research analyst desk document review photograph
- Unsplash: analyst reviewing printed report

**Generative prompt:**
```
B01, a professional research analyst at her desk examining a printed AI summary document, the page showing a formatted list of academic citations with author names and journal titles, focused professional expression, editorial newsprint desaturated treatment, flat print lighting, collage aesthetic, no text legible
```

---

### B11 — STILL · ai — implication plate
**Beat:** B11 | Duration: ~12s | Motion: kenburns — slow push-in on citation block

**Archive search:**
- Wikimedia: academic paper formal document typography

**Generative prompt:**
```
B11, close-up of a beautifully formatted academic document page with perfectly typeset citations, printed on aged paper, the formality of the typography radiating trustworthiness, editorial desaturated newsprint treatment, flat print lighting, no text legible, collage aesthetic
```

---

## GRAPHIC SLOTS (Manim — all own)

### B02 — GRAPHIC · own — citation click → 404
Manim scene: B02_CitationClick  
Mechanism: citation card center frame; cursor clicks; text blurs; crimson NOT FOUND chip pops in

### B03 — GRAPHIC · own — two identical citations
Manim scene: B03_TwoCitations  
Mechanism: two citation cards side by side, both same format, no label tells them apart

### B05 — GRAPHIC · own — naive expectation
Manim scene: B05_NaiveExpect  
Mechanism: confident text → real source diagram (the expectation to be overturned)

### B06 — GRAPHIC · own — plausibility engine
Manim scene: B06_PlausibilityEngine  
Mechanism: model box → two arrows: plausible text (teal, thick) vs grounded text (crimson dashed, crossed)

### B07 — GRAPHIC · own — same process, two outputs
Manim scene: B07_SameProcess  
Mechanism: one generate box → REAL (teal) and HALLUCINATED (crimson) chips, identical confidence label

### B09 — GRAPHIC · own — six citations, two failures
Manim scene: B09_SixCitations  
Mechanism: six citation chips; C2 flips crimson REVERSED; C4 flips crimson 404; others stay teal

### B12 — GRAPHIC · own — verification gate
Manim scene: B12_VerifyGate  
Mechanism: citations advance to OPEN IT gate; sorted into teal/crimson on exit

### B13 — GRAPHIC · own — four-item check
Manim scene: B13_CheckList  
Mechanism: four serif-label rows tick teal in sequence: author, title, journal+year, claim matches

### B14 — GRAPHIC · own — worked example
Manim scene: B14_Example  
Mechanism: six chips → four teal ticked, one crimson REVERSED with edit arrow, one crimson FABRICATED with X
