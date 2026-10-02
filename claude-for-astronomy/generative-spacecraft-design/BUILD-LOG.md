# BUILD-LOG — *Nothing Left To Remove.*

**AI in Astronomy & Space Science · Ep. 11** · slug `generative-spacecraft-design`
Built with `brutalist.art` (the free-only Fellow Tier), skill `ai-explainer`,
channel `claude-hai`, Pragmatist register. Built 2026-10-02.

**Total spend: $0.00.** Kokoro TTS runs locally; every plate is computed here;
no API key was used or required at any step.

---

## What shipped

| | 16:9 | 9:16 |
|---|---|---|
| `claude-for-astronomy_OmMali_02_10_2026.mp4` | 3840 × 2160 · 148.97 s · 3575 frames · 15.4 MB | — |
| `generative-spacecraft-design-9x16.mp4` | — | 2160 × 3840 · 148.97 s · 3575 frames · 16.2 MB |

24 fps, h264 + AAC, −20.9 LUFS integrated, both cuts sharing one audio mix.
**2:29.0** — 31 s inside the 3:00 cap.

Both masters live in this folder. Nothing was published; there is no
publishing machinery in this toolkit.

---

## The episode

Topic 11 of the brief is AI-designed spacecraft components. The obvious
telling is a marvel story: a bone-like bracket no human would draw, a third
lighter, the future is here. That version is true.

The interesting thing is that **this is the first episode in the series where
the model is not wrong at all.** Every earlier limit was the system failing to
see something — an accuracy ceiling, an unseen class, a non-identifiable
answer, a closed feedback loop. Here the optimiser is *provably optimal* for
the problem it was handed. There is no bug.

And it is still unsafe, because of what the brief did not say. "Lighter" was
in the brief. "Survive damage" was not. So the optimiser deleted every scrap
of material not carrying the specified load — including the second load path,
which by definition carries nothing until the first one breaks. **The deletion
is not an error. It is compliance.**

So I built it and measured it: a real plane-stress finite-element model and a
SIMP topology optimiser (`assets/topo.py`), then the published fail-safe test
— an 8 × 8 void swept over the domain, worst case taken.

| at 40% mass | undamaged | worst void | sensitivity |
|---|---|---|---|
| a plate machined thin | 100.03 | 121.41 | 1.21× |
| the generative bracket | **81.31** (1.23× stiffer) | **2536.90** | **31.2×** |

Under that void the ordering **reverses**: the optimised part is 20.9× softer
than the plate it beat. At the 90th percentile over all 398 locations it is
still 3.4× against the plate's 1.08×, and 38 of 398 locations cost more than
5×, so this is not one freak spot. At 60% mass the penalty collapses to 1.6×
and the part is still 1.20× stiffer than the plate — but the mass saving falls
from 60% to 40%, **a third of it given back.**

The fix is not a better optimiser; it is a better brief. And the cost of the
better brief is known in advance, in the one currency spacecraft trade in.

---

## Pipeline, in the order it ran

1. **Research** from primary sources → `SOURCES.md`, `FACTCHECK.md`.
2. **`assets/topo.py`** — the FE model and SIMP optimiser, validated before
   anything was trusted.
3. **`assets/gen_struct.py`** — the experiment, three asserted claims, eight
   plates.
4. **`beat_sheet.json`** — 14 beats, 419 words, sized to Ep. 10's measured
   0.3443 s/word.
5. **Paperwork** — SHOTLIST, PROMPTS, CHECKS-REPORT, PEDAGOGY.
6. **GATE P** — signed `VERDICT: PASSED`, Om Mali, 02/10/2026. Audio is not
   generated before this, even though audio here is free.
7. **Audio** — `generate_audio_kokoro.py`, voice `af_bella`, 14 MP3s totalling
   149.0 s. **These durations are the master clock from here on.**
8. **Pacing solved without rendering**, then **verified at 24 fps in both
   aspects** before committing to 4K.
9. **20 scenes rendered at 4K, one Manim process at a time**, each verified
   against its beat, with `frames/24 == duration` and monotonic mtimes.
10. **Remotion bookends** via `remotion_scenes.py`, then
    `compile.py --height 2160`.
11. **GATE V**, then the 9:16 derivative, then GATE V again — each with an
    explicit `--mp4`.
12. **Both masters read frame by frame** → `_qc/VISUAL-QC.md`.

---

## Gate results

| Gate | Result |
|---|---|
| F — paperwork set | present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0` |
| W — WCAG · margins · overlap | 10/10 `rc=0` |
| B — pixel layout, both aspects | 20/20 `rc=0`, after 5 fixes |
| P — human signature | PASSED, before audio |
| Pacing — 24 fps, both aspects | 20/20 inside `−0.25 s … +0.05 s` |
| V — 16:9 master | 28 frames · 0 BLOCKER · 0 MAJOR |
| V — 9:16 master | 28 frames · 0 BLOCKER · 0 MAJOR |
| Frame reading, both aspects | 12 further defects found and fixed |

**GATE T and GATE SHARPNESS were not run: they are not shipped in this
toolkit**, despite `ai-explainer/SKILL.md` describing GATE T as "ALWAYS RUN".
`scripts/type_check.py` does not exist and `run.sh` wires no such gate. Said
plainly rather than quietly skipped — see CHECKS-REPORT for what covers which
clause instead.

---

## The experiment, and the three times it refused

`gen_struct.py` asserts three claims and writes nothing if any fails.

**Validation first, because a wrong stiffness matrix is still symmetric and
still solves.** The FE core was checked against things that actually
constrain it: exact symmetry; **exactly 3 zero eigenvalues**; all three
rigid-body motions annihilated to machine precision; the uniaxial patch test
exact to six digits; and the solid cantilever **1.4–1.9% softer** than
Euler–Bernoulli at two mesh densities — the right direction and magnitude for
a short deep beam carrying shear. One check doubles as a result: the domain,
support and load are symmetric about mid-height, so the optimum must be, and
it measures `max|x − mirror(x)| = 2.1 × 10⁻¹¹`. An asymmetric answer would
have meant the element dof ordering was wrong, which nothing else would
reveal.

**Three errors it caught, all mine:**

1. **I quoted a number that was really my density floor.** The first version
   put three load cases at three heights on the free edge. Two of those sit in
   void, so the solve returned ≈ 8.5 × 10⁹ and the ratio came out at 89
   million. That is EMIN restated, not an engineering result. Fixed by giving
   the bracket a solid, non-design **mounting lug** — which real hardware has,
   because the bolt interface is a requirement, not something the optimiser
   may delete.
2. **Then the effect was real but trivial.** One lug, three load *directions*
   gave a 1.07× penalty, because on a short cantilever straight-down *is* the
   worst direction, so optimising for it is already nearly robust. True, and
   not the episode. The honest move was to find the mechanism that does carry
   a large effect — damage tolerance, which the literature names explicitly —
   rather than dress up a 7% result.
3. **I set a threshold before measuring and the script refused.** Claim 3
   asserted the 60%-mass bracket's damage sensitivity would fall below 1.5×.
   It reads **1.63×**, so nothing was written. The fix was to rewrite the
   claim to what the experiment shows — the penalty collapses by a factor of
   19 while the part stays stiffer than the plate — and to assert that as a
   ratio against a measured quantity rather than a number I guessed.

A fourth: the worst damage location initially came out *on the mounting pad*,
the same floor artefact as (1). Patches overlapping the lug are now excluded,
and the reel says what is excluded and why.

---

## Other errors this build caught

**A published figure that is wrong in the secondary sources.** Vendor and
trade-press write-ups of the Sentinel-1 bracket say "40% weight reduction"
and "30% above stiffness requirement". **ESA's own caption gives 1.4 kg →
0.94 kg, which is 32.9%**, and says only "improved stability" with no figure.
The reel uses ESA's numbers and says "a third lighter". The 40% and the 30%
appear nowhere, in the voice or on screen.

**Three plates that computed the truth and drew it badly** — the support
hatching was not clipped to its band and swept across the whole design
volume; `evolve.png`'s last two iterates were visually identical because SIMP
converges fast; and `damage.png` plotted strain energy, which concentrates
into a few elements when a path is severed and washed the rest of the part
away, so the panel stopped reading as *a bracket with a hole in it*.

**A patch script that reported nothing and wrote nothing.** Its third
substitution asserted out because an earlier edit had changed the surrounding
text; the file was never written, and the next command reported "syntax OK" on
the unmodified file. Same failure mode as Eps. 09 and 10. Any patch of this
shape needs its assertions checked *and* its output confirmed.

**Twelve defects no gate caught**, plus one GATE V caught after compile, plus
three pacing findings. All in `_qc/VISUAL-QC.md`. The two worth repeating:
B06's comparison bars were drawn **with their meaning inverted** (shorter =
stiffer, so the winner had the shorter bar), and B10's legend **named the
wrong line**. Neither is reachable by any geometric check.

---

## Pacing

Every scene is a `Paced` subclass: a run-time multiplier, a per-reveal hold,
and a `hold_to_beat()` tail that pads to the measured narration.
`TAIL_TRIM = 0.18` is subtracted from every target because `renderer.time`
under-reports the rendered length.

All 20 clips landed **−0.19 to −0.22 s** under their beats. Three findings got
them there, the structural one being that **the solve runs once, in landscape,
and eight of ten scenes do a different number of plays in portrait.** Seven
are shorter there, which the tail absorbs; B04 is longer and overshot by
+0.92 s until it was given an aspect-specific RT. A scene already sitting on
the 0.35 s floor cannot be fixed by more trim — only by lowering RT.

Undershoot is safe and overshoot is not: `compile.py` pads a short clip by
holding its last frame, which is invisible, but centre-cuts a long one, which
would clip the closing line off both ends.

---

## Aspect discipline

`scenes.py` renders both cuts from one source. Manim keeps `frame_height =
8.0` either way, so the vertical band plan is identical and only the
horizontal extent changes — x ±6.15 landscape, ±1.80 portrait.

**Portrait is not a crop.** It has less usable area, so it carries fewer
elements, larger. The rule, unchanged since Ep. 08: *anything the narration
speaks stays on screen; the on-screen-only extras are what portrait loses.*
The two-panel comparisons ship in **both arrangements** — `shapes`/`damage`
side by side, `shapes_v`/`damage_v` stacked — because a 4:1 image squeezed
into portrait's 3.44 units is 0.84 units tall and the truss is unreadable.

Portrait remains the stricter aspect, and its failures are the subtler kind:
this episode's worst portrait defect was a label printed straight across the
bracket, which GATE B passed because a plate is an `ImageMobject`, not a curve.

---

## Reproducing this reel

```bash
PY=.venv/Scripts/python.exe            # a Windows venv has no python3.exe
R=<this folder>

$PY assets/gen_struct.py --force       # plates; asserts three claims
$PY runtime/scripts/generate_audio_kokoro.py "$R"     # needs GATE P signed
$PY -m manim -qk --fps 24 -r 3840,2160 scenes.py <Scene>   # one at a time
$PY -m manim -qk --fps 24 -r 2160,3840 scenes.py <Scene>
$PY runtime/scripts/remotion_scenes.py "$R"
$PY runtime/scripts/compile.py "$R" --height 2160
$PY runtime/qc/final_frame_check.py "$R" \
   --mp4 "$R/claude-for-astronomy_OmMali_02_10_2026.mp4"
```

The 9:16 cut is built the same way through `shorts.py --drop --no-endcard`,
with the portrait clips staged into `short/manim/` and `--height 3840`.

**Pass `--mp4` explicitly to the frame check. Always.** And re-render the
plates with `--force` after changing anything in `topo.py`: `gen_struct.py`
caches the optimisations in `assets/.cache_struct.npz`, and the cache does not
know the physics changed.
