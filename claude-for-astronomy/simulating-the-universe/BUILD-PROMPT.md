# BUILD-PROMPT — rebuild *The Universe You Can Afford.* from this folder

Ep. 07 · `simulating-the-universe`. Everything below is free and local. **No API
keys.** If any step appears to want one, stop — that is a toolkit bug, not a
missing credential (CLAUDE.md rule 7).

## Paths

```
TOOLKIT=E:/NEU/Jobs/Humanitarians_AI/brutalist.art          # brutalist.art — the DOT tree
REEL=D:/study_other/new_humanitarians/humanitarians-youtube/claude-for-astronomy/simulating-the-universe
PY=$TOOLKIT/.venv/Scripts/python.exe
```

`brutalist.art` (dot) is **not** `brutalist-art/` or `brutalist_art/`. The
separator is never a typo.

## Windows preamble — every single invocation

```bash
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
export PATH="$TOOLKIT/.venv/Scripts:$PATH"
```

Without these, `run.sh` and the Python scripts die on cp1252 as soon as narration
carries typographic punctuation. Not yet patched in the toolkit.

## Hard rule for this reel: render one Manim process at a time

**Two Manim processes writing into one reel folder corrupt each other's output.**
The concat step silently drops frames — a 7.51 s beat came out 7.083 s with all
14 of its partial movie files summing to exactly the right 180 frames. Do not
parallelise the two aspects. See `BUILD-LOG.md` § 1.

After killing a render job, **check mtimes for monotonicity**, not just durations:
`TaskStop` kills the shell, not the Manim child, and an orphan will keep dropping
files into `manim/` that the next run skips as "already filled".

## Rebuild

### 0. Plates (only if you change the physics or the seed)

```bash
cd "$REEL" && "$PY" assets/gen_cosmos.py        # seed 7717 → assets/plots/
rm -rf media/videos                            # REQUIRED — see note at the end
```

It prints its own measured `ΔP/P`. Expect **3.7% for k < 60** and **58.0% for
k > 200**. If those numbers move, the physics changed; B09 quotes them on screen
and `SOURCES.md` records them.

### 1. GATE P — the human signs

`PEDAGOGY.md` must read `VERDICT: PASS` with a signature. **Do not write that
string anywhere else in the file**, including in prose explaining the gate:
`generate_audio_kokoro.py` opens on a plain substring match anywhere in the
document, so describing the gate unlocks it.

### 2. Audio — the master clock

```bash
cd "$TOOLKIT" && "$PY" runtime/scripts/generate_audio_kokoro.py "$REEL"
```

Kokoro `af_bella`, local, $0.00. Writes `mp3/beat-B*.mp3` + `mp3/timings.json` and
stamps `actual_duration_s` per beat. Expect 170.2 s total. **No `--speed` flag is
needed** — the script was sized to a word budget. Never adjust timing by hand.

### 3. Pacing (only if the narration changed)

```bash
"$PY" $SCRATCH/nat7.py     # per-scene natural length, no render
"$PY" $SCRATCH/pace7.py    # solves RT/HOLD and writes them into scenes.py
```

Then verify cheaply before spending 4K time:

```bash
cd "$REEL"
for S in B01_Presenter … B10_TheBox; do
  "$PY" -m manim -ql --fps 15 --disable_caching scenes.py "$S"
done
```

Compare each `media/videos/scenes/480p15/*.mp4` against its beat. A scene whose
body finishes *under* its beat will not respond to `RT` at all — `hold_to_beat()`
pins it to the target. That is correct, not a bug.

### 4. Gates F · L · A · W

**`run.sh` skips F, A and W on this reel.** All three are guarded on
`[ -n "$PENDING" ]`, and `PENDING` is empty because `run.sh` finds scenes with
`class (\w+)\(Scene\)` while every scene here subclasses `Paced`. Run them
directly:

```bash
cd "$REEL"
for f in FACTCHECK.md SHOTLIST.md PROMPTS.md; do test -f "$f" || echo "GATE F: missing $f"; done
"$PY" $TOOLKIT/runtime/qc/beat_lint.py beat_sheet.json
for S in B01_Presenter … B10_TheBox; do
  "$PY" $TOOLKIT/runtime/qc/static_scene_check.py scenes.py --class "$S" --quiet
  "$PY" $TOOLKIT/runtime/qc/wcag_margin_check.py  scenes.py --class "$S" --quiet
done
```

`rc>=2` is a failure, `rc==1` a warning. Expect `rc=0` throughout.

### 5. Manim, 4K, both aspects — sequentially

```bash
cd "$REEL"; mkdir -p manim _portrait
for S in B01_Presenter … B10_TheBox; do
  BID="${S%%_*}"
  "$PY" -m manim -qk --fps 24 --disable_caching -r 3840,2160 scenes.py "$S"
  cp "media/videos/scenes/2160p24/$S.mp4" "manim/$BID.mp4"
done
for S in B01_Presenter … B10_TheBox; do
  BID="${S%%_*}"
  "$PY" -m manim -qk --fps 24 --disable_caching -r 2160,3840 scenes.py "$S"
  cp "media/videos/scenes/3840p24/$S.mp4" "_portrait/$BID.mp4"
done
```

**Verify every render against its beat before slotting it** — that check is what
catches dropped frames, and GATE V cannot:

```
|ffprobe duration − actual_duration_s| ≤ 0.15 s   else re-render
frames / 24 == duration                          else the concat dropped frames
```

Expect a worst error of ~0.037 s, always *under* the beat.

### 6. GATE B — pixel-true layout, both aspects

```bash
cd "$REEL"
for S in B01_Presenter … B10_TheBox; do
  "$PY" $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict
  "$PY" $TOOLKIT/runtime/qc/manim_layout_audit.py scenes.py --class "$S" --png --curve-strict --portrait
done
```

Expect 20 × `rc=0`. Portrait is the stricter of the two — it has the same height and
a third of the width, so it fails on things landscape never notices.

### 7. 16:9 — Remotion bookends, then compile

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/remotion_scenes.py "$REEL"        # FOREGROUND (rule 5) — B00 B11 B12 B13 → media/
"$PY" runtime/scripts/compile.py "$REEL" --height 2160  # → simulating-the-universe.mp4
"$PY" runtime/qc/final_frame_check.py "$REEL"           # GATE V
```

The four Remotion renders are the memory-hungry step — they left 1.1 GB free of
31.7 GB here and the harness killed `run.sh`'s wrapper mid-pass. If that happens,
the child `compile.py` usually survives and finishes; check `*.mp4` mtimes and
carry on from `compile.py` rather than restarting the whole pass.

Add `--review` for the beat-marked cut (`…-slate.mp4`). Omit it for the master —
compile.py refuses to write a clean master that carries any slate.

### 8. 9:16 — full length, no beats cut

```bash
cd "$TOOLKIT"
"$PY" runtime/scripts/shorts.py "$REEL" --drop --no-endcard --handle "@HumanitariansAI"
cp "$REEL"/_portrait/B*.mp4 "$REEL"/short/manim/
cp "$REEL"/scenes.py "$REEL"/short/scenes.py
"$PY" runtime/scripts/remotion_scenes.py "$REEL/short"        # 4 × …916 at 2160×3840
"$PY" runtime/scripts/compile.py "$REEL/short" --height 3840
"$PY" runtime/qc/final_frame_check.py "$REEL/short"
cp "$REEL"/short/simulating-the-universe-short.mp4 "$REEL"/simulating-the-universe-9x16.mp4
```

`--drop` with **no arguments** means "drop nothing"; `--no-endcard` ends on B13.
Together they give a full-length 2:49.7 portrait cut with all 14 beats.

`compile.py` will warn `SKIN LINT: B00 … wants ClaudeComposerAsk` and `B13 … wants
ClaudeTitleOutro`. **Both are expected** — the linter checks composition names
against COLD OPEN LAW and OUTRO LAW and does not know `shorts.py`'s ONDA CHECK
deliberately rewired them to the `916` variants.

### 9. Look at the frames

Read `_qc/contact_sheet.png` and `short/_qc/contact_sheet.png`. The sheet carries
B00–B07 only, so **sample the tail yourself** — B08 through B13 in both aspects.
Sample *late* in each beat: a pale element mid-`FadeIn` looks exactly like a
rendering defect. See `_qc/VISUAL-QC.md`.

## Toolkit patches this reel depends on

Both are fixes in `$TOOLKIT`, already applied, and both are needed by any reel:

1. `runtime/scripts/shorts.py` — `link_or_copy()` falls back to `shutil.copy2` when
   `Path.symlink_to` raises `OSError 1314` (Windows without
   `SeCreateSymbolicLinkPrivilege`). Three call sites. Without it `shorts.py`
   cannot run on Windows at all.
2. `runtime/remotion/src/scenes/ClaudeVerdictArtifact916.tsx` and
   `ClaudeTitleOutro916.tsx` — rescaled from 42% and 19% canvas fill to ~79%.
   `_bench/consumers.json` confirmed this reel was the only consumer at the time.

## Still unpatched upstream

- `run.sh` does not export UTF-8 and crashes on cp1252 (§ preamble).
- `run.sh`'s scene discovery regex matches `(Scene)` only, so it silently skips
  GATE F, A and W on any reel whose scenes subclass a base class (§ 4).
- `generate_audio_kokoro.py` opens GATE P on a plain substring match (§ 1). The
  fix belongs in the checker; the gate was not modified for this build.

## Never

- Never publish. There is no publishing machinery here; the masters stay in this
  folder.
- Never hand-roll `npx remotion render` — go through `remotion_scenes.py`.
- Never fix timing by hand. Regenerate audio and recompile.
- Never re-render a plate without `rm -rf media/videos` first: Manim's cache key
  hashes scene *code* and does not hash the contents of images the scene loads, so
  a retuned plate will not invalidate anything.
