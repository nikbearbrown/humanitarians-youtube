# CHECKS-REPORT — *The Signal We Imagined.*

Ep. 13 · written **before the first slate compiled**, as the PROOF GATE in
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
| B03 | SHOW | a frequency axis, one tone named, 26 look-alikes, the tone turning ink | Manim |
| B04 | SHOW | `waterfall.png` + the interference named + the traced track | Manim + computed plate |
| B05 | SHOW | a fan of trial tracks, one lit, a bracket closing, one track outside | Manim |
| B06 | SHOW | `three.png` — three hypotheses named | Manim + computed plate |
| B07 | SHOW | `recall.png` + the ringed flat bar + two counters | Manim + computed plate |
| B08 | SHOW | `edge.png` + the cliff marked + the 0.06 Hz/s chip | Manim + computed plate |
| B09 | SHOW | `cadence.png` — three traces with a peak, three flat | Manim + computed plate |
| B10 | SHOW | `compare.png` + the 0.76 counter | Manim + computed plate |
| B11 | SHOW | five artefact lines | Remotion |
| B12 | SHOW | the handoff prompt types itself; three grading lines | Remotion |
| B13 | SHOW | title restate, rule, handle, subline | Remotion |

**No beat is a bare CARD.**

## Teaching-arc checklist

| Item | Where | Note |
|---|---|---|
| **FRAMEWORK before examples** | B02, then B04–B06 | B02 states the whole problem in one breath — we have never detected one, so you assume a form, and then you find it — before any method or number. No result appears until B07. |
| **WORKED EXAMPLE** | B04–B08 | One search followed all the way through: what the data is, what the algorithm does, the three hypotheses, the result, and the control that locates the cause. |
| **FALSIFIABILITY** | B07, B08 — and the generator | `gen_seti.py` asserts three claims and writes nothing if any fails. **B08 is a control**: it sweeps the search's lower edge and the blind spot appears exactly where the parameter crosses zero. A fourth claim was measured, failed its own test, and was **removed rather than weakened** — see FACTCHECK. |
| **SCAFFOLDED TASK** | B12 | The prompt is read aloud, then discussed. Three grading criteria; the second ("is the test independent of appearance") is the one that separates understanding from agreement, because a better classifier is still a guess about form. |
| **BOOKENDS** | B00 · B11 · B12 · B13 | All four, in order, in the fixed Claude skin. |
| **NO-SOURCE-NO-VERDICT** | every claim beat | B03 cites Sheikh et al. 2021; B04–B10 cite *this reel's own computation* and say so. The distinction between the published *diagnosis* and this reel's *measurement* is made explicitly in FACTCHECK and SOURCES. |

## Legibility contract

- **Artifact named in `shot.show`** — all 14.
- **~15–35% negative space** — GATE B reports no over- or under-fill in
  either aspect.
- **Nothing un-highlighted below ~40% opacity** — the reel uses colour and
  weight for emphasis, never opacity fades.
- **Comparisons side-by-side, held ≥2 s** — B06 (three fields), B07 (six
  bars), B09 (six traces), B10 (six bars). All held well over 2 s.

## PPT TEST

No beat could be exported as a static slide. Type struck on the spoken
contrast (B01); a card typing itself (B02); one tone standing alone and then
surrounded by twenty-six identical ones before turning ink (B03); a track
traced across a field the viewer is told they cannot see (B04); a fan of
trial tracks sweeping and a bracket closing around them (B05); a bar ringed
**flat on its axis** while a counter reads zero (B07); a curve followed off a
cliff (B08). **No two consecutive beats share a visual scheme.**

B05 is drawn natively rather than from a plate so the fan sweeps *on the
spoken phrase*; a plate could not time that.

## ILLUSTRATE LAW

The Claude UI appears at **B00, B11, B12, B13 only**. All ten inner beats
illustrate their own concept as reel-local Manim. No composer wallpaper.

## Gates at the time of writing

| Gate | Result |
|---|---|
| F — paperwork set | FACTCHECK · SHOTLIST · PROMPTS · SOURCES · PEDAGOGY all present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0`, first pass |
| W — WCAG · margins · overlap | 10/10 `rc=0`, first pass |
| B — pixel-true layout, both aspects | 20/20 `rc=0` (after 7 fixes) |
| Visual pre-flight — 20 frames read, both aspects | 2 further defects found and fixed |
| P — human signature | **PASSED** — `PEDAGOGY.md`, signed Om Mali, 16/10/2026 |

### The seven GATE B fixes, and the pattern in them

**Six of the seven are the same mistake**: a label positioned at
`pat[0] ± pw * k`. In landscape `pw` is 7 units and that lands comfortably
inside a 12.3-unit frame; in portrait `pw` is 3.4 and the *same expression*
lands outside a 3.6-unit frame. **An offset scaled to the plate is not an
offset scaled to the safe area.** Affected B04 (three labels off-frame in
portrait) and B08 (the axis label at x −2.01 against a 1.80 edge).

The others:

1. **B03 landscape** — the 26 look-alike tones rise to y 1.74 and x 4.32, and
   the Parkes/Proxima card spanned x 1.50…5.90, y 0.80…2.00, so ink lines
   were drawn straight through its type. The card moved below the axis.
2. **B07 portrait** — four stacked numbers plus a closing line inside 1.2
   units. The two sub-labels are on-screen-only; portrait drops them.
3. **B04 landscape, a regression from my own fix** — lowering the plate to
   clear the title pushed its bottom label into the closing line. The label
   moved *above* the plate, where it pairs with "these are us", which is the
   contrast the beat is actually about.

## Visual pre-flight — 20 frames read, both aspects

All 20 scene-aspects were rendered at 480p and read before any 4K render.
Only **two** defects survived GATE B this time, against twelve on Ep. 11 and
eight on Ep. 12 — the gate caught seven here because the scene code started
from two episodes of accumulated layout notes.

| Beat · aspect | What was wrong |
|---|---|
| **B06 portrait** | **the three hypothesis labels were printed straight across the stacked waterfall panels.** GATE B passed it because a plate is an `ImageMobject`, not a curve — the exact failure the file's own header warns about. The gutters in `three_v.png` are 0.08 units, far too small for type, so the labels moved below the stack and the plate shrank to make room. |
| B04 both | the sub-line sat **above** the headline it belongs to, so the explanation appeared over the thing it explained |

The first is the recurring one and it is worth stating plainly: **GATE B
cannot see anything that collides with the contents of a plate.** Ep. 11
shipped a label across a bracket, Ep. 12 a card across a curve, and this reel
would have shipped three labels across three spectrograms. The only check
that catches it is reading the frame.

## Gates after the build

| Gate | Result |
|---|---|
| P — human signature | PASSED before any audio was generated |
| Audio | 141.5 s measured (2:21.5), 38 s inside the cap, model error −5.1% |
| Pacing — 24 fps, both aspects | 20/20 inside `-0.25 s … +0.05 s` (after one HOLD fix) |
| V — 16:9 master | 28 frames · BLOCKER 0 · MAJOR 0 — **after fixing a real low-contrast fault** |
| V — 9:16 master | 28 frames · BLOCKER 0 · MAJOR 0 |
| Frame reading, both aspects | 2 defects found and fixed |

**GATE V earned its keep on this reel.** The first compile failed with four
MAJOR low-contrast defects on B04 and B06 — the spectrograms' mid-grey noise
was lifted toward ink and the interference lines were no more contrasty than
the background. The fix was measured against the gate's own metric rather
than guessed: display gamma 1.55 gave 0.237, 2.20 gave 0.286, and 2.80 gave
0.327 against a 0.30 floor. The intermediate attempt went back through the
gate and failed again before the right value was found. Details in
`_qc/VISUAL-QC.md`.

## Not run, and why

**GATE T (type-lock) could not be run: `scripts/type_check.py` does not exist
in this toolkit.** SKILL.md describes it as "ALWAYS RUN" and a hard block on
`./art run` and `./art final`, but the script is not shipped and `run.sh`
wires no such gate; the same is true of GATE SHARPNESS.

§8.1 min-size and §8.3 contrast are covered by GATE W; §8.2 overflow and §8.5
wordy-card by GATE B. **§8.4 kerning/font-coverage and §8.6 golden strings are
covered by nothing automated.** Ep. 09 shipped a frame where `✓` — absent
from EB Garamond — rendered as stray digits. The only non-ASCII marks here
are `→`, `↓` and `·`, all within the font's coverage and all checked in the
preview frames.

**`run.sh` would also skip F, A and W on this reel** — all three are guarded
on `[ -n "$PENDING" ]`, and `PENDING` is empty because `run.sh` discovers
scenes with `class (\w+)\(Scene\)` while every scene here subclasses `Paced`.
They were run explicitly.
