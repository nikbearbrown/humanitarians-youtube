# SHOTLIST — vox-mutational-signature
*Why the Tumor Genome Is a Fossil Record of What the Cell Encountered*

---

## Histogram (beat count by type)

| Type | Count |
|------|-------|
| GRAPHIC / CARD (own Manim) | 12 |
| STILL · geo | 2 |
| **Total** | **14** |

(+ B15 RECAP = 15 beats total)

## Rhythm check

B01 GRAPHIC — B02 GRAPHIC — B03 GRAPHIC — B04 GRAPHIC — B05 GRAPHIC — B06 STILL — B07 GRAPHIC — B08 GRAPHIC — B09 GRAPHIC — B10 GRAPHIC — B11 STILL — B12 GRAPHIC — B13 GRAPHIC — B14 GRAPHIC — B15 GRAPHIC

No run of 3+ consecutive same type. Two consecutive GRAPHIC runs do not exceed 5 before a STILL breaks them. PASS.

## Act map

| Beat | Act |
|------|-----|
| B01–B02 | COLD OPEN |
| B03 | THE QUESTION |
| B04–B05 | THE PROBLEM |
| B06–B10 | THE MECHANISM |
| B11–B12 | THE IMPLICATION |
| B13–B14 | THE EXAMPLE |
| B15 | RECAP |

Order: COLD OPEN → QUESTION → PROBLEM → MECHANISM → IMPLICATION → EXAMPLE → RECAP. PASS.

## Color law

TEAL=#1F6F5C — preserved pattern, intact sequence, correct signature identification  
CRIMSON=#BF3339 — DNA damage, adduct, broken/misread base, wrong mutation  
GOLD=#F5D061 — fill highlight ONLY (single editor's pen use)  
Two accents max. Stated in metadata.color_semantics.

## Exclusions confirmed

- No full chemical mechanism for all carcinogens (only B[a]P and UV covered in detail)
- No COSMIC signature database details
- No procarcinogen activation enzyme kinetics
- No aflatoxin-HBV interaction (separate card)
- No linear no-threshold model for radiation

## Estimated duration

| Beat | Est. (s) |
|------|----------|
| B01 | 9 |
| B02 | 12 |
| B03 | 10 |
| B04 | 10 |
| B05 | 10 |
| B06 | 12 |
| B07 | 11 |
| B08 | 11 |
| B09 | 13 |
| B10 | 12 |
| B11 | 16 |
| B12 | 12 |
| B13 | 10 |
| B14 | 18 |
| B15 | 13 |
| **Total** | **179 s / ~2:59** |

Under 5:00 hard cap. PASS.

---

## Per-slot sections (fill-in beats)

### B06 — STILL · geo — AdductChain
**Beat:** THE MECHANISM — shows the benzo[a]pyrene → BPDE → guanine adduct → G→T chain

**Public archive search:**
- Wikimedia Commons: search "benzo[a]pyrene DNA adduct" — IARC/WHO diagrams sometimes in the commons
- PubChem: compound 2153 (BPDE) — structure images freely available
- NCI Thesaurus image library — carcinogen mechanism diagrams

**Provenance note:** No photo exists; this is a mechanistic diagram. Use geometric/schematic only (geo source). AI generation is pre-approved for geo stills.

```
B06, four-panel horizontal schematic on cream background, no photograph, pure geometry:
Panel 1 (left): labeled rectangle "benzo[a]pyrene" in dark teal, inert, lipophilic droplet shape.
Panel 2: CYP1A1 enzyme arrow converting to labeled rectangle "BPDE" in crimson, reactive epoxide ring shown as small triangle on the molecule.
Panel 3: crimson BPDE covalently attached at N2 position of a simplified guanine base on a short double-helix ladder — the helix visibly kinked/bulged at the attachment point. Label: "bulky adduct, helix distorted."
Panel 4 (right): two base-pair rungs — top rung shows the damaged G with adduct, bottom rung shows the fixed mutation: G on template strand, T on new strand, labeled "G to T transversion (fixed)." Color the wrong base red.
Clean sans-serif labels, 2:1 landscape crop, no photorealism, no gradient fills, Okabe-Ito palette, white or cream background.
```

---

### B11 — STILL · geo — FourSignatures
**Beat:** THE IMPLICATION — four bar charts side by side, four carcinogen fingerprints

**Public archive search:**
- COSMIC Signatures website (cancer.sanger.ac.uk) — downloadable signature plots (CC BY 4.0)
- Alexandrov et al. 2013 Nature paper supplementary figures — check license
- These are the canonical reference; the card calls for a schematic four-panel comparison, not the exact COSMIC plots

**Provenance note:** Schematic bar charts showing the characteristic distribution pattern — not reproduced from COSMIC directly. Geometric/illustrative, not data-exact.

```
B11, four side-by-side vertical bar charts on cream background, each chart 96 bars wide representing the 96 trinucleotide substitution contexts (six substitution types x 16 flanking contexts), schematic not precise, labels below each chart:
Chart 1 "Tobacco (Sig 4)": dominant bars clustered at C[G>T]A, C[G>T]C contexts in red/crimson, rest near zero. Overall: spiky pattern concentrated in C>A (shown as G>T complement).
Chart 2 "UV (Sig 7)": dominant tall bars at C[C>T]A, C[C>T]G dipyrimidine contexts in amber/gold, double-mutation CC>TT shown as especially prominent. Clean spike pattern.
Chart 3 "Aflatoxin (Sig 22)": single dramatic spike at one position (G>T at AGG context, codon 249 region) in crimson, all other bars near zero. Most concentrated of all four.
Chart 4 "MMR Deficiency (Sig 6)": uniform distribution of bars across all 96 contexts in teal, no single dominant peak, flat plateau appearance.
Label each chart below with the carcinogen name and key mutation type. Four charts equal width arranged horizontally. No photorealism. Clean geometric bar chart style, cream background, dark labels.
```

---

## Notes on own-Manim beats

B01, B02, B03, B04, B05, B07, B08, B09, B10, B12, B13, B14, B15 are all GRAPHIC/own Manim — rendered by vox_scenes.py.
