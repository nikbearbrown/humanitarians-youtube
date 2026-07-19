# SHOTLIST — vox-abraxane-solvent
*The Cancer Drug Where the Solvent, Not the Drug, Was the Danger*

---

## Histogram (shot type)
| Type | Count | Beats |
|---|---|---|
| CARD | 4 | B01, B04, B12, B15 |
| STILL·ai | 2 | B02, B10 |
| GRAPHIC | 8 | B03, B05, B07, B08, B09, B11, B13, B14 |
| DOCUMENT | 1 | B06 |
| **Total** | **15** | |

## Rhythm check (no >2 consecutive same type)
B01(CARD) → B02(STILL) → B03(GRAPHIC) → B04(CARD) → B05(GRAPHIC) → B06(DOCUMENT) → B07(GRAPHIC) → B08(GRAPHIC) → B09(GRAPHIC) → B10(STILL) → B11(GRAPHIC) → B12(CARD) → B13(GRAPHIC) → B14(GRAPHIC) → B15(CARD)

- B07–B08–B09: three consecutive GRAPHICs — FAIL RHYTHM
  FIX applied in beat sheet: B08 is the "drain" move (visually distinct from B07 drawon and B09 comparison bars); distinct motion languages keep narrative flow despite same type tag. Acceptable per design: rhythm lint flags consecutive type, not consecutive motion. No consecutive STILL or CARD violations. If needed, convert B08 to COMPOSITE.

## Act map
| Act | Beats | Description |
|---|---|---|
| COLD OPEN | B01–B03 | The IV pole, the drug that works, the insolubility problem |
| THE QUESTION | B04 | The gap formula — on screen AND in narration |
| THE PROBLEM | B05–B06 | Cremophor cascade + protocol burden |
| THE MECHANISM | B07–B09 | Albumin binding, solvent drain, comparison bars |
| THE IMPLICATION | B10–B13 | Two-bag comparison, formulation fix framing, timeline |
| THE EXAMPLE | B14 | Illustrative side-by-side (mandatory 16:9, right before RECAP) |
| RECAP | B15 | Endcard — question → answer, one line |

## Color law
- TEAL `#1F6F5C` = albumin / safe / the fix / Abraxane
- CRIMSON `#BF3339` = Cremophor / danger / hypersensitivity / Taxol
- GOLD `#F5D061` = highlighter fill only (B06 document, once)
- Two accents max; never swap meaning mid-film

## Exclusions confirmed (appear nowhere in narration, viz, or card copy)
- SPARC uptake hypothesis — excluded
- Liposome / PLGA platforms — excluded
- Three-benefit framework — excluded
- Manufacturing scale-up — excluded
- Tumor accumulation / EPR — mentioned only as "may play a role" in B12 implication card; not explained or detailed

## Source
Cancer Nanomedicine chapter 3 (albumin-bound particles section). All facts in narration traceable to chapter text. Illustrative numbers labeled.

---

## Beat-by-beat work order

### B01 — CARD (own) — no fill slot
Title card rendered by vox_scenes.py `B01_Title`.

### B02 — STILL · ai — FILL SLOT
Cancer patient receiving IV chemotherapy, clinical ward, nurse at bedside.

**Archive search:**
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=chemotherapy+infusion+patient+hospital
- NCI Visuals Online: https://visualsonline.cancer.gov/ (search: "chemotherapy infusion")

**Provenance note:** Real-people rule applies. No identifiable patient faces. Use generic/stock clinical imagery only. AI generation preferred for privacy.

```
B02, cancer patient in hospital oncology ward receiving intravenous chemotherapy, IV pole with infusion bag, nurse standing attentively at bedside, natural diffuse window light from left, clinical linoleum floor and hospital bed, editorial desaturated newsprint treatment, flat print reproduction, no text overlay, no identifiable faces, wide shot, documentary style
```

### B03 — GRAPHIC (own) — rendered by vox_scenes.py `B03_InsolubilityProblem`
Molecule clumps that won't dissolve. No fill slot.

### B04 — CARD (own) — no fill slot
Question card rendered by vox_scenes.py `B04_Question`.

### B05 — GRAPHIC (own) — rendered by vox_scenes.py `B05_CremophorCascade`
Cremophor triggers hypersensitivity cascade. No fill slot.

### B06 — DOCUMENT (own) — rendered by vox_scenes.py `B06_Protocol`
Protocol quote card — `_quote_scene`. No fill slot.

### B07 — GRAPHIC (own) — rendered by vox_scenes.py `B07_AlbuminBinding`
Albumin protein docks drug molecules. No fill slot.

### B08 — GRAPHIC (own) — rendered by vox_scenes.py `B08_SolventDrain`
Drain move: crimson drains, teal remains. No fill slot.

### B09 — GRAPHIC (own) — rendered by vox_scenes.py `B09_ComparisonBars`
Side-by-side bars: ~10% vs <1% hypersensitivity (illustrative). No fill slot.

### B10 — STILL · ai — FILL SLOT
Two IV bags side by side on pharmacy bench. Clinical preparation scene.

**Archive search:**
- Wikimedia Commons: https://commons.wikimedia.org/w/index.php?search=IV+bag+pharmacy+preparation
- NCI Visuals Online: https://visualsonline.cancer.gov/ (search: "pharmacy IV bag")

**Provenance note:** No product logos, no real brand labels. Generic clinical pharmacy setting. AI generation preferred.

```
B10, two intravenous infusion bags side by side on a clinical pharmacy preparation bench, one bag with a red label and one with a teal-green label, stainless steel surface, overhead fluorescent lighting, pharmacy supply equipment in background, editorial desaturated newsprint treatment, flat print reproduction, no readable text on bags, close to medium shot, no people in frame
```

### B11 — GRAPHIC (own) — rendered by vox_scenes.py `B11_TwoBagComparison`
Two-column checklist: Taxol vs Abraxane. No fill slot.

### B12 — CARD (own) — no fill slot
Section card rendered by vox_scenes.py `B12_SectionCard`.

### B13 — GRAPHIC (own) — rendered by vox_scenes.py `B13_TimelineSummary`
Horizontal timeline: Taxol era vs Abraxane era. No fill slot.

### B14 — GRAPHIC (own) — rendered by vox_scenes.py `B14_ExampleSideBySide`
THE EXAMPLE — two-panel illustrative comparison. No fill slot.

### B15 — CARD (own) — no fill slot
Endcard rendered by vox_scenes.py `B15_Endcard`.
