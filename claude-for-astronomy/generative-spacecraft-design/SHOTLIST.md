# SHOTLIST — *Nothing Left To Remove.*

Ep. 11 · `generative-spacecraft-design` · 14 beats · 419 words
Channel `claude-hai`, Pragmatist register, Kokoro `af_bella`, $0.00.

**ILLUSTRATE LAW.** The Claude UI appears at **B00, B11, B12, B13 only**.
All ten inner beats illustrate their own concept as reel-local Manim
(`scenes.py`). No composer wallpaper.

**Aspect.** One `scenes.py` lays out both cuts. Manim keeps
`frame_height = 8.0` either way, so the vertical band plan is identical and
only the horizontal extent changes — x ±6.15 landscape, ±1.80 portrait.
Portrait is **not a crop**: it carries fewer elements, larger. The rule,
unchanged since Ep. 08 — *anything the narration speaks stays on screen; the
on-screen-only extras are what portrait loses.*

---

## Plates

All eight come from `assets/gen_struct.py`. Plates carry **imagery only** —
every label, counter and citation is vector type in `scenes.py`, so it is
sized per aspect and stays sharp at 4K.

| Plate | px | ratio | What it is |
|---|---|---|---|
| `domain.png` | 1560×720 | 0.462 | The brief: design volume, hatched root, solid lug, load arrow |
| `evolve.png` | 1464×744 | 0.508 | Four SIMP iterates in a 2×2 grid — 1, 3, 8, 90 |
| `shapes.png` | 1554×380 | 0.245 | Thinned plate ‖ optimised bracket, side by side |
| `shapes_v.png` | 980×1010 | 1.031 | The same pair, stacked, for portrait |
| `paths.png` | 1560×780 | 0.500 | Strain-energy density on the bracket — every member lit |
| `damage.png` | 1554×380 | 0.245 | The same void on each design, side by side |
| `damage_v.png` | 980×1010 | 1.031 | The same pair, stacked, for portrait |
| `price.png` | 1560×780 | 0.500 | Compliance vs mass budget: undamaged and worst-case damaged |

**Plate geometry.** `ph = pw × (ih/iw)`. The landscape figure band is 4.30
units, so a 0.50-ratio plate at pw 8.0 is 4.00 tall and leaves nothing for
labels — `paths` and `price` run at pw 6.6, and `domain` at 7.2. The 0.245
pair can go wide (pw 11.0 → 2.70 tall). The stacked variants are ~1.03, so
in portrait at pw 3.40 they are 3.50 tall and need the full figure band.

---

## Beats

| # | Act | Lane | Scene / composition | The shot |
|---|---|---|---|---|
| B00 | COLD OPEN | ask | `ClaudeComposerAsk` | Composer types the ask; send arms terracotta; `solving 7,200 elements, 90 iterations…`; three result lines land — it works / no spare path / 31× softer |
| B01 | FRAME | manim | `B01_Presenter` | OM MALI writes in, terracotta hairline; role line; card beside it; row one STRUCK (ten episodes / AI reads the sky), row two boxed (this one / AI makes the part); series line |
| B02 | FRAME | manim | `B02_OneBreath` | Three kinetic lines on a card: YOU GIVE IT THREE THINGS → IT GIVES BACK A SHAPE → **IT GETS THERE BY DELETING**, the third accented and underlined |
| B03 | THE PITCH | manim | `B03_RealPart` | Isotype bracket silhouette draws; published-ledger chip (ESA, Sentinel-1); mass bar runs 1.4 → 0.94 kg and stops; the delta fills terracotta; SLM tag |
| B04 | THE EXPERIMENT | manim | `B04_TheBrief` | `domain.png`; the root ringed, then the lug ringed, then the load arrow draws; budget chip 40% |
| B05 | THE EXPERIMENT | manim | `B05_WatchItDesign` | `evolve.png` four panels land in order, uniform grey → truss; iteration counter runs 1→90 |
| B06 | THE PITCH | manim | `B06_SameMass` | `shapes.png` / `shapes_v.png`; two mass chips both reading 40%; stiffness bar pair grows to value; accent counter 23% stiffer |
| B07 | THE CATCH | manim | `B07_OnePath` | `paths.png`; carrying members light terracotta in sequence; tally lands; a ghost arrow hunts for a second route and finds none; SPARE MASS struck through |
| B08 | THE CATCH | manim | `B08_OneVoid` | `damage.png` / `damage_v.png`, the void outlined in accent on both; 0.89%-of-area chip; plate bar nudges to 1.2×; bracket bar runs off scale to 31.2×; the scale relabels to contain it |
| B09 | THE RECEIPT | manim | `B09_KnownProblem` | Quotation card, published-not-measured-here; **NO ALTERNATIVE LOAD-PATHS** types in accented; second card — fail-safe is an aerospace requirement; third, smaller — NASA ST5, three evolved antennas, 2006 |
| B10 | THE TELL | manim | `B10_ThePrice` | `price.png`; the undamaged line steady and low; the worst-case line plunges as mass is added; marker at 60% mass — 1.6×, not 31×; saving counter rolls 60% → 40% |
| B11 | VERDICT | ask | `ClaudeVerdictArtifact` | Five artefact lines land in order, the fifth accented. Five, not four — a four-line card sits exactly on GATE V's bbox-fill floor (Ep. 10) |
| B12 | HANDOFF | ask | `ClaudeComposerAsk` | `Your turn.`; the prompt types itself; three grading lines |
| B13 | OUTRO | ask | `ClaudeTitleOutro` | Title restate, terracotta period, rule, handle, subline |

---

## Colour contract

Terracotta `#D97757` is the ONE accent and marks **what the optimiser did** —
the load it was given, the material it kept, the load path it built, and the
penalty when that path is cut. Ink marks **what a person would have done** —
the solid plate, the uniform material, the dumb baseline that turns out to be
the tolerant one.

The mapping never flips, so B04 teaches it once and every later plate reads
for free. The load-bearing moment is B08, where the ink plate barely moves and
the terracotta bracket leaves the scale — the accent that has meant "the
optimiser's work" all episode is now the thing that failed.

Accented text is `#A44A32` (4.7:1 on cream). `#B9B4A0` is strokes and fills
only — never text.

---

## Band plan (both aspects)

| | landscape | portrait |
|---|---|---|
| title | +3.02 | +3.14 |
| hairline | +2.66 | +2.84 |
| figure | +2.40 … −1.90 | +2.62 … −2.02 |
| closing line | −2.50 | −2.42 |
| citation | −3.20 | −2.95 |
| wordmark bug | −3.12 | −3.28 (right-anchored, LOGO LAW) |

---

## Portrait reductions

Dropped at 9:16, all of it on-screen-only, none of it spoken:

- **B04** — the SLM/vendor tag and the "that is the whole brief" sub-line.
- **B06** — the second mass chip (one chip plus "same mass" carries it).
- **B07** — the ghost arrow; the struck SPARE MASS phrase stays.
- **B08** — the 90th-percentile figure; the worst-case pair stays, because the
  voice speaks both numbers.
- **B09** — the third card (NASA ST5). The voice does not name it.
- **B10** — the 50%-mass midpoint marker; the two end points and the plunge stay.

Nothing the narration speaks is dropped in either aspect.

---

## PPT TEST

No beat could be exported as a static slide. Type struck on the spoken
contrast (B01, B07); a card typing itself line by line (B02, B09); a bar
running to a published value and stopping (B03); a structure assembling itself
out of uniform grey (B05); a bar leaving its own axis and forcing the axis to
relabel (B08); a curve collapsing as a counter rolls backwards (B10).
**No two consecutive beats share a visual scheme.**
