# BUILD-PROMPT.md — why-agents-fail

Paste-ready build for this reel, end to end. Never publishes; the master
stays in this folder.

## Precondition — GATE P

`PEDAGOGY.md` currently reads **`VERDICT: PENDING`**. A human must read it,
replace that line with `VERDICT: PASS`, and sign it **before** running Step 2.
Kokoro is free, so this is a quality gate, not a cost gate.

The signature also accepts the runtime deviation logged in PEDAGOGY.md: the
source script targets ~9 minutes; this narration measures **≈5.1 min**.

## Environment (every new shell)

`./art run` shells out to `python3`, which on this machine is a Microsoft
Store alias, not the real interpreter — it prints "Python was not found" and
silently no-ops. Use the explicit path below.

```bash
export PATH="/c/ffmpeg:$PATH"
export PYTHONUTF8=1
PY="/c/Users/divij/AppData/Local/Programs/Python/Python312/python"
TOOLKIT="/c/Users/divij/Desktop/mycroft/brutalist.art"
REEL="/c/Users/divij/Desktop/mycroft/accountability_layer/youtube/STEM2"
```

## Step 1 — re-verify the sheet (free, instant)

```bash
$PY "$TOOLKIT/runtime/qc/sheet_check.py" "$REEL" --strict
```

Expected: `clean — 10 beats, no findings`. Exit 2 means a hard slate-rule
violation; fix the props before spending time on renders.

## Step 2 — audio (the master clock)

```bash
$PY "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Writes `mp3/beat-B00.mp3` … `beat-B09.mp3` and fills `actual_duration_s` in
`beat_sheet.json`.

## Step 3 — RETIME the Manim scenes against real audio ⚠

**Do not skip this.** Every scene in `scenes.py` was timed against
`estimated_duration_s` (measured at the ~195 wpm the sibling reel
`accountability-mesh` actually produced) and currently lands within ±0.5s of
those estimates. Once Kokoro reports real durations, compare:

```bash
$PY - <<'EOF'
import json, pathlib
d = json.load(open('beat_sheet.json', encoding='utf-8'))
for b in d['beats']:
    m = b['shot'].get('manim')
    if m:
        est, act = b['estimated_duration_s'], b['actual_duration_s']
        print(f"{b['beat_id']}  {m['scene_class']:<22} est {est:>3}s  actual {act:6.2f}s  Δ{act-est:+6.2f}")
EOF
```

Any beat off by more than ~1.5s: adjust that scene's `self.wait(...)` holds
in `scenes.py` before rendering. A scene shorter than its audio freeze-frames
on its last shot; a scene longer gets cropped and loses its ending.

## Step 4 — render Manim (B01–B06)

```bash
cd "$REEL"
declare -A S=( [B01]=B01_FourFailures [B02]=B02_InfiniteLoop [B03]=B03_ContextDrift 
               [B04]=B04_HallucinatedArgs [B05]=B05_ConfidentlyWrong [B06]=B06_TwelveAttempts )
for B in B01 B02 B03 B04 B05 B06; do
  $PY -m manim -qh --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
```

**Then move the clips where compile.py actually looks** — it reads
`manim/<BID>.mp4` only, never Manim's own cache path. Skip this and every
beat compiles as a slate while the render reports success:

```bash
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06; do
  cp "media/videos/scenes/1080p30/$B.mp4" "manim/$B.mp4"
done
```

## Step 5 — render Remotion bookends (B00, B07, B08, B09)

```bash
$PY "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --force
```

Needs Node.js. If one beat fails with an ffmpeg `create-silent-audio` /
`merge-audio-track` error, that is a transient temp-dir race — retry that
beat alone. **`--only` takes exactly ONE beat id**; passing several in one
invocation errors out, so loop:

```bash
for B in B00 B07 B08 B09; do
  $PY "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --only "$B" --force
done
```

> ### ⚠ Never `rm -rf media/` between renders
> Remotion writes its bookends to `media/<BeatID>.mp4` — the **same folder**
> Manim uses for its own render cache (`media/videos/…`). Wiping `media/` to
> force a clean Manim slate silently destroys the cold open, verdict, handoff
> and outro, and compile.py then reports those four beats as SLATE or reuses
> a stale file. If only Manim scenes changed, overwrite `manim/<BeatID>.mp4`
> in place and leave `media/` alone. If you do wipe it, re-render every
> Remotion beat before compiling.

## Step 6 — compile

```bash
# fast preview
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 1080 --fps 30
# final master (4K UHD 3840x2160) — render Manim at -qk first
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 2160 --fps 30
```

**Read the retiming lines it prints**, e.g.
`[art] B04: clip 52.2s slowed 1.14x to fill 59.7s beat`. The stretch factor
must stay under **~1.15x** or the slow-motion becomes visible. The fix for a
large factor is to add `self.wait()` inside that Manim scene so its native
length already matches the beat's `actual_duration_s` — never to let
compile.py paper over it. A clip much *longer* than its beat gets
centre-cropped, so check the crop didn't cut a moment you need.

**Verify no beat silently slated:**

```bash
$PY -c "import json;m=json.load(open('clips/manifest.json'));print(m)" | tr ',' '\n' | grep -i slate
```

Any hit means that beat has no rendered clip — fix and re-render rather than
reaching for `--allow-slates`.

## Step 7 — visual QC (mandatory; the mp4 probe is not QC)

```bash
mkdir -p _qc/frames
ffmpeg -i "$REEL/why-agents-fail.mp4" -vf fps=2 _qc/frames/%05d.png -y
```

**Read the PNGs.** Audit the 9-point rubric: edge bleed, title-safe margins,
container overflow, collision, offscreen anchors, legibility, brand bug,
aspect, canvas fill. Log defects in `_qc/REPORT.md`, fix the root cause in
`scenes.py` or the beat-sheet props, re-render until zero BLOCKER/MAJOR.

Look specifically for: text crossing its own box border; text crossing the
frame edge; two chips or labels touching; a glyph rendering as a garbled
`.notdef` box instead of the intended symbol.

Known-good from the pre-render pass (re-confirm after the real render): the four-mode legend is width-clamped to the title-safe span on
B02–B06; B03's goal block sits at the window boundary without clipping.

## Step 8 — captions (last of all)

Must run **after** audio is final and after the last compile — `make_srt.py`
computes each beat's absolute offset from `actual_duration_s`, so the order
and durations have to match the shipped master.

```bash
$PY "$TOOLKIT/runtime/scripts/align.py" "$REEL" --model base --language en
$PY "$TOOLKIT/runtime/scripts/make_srt.py" "$REEL"
```

Regenerate `mp3/words.json` (the align step) whenever narration text changes.

## Step 9 — clean the folder

Only these survive: `beat_sheet.json`, the three gate docs, this file,
`scenes.py`, `graphics_lib.py`, `manim/*.mp4`, `media/<BeatID>.mp4`, the
final `<slug>.mp4` and its `.srt`. Everything else is regenerable scratch:

```bash
rm -rf "$REEL/_qc" "$REEL/media/videos" "$REEL/__pycache__"
```

Note `media/videos` — the Manim cache — **not** `media/` itself, which holds
the four rendered Remotion bookends.

## Never publish

Output stays in this folder for human review.
