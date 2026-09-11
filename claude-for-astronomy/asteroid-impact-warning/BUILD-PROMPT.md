# BUILD-PROMPT — rebuild *The Number Went Up.* from this folder

Ep. 08 · `asteroid-impact-warning`. Everything below is free and local. **No API
keys.** If any step appears to want one, stop — that is a toolkit bug, not a
missing credential (CLAUDE.md rule 7).

## Paths

```
TOOLKIT=E:/NEU/Jobs/Humanitarians_AI/brutalist.art          # brutalist.art — the DOT tree
REEL=D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/asteroid-impact-warning
PY="$TOOLKIT/.venv/Scripts/python.exe"
```

`brutalist.art` (dot) is **not** `brutalist-art/` or `brutalist_art/`. The
separator is never a typo.

## Two Windows preambles — both required, every invocation

```bash
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
```

Without these, `run.sh` and the Python scripts die on cp1252 as soon as
narration carries typographic punctuation.

**And call `$PY` explicitly — never `python3`.** Putting `.venv/Scripts` on
`PATH` is not enough: a Windows venv ships `python.exe` but no `python3.exe`, so
`python3` falls through to the system Python, which has none of the toolkit's
dependencies. That is what made the first audio run fail with
`pip install kokoro-onnx`.

## Hard rule: render one Manim process at a time

**Two Manim processes writing into one reel folder corrupt each other's
output.** The concat step silently drops frames — on Ep. 07 a 7.51 s beat came
out 7.083 s with all fourteen of its partial movie files summing to exactly the
right 180 frames. Do not parallelise the two aspects.

After killing a render job, **check mtimes for monotonicity**, not just
durations: `TaskStop` kills the shell, not the Manim child, and an orphan will
keep dropping files into `manim/` that the next run skips as "already filled".

## Rebuild

### 0. Plates (only if you change the physics or the seed)

```bash
cd "$REEL" && "$PY" assets/gen_neo.py        # seed 8801 → assets/plots/
rm -rf media/videos                          # REQUIRED — see the note at the end
```

Needs numpy, scipy and Pillow. **No matplotlib** — the venv does not ship it,
and PIL draws these plots fine.

The script prints its own diagnostics and **asserts its own physics**. Expect:

```
b_cap=8352 km = 1.311 R_E
peak P=3.86% at sigma/d=0.78
PASS: converged to 0.7063 vs predicted 0.7071 (delta -0.0008)
```

On failure it raises `SystemExit` and writes nothing. **If that check fails,
the physics is wrong — fix it, do not loosen the tolerance.** It has already
caught two errors in my derivation; see `PROMPTS.md`.

### 1. GATE P — the human signs

`PEDAGOGY.md` must contain `VERDICT: PASS` (as a substring — `PASSED` works)
with a signature. **Do not write that string anywhere else in the file**,
including in prose explaining the gate: `generate_audio_kokoro.py` opens on a
plain substring match anywhere in the document, so describing the gate unlocks
it.

### 2. Audio — the master clock

```bash
cd "$TOOLKIT" && "$PY" runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Kokoro `af_bella`, local, $0.00. Writes `mp3/beat-B*.mp3` + `mp3/timings.json`
and stamps `actual_duration_s` per beat. Expect **158.5 s**. No `--speed` flag
is needed. Never adjust timing by hand.

Budget a margin under the 3:00 cap because **the words-only prediction is noisy
in both directions** — Ep. 06 +10.4%, Ep. 07 −0.4%, Ep. 08 −5.0%. Do not assume
it under-predicts; I did, and it over-predicted.

### 3. Pacing (only if the narration changed)

```bash
"$PY" $SCRATCH/nat8.py     # per-scene natural length, no render
"$PY" $SCRATCH/pace8.py    # solves RT/HOLD and writes them into scenes.py
```

Then verify cheaply before spending 4K time, **both aspects**:

```bash
cd "$REEL"
for S in B01_Presenter … B10_TheTell; do
  "$PY" -m manim -ql --fps 24 --disable_caching scenes.py "$S"          # landscape
  "$PY" -m manim -ql --fps 24 --disable_caching -r 480,854 scenes.py "$S"  # portrait
done
```

Compare each against its beat. Two things to know:

- A scene whose body finishes under its beat will **not respond to `RT` at
  all** — `hold_to_beat()` pins it to the target regardless.
- A residual undershoot of ~0.1 s is frame quantisation inside `play()` and is
  **not** fixable by raising `HOLD` (a larger HOLD raises `renderer.time` and
  `hold_to_beat` shortens the tail by the same amount). Leave it: undershoot is
  padded with a held frame, overshoot is centre-cut and would clip the closer.

### 4. Gates F · L · A · W

**`run.sh` skips F, A and W on this reel.** All three are guarded on
`[ -n "$PENDING" ]`, and `PENDING` is empty because `run.sh` finds scenes with
`class (\w+)\(Scene\)` while every scene here subclasses `Paced`. Run them
directly:

```bash
cd "$REEL"
for f in FACTCHECK.md SHOTLIST.md PROMPTS.md; do test -f "$f" || echo "GATE F: missing $f"; done
"$PY" $TOOLKIT/runtime/qc/beat_lint.py beat_sheet.json
for S in B01_Presenter … B10_TheTell; do
  "$PY" $TOOLKIT/runtime/qc/static_scene_check.py scenes.py --class "$S" --quiet
  "$PY" $TOOLKIT/runtime/qc/wcag_margin_check.py  scenes.py --class "$S" --quiet
done
```

`rc>=2` is a failure, `rc==1` a warning. Expect `rc=0` throughout.

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

**Verify every render before slotting it** — that check is what catches dropped
frames, and GATE V cannot:

```
-0.25 s <= (ffprobe duration - actual_duration_s) <= +0.05 s   else re-render
frames / 24 == duration                                        else the concat dropped frames
```

The asymmetric tolerance is deliberate (§ 3). Expect a worst case of −0.100 s.

### 6. GATE B — pixel-true layout, both aspects

```bash
cd "$REEL"
for S in B01_Presenter … B10_TheTell; do
  "$PY" $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict
  "$PY" $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict --portrait
done
```

Expect 20 × `rc=0`. **`layout_audit.md` is overwritten by every run** — copy it
per scene if you need to read more than the last one. Portrait is much the
stricter aspect: it failed 8/10 on this reel's first pass where landscape
failed 1/10.

### 7. 16:9 — Remotion bookends, then compile

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/remotion_scenes.py "$REEL"        # FOREGROUND (rule 5) — B00 B11 B12 B13
"$PY" runtime/scripts/compile.py "$REEL" --height 2160  # → asteroid-impact-warning.mp4
"$PY" runtime/qc/final_frame_check.py "$REEL"           # GATE V
```

The four Remotion renders are the slow, memory-hungry step (~15 min; B12 is the
longest at 16.2 s). On Ep. 07 they left 1.1 GB free of 31.7 GB and the harness
killed `run.sh`'s wrapper. If that happens the child `compile.py` usually
survives and finishes — check `*.mp4` mtimes and carry on from `compile.py`
rather than restarting the pass.

Add `--review` for the beat-marked cut (`…-slate.mp4`). Omit it for the
master — `compile.py` refuses to write a clean master carrying any slate.

### 8. 9:16 — full length, no beats cut

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/shorts.py "$REEL" --drop --no-endcard --handle "@HumanitariansAI"
cp "$REEL"/_portrait/B*.mp4 "$REEL"/short/manim/
cp "$REEL"/scenes.py "$REEL"/short/scenes.py
"$PY" runtime/scripts/remotion_scenes.py "$REEL/short"        # 4 × …916 at 2160×3840
"$PY" runtime/scripts/compile.py "$REEL/short" --height 3840
"$PY" runtime/qc/final_frame_check.py "$REEL/short"
cp "$REEL"/short/asteroid-impact-warning-short.mp4 "$REEL"/asteroid-impact-warning-9x16.mp4
```

`--drop` with **no arguments** means "drop nothing"; `--no-endcard` ends on B13.
Together they give a full-length 2:38.5 portrait cut with all 14 beats.

`compile.py` will warn `SKIN LINT: B00 … wants ClaudeComposerAsk` and
`B13 … wants ClaudeTitleOutro`. **Both are expected** — the linter checks
composition names against COLD OPEN LAW and OUTRO LAW and does not know
`shorts.py`'s ONDA CHECK deliberately rewired them to the `916` variants.

### 9. Look at the frames

Read `_qc/contact_sheet.png` and `short/_qc/contact_sheet.png`. **The sheet
carries only 16 of the 28 sampled frames**, so sample the tail yourself —
B08 through B13 in both aspects, which is the whole verdict / handoff / outro
run. Sample *late* in each beat: a pale element mid-`FadeIn` looks exactly like
a rendering defect.

And read the finished frame of every Manim scene at 480p in both aspects before
committing to 4K. Five real defects in this build were invisible to every gate,
including a plate that sat over the title. See `_qc/VISUAL-QC.md`.

If a position looks wrong, **measure it** — anything placed with `next_to()` has
a y that depends on its neighbour's rendered height, and guessing at those is
what put a caption under a chip here.

## Toolkit patches this reel depends on

Both are fixes in `$TOOLKIT`, already applied, needed by any reel:

1. `runtime/scripts/shorts.py` — `link_or_copy()` falls back to `shutil.copy2`
   when `Path.symlink_to` raises `OSError 1314` (Windows without
   `SeCreateSymbolicLinkPrivilege`). Without it `shorts.py` cannot run at all.
2. `runtime/remotion/src/scenes/ClaudeVerdictArtifact916.tsx` and
   `ClaudeTitleOutro916.tsx` — rescaled from 42% and 19% canvas fill to ~79%
   (done for Ep. 07). This reel needed no further work on them.

## Still unpatched upstream

- `run.sh` does not export UTF-8 and crashes on cp1252 (§ preamble).
- `run.sh`'s scene-discovery regex matches `(Scene)` only, so it silently skips
  GATE F, A and W on any reel whose scenes subclass a base class (§ 4).
- **`scripts/type_check.py` (GATE T) does not exist.** SKILL.md calls it
  "ALWAYS RUN" and a hard block on `./art run` and `./art final`; the script is
  not shipped and no such gate is wired. GATE SHARPNESS likewise. §8.1/§8.3 are
  covered by GATE W and §8.2/§8.5 by GATE B; §8.4 kerning and §8.6 golden
  strings are covered by nothing automated.
- `generate_audio_kokoro.py` opens GATE P on a plain substring match (§ 1).

## Never

- Never publish. There is no publishing machinery here; the masters stay in
  this folder.
- Never hand-roll `npx remotion render` — go through `remotion_scenes.py`.
- Never fix timing by hand. Regenerate audio and recompile.
- Never re-render a plate without `rm -rf media/videos` first: Manim's cache key
  hashes scene *code* and does not hash the contents of images the scene loads,
  so a retuned plate will not invalidate anything.
