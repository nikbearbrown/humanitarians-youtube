# BUILD-LOG — *The Same Sunspot, Twice.*

**AI in Astronomy & Space Science · Ep. 12** · slug `predicting-solar-storms`
Built with `brutalist.art` (the free-only Fellow Tier), skill `ai-explainer`,
channel `claude-hai`, Pragmatist register. Built 2026-10-09.

**Total spend: $0.00.** Kokoro TTS runs locally; every plate is computed
here; no API key was used or required at any step.

---

## What shipped

| | 16:9 | 9:16 |
|---|---|---|
| `claude-for-astronomy_OmMali_09_10_2026.mp4` | 3840 × 2160 · 142.13 s · 3411 frames · 15.6 MB | — |
| `predicting-solar-storms-9x16.mp4` | — | 2160 × 3840 · 142.13 s · 3411 frames · 16.4 MB |

24 fps, h264 + AAC, −21.1 LUFS integrated, both cuts sharing one audio mix.
**2:22.1** — 38 s inside the 3:00 cap. Both masters live in this folder.
Nothing was published.

---

## The episode

Topic 12 of the brief is ML forecasting of solar flares. The capability
version — the Sun is dangerous, the data is huge, here comes the classifier —
is true and is the thing most likely to mislead.

This is the first episode in the series **about the evaluation rather than
the system.** The model, the data and the objective can all be fine and the
number still be wrong, because of how the test set was built. It is the
earliest possible failure: it happens before deployment is a question, and it
decides whether anything else gets believed.

A sunspot region is measured every hour for days, so one region is dozens of
nearly identical rows, and whether a region flares is a property *of the
region*. Shuffle those rows before splitting and the same region lands on
both sides.

| median TSS, 12 runs | random split | by-region split |
|---|---|---|
| plain model | 0.356 | **0.374** |
| flexible model | **0.484** | 0.121 |

Under a random split **100% of test regions are also in training** (0% by
region), the nearest training row sits at distance 0.13 instead of 0.38, and
the flexible model wins. Split honestly and the ordering reverses: it loses
**three quarters** of its score while the plain model does not move. The
control settles the cause — remove the region fingerprint and the inflation
goes from **+0.31 to exactly zero**.

The fix costs nothing: split by region, not by row.

---

## Pipeline, in the order it ran

1. **Research** from primary sources → `SOURCES.md`, `FACTCHECK.md`.
2. **`assets/flares.py`** — the simulator, two models of deliberately
   different capacity, and TSS.
3. **`assets/gen_solar.py`** — the experiment, three asserted claims, seven
   plates, 12 repeats, medians throughout.
4. **`beat_sheet.json`** — 14 beats, 400 words.
5. **Paperwork** — SHOTLIST, PROMPTS, CHECKS-REPORT, PEDAGOGY.
6. **GATE P** — signed, Om Mali, 09/10/2026.
7. **Audio** — Kokoro `af_bella`, 14 MP3s totalling 142.1 s. **The master
   clock from here on.**
8. **Pacing solved without rendering**, then **verified at 24 fps in both
   aspects**.
9. **20 scenes rendered at 4K, one Manim process at a time**, each verified.
10. **Remotion bookends**, then `compile.py --height 2160`.
11. **GATE V**, then the 9:16 derivative, then GATE V again — each with an
    explicit `--mp4`.
12. **Both masters read frame by frame** → `_qc/VISUAL-QC.md`.

---

## Gate results

| Gate | Result |
|---|---|
| F — paperwork set | present |
| L — beat-mix lint | clean |
| A — static pre-flight | 10/10 `rc=0` (after 1 fix) |
| W — WCAG · margins · overlap | 10/10 `rc=0` |
| B — pixel layout, both aspects | 20/20 `rc=0`, after 6 fixes |
| P — human signature | PASSED, before audio |
| Pacing — 24 fps, both aspects | 20/20 inside `−0.25 s … +0.05 s` |
| V — 16:9 master | 28 frames · 0 BLOCKER · 0 MAJOR |
| V — 9:16 master | 28 frames · 0 BLOCKER · 0 MAJOR |
| Frame reading, both aspects | 8 further defects found and fixed |

**GATE T and GATE SHARPNESS were not run: they are not shipped in this
toolkit**, despite SKILL.md describing GATE T as "ALWAYS RUN".

---

## The experiment, and the two times it caught me

`gen_solar.py` asserts three claims and writes nothing if any fails.

1. **I simulated the leak away.** The first version used a within-region
   random walk of σ 0.12/hour on a unit fingerprint. Over 72 hours that walk
   wanders further than the fingerprint itself, so rows of one region ended
   up no more alike than rows of different regions — and the
   nearest-neighbour distance came out at 0.18 under *every* split, which is
   how it showed up. A real active region's parameters barely move hour to
   hour; that is exactly why its rows are near-duplicates.
2. **I inflated a bad number.** The second version used k=5, where the
   flexible model was simply worse than logistic regression under every split
   (0.16 against 0.31). Its "inflation" was then the inflation of a model
   nobody would ship. At k=25 it estimates a region's flare *rate* rather
   than echoing one neighbour's coin flip, and is genuinely competitive when
   evaluated honestly — which is the situation the episode is about.

Both were caught by reading the diagnostics rather than the headline.

---

## Other errors this build caught

**A published figure that most sources get wrong.** SpaceX's initial
announcement said up to **40** Starlink satellites were lost in February 2022
and the press repeated it. The peer-reviewed (*Space Weather*) and NASA
figure is **38 of 49**. The reel uses 38; the 40 appears nowhere. Same class
of correction as Ep. 11's ESA bracket, where the vendor's 40% was really 33%.

**Eight defects no gate caught**, two of which were regressions from my own
fixes. The recurring class: **GATE B cannot see anything that collides with
the contents of a plate**, because a plate is an `ImageMobject`, not a curve.
This reel would have shipped a card across a plot and a label across a curve.

**A pacing diagnosis that was wrong.** B09 landed at −0.01 s, one frame from
overshooting. I diagnosed a tail above the floor and rebuilt the per-scene
trim override; it moved nothing, because the scene was floored. RT was the
lever. The trim mechanism has now been tried on four scenes across two
episodes and moved the duration by exactly zero every time; it is gone, and
the chassis docstring says so.

**The 9:16 compile was killed twice by the low-memory reaper**, both times
mid-mux, leaving a stub with no `moov` atom. Nothing upstream was damaged
either time.

---

## Aspect discipline

`scenes.py` renders both cuts from one source. `frame_height = 8.0` either
way; only the horizontal extent changes — x ±6.15 landscape, ±1.80 portrait.

**Portrait is not a crop.** The two-panel split plate ships in both
arrangements (`split` side by side, `split_v` stacked) because at portrait's
3.44 units each panel would be 1.7 across and the dots — which *are* the
plate — would vanish.

The recurring portrait bug this time was arithmetic: a label positioned at
`pat[0] ± pw * k` lands inside the frame in landscape, where `pw` is 7 units,
and outside it in portrait, where `pw` is 3.4. **An offset scaled to the
plate is not an offset scaled to the safe area.**

---

## Reproducing this reel

```bash
PY=.venv/Scripts/python.exe            # a Windows venv has no python3.exe
R=<this folder>

$PY assets/gen_solar.py --force        # plates; asserts three claims
$PY runtime/scripts/generate_audio_kokoro.py "$R"     # needs GATE P signed
$PY -m manim -qk --fps 24 -r 3840,2160 scenes.py <Scene>   # one at a time
$PY -m manim -qk --fps 24 -r 2160,3840 scenes.py <Scene>
$PY runtime/scripts/remotion_scenes.py "$R"
$PY runtime/scripts/compile.py "$R" --height 2160
$PY runtime/qc/final_frame_check.py "$R" \
   --mp4 "$R/claude-for-astronomy_OmMali_09_10_2026.mp4"
```

The 9:16 cut is built through `shorts.py --drop --no-endcard`, with the
portrait clips staged into `short/manim/` and `--height 3840`.

**Pass `--mp4` explicitly to the frame check. Always.** And re-run the
generator with `--force` after changing `flares.py`: the optimisations and
the damage survey are cached in `assets/.cache_solar.npz`, and the cache does
not know the model changed.
