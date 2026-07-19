# SHOTLIST — vox-tumor-pressure
## "Why the Drug Reached the Tumor and the Tumor Still Grew Back"
### CANCER NANOMEDICINE · Source: cancer-nanomedicine/chapters/02-tumor-transport-barriers.md

---

## Histogram & Rhythm Check

| Beat | Act | Type | Source | Duration (est.) | Motion |
|------|-----|------|--------|-----------------|--------|
| B01 | COLD OPEN | CARD | own | 9.0s | hold |
| B02 | COLD OPEN | STILL | ai | 10.0s | kenburns |
| B03 | THE QUESTION | CARD | own | 9.0s | hold |
| B04 | THE PROBLEM | GRAPHIC | own | 11.0s | reveal |
| B05 | THE PROBLEM | GRAPHIC | own | 10.0s | drawon |
| B06 | THE MECHANISM | GRAPHIC | own | 12.0s | trace |
| B07 | THE MECHANISM | GRAPHIC | own | 11.0s | trace |
| B08 | THE IMPLICATION | GRAPHIC | own | 11.0s | reveal |
| B09 | THE IMPLICATION | DOCUMENT | own | 10.0s | highlight |
| B10 | THE EXAMPLE | GRAPHIC | own | 14.0s | drawon |
| B11 | RECAP | CARD | own | 11.0s | hold |

**Total estimated duration:** ~118s (~1:58) — within 5:00 cap. ✓

**Rhythm check:** No more than 2 consecutive beats of the same shot type.
- B01–B02: CARD, STILL — OK (different types)
- B03: CARD — OK (different from STILL)
- B04–B05: GRAPHIC, GRAPHIC — 2 consecutive max reached
- B06–B07: GRAPHIC, GRAPHIC — 2 consecutive max reached
- B08–B09: GRAPHIC, DOCUMENT — OK (different types)
- B10: GRAPHIC — OK
- B11: CARD — OK
✓ No run of 3+ same type.

---

## Act Map

| Act | Beats | Description |
|-----|-------|-------------|
| COLD OPEN | B01, B02 | The regrowth paradox — drug accumulated, rim cleared, tumor regrows inside |
| THE QUESTION | B03 | Gap formula on screen and in narration |
| THE PROBLEM | B04, B05 | Leaky vessels + broken lymphatics = fluid buildup = pressure |
| THE MECHANISM | B06, B07 | Outward IFP flow pushes particles back to rim; core stays untouched |
| THE IMPLICATION | B08, B09 | Hypoxic selection makes core cells the most resistant |
| THE EXAMPLE | B10 | Illustrative mouse tumor scenario with IFP numbers |
| RECAP | B11 | Question restated and answered in one line |

---

## Color Law

- **TEAL** (`#1F6F5C`): drug / nanoparticles accumulating at the rim — the "good/reached" side
- **CRIMSON** (`#BF3339`): unreached core / outward pressure arrows / regrowth — the "bad/missed" side
- **GOLD** (`#F5D061`): pressure gradient highlight — editor's pen, fill only, once per graphic
- Never swap mid-film. ✓

---

## Exclusion Confirmations

- [x] NO diffusion limit derivation (1–2mm threshold mechanics excluded)
- [x] NO four-barrier list (barrier enumeration not used)
- [x] NO 30-vs-150nm size debate (particle size comparison excluded)
- [x] NO radiation resistance (hypoxic radiation resistance excluded)
- [x] Outward-pressure mechanism: INCLUDED (B04–B07)
- [x] Inside-out regrowth payoff: INCLUDED (B08–B09, B11)

---

## Media Slots — Fill-In Beats

### B02 — STILL · ai

**Beat:** B02 — COLD OPEN — MRI tumor core image  
**Duration:** ~10.0s  
**Motion:** kenburns (slow push-in toward the core)

**Archive search links:**
- Wikimedia Commons MRI tumor cross-section: https://commons.wikimedia.org/wiki/Category:MRI_images_of_tumors
- No public-domain mouse MRI is suitable; generate fresh.

**Provenance note:** Illustrative image only — no real patient data. Must carry AI-disclosure line in provenance sidecar.

**Generative prompt:**
```
B02, editorial MRI cross-section slice of a mouse tumor on aged newsprint ground. The tumor is a roughly oval mass. The outer rim of the tumor is dark gray — drug-killed tissue, dead. A small circular core in the center (approximately 2mm diameter) is lighter in tone — viable, untreated tissue. A thin crimson hand-drawn annotation ring circles the core. Flat-print editorial style, no gradients, no digital glow, no photographic lighting. The newsprint texture shows through. Camera slow-push-in toward the core. Okabe-Ito colorblind-safe palette. No text overlaid on the image. No scan artifacts. Clean schematic-style medical illustration aesthetic.
```

---

## Own-Manim Beats (no fill needed)

- **B01** — Title card (B01_Title scene)
- **B03** — Question card (B03_Question scene)
- **B04** — Leaky vessels reveal (B04_LeakyVessels scene)
- **B05** — Pressure builds drawon (B05_PressureBuilds scene)
- **B06** — Pressure flow trace (B06_PressureFlow scene)
- **B07** — Particles pushed back trace (B07_ParticlesPushedBack scene)
- **B08** — Hypoxic core reveal (B08_HypoxicCore scene)
- **B09** — Inside-out quote card (B09_InsideOutQuote scene)
- **B10** — Example drawon (B10_Example scene)
- **B11** — Endcard (B11_Endcard scene)
