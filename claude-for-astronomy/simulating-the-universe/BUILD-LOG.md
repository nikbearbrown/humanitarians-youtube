# BUILD-LOG — *The Universe You Can Afford.*

Ep. 07 · `simulating-the-universe` · toolkit `brutalist.art` · skill `ai-explainer`
· channel `claude-hai` · **$0.00** (Kokoro is local; every plate is computed here)

## Deliverables

| Cut | File | Resolution | Duration | Size | Loudness |
|---|---|---|---|---|---|
| 16:9 master | `simulating-the-universe.mp4` | 3840×2160 @ 24 | 169.74 s (2:49.7) | 24.0 MB | −20.9 LUFS |
| 9:16 master | `simulating-the-universe-9x16.mp4` | 2160×3840 @ 24 | 169.74 s (2:49.7) | 27.4 MB | −20.9 LUFS |
| review cut | `simulating-the-universe-slate.mp4` | 3840×2160 | 169.74 s | 27.7 MB | — |
| 9:16 in place | `short/simulating-the-universe-short.mp4` | 2160×3840 | 169.74 s | 27.4 MB | — |

Both masters are 4073 frames — `frames / 24 == duration` exactly, and both carry
all 14 beats. The 9:16 is **not a crop**: every Manim beat is re-laid-out from the
same `scenes.py` at 2160×3840, and all four Remotion bookends re-render against
their `…916` compositions.

## Gates

| Gate | What it checks | Result |
|---|---|---|
| F | paperwork set present | PASS — FACTCHECK · SHOTLIST · PROMPTS all present |
| L | beat-mix lint | PASS — `[beat-lint] clean — beat mix OK` |
| A | static pre-flight | PASS — 10/10 `rc=0` |
| W | WCAG contrast · margins · text-on-text | PASS — 10/10 `rc=0` |
| **B** | pixel-true layout audit, per scene, both aspects | **20/20 `rc=0`** — no errors, **no warnings** |
| **P** | human narration signature | signed `VERDICT: PASS`, Om Mali, 09/04/2026 |
| **V** | frame-level QC on each compiled master | **28 frames · 0 BLOCKER · 0 MAJOR**, both cuts |

Beyond the gates, every frame of both contact sheets was read, plus hand-sampled
late frames of B08 and B10 in each aspect (see `_qc/VISUAL-QC.md`).

**Gates F, A and W were run explicitly, not by `run.sh`.** `run.sh` guards all
three on `[ -n "$PENDING" ]`, and `PENDING` is empty for this reel because it
discovers scenes with `class (\w+)\(Scene\)` while every scene here subclasses
`Paced` — so a pass that renders nothing silently skips them. GATE L is not
guarded that way and did run inside the pass; it was re-run anyway. Commands are in
`BUILD-PROMPT.md`. **Do not read a clean `run.sh` as evidence these three ran.**

## Audio is the clock

Written to a word budget *before* the sheet was authored — 443 words, predicted
2:50.8. Measured:

```
B00 12.71  B01  7.51  B02 12.74  B03 13.91  B04 12.37  B05 12.42  B06 10.86
B07 12.95  B08 11.63  B09 13.82  B10 10.52  B11 13.61  B12 20.27  B13  4.42
TOTAL 170.2 s = 2:50.2      margin to the 3:00 cap = 9.8 s
```

**No `--speed` correction was needed.** Ep. 06 had to be re-cut and then run at
`--speed 1.13` because its script was written first and sized afterwards; sizing
first removed that whole cycle. Kokoro `af_bella`, local, free.

## Pacing

Every Manim scene is paced to its own beat by the `Paced` base class (RT
multiplier · per-reveal HOLD · `hold_to_beat()` on the tail), solved from a
no-render measurement pass. Final landing, 4K, both aspects:

```
B01  7.500 / 7.51   B02 12.708 / 12.74   B03 13.875 / 13.91   B04 12.333 / 12.37
B05 12.417 / 12.42  B06 10.833 / 10.86   B07 12.917 / 12.95   B08 11.625 / 11.63
B09 13.792 / 13.82  B10 10.500 / 10.52
```

Worst error **0.037 s**, and every scene lands *under* its beat, which is the safe
direction — `compile.py` never has to stretch a clip, so there is no slow motion
anywhere. Manim subtotal 118.50 s against a 118.73 s budget.

Two scenes were re-solved after the low-resolution pre-flight: B02 was 0.13 s long
(`RT` 1.526 → 1.508). B06 was 0.27 s long and **did not respond to `RT` at all** —
its body finishes under its beat, so `hold_to_beat()` pins the total to the target
regardless of how fast the reveals run. The residue there is frame quantisation of
the tail wait, not a pacing error, and it is 0.027 s in the final cut.

## Defects found and fixed in this build

### 1. Concurrent Manim renders corrupt each other's output — the worst one

Ep. 06 rendered its two aspects as two parallel background jobs. Repeating that
here produced a landscape B01 of **7.083 s against a 7.51 s beat** — 170 frames
instead of 180. The diagnosis mattered because every obvious suspect was innocent:

- the 14 partial movie files summed to **exactly 180 frames**
- an instrumented `hold_to_beat` printed `target=7.510 now=6.958` — correct
- `--disable_caching` changed nothing, and no stale partials existed
- the same scene rendered **alone** at 480p24, 1080p24, 2160p24 *and* 2160×3840
  gave exactly 7.500 s / 180 frames every time

So the scene logic and the pacing were right and **the ffmpeg concat step dropped
frames**. Two renders writing into one reel's `media/` also killed one job outright
at B01 and another at B07.

Everything those jobs produced was discarded — `manim/`, `_portrait/`, and both 4K
`media/videos/scenes/` trees — and all 20 scenes were re-rendered **sequentially**,
each verified against its measured beat before being slotted:

```
render → ffprobe → |duration − beat| ≤ 0.15 s ? slot : retry once : FAIL
```

There is a sting in the tail. `TaskStop` killed the first landscape job's shell but
**not its Manim child**, which kept rendering and dropped its B07 and B08 into
`manim/` mid-way through the new sequential run — mtimes 13:59:42 and 14:00:21
inside an otherwise strictly ~26 s-spaced sequence, so the new run skipped them as
"already filled". Both were within tolerance and would have shipped. They were
deleted and re-rendered clean. **Check mtimes for monotonicity, not just
durations**, after killing a render job.

### 2. `run.sh` was killed for low memory mid-pass

The four 4K Remotion renders left 1.1 GB free of 31.7 GB and the harness killed the
wrapper. Its `compile.py` child survived and finished the review cut, so the pass
was completed by hand from that point — Remotion had already written all four
bookends, and gates F/L/A/W and B had already passed, so nothing was skipped. The
clean master was compiled directly with `compile.py --height 2160`.

Note that `run.sh` cannot render this reel's Manim beats at all: it discovers
scenes with `class (\w+)\(Scene\)`, and every scene here subclasses `Paced`. That
is why the 20 renders are driven directly and slotted into `manim/` before the
pass. It is not a bug in the reel.

### 3. Portrait `916` bookends were badly underfilled

Fixed at the root in the toolkit, not worked around here.
`ClaudeVerdictArtifact916` filled **42%** of its canvas and `ClaudeTitleOutro916`
**19%** — the same defect Ep. 05 fixed for the landscape components and never
carried to the portrait ones. Rescaled both (`CARD_W = width * 0.84`, fonts keyed
to `height`, `justifyContent: 'space-between'` with `PAD_Y = height * 0.13`, and a
terracotta rule above the handle). A second round was needed after the rescaled
card crossed the top safe edge and its shadow crossed the sides; final ink extent
is rows 486…3380, cols 165…1994 against safe bands 192…3648 / 108…2052, **79%**
coverage. `_bench/consumers.json` confirmed this reel was the only consumer, so the
root fix was safe.

### 4. `shorts.py` could not run on Windows at all

It linked every staged file with `Path.symlink_to`, which raises `OSError 1314`
without `SeCreateSymbolicLinkPrivilege`. Added a `link_or_copy` helper that falls
back to `shutil.copy2`, at all three call sites. Also a toolkit fix.

### 5. GATE P opens on a plain substring

`generate_audio_kokoro.py` checks `"VERDICT: PASS" in PEDAGOGY.md`. Explaining the
gate in prose therefore **unlocks it** — an early draft of `PEDAGOGY.md` quoted the
string while its verdict still read PENDING, and a dry run confirmed all 14 beats
"would generate". The prose was reworded to describe rather than quote, and a
warning sits at the top of the file. The real fix belongs in the checker; the gate
was not modified, and audio was generated only after a genuine signature with **no
override flag**.

### 6. The physics was wrong the first time

See `FACTCHECK.md` § DOUBLE-CHECK LAW and `PROMPTS.md`. The first particle-mesh
integrator omitted the Hubble drag term and mis-scaled the initial velocity, and
the two calculations disagreed by a **factor of twenty** on the largest scales.
Deriving the equation of motion by requiring the Zel'dovich growing mode to be an
exact solution in the linear regime gives `dv/dD = -(3/2D) v + (3/2D²) g`, and the
disagreement fell to **3.7% for k < 60 and 58.0% for k > 200** — the two numbers
B09 quotes.

It was caught only because `assets/gen_cosmos.py` prints its own measured `ΔP/P` on
every run. A generator that does not report its own error produces decoration.

Four rendering defects in the same script were caught by looking at its output:
washed-out plates (`gamma 0.38` → `1.15`), moiré from one particle per cell
(589,824 particles on a 512² mesh, `np.bincount` not `np.add.at`), a red/blue
residual outside the palette, and a halo zoom that showed two identical panels
until it was centred on the largest *disagreement* rather than the densest
structure.

### 7. Windows encoding

`run.sh` and the Python scripts crash on cp1252 when narration carries typographic
punctuation. Every invocation in this build exported `PYTHONUTF8=1` and
`PYTHONIOENCODING=utf-8`. Still unpatched in the toolkit — see `BUILD-PROMPT.md`.

## The 9:16 cut

```bash
python3 runtime/scripts/shorts.py <reel> --drop --no-endcard --handle "@HumanitariansAI"
#   → 14 beats · nothing dropped · ONDA CHECK rewired B00/B11/B12/B13 to …916
cp _portrait/B*.mp4 short/manim/ ; cp scenes.py short/scenes.py
python3 runtime/scripts/remotion_scenes.py <reel>/short     # 4 × 2160×3840
python3 runtime/scripts/compile.py <reel>/short --height 3840
python3 runtime/qc/final_frame_check.py <reel>/short
```

`--drop` with no arguments and `--no-endcard` give a full-length portrait cut: no
beats cut, no endcard appended, ends on B13. Six scenes shed a secondary element by
design — 9:16 has the same height and a third of the width, so it has *less* usable
area, not a different crop of the same area. See `SHOTLIST.md` § "Where portrait
carries less".

`compile.py` emits two SKIN LINT warnings on the short (`B00 … wants
ClaudeComposerAsk`, `B13 … wants ClaudeTitleOutro`). **Both are expected**: the
linter enforces COLD OPEN LAW and OUTRO LAW on composition *names* and does not
know that `shorts.py`'s ONDA CHECK deliberately rewired them to the `916` variants.

**The second aspect is a real check on the first.** Ep. 06's worst layout defect
was a pair of transposed `P()` values that were invisible in a 14.22-unit-wide
frame and a GATE V blocker in a 4.5-unit one. Nothing similar surfaced here — GATE
B passed 10/10 in portrait on the first attempt, because the layout bugs it would
have caught were fixed during scene authoring.

## Provenance

`beat_sheet.json` carries the build stamp: 14/14 slots filled, motion histogram
`drawon:3 annotate:3 type-on:2 kinetic:2 stagger:2 isotype:1 fade:1` (no lane over
threshold), and per-beat Remotion provenance stamped by `remotion_scenes.py`.

Plates: `assets/gen_cosmos.py`, seed **7717**, outputs in `assets/plots/`. Rerun
with `python assets/gen_cosmos.py`; **delete `media/videos` before re-rendering**,
because Manim's cache key hashes scene code and not the contents of the images a
scene loads.
