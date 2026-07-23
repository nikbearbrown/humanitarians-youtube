# SHOTLIST — vox-ultraviolet-catastrophe (fresh build)

Typed work order. Archive slots need a real image + `<beat>.source.txt`
sidecar (URL, license, credit). After dropping a still, set `shot.focus`
[fx, fy] in beat_sheet.json toward the subject (0–1 image coords) so the Ken
Burns move is motivated. GRAPHIC beats render from this reel's
`vox_scenes.py` after audio lock (durations first — audio is the clock).

Shot-type histogram: GRAPHIC 10 · STILL 5 · CARD 2 · COMPOSITE 1 · DOCUMENT 1
(19 beats). GRAPHIC = 53% — over the 40% pantry cap, ACCEPTED deliberately:
the chart arc is the evidence section and the film is short-form. Consecutive
GRAPHIC run B11→B13 (6 beats) is the equation-tangent group + chart return;
the tangent is one visual unit by doctrine.

---

## Archive slots (YOURS)

### B01 — STILL · foundry glow (cold open)
Want: foundry interior, worker + glowing iron, 1900s–1930s. High-res (zoom crops in).
- https://www.loc.gov/photos/?q=foundry+molten+iron&fa=rights:public+domain
- https://commons.wikimedia.org/w/index.php?search=foundry+glowing+iron+worker&title=Special:MediaSearch&type=image
- https://www.si.edu/search/collection-images?edan_q=iron%20foundry%20furnace
- Hine's steel-industry photos (LOC, PD) are the strongest candidates.

### B03 — STILL · the Berlin measurement
Want: Physikalisch-Technische Reichsanstalt lab, or Lummer / Pringsheim portrait at bench, ~1900.
- https://commons.wikimedia.org/w/index.php?search=Physikalisch-Technische+Reichsanstalt&title=Special:MediaSearch&type=image
- https://commons.wikimedia.org/w/index.php?search=Otto+Lummer&title=Special:MediaSearch&type=image
- https://commons.wikimedia.org/w/index.php?search=Ernst+Pringsheim&title=Special:MediaSearch&type=image
- Fallback: any precision-spectroscopy bench circa 1900 (Smithsonian).

### B05 — COMPOSITE · cavity plate
Want: kiln/furnace interior or peephole into a firing chamber (the "cavity").
Annotation (standing-wave arcs) lands on the assembly plane — plate only here.
- https://commons.wikimedia.org/w/index.php?search=kiln+interior+firing+chamber&title=Special:MediaSearch&type=image
- https://www.loc.gov/photos/?q=brick+kiln+interior&fa=rights:public+domain

### B08 — STILL · the hot poker
Want: domestic hearth, fire irons visible, early-1900s interior.
- https://www.loc.gov/photos/?q=fireplace+hearth+interior&fa=rights:public+domain
- https://commons.wikimedia.org/w/index.php?search=hearth+fire+poker+interior+1900&title=Special:MediaSearch&type=image

### B10 — STILL · Planck working
Want: Planck at desk/blackboard near 1900 (mid-career, dark hair — not the elderly icon).
- https://commons.wikimedia.org/w/index.php?search=Max+Planck+1900&title=Special:MediaSearch&type=image
- https://commons.wikimedia.org/wiki/Category:Max_Planck

### B14 — DOCUMENT · the 1901 paper
Want: title/first page scan of "Über das Gesetz der Energieverteilung im
Normalspectrum", Annalen der Physik 309 (4), 553 (1901). Real scan, not a
re-set. PD (published 1901).
- https://archive.org/search?query=Annalen+der+Physik+1901+Band+309
- https://de.wikisource.org/wiki/%C3%9Cber_das_Gesetz_der_Energieverteilung_im_Normalspectrum
- https://onlinelibrary.wiley.com/doi/10.1002/andp.19013090310 (reference; use a PD scan for the plate)

### B15 — STILL · Planck portrait (bio kicker)
Want: period-correct portrait ~1901 (age ~42). Name label + dates render at assembly.
- https://commons.wikimedia.org/w/index.php?search=Max+Planck+portrait+1901&title=Special:MediaSearch&type=image
- https://commons.wikimedia.org/wiki/Category:Max_Planck

## GRAPHIC slots (PIPELINE — render after audio lock)

| beat | scene | what |
|---|---|---|
| B04 | V04_MeasuredHump | axes + navy measured hump draw-on; fainter hotter hump, peak shifted right |
| B06 | V06_EqualShares | isotype squares (~30 modes), identical kT chip each, count-up from audio window |
| B07 | V07_RJRunaway | crimson RJ curve: hugs data at left, runs away off-frame on cue |
| B09 | V09_WhichAssumption | three assumptions; terracotta hand-ring on "energy flows continuously" |
| B11 | V11_Staircase | energy staircase 0, hν, 2hν, 3hν; marker snaps to steps on "nothing in between" |
| T01–T03 | T01_EqSentences / T02_EqGlossary / T03_EqExample | equation tangent E = hν (zones 2→3→4; spotlight h in T02; no values-claim zone — physics, not a contested judgment) |
| B12 | V12_PlanckCurve | runaway greys out; navy Planck curve traces the data; PLANCK 1900 chip |
| B13 | V13_TwentyOrders | 10²⁰ number beat; zeros count up on "twenty zeros" |

Single continuous chart arc across V04 → V07 → V12 (same axes, same framing —
the conversion reel proved this idiom).

## CARD slots (PIPELINE)

B02 title card, B16 end/next card — design system only, copy in beat_sheet.

## VERIFY before render (claims are counts)

- Hump shapes vs real Planck curves at two temperatures (V04)
- x = hν/kBT ≈ 47.9 at ν = 3×10¹⁵ Hz, T = 3000 K; ratio ≈ 7×10⁻²⁰ (T03, B13)
- Red-chunk figure 1.8 eV (≈660 nm) for the tangent example card (T03)
- Planck's fitted h = 6.55×10⁻³⁴ vs modern 6.626×10⁻³⁴ (B14 narration: "within one percent")
