# SHOTLIST — vox-infinite-square-well

Typed work order. Pantry laws apply: beat-prefixed drops only, `source-`
names for archival copies, never two same-beat files in the pantry at once,
portrait clips auto-916 (images need hand `-916` overrides).

Shot-type histogram: GRAPHIC 8 · STILL 2 · CARD 2 · COMPOSITE 1 (13 beats,
GRAPHIC 62% — HIGH, flagged deliberately: this is the derivation film, the
argument IS graphics; expect the compiler lint, accept at the gate or
convert B03/B06 to found media if it grates). No DOCUMENT beat this film; the corral photo is the
archival star. No bio kicker (relevance-gated — the corral return is the
kicker).

**PLANE BEATS: T01–T03 spotlights, B05 chips (DECREED/DERIVED), B09
annotation ring on the corral rings. All in `annotations.json`.**

---
camera archival glass-plate photograph circa 1900

## Archive slots (YOURS)

### B01 + B09 — STILL·archive · the quantum corral (1993) — ONE image, two crops
Crommie, M.F., Lutz, C.P. & Eigler, D.M., "Confinement of electrons to
quantum corrals on a metal surface," Science 262, 218 (1993). The famous
48-Fe-atoms-on-Cu(111) STM image.
- https://commons.wikimedia.org/w/index.php?search=quantum+corral&title=Special:MediaSearch&type=image
- https://www.ibm.com/history (STM gallery / Almaden images)
- Also usable: the NIST/public-agency corral re-creations if IBM's original proves encumbered

**RIGHTS NOTE (your judgment call): the IBM image is NOT public domain.**
Use here is commentary/criticism of the published scientific result, with
on-screen credit and full citation in the description — standard practice
for this exact image in every physics documentary, but it is a fair-use
position, not a license. The Wikimedia copies carry their own license tags —
prefer one with an explicit free license if available. Drop as
`B01 — corral.png` (I'll derive the B09 tight crop + both -916s from it).

### B05 — COMPOSITE·archive · Bohr 1913 / Schrödinger 1926 portraits
REAL ARCHIVES, no AI (both long dead, PD portraits exist):
- Bohr ~1913: https://commons.wikimedia.org/wiki/Category:Niels_Bohr (the young Bohr portraits are PD)
- Schrödinger ~1926: https://commons.wikimedia.org/wiki/Category:Erwin_Schr%C3%B6dinger
Drop as `B05 — bohr.png` and I'll composite the side-by-side plate on cream
(two portraits, gap for the DECREED/DERIVED chips which land at assembly) —
or drop both prefixed `B05a/B05b` unprefixed-style and I'll assemble.
Sidecars: Commons file URLs + license tags.

## GRAPHIC slots (PIPELINE — render after audio lock)

| beat | scene | what |
|---|---|---|
| B03 | B03_GuitarString | modes 1–3 draw between pins; fractional mode (crimson) misses the pin, fades; string relabels to \|ψ\|² chip |
| B04 | B04_TheOneLine | continuous k-dial collapses to ticks when ψ(0)=0, ψ(L)=0 land; 'sin(kL)=0 → kL=nπ' card stamps |
| T01–T03 | T01_EqSentences / T02_EqGlossary / T03_EqExample | tangent Eₙ = n²π²ℏ²/2mL² (spotlights n → n → mL²; example: 0.38 eV vs 3×10⁻⁴² eV) |
| B06 | B06_TheLadder | modes n=1..4 with node dots (0,1,2,3); ladder rungs at 1,4,9,16 widening |
| B07 | B07_NeverZero | crimson X on E=0; E₁ rung above with gap; struck side-card 'still + confined' |
| B08 | B08_FemtoSlosh | 1+2 slosh, ≥2 periods; 'T ≈ 3.7 fs' chip on first return (film-five rhyme) |

## CARD slots (PIPELINE)

B02 title, B10 next-tease (FINITE WELLS & BARRIERS) — copy in beat_sheet.

## VERIFY before render (recomputed at plan time; formalize in FACTCHECK.md)

- E₁(electron, 1 nm) = 0.376 eV ✓; E₂ = 1.50; E₃ = 3.38 (ratios 1:4:9 ✓)
- **Marble (1 g, 1 cm): 4.9×10⁻⁶¹ J = 3.4×10⁻⁴² eV — CHAPTER ERRATUM
  (chapter says 5×10⁻⁶² J ≈ 3×10⁻⁴³; 10× slip). Narration uses 10⁻⁴².**
- T = h/3E₁ = 3.67 fs ✓ (chapter 3.66, rounding)
- sin(kL)=0 ⇒ kₙ=nπ/L; nodes = n−1; Bohr 1913 postulate vs Schrödinger 1926
  derivation — chapter's hinge
- Corral: 48 Fe on Cu, 1993, Science 262, 218 ✓
- Ch 6 file exists: 06-finite-wells-steps-and-barriers.md ✓
