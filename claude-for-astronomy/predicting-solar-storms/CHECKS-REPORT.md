# CHECKS-REPORT — *The Same Sunspot, Twice.*

Ep. 12 · written **before the first slate compiled**, as the PROOF GATE in
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
| B03 | SHOW | 49 isotype marks, 38 of which turn and fall | Manim |
| B04 | SHOW | `regions.png` + a ringed track + two chips | Manim + computed plate |
| B05 | SHOW | `split.png` + the 100% / 0% counters | Manim + computed plate |
| B06 | SHOW | `nearest.png` + the two named distributions | Manim + computed plate |
| B07 | SHOW | two bars growing to value + the +0.13 bracket | Manim |
| B08 | SHOW | `scores.png` + the ringed pair + the −75% counter | Manim + computed plate |
| B09 | SHOW | `spread.png` — twelve points per column | Manim + computed plate |
| B10 | SHOW | `control.png` + the fix typing itself | Manim + computed plate |
| B11 | SHOW | five artefact lines | Remotion |
| B12 | SHOW | the handoff prompt types itself; three grading lines | Remotion |
| B13 | SHOW | title restate, rule, handle, subline | Remotion |

**No beat is a bare CARD.**

## Teaching-arc checklist

| Item | Where | Note |
|---|---|---|
| **FRAMEWORK before examples** | B02, then B04–B06 | B02 states the whole mechanism in one breath — one region is many rows, shuffle before splitting and you test its memory — before any number. No result appears until B07. |
| **WORKED EXAMPLE** | B04–B08 | One dataset followed all the way through: its shape, the two splits, the leak measured, the headline score, and the reversal. |
| **FALSIFIABILITY** | B07–B10 — and the generator | `gen_solar.py` asserts three claims over 12 repeats and writes nothing if any fails. **B10 is a control**: it removes the suspected cause and the effect vanishes. Without that beat the episode would only be a correlation. |
| **SCAFFOLDED TASK** | B12 | The prompt is read aloud, then discussed. Three grading criteria, the first of which ("does it name the unit that repeats, not just 'rows'") is the one that separates understanding from agreement. |
| **BOOKENDS** | B00 · B11 · B12 · B13 | All four, in order, in the fixed Claude skin. |
| **NO-SOURCE-NO-VERDICT** | every claim beat | B03 cites NASA and *Space Weather*; B04–B10 cite *this reel's own computation* and say so on the citation line. The distinction between the published *diagnosis* and this reel's *measurement* is made explicitly in FACTCHECK and SOURCES. |

## Legibility contract

- **Artifact named in `shot.show`** — all 14.
- **~15–35% negative space** — GATE B reports no over- or under-fill in
  either aspect.
- **Nothing un-highlighted below ~40% opacity** — the only opacity change is
  B03's 38 fallen marks at 0.28, which is the point of the beat, not a fade
  for emphasis.
- **Comparisons side-by-side, held ≥2 s** — B05 (two splits), B06 (two
  distributions), B07 (two bars), B08 (four bars), B09 (four columns). All
  held well over 2 s at the solved pacing.

## PPT TEST

No beat could be exported as a static slide. Type struck on the spoken
contrast (B01); a card typing itself (B02); an isotype count where 38 of 49
marks change colour and fall (B03); a ring travelling to one track while a
counter runs its rows (B04); the same tracks re-coloured two ways (B05); bars
growing to value on the spoken figure (B07); a bar collapsing while a counter
runs backwards (B08); twelve points landing per column (B09); a curve
followed to zero and a fix typing itself (B10). **No two consecutive beats
share a visual scheme.**

B07 is drawn natively rather than from `scores.png` for exactly this reason:
two consecutive plate beats of the same chart would be a slideshow. B07 grows
the first pair on the spoken figures; B08 then shows all four with the second
pair collapsing.

## ILLUSTRATE LAW

The Claude UI appears at **B00, B11, B12, B13 only**. All ten inner beats
illustrate their own concept as reel-local Manim. No composer wallpaper.

## Gates at the time of writing

| Gate | Result |
|---|---|
| F — paperwork set | FACTCHECK · SHOTLIST · PROMPTS · SOURCES · PEDAGOGY all present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0` (after 1 fix) |
| W — WCAG · margins · overlap | 10/10 `rc=0` |
| B — pixel-true layout, both aspects | 20/20 `rc=0` (after 6 fixes, two of them regressions from my own fixes) |
| Visual pre-flight — 20 frames read, both aspects | 8 further defects found and fixed, none caught by any gate |
| P — human signature | **pending** — `PEDAGOGY.md` |

### Visual pre-flight — 8 further defects, none caught by any gate

All 20 scene-aspects were rendered at 480p and read before any 4K render.

| Beat · aspect | What was wrong |
|---|---|
| B03 both | the isotype read as a washed-out mess: 14×4 left a ragged boundary ten marks into row 3, and the fallen marks at 0.28 opacity looked like a rendering fault rather than a loss. Now 7×7 at 0.50. |
| B06 both | **"after shuffling" was printed ON the terracotta peak**, which reaches the top of the plot — the frame read "fter shuffling". Both labels moved above the plate. |
| B07 both | three text rows crammed between the axis and the closing line; portrait had 0.07 units between two of them |
| B10 landscape | **the fix card crossed the safe edge at x 6.30 against X_MAX 6.15, and overlapped the plot.** GATE B passed it because the card is a `RoundedRectangle`, not text, and the text inside did stay in bounds. |
| B04 portrait | the second chip sat 0.08 units off the closing line |
| B03 landscape | *a regression from my own fix* — moving the date left put it under the ledger chip |
| B06 landscape | *a regression from my own fix* — I read the plate's centre as 0 when it is +0.76, so the labels I moved "above the plate" landed at 2.59 and straddled the hairline |
| B10 landscape | **"no fingerprint, no inflation" was printed across the curve.** GATE B cannot see this: the curve lives inside the plate image, not as a Manim mobject. Moved to the empty upper-left quadrant. |

Two of the eight are the recurring class — an element GATE B scores as
non-intersecting because the thing it collides with is **inside a plate
image**. A plate is an `ImageMobject`, not a curve. Two more were regressions
from my own fixes, caught only by re-running the gate and re-reading the
frame after each change.

### The four earlier pre-flight fixes, for the record

1. **B05, GATE A — plate geometry left undone.** `split.png` is 0.452, so at
   pw 10.60 it is **4.79 units tall against a 4.30 figure band**, and the
   panel label landed at y 3.54 — above the title. This is the Ep. 08 B04
   defect repeating: `ph = pw × (ih/iw)` is arithmetic, not an estimate.
   Now pw 7.40 → ph 3.35.
2. **B04 landscape, GATE B.** `regions.png` at pw 7.60 was 3.60 tall centred
   at +0.66, so its top reached +2.46 and the track label straddled the
   hairline at +2.66. Shrunk to pw 7.00 and the ring moved to the top track,
   so its label sits in open space.
3. **B03 portrait, GATE B.** The "published ledger" chip sat directly under
   the date card and its rounded-rectangle stroke read as a curve beneath the
   type. Portrait drops the chip; the citation line names the sources anyway.
4. **B07 portrait, GATE B.** The two bar labels at y −2.26 ran into the
   closing line at −2.42. Moved up and reduced.

## Not run, and why

**GATE T (type-lock) could not be run: `scripts/type_check.py` does not exist
in this toolkit.** SKILL.md describes it as "ALWAYS RUN" and a hard block on
`./art run` and `./art final`, but the script is not shipped and `run.sh`
wires no such gate; the same is true of GATE SHARPNESS.

§8.1 min-size and §8.3 contrast are covered by GATE W; §8.2 overflow and §8.5
wordy-card by GATE B. **§8.4 kerning/font-coverage and §8.6 golden strings are
covered by nothing automated.** Ep. 09 shipped a frame where the `✓`
character — absent from EB Garamond — rendered as stray digits, and only
reading frames caught it. The only non-ASCII marks in this reel are `→`, `·`
and the `−` in "−75%", all within EB Garamond's coverage and all checked in
the preview frames.

**`run.sh` would also skip F, A and W on this reel** — all three are guarded
on `[ -n "$PENDING" ]`, and `PENDING` is empty because `run.sh` discovers
scenes with `class (\w+)\(Scene\)` while every scene here subclasses `Paced`.
They were run explicitly, which is what the table above records.
