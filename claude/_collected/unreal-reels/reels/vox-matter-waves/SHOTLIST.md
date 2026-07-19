# SHOTLIST — vox-matter-waves


Working on Vox style explainer videos


Typed work order. `pantry` command applies: drop restored beat-prefixed assets
into `pantry/`, portrait clips auto-become `-916` overrides. Set `shot.focus`
per still after intake. GRAPHIC beats render from this reel's `vox_scenes.py`
after audio lock.

Shot-type histogram: GRAPHIC 9 · STILL 5 · CARD 2 · COMPOSITE 1 (16 beats,
GRAPHIC 56% — accepted; the buildup and scale bar are the evidence section).

---

## Archive / people slots (YOURS)

### B01 — STILL · de Broglie, 1924 (cold open)
- https://commons.wikimedia.org/w/index.php?search=Louis+de+Broglie+1924&title=Special:MediaSearch&type=image
- https://commons.wikimedia.org/wiki/Category:Louis_de_Broglie

People prompt:
```
Hyper-realistic portrait of a 32-year-old Louis de Broglie, 1924, French physicist in formal academic dress, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

### B04 — STILL · Davisson & Germer at Bell Labs
- https://commons.wikimedia.org/w/index.php?search=Davisson+Germer&title=Special:MediaSearch&type=image
- https://www.si.edu/search/collection-images?edan_q=Davisson%20Germer%20electron

People prompt:
```
Hyper-realistic portrait of 46-year-old Clinton Davisson and 31-year-old Lester Germer, 1927, American physicists beside a vacuum-tube electron apparatus at Bell Laboratories, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

### B07 — STILL · Tonomura at Hitachi
- https://commons.wikimedia.org/w/index.php?search=Akira+Tonomura&title=Special:MediaSearch&type=image

People prompt:
```

slight smile,
Hyper-realistic portrait of a 47-year-old Akira Tonomura, 1989, Japanese physicist beside a tall electron microscope column at Hitachi, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

### B10 — STILL·ai · person through a doorway (NATGEO)
```
hyperrealist photography, in the style of National Geographic, natural skin, visible pores — a person mid-stride walking through a narrow old doorway, natural window light, shallow depth of field --ar 16:9
```

### B12 — COMPOSITE·ai · buckyball plate
```
scientific render of a C60 buckminsterfullerene molecule, soccer-ball carbon lattice, studio lighting on neutral ground, photoreal macro --ar 16:9
```
Chips ('1999: 60 atoms / 2019: 2,000 atoms') land at assembly.

### B13 — STILL · de Broglie kicker (direct gaze)
People prompt:
```
Hyper-realistic portrait of a 32-year-old Louis de Broglie, 1924, French physicist, direct gaze, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features --ar 16:9
```

## GRAPHIC slots (PIPELINE — render after audio lock)

| beat | scene | what |
|---|---|---|
| B03 | B03_TheReversal | light→particles ✓ (film two); the arrow flips: particles→waves? |
| T01–T03 | T01_EqSentences / T02_EqGlossary / T03_EqExample | tangent λ = h/p (spotlight λ; example: 150 V → 0.1 nm ≈ atomic spacing) |
| B05 | B05_AccidentPeaks | jumbled dots + flat scatter → heat → ordered lattice + sharp peak |
| B06 | B06_NumbersAgree | calc card: 54 V → 0.167 nm → Bragg → ≈50° observed; 'parameter-free' chip |
| B08 | B08_TheBuildup | four detector panels: 10 / 200 / 6,000 / 70,000 dots → fringes (THE visual) |
| B09 | B09_BothPaths | one dot in → two ghost waves around the biprism → fringes → one dot lands |
| B11 | B11_ScaleBar | log scale: electron 0.167 nm · C₆₀ 2.5 pm · proton 10⁻¹⁵ · you 10⁻³⁵ (hand-ring) |

## CARD slots (PIPELINE)

B02 title, B14 next-tease (THE WAVE FUNCTION) — copy in beat_sheet.

## VERIFY before render (all recomputed in FACTCHECK.md)

- 1.226/√150 = 0.100 nm; 54 eV → p = 3.970×10⁻²⁴, λ = 0.167 nm
- Bragg d = 0.091 nm → θ = 66.5°; geometry ≈47° vs observed 50°; inner
  potential closes the gap (chapter) — B06's "exactly" = corrected prediction
- 70 kg × 1 m/s → 9.5×10⁻³⁶ m ≈ 10⁻³⁵; ~20 orders below proton radius
- Counts 10/200/6,000/70,000 (Tonomura 1989); C₆₀ 1999; ~2,000 atoms 2019
- Ages COMPUTED: de Broglie 32 (1924) · Davisson 46, Germer 31 (1927) · Tonomura 47 (1989)
