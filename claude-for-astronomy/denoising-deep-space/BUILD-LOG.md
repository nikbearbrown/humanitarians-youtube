# BUILD-LOG — *The Sharpest Guess.*

Ep. 09 · `denoising-deep-space` · toolkit `brutalist.art` · skill `ai-explainer`
· channel `claude-hai` · **$0.00** (Kokoro is local; every plate is computed here)

## Deliverables

| Cut | File | Resolution | Duration | Size | Loudness |
|---|---|---|---|---|---|
| 16:9 master | `denoising-deep-space.mp4` | 3840×2160 @ 24 | 163.59 s (2:43.6) | 36.1 MB | −20.9 LUFS |
| 9:16 master | `denoising-deep-space-9x16.mp4` | 2160×3840 @ 24 | 163.59 s (2:43.6) | 27.4 MB | −20.9 LUFS |
| 9:16 in place | `short/denoising-deep-space-short.mp4` | 2160×3840 | 163.59 s | 27.4 MB | — |

Both masters are **3926 frames** — `frames / 24 == duration` exactly — and both
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
| **B** | pixel-true layout audit, per scene, both aspects | **20/20 `rc=0`** (after 7 fixes) |
| **P** | human narration signature | signed `VERDICT: PASS`, Om Mali, 18/09/2026 |
| **V** | frame-level QC on each compiled master | **28 frames · 0 BLOCKER · 0 MAJOR**, both cuts |
| T | type-lock | **COULD NOT RUN — `type_check.py` is not in this toolkit.** See below. |

Beyond the gates, both contact sheets were read in full and the tail beats
(B08–B13) hand-sampled from each finished master, because the contact sheet
carries only 16 of the 28 sampled frames. See `_qc/VISUAL-QC.md`.

**Gates F, A and W were run explicitly, not by `run.sh`.** All three are guarded
on `[ -n "$PENDING" ]`, and `PENDING` is empty for this reel because `run.sh`
discovers scenes with `class (\w+)\(Scene\)` while every scene here subclasses
`Paced`. **Do not read a clean `run.sh` as evidence these three ran.**

**GATE T is described in `skills/make/ai-explainer/SKILL.md` as "ALWAYS RUN" and
as a hard block on `./art run` and `./art final`, but the script it names does
not exist here** — `find . -name type_check.py` returns nothing and `run.sh`
wires no such gate, as is also true of GATE SHARPNESS. §8.1 min-size and §8.3
contrast are covered by GATE W, §8.2 overflow and §8.5 wordy-card by GATE B.
§8.4 kerning and §8.6 golden strings are covered by nothing automated — and
**this reel is the clearest case yet for why that matters**: the `✓` character
is absent from EB Garamond and rendered as stray digits on screen, which is
exactly a §8.4-class defect. It was caught by reading frames.

## Audio is the clock

434 words predicted 2:39.2. Measured:

```
B00 10.94  B01  6.83  B02 14.25  B03 12.76  B04 12.14  B05 13.12  B06 11.75
B07 12.42  B08 11.95  B09 12.80  B10 12.25  B11 12.03  B12 14.87  B13  5.48
TOTAL 163.6 s = 2:43.6      margin to the 3:00 cap = 16.4 s
```

No `--speed` correction needed. Kokoro `af_bella`, local, free.

### The prediction model: four episodes of evidence

| Episode | words | predicted | measured | error |
|---|---|---|---|---|
| Ep. 06 | 487 | 2:50 | 3:07.7 | **+10.4%** |
| Ep. 07 | 443 | 2:50.8 | 2:50.2 | −0.4% |
| Ep. 08 | 434 | 2:46.8 | 2:38.5 | **−5.0%** |
| Ep. 09 | 436 | 2:39.2 | **2:43.6** | **+2.7%** |

Ep. 08's build log claimed the model *under*-predicts spoken numerals and set
its margin on that basis. Ep. 08 then over-predicted by 5%, and Ep. 09 —
written on the same rate — under-predicted by 2.7%. **The error is not
systematically signed; it is noise of order ±5–10%.** That is the correct
reason to budget margin, and it is what `beat_sheet.json` now records.

## Pacing

Every Manim scene is paced to its beat by the `Paced` base class, solved from a
no-render measurement pass. Final landing, 4K, identical in both aspects:

```
B01  6.625 / 6.83   B02 14.083 / 14.25  B03 12.542 / 12.76  B04 11.958 / 12.14
B05 12.917 / 13.12  B06 11.542 / 11.75  B07 12.208 / 12.42  B08 11.750 / 11.95
B09 12.583 / 12.80  B10 12.042 / 12.25
```

**Every scene lands under its beat**, worst case 0.218 s, total slack 2.0 s
across 163.6 s. `compile.py` reported no stretch and no centre-cut on either
aspect.

### A permanent fix to the chassis: `TAIL_TRIM`

Landscape B10 **overshot by +0.12 s** — the dangerous direction, because
`compile.py` centre-cuts a long clip and would clip the closing line off both
ends. Diagnosis: `renderer.time` under-reports the true rendered length,
because each `play()`'s frame count rounds up and the error accumulates with the
number of reveals. B10 has 20 of them, the most in the reel, and the shortfall
reached 0.53 s.

**This cannot be fixed by lowering `RT` or `HOLD`.** A smaller body raises
`target − now` by exactly the same amount and the total does not move — which is
why Ep. 08 left a comparable undershoot alone rather than chase it. The target
itself has to carry the margin, so `hold_to_beat` now subtracts a module-level
`TAIL_TRIM = 0.18`.

That moved nine scenes by exactly the trim and left B10 unchanged, which
revealed a second fact: B10 was already on the 0.35 s floor, so its *body* was
too long rather than its tail. Its `RT` was reduced 1.307 → 1.278 and it now
lands at −0.21 and is stable (1.255 gives the same result, i.e. `hold_to_beat`
is pinning it again).

## Defects found and fixed in this build

### 1. The plate generator refused to run five times; four were my errors

`assets/gen_deconv.py` asserts two claims — that detector striping is
recoverable while lost information is not, and that two skies differing by half
their structure produce identical images — and raises `SystemExit` rather than
write a plate if either fails.

1. **The stripe residual measured the wrong quantity.** It compared the cleaned
   frame against the noiseless scene, folding in the Gaussian read noise that
   stripe removal never claimed to touch, and reported **22%** for a method
   recovering the pattern to **3.6%**.
2. **An arbitrary threshold.** "Lost information > 20% of the truth" was a
   number picked before any measurement; it then read 19.2%. The honest fix was
   not to retune the threshold until it passed but to assert something that
   carries the claim: that the destroyed information **exceeds the noise**, and
   therefore dominates rather than rounds away.
3. **The wrong comparison region.** That noise comparison was first made over
   the whole frame, where the noise fills 65,536 pixels and the galaxy occupies
   a few thousand, so empty sky dominated the ratio and it read **0.5×**.
   Restricted to the source footprint (17,814 px): **1.3×**.
4. **A prior 255× too weak** — numpy's unnormalised-FFT factor wrong by N.
   **Nothing crashed.** A too-weak prior does not fail loudly; it simply stops
   contributing. Posterior samples collapsed onto the mean, the "three answers"
   plate showed three nearly identical pictures (**2.8%** apart instead of
   **35.9%**), and the variance ratio was computed against a mis-scaled prior.
   **This is the dangerous class: a silent numerical error that produces a
   plausible picture.** Found by measuring a draw's standard deviation against
   the galaxy's. Now derived — `std = √(Σspec)/N` — and asserted over 24 draws,
   because a single realisation of a k^−2.6 spectrum scatters by tens of per
   cent and comparing one draw against another compares two noisy numbers.
5. **A self-check noisier than the effect it checked.** The checks were first
   Monte Carlo; at the smallest disc the target probability is ~10⁻⁵, so
   800,000 samples left about eight hits per point and `argmax` returned noise.
   Replaced with exact quadrature and closed-form variance.

Final: truths differing by **52.4%** produce observations differing by
**0.0000 noise σ**; three priors forced to χ²/N = 1.008/1.007/1.008 give
reconstructions **35.9%** apart; above the cutoff posterior variance equals
prior variance to **1.0000**; the variance ratio spans **53×** (0.0006 → 0.0306).

### 2. Two plates were computing something true but uninformative

Both from one cause: most of the 256² grid's Fourier modes lie **above** the
cutoff, where `H = 0` exactly, so anything averaged over all modes is dominated
by the region the telescope cannot see.

- **`threeanswers` spread only 2.8%** because the Wiener/MAP estimate is
  identically zero above the cutoff for *every* prior — so three different
  priors gave three nearly identical pictures. That is a real and important
  fact (the posterior **mean** cannot differ above the cutoff) but it is not
  what a generative denoiser returns. A diffusion model returns a **sample**.
  Three priors, three samples: 35.9% apart.
- **`varratio` moved only 1.3×** because averaging `var/P` over all modes pins
  the ratio near the fraction above cutoff, where it is 1 whatever the data
  does. Restricted to the observable band (**1,153 of 65,536 modes — 1.8%**):
  53×. The paper this metric comes from takes its ratio inside an aperture for
  the same reason.

### 3. A unit error caught before shipping

**"133 GPU-hours" collapsed 133 hours × 32 V100s by a factor of 32** (~4,256
GPU-hours). Corrected on screen to "133 hours on 32 GPUs" in both `scenes.py`
and the beat sheet's `show` block. Exactly the class of error the DOUBLE-CHECK
LAW exists to catch: a unit dropped while paraphrasing.

### 4. Seven GATE B failures

Landscape 9/10, portrait 8/10 on the first pass.

| Beat | Failure | Fix |
|---|---|---|
| B06 landscape | "all three match the data equally well" sat 0.10 units from a rule and GATE B read it as a label on a curve | rule removed — the sentence says "equally" on its own |
| B07 landscape | "the training set" sat on the bottom row of tiles (a `Square` has a stroke) | label moved above the grid as a heading |
| B09 **both** | the varratio plate is 2:1, the tallest in the reel; at `pw = 7.2` it is 3.60 units tall and I wrote `P(0.92, …)` for its y-centre, so it spanned to **+2.72** — past FIG_TOP — and its axis label collided with the title | sized to 5.80 wide, both axis labels moved below it, ring label dropped |
| B05 portrait | "noise sigma between their images" landed exactly on the closing line | figure blocks restacked |
| B07 portrait | the counter's subline landed on the closing line | counter raised |
| B08 portrait | "the prior did" sat on the chip below it | rows raised, chip lowered |

### 5. Eleven defects that no gate caught

Found by rendering both aspects at 480p and **reading the finished frame of
every scene**. Two were outright rendering bugs:

1. **The `✓` character is absent from EB Garamond** and rendered as stray digits
   ("27/3") on screen in B10. Replaced with a tick drawn from two `Line`s.
   **Never rely on a glyph outside the font's coverage.**
2. **B07's tile grid rendered as vertical bars**, because the tile side (0.24)
   exceeded the row pitch (`bh*0.58/6 = 0.222`), so consecutive rows overlapped
   into columns.

The rest were crowding a box-overlap check passes but an eye does not: B03's
caption against its panel labels (twice — the second time at full zoom); B04's
`LOSSY` chip against first the "blurred" label and then the 98% counter; B08's
two-part rows reading as misaligned; B10's empty white comparison cards reading
as unfilled placeholders (given schematic content — a soft blob against a
tighter shape with dots); and four portrait crowding cases resolved by dropping
elements.

## The 9:16 cut

```bash
python  runtime/scripts/shorts.py <reel> --drop --no-endcard --handle "@HumanitariansAI"
cp _portrait/B*.mp4 short/manim/ ; cp scenes.py short/scenes.py
python  runtime/scripts/remotion_scenes.py <reel>/short     # 4 × 2160×3840
python  runtime/scripts/compile.py <reel>/short --height 3840
python  runtime/qc/final_frame_check.py <reel>/short
```

Five scenes drop a secondary element by design. **The rule for choosing what
goes: anything the narration SPEAKS stays on screen.** That is why B10 drops
the two comparison cards (never spoken) and keeps QUALITATIVELY (spoken as its
own sentence), and why B08 drops five unreadable panel labels rather than the
two sentence rows.

`compile.py` emits two SKIN LINT warnings on the short (`B00 … wants
ClaudeComposerAsk`, `B13 … wants ClaudeTitleOutro`). **Both are expected** — the
linter enforces COLD OPEN LAW and OUTRO LAW on composition *names* and does not
know that `shorts.py`'s ONDA CHECK deliberately rewired them to the `916`
variants.

## What did not go wrong

- **Concurrent Manim renders.** All twenty scenes rendered sequentially, each
  verified against its measured beat before slotting, `frames/24 == duration`
  checked on all twenty. Zero mismatches.
- **`run.sh` killed for memory.** Not attempted; the pass was driven directly.
- **The portrait `916` components.** Ep. 07's root fixes to
  `ClaudeVerdictArtifact916` and `ClaudeTitleOutro916` are still correct.

## Provenance

`beat_sheet.json` carries the build stamp: 14/14 slots filled, motion histogram
`annotate:3 stagger:3 type-on:2 kinetic:2 drawon:2 isotype:1 fade:1`, and
per-beat Remotion provenance stamped by `remotion_scenes.py`.

Plates: `assets/gen_deconv.py`, seed **9109**, 256², outputs in `assets/plots/`.
Rerun with `python assets/gen_deconv.py`; **delete `media/videos` before
re-rendering**, because Manim's cache key hashes scene code and not the contents
of the images a scene loads.
