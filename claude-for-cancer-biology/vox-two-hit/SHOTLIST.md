# SHOTLIST — vox-two-hit
## Why Knudson's Math Solved Cancer Genetics Before Molecular Biology Did

---

## Histogram (shot-type count)
| Type | Count | Beats |
|---|---|---|
| CARD | 3 | B01, B04, B16 |
| STILL · ai | 2 | B02, B11 |
| GRAPHIC · own | 11 | B03, B05–B10, B12–B15 |

Rhythm check: no more than 2 consecutive same-type beats. Sequence: CARD, STILL, GRAPHIC, CARD, GRAPHIC×6, STILL, GRAPHIC×3, CARD. No consecutive same-type violations.

## Act map
| Act | Beats | Description |
|---|---|---|
| COLD OPEN | B01–B03 | Title + clinical mystery (eye exam + onset pattern) |
| THE QUESTION | B04 | The question on screen and in narration |
| THE PROBLEM | B05–B06 | Naive assumption demolished; two-hit requirement introduced |
| THE MECHANISM | B07–B10 | Sporadic vs familial field comparison; probability asymmetry; dominant/recessive paradox resolved |
| THE IMPLICATION | B11, B14–B15 | Knudson's 1971 paper; the pattern as mathematical signature; screening implication |
| THE EXAMPLE | B12–B13 | 1986 molecular confirmation + two-children illustrative example |
| RECAP | B16 | Endcard: question to answer |

Note: B12 (molecular confirmation) and B13 (two-children example) serve as the implication + example before the recap. B14–B15 follow B11 as the implication elaboration.

## Color law
TEAL #1F6F5C = the pre-loaded germline hit / the familial advantage / the mechanism that works.
CRIMSON #BF3339 = the somatic hit / the tumor event / what must happen twice.
GOLD #F5D061 = editor's-pen highlight — fill only, once, at B12 "confirmed" payoff.
Never swapped mid-film.

## Exclusions confirmed
- No RB1 protein biochemistry: absent. No Rb/E2F gate mechanism: absent.
- No other two-hit tumor suppressor genes in detail: B15 lists BRCA1/2/APC/TP53 by name only as brief mention, no mechanism.
- No PTEN haploinsufficiency exception: absent.
- No Knudson career history: absent. (His name and publication year appear; no biography.)

---

## Per-slot work orders (STILL · ai beats only)

---

### B02 — STILL · ai — Pediatric eye examination

**Beat:** B02 (11–23 s) — cold open, establishing the clinical mystery.

**Archive search:**
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=ophthalmoscope+child+examination
- US National Cancer Institute Image Library: https://visualsonline.cancer.gov/

**Generative prompt:**
```
B02, pediatric eye examination, young child age 3-5 sitting in clinical chair, ophthalmologist using an indirect ophthalmoscope, warm clinical overhead lighting, mid-range shot, child's face partially visible, medical setting with clean background, desaturated editorial newsprint treatment, contrast 1.15, flat print reproduction style, no text overlays, no logos
```

**Prompt law:** object (ophthalmoscope), count (one child, one clinician), geometry (mid-range, child seated), material (clinical equipment), camera angle (slight angle showing both), light (overhead warm clinical), exclusions (no text, no logos, no other patients).

**Notes:** Real pediatric patient imagery requires model-release; use AI generation. Ken Burns: slow push-in toward child's face, focus [0.55, 0.45].

---

### B11 — STILL · ai — 1971 Knudson paper / age-at-onset curves

**Beat:** B11 (121–134 s) — the statistical prediction moment.

**Archive search:**
- Knudson (1971) PNAS paper: https://www.pnas.org/doi/10.1073/pnas.68.4.820 — public domain figure possible; check PNAS permissions.
- Wikimedia: https://commons.wikimedia.org/w/index.php?search=retinoblastoma+statistics+Knudson

**Generative prompt:**
```
B11, 1971 scientific journal page with two age-of-onset statistical distribution curves for retinoblastoma, two clearly labeled curves one for familial cases and one for sporadic cases, handwritten or typewritten mathematical annotation, aged yellowed newsprint texture, graph paper background, editorial collage treatment, desaturated flat print reproduction, 1970s academic aesthetic, no modern design elements, no color except aged yellowing
```

**Prompt law:** object (distribution curves, two labeled), count (two curves), geometry (full page filling frame), material (aged journal paper), camera angle (flat top-down scan), light (even flat document lighting), exclusions (no modern fonts, no color graphics, no digital look).

**Notes:** The actual Knudson (1971) PNAS figures may be usable under fair use for educational purposes. Check. Otherwise generate. Ken Burns: slow zoom into the curve intersection point.

---

## All GRAPHIC beats (own Manim — no fill-in needed)

B03 · B05 · B06 · B07 · B08 · B09 · B10 · B12 · B13 · B14 · B15

These are coded in vox_scenes.py and render automatically. No media intake required.
