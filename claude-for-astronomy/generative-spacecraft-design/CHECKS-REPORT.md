# CHECKS-REPORT — *Nothing Left To Remove.*

Ep. 11 · written **before the first slate compiled**, as the PROOF GATE in
`skills/make/ai-explainer/SKILL.md` requires. Classification rules are
nopunt's.

```
14 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

nopunt's rule: **HOLD** is legitimate only for a genuine archival
*photograph*. This reel has none, so it has no HOLDs — and no PUNTs.

| Beat | Class | Artifact named in `shot.show` | Tool |
|---|---|---|---|
| B00 | SHOW | the composer types the ask; three result lines land | Remotion |
| B01 | SHOW | name card; two rows, one struck, one boxed | Manim |
| B02 | SHOW | three kinetic lines, the third accented and underlined | Manim |
| B03 | SHOW | isotype bracket + the 1.4 → 0.94 kg mass bar | Manim |
| B04 | SHOW | `domain.png` + two rings + the load arrow + the budget chip | Manim + computed plate |
| B05 | SHOW | `evolve.png` — four SIMP iterates, landing in order | Manim + computed plate |
| B06 | SHOW | `shapes.png` — two shapes, two mass chips, a bar pair | Manim + computed plate |
| B07 | SHOW | `paths.png` — strain energy, every member lit | Manim + computed plate |
| B08 | SHOW | `damage.png` — the same void on each design + two counters | Manim + computed plate |
| B09 | SHOW | the quotation card, the requirement card, the ST5 card | Manim |
| B10 | SHOW | `price.png` + the 1.6× counter + the 60% → 40% roll-back | Manim + computed plate |
| B11 | SHOW | five artefact lines, one per spoken clause plus the price | Remotion |
| B12 | SHOW | the handoff prompt types itself; three grading lines | Remotion |
| B13 | SHOW | title restate, rule, handle, subline | Remotion |

**No beat is a bare CARD.**

## Teaching-arc checklist

| Item | Where | Note |
|---|---|---|
| **FRAMEWORK before examples** | B02, then B03–B05 | B02 states the whole mechanism in one breath — three things in, a shape out, and it gets there by deleting — before any specific. B03 then gives the flown part, B04 the brief, B05 the search. No result appears until B06. |
| **WORKED EXAMPLE** | B04–B08 | One bracket followed all the way through: the problem it was given, the shape it returned, why that shape is better, where the load travels, and what one void does to it. |
| **FALSIFIABILITY** | B06, B08, B10 — and the generator | `gen_struct.py` asserts three claims and writes nothing if any fails. **It refused once**, on a threshold I had chosen before measuring, and the claim was rewritten rather than the tolerance loosened. The FE core is separately validated against three rigid-body modes, a patch test and the Euler–Bernoulli limit. |
| **SCAFFOLDED TASK** | B12 | The prompt is read aloud verbatim, then discussed: run it on something you have already shipped. Three grading criteria on screen, the third of which ("would the fix have changed your last decision") is the one that makes it bite. |
| **BOOKENDS** | B00 · B11 · B12 · B13 | All four, in order, in the fixed Claude skin. |
| **NO-SOURCE-NO-VERDICT** | every claim beat | B03 and B09 cite published sources; B04–B08 and B10 cite *this reel's own computation* and say so explicitly on the citation line. |

## Legibility contract

- **Artifact named in `shot.show`** — all 14.
- **~15–35% negative space** — GATE B reports no over- or under-fill in
  either aspect.
- **Nothing un-highlighted below ~40% opacity** — the reel uses colour and
  weight for emphasis, never opacity fades.
- **Comparisons side-by-side, held ≥2 s** — B06 (two shapes), B08 (two
  damaged designs, two counters), B10 (two curves). All held well over 2 s at
  the solved pacing.

## PPT TEST

No beat could be exported as a static slide. Type struck on the spoken
contrast (B01, B07); a card typing itself line by line (B02, B09); a bar
running to a published value and stopping, with the delta filling behind it
(B03); a structure assembling itself out of uniform grey (B05); a bar leaving
its own axis and forcing the axis to relabel (B08); a curve collapsing while a
counter rolls backwards (B10). **No two consecutive beats share a visual
scheme.**

## ILLUSTRATE LAW

The Claude UI appears at **B00, B11, B12, B13 only**. All ten inner beats
illustrate their own concept as reel-local Manim. No composer wallpaper.

## Gates at the time of writing

| Gate | Result |
|---|---|
| F — paperwork set | FACTCHECK · SHOTLIST · PROMPTS · SOURCES · PEDAGOGY all present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0` |
| W — WCAG · margins · overlap | 10/10 `rc=0` |
| B — pixel-true layout, both aspects | 20/20 `rc=0` (after 5 fixes) |
| Visual pre-flight — 20 frames read, both aspects | 12 defects found and fixed, none of which any gate caught |
| P — human signature | **PASSED** — `PEDAGOGY.md`, signed Om Mali, 02/10/2026 |

### The five GATE B fixes, for the record

1. **B02 portrait, the real bug.** The three headline rows were fitted to a
   4.60-unit maximum width in portrait, where the safe area is 3.60 wide and
   the card behind them is 3.46. They ran off the frame *and* across the
   card's own stroke. The portrait figure in a `P()` pair is not free: it has
   to be no wider than the container it sits in.
2. **B06 landscape.** The panel labels sat at y 2.45…2.74, straddling the
   hairline at +2.66. Moved beneath the panels.
3. **B08 landscape.** The "0.89% of the area" chip and the "the plate" label
   overlapped by their strokes. The chip moved up under the plate.
4. **B08 portrait.** The same chip sat directly on top of both value labels.
   In portrait it now goes *above* the plate, in the gap between the hairline
   and the figure band, and the plate drops 0.06 to make that gap real.
5. **B03 portrait — a regression from my own fix.** Having moved "a third
   lighter" out of a run-on line, I put it at y −1.12, which is where
   "0.94 kg" already was. Caught by re-running the gate after the fix, which
   is the only reason to re-run it.

### The twelve defects only reading frames caught

Every one of these passed GATE A, GATE W and GATE B. A gate checks whether
shapes intersect; it does not check whether the frame is right.

| Beat · aspect | What was wrong |
|---|---|
| B02 landscape | the card was 5.00 units tall and ran through the hairline and the title's descenders |
| B04 both | the rings did not sit on what they ringed — I guessed ±0.46 of the plate width where the real geometry is ∓0.383 / +0.385 |
| B04 landscape | the budget chip's lower edge sat 0.08 units off the note beneath it |
| B06 landscape | **the bars read backwards.** Drawn from compliance, a shorter bar means stiffer — so the optimised part had the shorter bar, which looks like losing. They now show stiffness. |
| B06 landscape | the "the pitch is true" sub-line sat 0.02 units off the citation; dropped, since it is spoken |
| B06 portrait | "the optimiser's answer" was printed **across the bracket**. GATE B passed it because a plate is an `ImageMobject`, not a curve. |
| B07 landscape | the struck "spare mass" crowded both its neighbours; moved to the side column, and the closer rewritten so the sentence is not split across the frame |
| B07 portrait | the same phrase sat 0.14 units off the closing line |
| B08 landscape | the 90th-percentile line sat 0.06 units off the citation |
| B10 landscape | at x = +0.15 the worst-void curve passes y = −0.84, so the "undamaged" legend sat **on the line it was not naming** |
| B03 portrait | "1.4 kg" and "a third lighter" read as one run-on line, the second ending at x = 1.79 against a safe edge of 1.80 |
| B03 portrait | the ledger chip then sat 0.04 units — eleven pixels at 4K — off "1.4 kg" |

The recurring one is worth naming: **four of the twelve are a gap of 0.02 to
0.08 units between two elements that GATE B scores as non-intersecting.** At
4K, 0.04 units is eleven pixels, and eleven pixels reads as contact. Ep. 10's
B04 shipped exactly this and it was caught the same way.

## Gates after the build

| Gate | Result |
|---|---|
| P — human signature | PASSED before any audio was generated |
| Audio | 149.0 s measured (2:29.0), 31 s inside the cap, model error +3.3% |
| Pacing — 24 fps, both aspects | 20/20 inside `-0.25 s … +0.05 s`, all at -0.19 to -0.22 |
| V — frame QC, 16:9 master | 28 frames · BLOCKER 0 · MAJOR 0 → `_qc/REPORT-16x9.md` |
| V — frame QC, 9:16 master | 28 frames · BLOCKER 0 · MAJOR 0 → `_qc/REPORT-9x16.md` |
| Frame reading, both aspects | 12 defects found and fixed; 1 more caught by GATE V after compile |

Both GATE V runs used an explicit `--mp4`. Given only a reel folder the check
takes `glob("*.mp4")[0]`, and with two cuts in the folder that is not
reliably the file you mean — Ep. 10 lost a re-render chasing a regression that
was really the gate grading the vertical cut while reporting as the landscape
one.

## Not run, and why

**GATE T (type-lock) could not be run: `scripts/type_check.py` does not exist
in this toolkit.** SKILL.md describes it as "ALWAYS RUN" and a hard block on
`./art run` and `./art final`, but the script is not shipped and `run.sh`
wires no such gate; the same is true of GATE SHARPNESS.

§8.1 min-size and §8.3 contrast are covered by GATE W; §8.2 overflow and §8.5
wordy-card by GATE B. **§8.4 kerning/font-coverage and §8.6 golden strings are
covered by nothing automated.** Ep. 09 shipped a frame where the `✓`
character — absent from EB Garamond — rendered as stray digits, and only
reading frames caught it. This reel uses no glyph outside the font's coverage
for that reason: the only non-ASCII marks are the `→` in two labels and the
`·` separators, both of which EB Garamond covers and both of which were
checked in the preview frames.

**`run.sh` would also skip F, A and W on this reel** — all three are guarded
on `[ -n "$PENDING" ]`, and `PENDING` is empty because `run.sh` discovers
scenes with `class (\w+)\(Scene\)` while every scene here subclasses `Paced`.
They were run explicitly, which is what the table above records.
