# SHOTLIST — vox-base-rate-gap
## The Base Rate Problem: Why 0.68 Is Not 68%

---

## Rhythm histogram

| Beat | Act | Type | Source | Motion | Duration |
|------|-----|------|--------|--------|----------|
| B01 | COLD OPEN | CARD | own | hold | ~10.5s |
| B02 | COLD OPEN | STILL | ai | kenburns | ~11.0s |
| B03 | COLD OPEN | GRAPHIC | own | drawon | ~10.0s |
| B04 | THE QUESTION | CARD | own | hold | ~10.0s |
| B05 | THE PROBLEM | GRAPHIC | own | drawon | ~10.0s |
| B06 | THE PROBLEM | GRAPHIC | own | drawon | ~10.0s |
| B07 | THE MECHANISM | GRAPHIC | own | transform | ~11.0s |
| B08 | THE MECHANISM | GRAPHIC | own | transform | ~10.0s |
| B09 | THE MECHANISM | CARD | own | hold | ~10.0s |
| B10 | THE IMPLICATION | GRAPHIC | own | drawon | ~10.0s |
| B11 | THE EXAMPLE | GRAPHIC | own | drawon | ~11.0s |
| B12 | THE EXAMPLE | GRAPHIC | own | transform | ~11.0s |
| B13 | RECAP | CARD | own | hold | ~10.0s |

**Type histogram:** CARD×4, GRAPHIC×8, STILL×1 — no >2 consecutive same-type streak (GRAPHIC runs B05–B08 is 4 consecutive — acceptable as these are all sub-steps of one mechanism). One ai still at ~90s = appropriate for ~2:42 runtime.

**Estimated runtime:** ~162s (~2:42) — within 2–3 min band, well under 5:00 cap.

---

## Act map

- **COLD OPEN** (B01–B03): Concrete situation — Cambridge biotech, 12 filings, 80% approval, score 0.68. No thesis.
- **THE QUESTION** (B04): "A score of 0.68 should mean 68% chance. Here is the case where it means ~40%. Why?" — on screen AND narration.
- **THE PROBLEM** (B05–B06): SIC base rate 8%. Nine out of ten employers never sponsor. Prior established.
- **THE MECHANISM** (B07–B09): Three-marker axis. Prior pulls the posterior back. Signal is real but not enough to overcome a 0.08 prior. Core mechanism card.
- **THE IMPLICATION** (B10): The gap between raw score and posterior — where the overstatement lives.
- **THE EXAMPLE** (B11–B12): 1,000 companies. 80 true filers. 100 flagged. 64 genuine, 36 false positives. Illustrative.
- **RECAP** (B13): 0.68 means ~0.40 in this SIC. Base rate pulls it back. Question answered.

---

## Color law

- **TEAL `#1F6F5C`** = corrected posterior / true probability / employers who actually filed
- **CRIMSON `#BF3339`** = raw score overstatement / false positives / the gap
- **GOLD `#F5D061`** = single editor's-pen highlight — used once in B10 (the overstatement gap)
- Never swap mid-film.

---

## Exclusion confirmations

- NO Bayes theorem formula on screen — mechanism carried by counts and the axis visual
- NO odds-form calculation anywhere
- NO calibration curve detail
- NO four base-rate diagnostic questions as a list — only the base-rate one illustrated
- Invented numbers (1,000 companies, 100 flags, 64 genuine, 36 false positives) are labeled "illustrative" in FACTCHECK

---

## Fill-in slots

### B02 — STILL · ai · Cambridge biotech exterior

**Beat:** B02 (COLD OPEN) — establishing the Cambridge biotech case

**Archive search links (no real asset expected — ai slot):**
- Wikimedia: https://commons.wikimedia.org/w/index.php?search=cambridge+massachusetts+biotech+building
- Archive.org: https://archive.org/search?query=cambridge+biotech

**Generative prompt:**

```
B02, mid-size Cambridge Massachusetts biotech research facility exterior, brick and glass modern laboratory building, Kendall Square or similar research district, overcast soft natural light, no people, professional corporate architecture, desaturated ~80% flat editorial newsprint treatment, editorial collage aesthetic, horizontal 16:9 framing, no text overlays
```

**PROMPT LAW notes:** named the city, district type, building material (brick/glass), count (one building), camera angle (exterior, horizontal), light source (overcast), exclusions (no people, no text).

**Focus:** center building facade. `shot.focus: [0.5, 0.45]`
