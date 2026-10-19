# BUILD-PROMPT — rebuild *The Same Sunspot, Twice.* from this folder

Ep. 12 · `predicting-solar-storms`. Everything below is free and local. **No API
keys.** If any step appears to want one, stop — that is a toolkit bug, not a
missing credential (CLAUDE.md rule 7).

## Paths

```
TOOLKIT=E:/NEU/Jobs/Humanitarians_AI/brutalist.art          # brutalist.art — the DOT tree
REEL=D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/predicting-solar-storms
PY="$TOOLKIT/.venv/Scripts/python.exe"
```

`brutalist.art` (dot) is **not** `brutalist-art/` or `brutalist_art/`.

## Two Windows preambles — both required, every invocation

```bash
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
```

Without these the Python scripts die on cp1252 as soon as narration carries
typographic punctuation.

**And call `$PY` explicitly — never `python3`.** A Windows venv ships
`python.exe` but no `python3.exe`, so `python3` falls through to the system
Python, which has none of the toolkit's dependencies. That is what made Ep. 08's
first audio run fail with `pip install kokoro-onnx`.

## Hard rule: render one Manim process at a time

**Two Manim processes writing into one reel folder corrupt each other's
output** — the concat step silently drops frames (Ep. 07: a 7.51 s beat came out
7.083 s with all fourteen partial files summing to exactly the right count). Do
not parallelise the aspects. After killing a render job, **check mtimes for
monotonicity**: `TaskStop` kills the shell, not the Manim child.

## Rebuild

### 0. Plates (only if you change the physics or the seed)

```bash
cd "$REEL" && "$PY" assets/gen_solar.py --force   # → assets/plots/
rm -rf media/videos                          # REQUIRED — see the note at the end
```

numpy and Pillow. **No sklearn** -- both models are written out: a
class-weighted logistic regression and a k-nearest-neighbour. They are chosen
to differ on exactly one axis, CAPACITY, because that is what converts a
repeated unit into an inflated score.

**Seed 1212.** 12 repeats; every headline number is a MEDIAN, with the full
spread drawn in `spread.png`. The optimisations and the sweep are cached in
`assets/.cache_solar.npz`, so pass `--force` after editing `flares.py` or the
cache will restyle plates computed from the old model.

The script **asserts three claims** and writes nothing if any fails. Expect:

```
rows 20228  regions 350  base rate 1 in 58
split random   test regions also seen in training: 100.0%
split region   test regions also seen in training:   0.0%
1. RANDOM split   baseline 0.356   flexible 0.484   -> flexible wins by +0.128
2. BY-REGION      baseline 0.374   flexible 0.121   -> flexible loses by -0.253
3. control: inflation at fingerprint 0.00 = +0.000, at 1.00 = +0.306
```

**If an assertion fails, rewrite the CLAIM -- do not loosen the tolerance.**
Three traps worth knowing before you touch it:

- **Do not let the within-region drift exceed the fingerprint.** A real
  active region's parameters barely move hour to hour, which is exactly why
  its rows are near-duplicates. A first version used sigma 0.12/hour on a
  unit fingerprint; over a 72-hour lifetime the walk wandered further than
  the fingerprint itself, rows of one region stopped being alike, and the
  leak -- the whole subject -- was simulated away. It showed up as a
  nearest-neighbour distance of 0.18 under EVERY split.
- **k has to be large enough to estimate a region's RATE.** At k=5 the
  flexible model was simply worse than logistic regression under every split,
  so its inflation was the inflation of a bad number and proved nothing.
  k=25 makes it genuinely competitive when evaluated honestly, which is the
  situation the episode is about.
- **Calibrate the threshold on NOISE, not on interference.** Otherwise it
  tracks the brightest interference line and nothing can exceed it.

### 1. GATE P — the human signs

`PEDAGOGY.md` must contain `VERDICT: PASS` (as a substring) with a signature.
**Do not write that string anywhere else in the file**, including in prose
explaining the gate: `generate_audio_kokoro.py` opens on a plain substring
match anywhere in the document.

### 2. Audio — the master clock

```bash
cd "$TOOLKIT" && "$PY" runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Kokoro `af_bella`, local, $0.00. Expect **142.1 s** (2:22.1). No `--speed`
needed — 38 s of headroom under the cap.

Budget margin under the 3:00 cap because **the words-only prediction is noise of
order ±5–10% with no consistent sign**: Ep. 06 +10.4%, Ep. 07 −0.4%, Ep. 08
−5.0%, Ep. 09 +2.7%, Ep. 10 −8.2%, Ep. 11 +3.3%, Ep. 12 −0.1%. Do not assume a direction.

### 3. Pacing (only if the narration changed)

```bash
"$PY" $SCRATCH/nat12.py     # per-scene natural length, no render
"$PY" $SCRATCH/pace12.py    # solves RT/HOLD and writes them into scenes.py
"$PY" $SCRATCH/natboth12.py # natural length in BOTH aspects - see below
```

Then verify at **24 fps** — the real frame rate — in **both aspects**:

```bash
cd "$REEL"
for S in B01_Presenter … B10_TheTell; do
  "$PY" -m manim -ql --fps 24 --disable_caching scenes.py "$S"
  "$PY" -m manim -ql --fps 24 --disable_caching -r 480,854 scenes.py "$S"
done
```

Accept `−0.25 s … +0.05 s`. The asymmetry is the point: a short clip is padded
with a held frame (invisible), a long one is **centre-cut** and loses the
closing line off both ends.

Three things to know:

- `hold_to_beat` subtracts a module-level **`TAIL_TRIM = 0.18`**, because
  `renderer.time` under-reports the true rendered length (each play's frame
  count rounds up, and the error grows with the number of reveals).
- A residual undershoot **cannot** be fixed by lowering `RT` or `HOLD` — a
  smaller body raises `target − now` by the same amount and the total does not
  move. Only the trim, or a scene short enough to hit the 0.35 s floor, changes
  it.
- **The lever is always RT.** A per-scene trim override was built and tried
  on FOUR scenes across two episodes -- Ep. 11's B01 and B07, Ep. 12's B07 and
  B09 -- and moved the measured duration by exactly zero every time, because
  `target - trim - now` was already below the 0.35 s floor in all four. Once
  the wait is floored the total is just `body + floor`, and only a smaller
  body changes it. A scene landing above -0.15 s is floored: lower its RT.
- **If RT is already at the 1.55 cap**, raise HOLD instead; that also grows
  the body. Ep. 13's B06 needed this.
- **The solve runs ONCE, in landscape.** `natboth12.py` measures both aspects
  and flags scenes whose portrait branch does a different number of plays.
  Scenes that are SHORTER in portrait are safe -- the tail pads them. Only a
  scene that is LONGER in portrait needs its own multiplier, as Ep. 11's B04
  did.

### 4. Gates F · L · A · W

**`run.sh` skips F, A and W on this reel** — all three are guarded on
`[ -n "$PENDING" ]`, and `PENDING` is empty because `run.sh` finds scenes with
`class (\w+)\(Scene\)` while every scene here subclasses `Paced`.

```bash
cd "$REEL"
for f in FACTCHECK.md SHOTLIST.md PROMPTS.md; do test -f "$f" || echo "GATE F: missing $f"; done
"$PY" $TOOLKIT/runtime/qc/beat_lint.py beat_sheet.json
for S in B01_Presenter … B10_TheTell; do
  "$PY" $TOOLKIT/runtime/qc/static_scene_check.py scenes.py --class "$S" --quiet
  "$PY" $TOOLKIT/runtime/qc/wcag_margin_check.py  scenes.py --class "$S" --quiet
done
```

### 5. Manim, 4K, both aspects — sequentially

```bash
cd "$REEL"; mkdir -p manim _portrait
for S in B01_Presenter … B10_TheTell; do
  BID="${S%%_*}"
  "$PY" -m manim -qk --fps 24 --disable_caching -r 3840,2160 scenes.py "$S"
  cp "media/videos/scenes/2160p24/$S.mp4" "manim/$BID.mp4"
done
for S in B01_Presenter … B10_TheTell; do
  BID="${S%%_*}"
  "$PY" -m manim -qk --fps 24 --disable_caching -r 2160,3840 scenes.py "$S"
  cp "media/videos/scenes/3840p24/$S.mp4" "_portrait/$BID.mp4"
done
```

**Verify every render before slotting it:**

```
-0.25 s <= (duration - actual_duration_s) <= +0.05 s   else re-render
frames / 24 == duration                                else the concat dropped frames
```

### 6. GATE B — pixel-true layout, both aspects

```bash
for S in B01_Presenter … B10_TheTell; do
  "$PY" $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict
  "$PY" $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict --portrait
done
```

Expect 20 × `rc=0`. **`layout_audit.md` is overwritten by every run** — copy it
per scene to read more than the last.

**Size every plate to its band before rendering.** `ph = pw × (ih/iw)` and
the landscape figure band is 4.30 units. The seven plates are `regions`
1560×740 (0.474), `split` 1550×700 (0.452), `nearest` 1560×700 (0.449),
`scores` / `spread` / `control` 1560×780 (0.500), and the stacked portrait
variant `split_v` 760×830 (1.092). **Ep. 12 put a 4.79-unit plate in the
4.30-unit band** and a label landed at y 3.54, above the title.

**The two-panel comparison ships in BOTH arrangements.** At portrait's 3.44
units each panel of `split.png` is 1.7 across and the dots -- which ARE the
plate -- vanish, so portrait loads `split_v.png`.

### 7. 16:9 — Remotion bookends, then compile

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/remotion_scenes.py "$REEL"        # FOREGROUND (rule 5)
"$PY" runtime/scripts/compile.py "$REEL" --height 2160  # → predicting-solar-storms.mp4
"$PY" runtime/qc/final_frame_check.py "$REEL" \\
      --mp4 "$REEL/claude-for-astronomy_OmMali_09_10_2026.mp4"   # ALWAYS --mp4
```

The four Remotion renders are the slow, memory-hungry step (~15 min). On Ep. 07
they left 1.1 GB free of 31.7 GB and the harness killed `run.sh`'s wrapper; the
child `compile.py` usually survives, so check mtimes and carry on from there.

### 8. 9:16 — full length, no beats cut

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/shorts.py "$REEL" --drop --no-endcard --handle "@HumanitariansAI"
cp "$REEL"/_portrait/B*.mp4 "$REEL"/short/manim/
cp "$REEL"/scenes.py "$REEL"/short/scenes.py
"$PY" runtime/scripts/remotion_scenes.py "$REEL/short"
"$PY" runtime/scripts/compile.py "$REEL/short" --height 3840
"$PY" runtime/qc/final_frame_check.py "$REEL/short" \\
      --mp4 "$REEL/short/predicting-solar-storms-short.mp4"
cp "$REEL"/short/predicting-solar-storms-short.mp4 "$REEL"/predicting-solar-storms-9x16.mp4
```

**`final_frame_check.py` given only a folder takes `glob("*.mp4")[0]`**, which
is whichever filename happens to sort first. Against the build-time name it
picks the WRONG one: `predicting-solar-storms-9x16.mp4` beats
`predicting-solar-storms.mp4` because `-` precedes `.`, which is how
Ep. 10 lost a re-render to a phantom regression. Against the delivered name it
happens to pick the right one, because `claude-` beats `generative-`. **Do not
rely on either: always pass `--mp4`**, and copy the reports to aspect-suffixed
names, because the gate overwrites `_qc/REPORT.md` and
`_qc/contact_sheet.png` on every run.

**The 16:9 master is renamed on delivery** to
`claude-for-astronomy_OmMali_DD_MM_YYYY.mp4` with that week's release date;
the 9:16 keeps the slug. `compile.py` writes `<slug>.mp4`, so the rename is a
manual step.

Two expected SKIN LINT warnings (`B00 … wants ClaudeComposerAsk`, `B13 … wants
ClaudeTitleOutro`): the linter checks composition *names* and does not know
`shorts.py`'s ONDA CHECK rewired them to the `916` variants.

### 9. Look at the frames — this is where the real defects are

Read `_qc/contact_sheet.png` and `short/_qc/contact_sheet.png`, then **sample
the tail yourself** — the sheet carries only 16 of 28 frames, and B08–B13 is the
whole verdict / handoff / outro run. Sample *late* in each beat: a pale element
mid-`FadeIn` looks exactly like a rendering defect.

And read the finished frame of **every** Manim scene at 480p in **both** aspects
before committing to 4K. **Twelve defects in this build were invisible to
every gate**, plus one GATE V caught only after the compile. Three specific
habits:

- **Ask whether the picture says what the beat says.** B06's comparison bars
  were drawn from compliance, where shorter means stiffer — so the winning
  design had the SHORTER bar and the chart argued the opposite of the
  narration. B10's legend named the wrong curve. No geometric check reaches
  either.
- **A gap of 0.04 units is eleven pixels at 4K, and eleven pixels reads as
  contact.** Four of the twelve were sub-0.08-unit gaps that GATE B scores as
  non-intersecting. Leave >= 0.15 between any two elements.
- **A plate is an `ImageMobject`, not a curve**, so GATE B will not flag a
  label printed across it. B06 portrait shipped "the optimiser's answer"
  straight over the bracket until the frame was read.
- **Never use a glyph outside the font's coverage.** `✓` is absent from EB
  Garamond and Ep. 09 shipped it as stray digits. Draw marks from `Line`s.
- **Measure anything placed with `next_to()`** — its y depends on its
  neighbour's rendered height, and guessing is what put a caption under a chip
  here and in Ep. 08.

## Toolkit patches this reel depends on

Already applied, needed by any reel:

1. `runtime/scripts/shorts.py` — `link_or_copy()` falls back to `shutil.copy2`
   when `Path.symlink_to` raises `OSError 1314`. Without it `shorts.py` cannot
   run on Windows.
2. `ClaudeVerdictArtifact916.tsx` / `ClaudeTitleOutro916.tsx` — rescaled from
   42% and 19% canvas fill to ~79% (Ep. 07). No further work needed.

**Write the verdict card with FIVE lines, not four.** GATE V measures the
content bounding box against the title-safe area and wants >= 55%; a four-line
`ClaudeVerdictArtifact` sits almost exactly on that line and the verdict flips
on encoder noise (Ep. 10). Five clears it, and gives the recap room to state
the cost — which an episode about quantifying a cost ought to do on the page a
viewer can pause.

**Give every scene its footer EARLY.** GATE V samples each beat at 50% and
85% of its span. B01 is the one scene that does not call `chrome()`, and with
its citation and brand bug landing last, the content bbox covered only the top
half of the frame for most of the beat — 44% fill, a MAJOR. Moving the footer
into the header fixed it without changing the play count or the duration.

## Still unpatched upstream

- `run.sh` does not export UTF-8 and crashes on cp1252.
- `run.sh`'s scene-discovery regex matches `(Scene)` only, so it silently skips
  GATE F, A and W on any reel whose scenes subclass a base class.
- **`scripts/type_check.py` (GATE T) does not exist.** SKILL.md calls it
  "ALWAYS RUN" and a hard block on `./art final`. §8.1/§8.3 are covered by
  GATE W and §8.2/§8.5 by GATE B; **§8.4 (kerning / font coverage) and §8.6
  (golden strings) are covered by nothing** — Ep. 09's missing `✓` glyph was
  exactly a §8.4 defect that reached a rendered frame.
- `generate_audio_kokoro.py` opens GATE P on a plain substring match.

## Never

- Never publish. The masters stay in this folder.
- Never hand-roll `npx remotion render` — go through `remotion_scenes.py`.
- Never fix timing by hand. Regenerate audio and recompile.
- Never re-render a plate without `rm -rf media/videos` first: Manim's cache key
  hashes scene *code*, not the contents of images a scene loads.
