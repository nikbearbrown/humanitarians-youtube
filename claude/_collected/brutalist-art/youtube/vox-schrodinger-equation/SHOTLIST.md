# SHOTLIST — vox-schrodinger-equation

Typed work order. `pantry` command applies: beat-prefixed assets only;
archival copies use `source-` names (film-four lesson — prefixed archives get
re-cropped on every intake). Never two same-beat files in the pantry at once.

Shot-type histogram: GRAPHIC 7 · STILL 3 · CARD 2 · DOCUMENT 1 (13 beats,
GRAPHIC 54% — accepted; tangent + clock/menu/slosh are the evidence section,
matter-waves precedent).

**PLANE BEATS: B09 (Fourier document annotation), T01–T03 (word-keyed
spotlights), B10 (kicker typography). Draft regions in `annotations.json` —
B09 needs_review until the scan is in hand.**

ALL PROMPTS FOLLOW THE PROMPT LAW (aspects/stock-styles.md): object, size,
geometry, distribution, material, light, ground, exclusions.

---

## Archive / people slots (YOURS)

### B01 — STILL · Erwin Schrödinger, 1926 (cold open)
- https://commons.wikimedia.org/w/index.php?search=Erwin+Schr%C3%B6dinger&title=Special:MediaSearch&type=image

People prompt:
```
Hyper-realistic portrait of a 38-year-old Erwin Schrödinger, 1926, Austrian physicist at a cluttered desk in Zurich, round wire spectacles, bow tie, four manuscript stacks and an open notebook before him, warm lamplight from the left, shelves of bound journals behind him falling to soft shadow, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features, no text, no labels --ar 16:9
```

### B06 — STILL·ai · open laser cavity (PROMPT LAW showcase)
```
hyperrealist macro photograph in the style of National Geographic laboratory photography — a single open helium-neon laser cavity on an optical bench: two circular mirrors in black anodized mounts facing each other 40 centimeters apart, one thin continuous red beam standing perfectly straight and centered between them, a faint red glow in the slim glass tube at the midpoint; photographed from 30 degrees off-axis at bench height, cavity filling 70 percent of the frame; matte black optical bench with a regular grid of threaded holes, dim laboratory background falling to darkness; no hands, no people, no text, no labels, no lens flare --ar 16:9
```
Wrong = a sealed laser pointer, a sci-fi beam array, fog effects, or a beam
that bends. The standing beam BETWEEN two facing mirrors is the content.

### B09 — DOCUMENT · Fourier, Théorie analytique de la chaleur (1822) title page
The claim is the DATE: quantum's completeness mathematics predates quantum
by a century. Title page with "1822" visible.
- https://archive.org/search?query=Th%C3%A9orie+analytique+de+la+chaleur+Fourier+1822
- https://gallica.bnf.fr/ark:/12148/bpt6k1045508v (Gallica copy)
- https://www.google.com/books/edition/Th%C3%A9orie_analytique_de_la_chaleur/TDQJAAAAIAAJ

Published 1822 → public domain everywhere. `.source.txt` sidecar with the
scan URL. Drop the page in pantry as `B09 — fourier-1822-title.png` (nothing
else B09-prefixed in the pantry with it); I set the annotation regions from
the actual scan and crop deliberately (title + date must survive — flag if
the default crop would lose either).

### B10 — STILL · Schrödinger kicker (direct gaze)
People prompt:
```
Hyper-realistic portrait of a 38-year-old Erwin Schrödinger, 1926, Austrian physicist, direct gaze, faint knowing half-smile, round wire spectacles, dark jacket, plain warm-gray studio backdrop, single soft key light from the left, in the style of Edward Burtynsky, hyper-realist photograph, clean sharp focus, clear facial features, no text, no labels --ar 16:9
```
Kicker typography (Erwin Schrödinger · 1887–1961 · "His doubt became the
cat.") renders on the Remotion plane; degrades to serif label.

## GRAPHIC slots (PIPELINE — render after audio lock)

| beat | scene | what |
|---|---|---|
| T01–T03 | T01_EqSentences / T02_EqGlossary / T03_EqExample | tangent iℏ∂Ψ/∂t = ĤΨ (spotlights iℏ → iℏ-row → Ĥ; example: 1 eV → 2.4×10¹⁴ turns/s) |
| B04 | B04_TheFork | TDSE forks via Ψ=ψ·φ: time clock e^(−iEt/ℏ) (terra) vs eigenvalue problem Ĥψ=Eψ (navy); E chips the hinge |
| B05 | B05_ClockAndShadow | THE visual: spinning phasor + Re/Im oscillating vs FROZEN \|Ψ\|² hump |
| B07 | B07_TheMenu | two walls; modes n=1,2,3 draw on with E-ladder; wrong-fit wave (crimson) fades — doesn't fit, doesn't exist |
| B08 | B08_TheSlosh | 1+2 superposition \|Ψ\|² sloshing at the beat frequency; flat ⟨E⟩ line beneath — 'energy: constant' |

## CARD slots (PIPELINE)

B02 title, B11 next-tease (THE INFINITE SQUARE WELL) — copy in beat_sheet.

## VERIFY before render (all to be recomputed in FACTCHECK.md)

- Four papers, six months, 1926 ("Quantisierung als Eigenwertproblem" I–IV,
  Annalen der Physik) — chapter + record
- φ(t) = e^(−iEt/ℏ); TISE eigenvalue problem; E real (self-adjoint Ĥ) — chapter
- 1 eV → E/h = 2.418×10¹⁴ Hz = "two hundred forty trillion TURNS a second"
  (turns = Hz; deliberately not rad/s)
- Clock/shadow metaphor and laser-cavity analogy are the chapter's own
- Slosh: cross term at ω = (E₂−E₁)/ℏ; ⟨H⟩ = Σ|cₙ|²Eₙ constant — chapter
- Fourier, Théorie analytique de la chaleur, 1822; completeness for the
  heat equation — chapter ("a century older than quantum mechanics")
- Ages COMPUTED: Schrödinger b. 12 Aug 1887 → 38 in Jan–Jun 1926; d. 1961
- Cat 1935; "decades uneasy" — editorial, label with sources in FACTCHECK
