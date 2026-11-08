# BUILD-PROMPT — rebuild *Aim Where It's Going.* from this folder

Ep. 16 · `predictive-adaptive-optics`. Everything below is free and local.
**No API keys.** If any step appears to want one, stop — that is a toolkit bug,
not a missing credential (CLAUDE.md rule 7).

## Paths

```
TOOLKIT=E:/NEU/Jobs/Humanitarians_AI/brutalist.art          # brutalist.art — the DOT tree
REEL=D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/predictive-adaptive-optics
PY="$TOOLKIT/.venv/Scripts/python.exe"
```

`brutalist.art` (dot) is **not** `brutalist-art/` or `brutalist_art/`. The
separator is never a typo.

## Two Windows preambles — both required, every invocation

```bash
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
```

Without these the Python scripts die on cp1252 as soon as narration carries
typographic punctuation.

**And call `$PY` explicitly — never `python` or `python3`.** The system Python
on this machine has none of the toolkit's dependencies; that is what made the
first audio run of this episode fail with `pip install kokoro-onnx` even
though Kokoro was installed. Putting `.venv/Scripts` on PATH is not enough —
a Windows venv ships `python.exe` but no `python3.exe`.

## Hard rule: render one Manim process at a time

**Two Manim processes writing into one reel folder corrupt each other's
output.** The concat step silently drops frames. Do not parallelise the two
aspects.

## Rebuild

### 0. Plates (only if the physics or the seed changes)

```bash
cd "$REEL" && "$PY" assets/gen_ao.py      # seed 1616 → assets/plots/
rm -rf media/videos                        # REQUIRED — see the note at the end
```

Needs numpy, scipy and Pillow. **No matplotlib** — PIL draws these plates.

The script **asserts eight claims and writes no plate if any fails**:

```
  translation operator is exact                  ok   rel err 2.2e-07
  Kolmogorov lag exponent is 5/3                 ok   1.666667
  sigma^2(tau0) = 1 rad^2                        ok   0.9972 rad^2
  screens reproduce the spectral integral        ok   ratio 1.0205
  in-band lag error goes as tau^2, not tau^(5/3) ok   1.990
  prediction still wins at realistic noise       ok   11.20x (1 layer) 4.82x (3 layers)
  more layers cost the predictor                 ok   11.20 > 5.24 > 4.82
  looking BACK beats looking ACROSS              ok   L1 5.1/1.2  L2 3.7/1.0  L3 3.7/1.1
```

**If one fails, the physics is wrong — fix it, do not loosen the tolerance.**
These asserts already caught two errors in my own derivation (a spurious √2
and a sign error in the sub-pixel shift). `--cache DIR` reuses modal telemetry.

### 1. GATE P — the human signs

`PEDAGOGY.md` must carry a signed `VERDICT: PASS`. The checker takes the
**first** VERDICT token on any line and requires that one to say PASS, so
prose explaining the gate no longer unlocks it (the old plain-substring bug).

### 2. Audio — the master clock

```bash
cd "$TOOLKIT" && "$PY" runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Kokoro `af_bella`, local, $0.00. Writes `mp3/beat-B*.mp3` + `mp3/timings.json`
and stamps `actual_duration_s` per beat. Expect **160.8 s**. Never adjust
timing by hand.

### 3. Pacing (only if the narration changed)

```bash
"$PY" $SCRATCH/nat16.py     # natural length per scene, BOTH aspects, no render
"$PY" $SCRATCH/pace16.py    # solves RT/HOLD + RT_PORTRAIT into scenes.py
```

`nat16.py` measures both aspects because **five scenes play fewer reveals in
portrait**; solving once in landscape would leave them frozen for seconds.
`pace16.py` caps `RT_PORTRAIT` at 2.00 — B04 wants 2.190 and is capped.

Then verify cheaply before spending 4K time, **both aspects**:

```bash
cd "$REEL"
for S in B01_Presenter … B10_TheTell; do
  "$PY" -m manim -ql --fps 24 --disable_caching scenes.py "$S"             # landscape
  "$PY" -m manim -ql --fps 24 --disable_caching -r 480,854 scenes.py "$S"  # portrait
done
```

A scene whose body finishes under its beat will **not respond to RT at all** —
`hold_to_beat()` pins it to the target regardless. A residual ~0.2 s undershoot
is frame quantisation and is **not** fixable by raising HOLD. Leave it.

### 4. Gates F · L · A · W

`run.sh` **skips F, A and W on this reel** (its scene-discovery regex matches a
direct `Scene` subclass; every scene here subclasses `Paced`). Run them
directly:

```bash
cd "$REEL"
for f in FACTCHECK.md SHOTLIST.md PROMPTS.md SOURCES.md PEDAGOGY.md; do
  test -f "$f" || echo "GATE F: missing $f"; done
"$PY" $TOOLKIT/runtime/qc/beat_lint.py beat_sheet.json
for S in B01_Presenter … B10_TheTell; do
  "$PY" -I $TOOLKIT/runtime/qc/static_scene_check.py scenes.py --class "$S"
  "$PY" -I $TOOLKIT/runtime/qc/wcag_margin_check.py  scenes.py --class "$S" --palette claude
done
```

`static_scene_check.py` **requires `--class`** — without it it looks for
`BearsDoodlesVideo` and reports "not found", which is not a pass.

### 5. GATE B — pixel layout, both aspects, WITH `--curve-strict`

```bash
for S in B01_Presenter … B10_TheTell; do
  "$PY" -I $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict
  "$PY" -I $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict --portrait
done
```

**Do not omit `--curve-strict`.** This build's first GATE B pass did, and it
had to be re-run. Expect 20 × CLEAN. `layout_audit.md` is **overwritten by
every run** — read it inside the loop. Portrait is the stricter aspect;
it failed 2/10 here where landscape failed 0/10. Send stderr to `/dev/null`:
GLib-GIO spam will otherwise swamp the output.

### 6. Manim, 4K, both aspects — sequentially

```bash
cd "$REEL"; rm -rf media/videos; mkdir -p manim _portrait
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

**Verify every render before slotting it** — this is what catches dropped
frames, and GATE V cannot:

```
-0.25 s <= (ffprobe duration - actual_duration_s) <= +0.05 s   else re-render
frames / 24 == duration                                        else the concat dropped frames
```

The asymmetric tolerance is deliberate (§ 3). Expect a worst case of −0.220 s.

### 7. 16:9 — Remotion bookends, then compile

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/remotion_scenes.py "$REEL"                 # B00 B11 B12 B13
"$PY" runtime/scripts/compile.py "$REEL" --height 2160           # → predictive-adaptive-optics.mp4
"$PY" runtime/qc/final_frame_check.py "$REEL" --mp4 "$REEL/predictive-adaptive-optics.mp4"
```

**Pass `--mp4` explicitly.** With two cuts in the reel root the frame check
otherwise picks a file by pattern and can silently grade the wrong one.

`compile.py` warns that `reveal` carries 50% of beats, over the ~40% pantry
cap. Expected here and recorded in `BUILD-LOG.md`, not silently cleared.

### 8. 9:16 — full length, no beats cut

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/shorts.py "$REEL" --drop --no-endcard --handle "@HumanitariansAI"
cp "$REEL"/_portrait/B*.mp4 "$REEL"/short/manim/
cp "$REEL"/scenes.py "$REEL"/short/scenes.py
cp -r "$REEL"/assets "$REEL"/short/assets
"$PY" runtime/scripts/remotion_scenes.py "$REEL/short"           # 4 × …916 at 2160×3840
"$PY" runtime/scripts/compile.py "$REEL/short" --height 3840
"$PY" runtime/qc/final_frame_check.py "$REEL/short" --mp4 "$REEL/short/predictive-adaptive-optics-short.mp4"
cp "$REEL"/short/predictive-adaptive-optics-short.mp4 "$REEL"/predictive-adaptive-optics-9x16.mp4
```

`--drop` with **no arguments** means "drop nothing"; `--no-endcard` ends on
B13. Together they give a full-length 2:40.8 portrait cut with all 14 beats.

`shorts.py` will print `ONDA CHECK` lines rewiring the four Remotion beats to
their `916` compositions. That is correct, and any pre-existing centre-cut
`media/<bid>-916.mp4` is stale and must be deleted.

### 9. Look at the frames — in BOTH cuts

Read `_qc/contact_sheet.png` and `short/_qc/contact_sheet.png`. **The sheet
carries only 16 of the 28 sampled frames**, so sample B08–B13 yourself from
each finished master — that is the whole budget / on-sky / tell / verdict /
handoff / outro run. Sample *late* in each beat: a pale element mid-`FadeIn`
looks exactly like a rendering defect.

**The one real defect in this build was found here and nowhere else**, and it
was string-dependent: a strikethrough that sat correctly on a word with a
descender and through the letter-tops on a word without one. If a position
looks wrong, **measure it** rather than squinting at a 480p frame.

### 10. Deliver

```bash
cd "$REEL"
mv predictive-adaptive-optics.mp4 claude-for-astronomy_OmMali_06_11_2026.mp4
```

The dated name is the series convention (weekly Thursdays; Ep. 15 was
`30_10_2026`) and **nothing in the toolkit does it** — check the sibling
episode folders before finishing. The 9:16 keeps the slug name.

## Toolkit patches this reel depends on

1. `runtime/scripts/shorts.py` — `link_or_copy()` falls back to `shutil.copy2`
   when `Path.symlink_to` raises `OSError 1314` (Windows without
   `SeCreateSymbolicLinkPrivilege`). Without it `shorts.py` cannot run at all.
2. `runtime/remotion/src/scenes/ClaudeVerdictArtifact916.tsx` and
   `ClaudeTitleOutro916.tsx` — rescaled from 42% and 19% canvas fill to ~79%
   (done for Ep. 07). This reel needed no further work on them.

## Still unpatched upstream

- `run.sh` does not export UTF-8 and crashes on cp1252.
- `run.sh`'s scene-discovery regex matches a direct `Scene` subclass only, so
  it silently skips GATE F, A and W on any reel using a base class (§ 4).
- **`scripts/type_check.py` (GATE T) does not exist.** SKILL.md calls it
  "ALWAYS RUN" and a hard block on `./art run` and `./art final`; the script is
  not shipped and no such gate is wired. GATE SHARPNESS likewise.
- `remotion_scenes.py`'s unknown-prop warning says the field will render with
  "that field's DEFAULT text", which is misleading when the component has no
  such field at all — as `ClaudeVerdictArtifact` does not. Check the component
  before chasing it.

## Never

- Never publish. There is no publishing machinery here; the masters stay in
  this folder.
- Never hand-roll `npx remotion render` — go through `remotion_scenes.py`.
- Never fix timing by hand. Regenerate audio and recompile.
- Never re-render a plate without `rm -rf media/videos` first: Manim's cache
  key hashes scene *code* and does not hash the contents of images the scene
  loads, so a retuned plate will not invalidate anything.
