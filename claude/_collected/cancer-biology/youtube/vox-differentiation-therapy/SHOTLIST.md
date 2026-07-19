# SHOTLIST — vox-differentiation-therapy
## Why a Cancer Drug That Restores Differentiation Is Better Than One That Kills

---

## Histogram
| Beat | Type | Source | Duration (est) |
|------|------|--------|---------------|
| B01 | CARD | own | 9s |
| B02 | STILL | ai | 10s |
| B03 | GRAPHIC | own | 10s |
| B04 | CARD | own | 14s |
| B05 | GRAPHIC | own | 11s |
| B06 | GRAPHIC | own | 10s |
| B07 | GRAPHIC | own | 12s |
| B08 | GRAPHIC | own | 12s |
| B09 | GRAPHIC | own | 13s |
| B10 | STILL | geo | 11s |
| B11 | GRAPHIC | own | 16s |
| B12 | CARD | own | 11s |

Total estimated: ~139s ≈ 2:19 (target 3–5 min; audio will expand natural timing)

## Rhythm Check
- No more than 2 consecutive own-Manim beats: B05–B09 is a 5-beat run of own graphics (THE MECHANISM), which is acceptable for the core mechanism teaching block. B07–B09 is 3 own-graphic consecutives — needs one style variation within.
- Still economy: 2 stills for a ~2.5–3 min film = correct (1 per 90s rule)

## Act Map
| Act | Beats | Notes |
|-----|-------|-------|
| COLD OPEN | B01–B03 | Concrete: blast count falls, neutrophils appear, mutation confirmed |
| THE QUESTION | B04 | On screen AND narration: cells fall without dying — why? |
| THE PROBLEM | B05–B06 | Normal differentiation vs AML stall |
| THE MECHANISM | B07–B09 | 2HG → demethylase block → lock; ivosidenib → lock removed |
| THE IMPLICATION | B10 | Program was intact; lock prevented it |
| THE EXAMPLE | B11 | Illustrative time-lapse of bone marrow response |
| RECAP | B12 | Question → answer in one line |

## Color Law
- TEAL: differentiated/mature cells, drug working, epigenetic lock released, neutrophil
- CRIMSON: immature blast, 2HG presence, epigenetic lock engaged, arrest
- GOLD: single highlight (editor's pen mark on the locked door in B08), fill only
- Two accents max; never swapped

## Exclusion Confirmations
- [x] No IDH biochemistry beyond 2HG-as-competitive-inhibitor concept
- [x] No comparison of IDH1 vs IDH2 inhibitors
- [x] No distinction between AML and glioma IDH mutations
- [x] No DNMT inhibitor mechanism
- [x] No discussion of EZH2 inhibitors

---

## Fill-in Slots

### B02 — STILL · ai
**Beat:** B02 — COLD OPEN — blood smear with mature neutrophils
**Narration:** "On the blood smear: mature neutrophils with segmented nuclei — cells that should not exist in this bone marrow."

**Archive search:**
- Wikimedia: https://commons.wikimedia.org/wiki/Category:Neutrophils (micrographs)
- Archive.org: https://archive.org/search?query=blood+smear+neutrophil+leukemia

**Generative prompt:**
```
B02, clinical blood smear microscopy image showing mature neutrophils with segmented multilobed nuclei, photorealistic laboratory style, purple-pink Giemsa stain on pale background, several segmented neutrophils in center frame with visible nuclear lobes, one or two immature blast cells at periphery with large round pale nuclei for contrast, 16:9 composition, centered focus, neutral clinical tone, no text overlays, no labels
```

### B10 — STILL · geo
**Beat:** B10 — THE IMPLICATION — locked door diagram
**Narration:** "The cell was always going to differentiate. The program was intact. Only the chemical lock prevented it from running."

**Archive search:**
- Wikimedia: https://commons.wikimedia.org/wiki/Category:Epigenetics (diagrams)
- This is a conceptual diagram best generated

**Generative prompt:**
```
B10, clean minimal scientific diagram on cream white background, showing a locked door labeled "differentiation program" with a key jammed in the lock labeled "2HG", the key glows red-crimson, an arrow shows the key being removed (labeled "ivosidenib"), the door swings open with teal-green light beyond, a cell silhouette transforms from round immature blast (crimson) through the doorway to a mature segmented neutrophil (teal), flat vector illustration style, no photorealism, 16:9 horizontal composition, editorial scientific aesthetic
```
