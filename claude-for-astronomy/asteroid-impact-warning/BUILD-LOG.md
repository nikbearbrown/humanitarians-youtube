# BUILD-LOG — *The Number Went Up.*

Ep. 08 · `asteroid-impact-warning` · toolkit `brutalist.art` · skill `ai-explainer`
· channel `claude-hai` · **$0.00** (Kokoro is local; every plate is computed here)

## Deliverables

| Cut | File | Resolution | Duration | Size | Loudness |
|---|---|---|---|---|---|
| 16:9 master | `asteroid-impact-warning.mp4` | 3840×2160 @ 24 | 158.46 s (2:38.5) | 23.8 MB | −20.9 LUFS |
| 9:16 master | `asteroid-impact-warning-9x16.mp4` | 2160×3840 @ 24 | 158.46 s (2:38.5) | 23.4 MB | −20.9 LUFS |
| 9:16 in place | `short/asteroid-impact-warning-short.mp4` | 2160×3840 | 158.46 s | 23.4 MB | — |

Both masters are **3803 frames** — `frames / 24 == duration` exactly — and both
carry all 14 beats. The 9:16 is **not a crop**: every Manim beat is re-laid-out
from the same `scenes.py` at 2160×3840, and all four Remotion bookends
re-render against their `…916` compositions.

## Gates

| Gate | What it checks | Result |
|---|---|---|
| F | paperwork set present | PASS |
| L | beat-mix lint | PASS — `clean — beat mix OK` |
| A | static pre-flight | PASS — 10/10 `rc=0` |
| W | WCAG contrast · margins · text-overlap | PASS — 10/10 `rc=0` |
| **B** | pixel-true layout audit, per scene, both aspects | **20/20 `rc=0`** — no errors, no warnings |
| **P** | human narration signature | signed `VERDICT: PASSED`, Om Mali, 11/09/26 |
| **V** | frame-level QC on each compiled master | **28 frames · 0 BLOCKER · 0 MAJOR**, both cuts |
| T | type-lock | **COULD NOT RUN — `type_check.py` is not in this toolkit.** See below. |

Beyond the gates, both contact sheets were read in full and the tail beats
(B08–B13) hand-sampled from each finished master, because the contact sheet
carries only 16 of the 28 sampled frames. See `_qc/VISUAL-QC.md`.

**Gates F, A and W were run explicitly, not by `run.sh`.** All three are
guarded on `[ -n "$PENDING" ]`, and `PENDING` is empty for this reel because
`run.sh` discovers scenes with `class (\w+)\(Scene\)` while every scene here
subclasses `Paced` — so a pass that renders nothing silently skips them. GATE L
is not guarded that way. **Do not read a clean `run.sh` as evidence these three
ran.** Commands are in `BUILD-PROMPT.md`.

**GATE T is described in `skills/make/ai-explainer/SKILL.md` as "ALWAYS RUN"
and as a hard block on both `./art run` and `./art final`, but the script it
names does not exist here** — `find . -name type_check.py` returns nothing and
`run.sh` wires no such gate, as is also true of GATE SHARPNESS. This is a gap
between the doctrine and the shipped toolkit, not a step skipped in this build.
What GATE T would check is partly covered: §8.1 min-size and §8.3 contrast by
GATE W, §8.2 overflow and §8.5 wordy-card by GATE B. §8.4 kerning and §8.6
golden strings are covered by nothing automated and were verified by reading
frames.

## Audio is the clock

Written to a word budget before the sheet was authored: 434 words. Measured:

```
B00 11.65  B01  7.21  B02 13.01  B03 14.08  B04 12.37  B05 10.97  B06 12.10
B07 12.39  B08 13.70  B09  8.13  B10 10.94  B11 10.52  B12 16.23  B13  5.16
TOTAL 158.5 s = 2:38.5      margin to the 3:00 cap = 21.5 s
```

No `--speed` correction was needed. Kokoro `af_bella`, local, free.

### The prediction model is noisy, not biased — and I got its sign wrong

| Episode | words | predicted | measured | error |
|---|---|---|---|---|
| Ep. 06 | 487 | 2:50 | 3:07.7 | **+10.4%** |
| Ep. 07 | 443 | 2:50.8 | 2:50.2 | −0.4% |
| Ep. 08 | 434 | 2:46.8 | **2:38.5** | **−5.0%** |

I deliberately widened Ep. 08's margin to 13 s (against Ep. 07's 9.8 s) on the
reasoning that the words-only model *under*-predicts spoken numerals, as it had
on Ep. 06, and this script is numeral-heavy. **It over-predicted by 5%
instead.** The margin was harmless and the episode landed well inside the cap,
but the stated reason for it was wrong: across three episodes the error is
±5–10% with no consistent sign, so the right description is "budget a margin
because the model is noisy", not "budget a margin because numerals run long".

A first draft came in at 454 words (2:54.5 predicted). Six lines were cut
**before GATE P**, which moved four figures off the voice and onto the screen —
where SHOW-DON'T-TELL wanted them anyway. That trim was right for a different
reason than I gave: it improved the beats, not the timing.

## Pacing

Every Manim scene is paced to its own beat by the `Paced` base class (RT
multiplier · per-reveal HOLD · `hold_to_beat()` on the tail), solved from a
no-render measurement pass. Final landing, 4K, identical in both aspects:

```
B01  7.208 / 7.21   B02 13.000 / 13.01  B03 14.042 / 14.08  B04 12.333 / 12.37
B05 10.875 / 10.97  B06 12.000 / 12.10  B07 12.375 / 12.39  B08 13.667 / 13.70
B09  8.125 / 8.13   B10 10.916 / 10.94
```

**Every scene lands under its beat**, worst case 0.100 s (B06), total slack
0.36 s across 158.5 s. `compile.py` reported no stretch and no centre-cut on
either aspect, so there is no slow motion anywhere.

### Why the last 0.1 s was left on the table

B05 and B06 land 0.095 s and 0.100 s short. This is **frame quantisation inside
Manim's `play()`** — thirteen reveals each rounding to a whole frame — and it is
not fixable by raising `HOLD`: a larger HOLD raises `renderer.time`, and
`hold_to_beat()` then shortens the tail by exactly the same amount, so the total
does not move. Closing it properly would mean reimplementing Manim's frame-count
arithmetic inside `Paced`.

I chose not to, because the asymmetry runs the other way: a clip **shorter**
than its beat is padded with a held frame, which is invisible, while a clip
**longer** than its beat is centre-cut, which would clip the closing line off
both ends. Undershoot is the correct side to err on, and the render loop's
tolerance is written accordingly (`−0.25 s … +0.05 s`).

## Defects found and fixed in this build

### 1. The plate generator's self-check refuted my own physics — twice

`assets/gen_neo.py` asserts that the impact-probability curve peaks where
geometry says it must, and raises `SystemExit` rather than write a plate if it
disagrees. It earned its keep immediately.

**First failure.** I predicted σ_peak = d from the one-dimensional argument
(maximise σ⁻¹·exp(−d²/2σ²)). The numbers said 0.67 and **the numbers were
right**: the uncertainty shrinks in *both* target-plane directions at once, so
the probability goes as the disc area times the 2-D density, and maximising
b_cap²σ⁻²·exp(−d²/2σ²) gives **σ_peak → d/√2 = 0.7071**.

**Second failure.** With the prediction corrected, the check still failed — at
`b_cap/d = 0.001` the peak probability is ~10⁻⁵, so even 800,000 Monte Carlo
samples leave about eight hits per point and `argmax` over the noisy curve
returns noise. Replaced the estimator with exact quadrature (the inner
y-integral in closed form via `erf`). **A self-check noisier than the effect it
checks is not a check.** Final:

```
b_cap/d=0.1250  ->  peak at sigma/d=0.7788
b_cap/d=0.0250  ->  peak at sigma/d=0.7106
b_cap/d=0.0050  ->  peak at sigma/d=0.7063
b_cap/d=0.0010  ->  peak at sigma/d=0.7063
PASS: converged to 0.7063 vs predicted 0.7071 (delta -0.0008)
```

Also caught by arithmetic rather than by eye: the capture radius needs v∞
recovered from the published impact speed first (`v_imp² = v∞² + v_esc²`);
using 17.3 km/s directly understates `b_cap` by ~12%. The code comments the
trap and prints **b_cap = 8352 km = 1.311 R_E**.

### 2. Four rendering defects in the same generator, all found by looking

1. **The mover was invisible.** At 5200 flux spread along a trail, the one real
   object sat inside the difference image's noise — the plate was a picture of
   nothing. Raised to 34,000 and gave the difference frame its own signed
   stretch.
2. **The dipole rendered as a single dot** and **the bleed class as two black
   rectangles.** Both came from per-panel percentile stretching, which rescales
   each cut-out against its own brightest pixels — so a stamp containing one
   saturated column maps everything else to black, and the eight classes stop
   being comparable, which is the exact comparison the beat makes. One shared
   physical stretch on a 0.20 grey pedestal fixed both, and the pedestal is
   what makes a *negative* lobe visible at all.
3. **The b-plane panels drew as horizontal bands.** At σ = 14 d the 3σ ellipse
   is far wider than its panel, so the nested outlines clipped into stripes
   that looked like a rendering bug. Replaced the outlines with the actual 2-D
   Gaussian density as a raster, and chose the three σ values so the widest
   contour fits.
4. **`completeness.png` computed a power law it never drew,** and put its end
   bars on the frame edges where they clipped. Rewritten as a categorical
   three-class ledger with the 90% rule drawn *behind* the bars.

### 3. Nine GATE B failures, eight of them portrait

GATE B's first pass: landscape 9/10, **portrait 2/10**. Portrait is the
stricter aspect — same height, a third of the width — exactly as Ep. 07 found.
Every failure was one element too many in a stacked column:

| Beat | Failure | Fix |
|---|---|---|
| B07 landscape | the Torino chip sat **on** the probability polyline | narrowed it and moved it clear of the plot's right edge |
| B03 portrait | caption ran 0.02 units past the safe edge | `_fit` to 3.32 |
| B04 portrait | second subline landed **exactly on** the closing line; chip landed on the wordmark bug | portrait drops both sublines |
| B05 portrait | last subline on the citation; last figure on the closing line | portrait drops the 0.4% counter |
| B06 portrait | boundary label crossed the right safe edge | narrowed and repositioned |
| B07 portrait | rotated y-label crossed the safe edge | landscape-only — **the identical defect Ep. 07's B07 hit** |
| B08 portrait | "the peak" overlapped the b-plane scale key by 77% | landscape-only |
| B09 portrait | "ruled out" landed on the closing line at 100% | portrait drops the chip |
| B10 portrait | three separate label pairs stacked on each other | portrait drops the completeness plate |

**The rule used to decide what portrait loses: anything the narration SPEAKS
stays on screen; the on-screen-only extras go.** That is why B10 drops the
plate (never spoken) rather than the counter (spoken), and why B05 drops 0.4%
(never spoken) rather than 99.6% or 90% (both spoken).

### 4. Five compositional defects that no gate caught

GATE B samples a handful of snapshots and judges pairwise text boxes. It does
not judge whether a figure is the right *size* for its band, and it never
sampled the frame where B04's plate sat over the title. These were found by
rendering both aspects at 480p and **reading the finished frame of every
scene**:

1. **B04's plate covered the title.** At `pw = 7.4` the plate is 4.19 units
   tall in a 4.30-unit band centred at y = 0.95 — so it ran from −1.15 to
   +3.05, straight over the title at +3.02 and across the hairline. Sized to
   3.34 and centred flush under the band's top edge.
2. **B05's underline was drawn through its own subline** — in *both* aspects.
   `_underline` sits ~0.25 below a 34–48 pt number and the subline sat at 0.31.
   Rule pulled tight to the number, subline pushed clear.
3. **B03's plate was undersized**, leaving dead air either side (FILL-THE-CANVAS
   LAW). Widened 6.9 → 7.6. Not further: `_cap` positions itself with
   `next_to()`, so its y is a *consequence* of the plate's height, and at
   `pw = 8.8` the caption landed at −1.30…−1.14 against the chip's
   −1.80…−1.16. Measured with a bounding-box probe rather than guessed —
   guessing is how the collision got in.
4. **B03's chip still touched the caption's descenders** after that fix. Not a
   box overlap, so GATE B passed it; visible at full zoom. Nudged 0.14 units.
   **A gate passing is not the same as the frame being right.**
5. **B06's boundary label abutted the COMPUTED box** in landscape and the arrow
   shaft in portrait.

### 5. An unbounded Gaussian put a line through the title

B09's uncertainty fan used `rng.normal()` directly, so roughly one draw in
twenty-six lands two or three sigma out. One landed at **y = 3.6** — above the
hairline and through the title. GATE A caught it. Added `_kclip()`, a truncated
normal, and applied it to B06's fan too, which had the same flaw pointing
downward into the closing-line band. Clipping is the *correct* fix here, not a
workaround: the fan is a picture of an uncertainty region, and the region
genuinely is finite.

### 6. `python3` is not the venv interpreter

The first audio run failed with `pip install kokoro-onnx`. Putting
`.venv/Scripts` on `PATH` is not enough — a Windows venv ships `python.exe` but
no `python3.exe`, so `python3` falls through to the system Python 3.13, which
has none of the toolkit's dependencies. **Call
`.venv/Scripts/python.exe` explicitly.** Every invocation in this build does.

### 7. Windows encoding

`run.sh` and the Python scripts die on cp1252 as soon as narration carries
typographic punctuation. Every invocation exported `PYTHONUTF8=1` and
`PYTHONIOENCODING=utf-8`. Still unpatched in the toolkit.

### 8. One inconsistency of my own authoring

I spelled the motion lane `draw-on` on B03 but `drawon` on B06 and B08, so
`compile.py`'s histogram split them into two lanes. Harmless — GATE L's
threshold check passes either way — but wrong in the sheet. Normalised to
`drawon` and the 16:9 master recompiled so its build stamp matches. The
histogram now reads `drawon:3 annotate:3 type-on:2 kinetic:2 stagger:2
isotype:1 fade:1`.

## The 9:16 cut

```bash
python  runtime/scripts/shorts.py <reel> --drop --no-endcard --handle "@HumanitariansAI"
#   → 14 beats · nothing dropped · ONDA CHECK rewired B00/B11/B12/B13 to …916
cp _portrait/B*.mp4 short/manim/ ; cp scenes.py short/scenes.py
python  runtime/scripts/remotion_scenes.py <reel>/short     # 4 × 2160×3840
python  runtime/scripts/compile.py <reel>/short --height 3840
python  runtime/qc/final_frame_check.py <reel>/short
```

`--drop` with no arguments and `--no-endcard` give a full-length portrait cut:
no beats cut, no endcard, ends on B13.

`compile.py` emits two SKIN LINT warnings on the short (`B00 … wants
ClaudeComposerAsk`, `B13 … wants ClaudeTitleOutro`). **Both are expected**: the
linter enforces COLD OPEN LAW and OUTRO LAW on composition *names* and does not
know that `shorts.py`'s ONDA CHECK deliberately rewired them to the `916`
variants.

Unlike Ep. 07, the portrait `916` components needed no work — Ep. 07's root
fixes to `ClaudeVerdictArtifact916` and `ClaudeTitleOutro916` (42% and 19%
canvas fill → ~79%) are still in place and still correct.

## What did not go wrong this time

Ep. 07's two worst process failures were avoided by following its own build
log:

- **Concurrent Manim renders.** Ep. 07 lost a full render pass to two processes
  corrupting each other's ffmpeg concat — silently dropping ten frames from a
  clip whose fourteen partial files summed to exactly the right count. This
  build rendered all twenty scenes **sequentially**, verified each against its
  measured beat before slotting it, and checked `frames/24 == duration` on all
  twenty. Zero mismatches.
- **`run.sh` killed for memory mid-pass.** Not attempted. `run.sh` cannot render
  this reel's scenes anyway (see the `(Scene)` regex note above), so the pass
  was driven directly: `remotion_scenes.py` → `compile.py` → `final_frame_check.py`.

## Provenance

`beat_sheet.json` carries the build stamp: 14/14 slots filled, the motion
histogram above, and per-beat Remotion provenance stamped by
`remotion_scenes.py`.

Plates: `assets/gen_neo.py`, seed **8801**, outputs in `assets/plots/`. Rerun
with `python assets/gen_neo.py`; **delete `media/videos` before re-rendering**,
because Manim's cache key hashes scene code and not the contents of the images
a scene loads.
