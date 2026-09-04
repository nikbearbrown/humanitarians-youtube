# BUILD-PROMPT.md — how-do-you-know-it-worked

Paste-ready build for this reel, end to end. Never publishes; the master
stays in this folder. **13 beats (B00-B12)** — see CHECKS-REPORT.md
"Beat-count deviation" for why this isn't the ai-explainer default of 10.

## Precondition — GATE P

`PEDAGOGY.md` currently reads **`VERDICT: PENDING`**. A human must read it,
replace that line with `VERDICT: PASS`, and sign it **before** running Step
2. Kokoro is free, so this is a quality gate, not a cost gate.

The signature also covers two declared deviations logged in PEDAGOGY.md /
SOURCES.md: the constructed worked example ("34% YoY... source: 10-K")
threaded through B02-B06, and the beat count (13, not the 10-beat default).

## Environment (every new shell)

`./art run` shells out to `python3`, which on this machine is a Microsoft
Store alias, not the real interpreter — it prints "Python was not found"
and silently no-ops. Use the explicit path below.

```bash
export PATH="/c/ffmpeg:$PATH"
export PYTHONUTF8=1
PY="/c/Users/divij/AppData/Local/Programs/Python/Python312/python"
TOOLKIT="/c/Users/divij/Desktop/mycroft/brutalist.art"
REEL="/c/Users/divij/Desktop/mycroft/accountability_layer/youtube/STEM5"
```

## Step 1 — re-verify the sheet (free, instant)

```bash
$PY "$TOOLKIT/runtime/qc/sheet_check.py" "$REEL" --strict
```

Expected: `clean — 13 beats, no findings`. Exit 2 means a hard slate-rule
violation on a Remotion beat's props (B00, B10, B11, B12) — fix before
spending time on renders. This has not been run yet as of this writing;
run it before Step 2 regardless of GATE P status, since it's free.

## Step 2 — audio (the master clock)

```bash
$PY "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Writes `mp3/beat-B00.mp3` ... `beat-B12.mp3` and fills `actual_duration_s`
in `beat_sheet.json` for all 13 beats.

## Step 3 — RETIME the Manim scenes against real audio ⚠

**Do not skip this.** Every scene in `scenes.py` was timed against
`estimated_duration_s` (a placeholder estimate, not yet measured against
real Kokoro output for this reel). Once Kokoro reports real durations,
compare:

```bash
$PY - <<'EOF'
import json, pathlib
d = json.load(open('beat_sheet.json', encoding='utf-8'))
for b in d['beats']:
    m = b['shot'].get('manim')
    if m:
        est, act = b['estimated_duration_s'], b['actual_duration_s']
        print(f"{b['beat_id']}  {m['scene_class']:<26} est {est:>3}s  actual {act:6.2f}s  D{act-est:+6.2f}")
EOF
```

Any beat off by more than ~1.5s: adjust that scene's `self.wait(...)` holds
in `scenes.py` before rendering. A scene shorter than its audio
freeze-frames on its last shot; a scene longer gets cropped and loses its
ending. Per `youtube/CLAUDE.md` §5, spread added/trimmed time across
several of the longer holds near a beat's end, not into one static dump.

## Step 4 — render Manim (B01-B09)

```bash
cd "$REEL"
declare -A S=( [B01]=B01_TheTrustProblem [B02]=B02_ClaimExtraction
               [B03]=B03_VerifyAgainstReality [B04]=B04_VerificationRollup
               [B05]=B05_AskTwice [B06]=B06_ConsistencyFlag
               [B07]=B07_ProofToEvidence [B08]=B08_GoodAtCatching
               [B09]=B09_TheFramework )
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09; do
  $PY -m manim -qh --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
```

**Then move the clips where compile.py actually looks** — it reads
`manim/<BID>.mp4` only, never Manim's own cache path. Skip this and every
beat compiles as a slate while the render reports success:

```bash
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09; do
  cp "media/videos/scenes/1080p30/$B.mp4" "manim/$B.mp4"
done
```

(Use `media/videos/scenes/2160p30/` instead if rendering `-qk` for the
final 4K pass — see Step 6.)

## Step 5 — render Remotion bookends (B00, B10, B11, B12)

```bash
for B in B00 B10 B11 B12; do
  $PY "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --only "$B" --force
done
```

Needs Node.js. If one beat fails with an ffmpeg `create-silent-audio` /
`merge-audio-track` error, that is a transient temp-dir race — retry that
beat alone. **`--only` takes exactly ONE beat id per invocation.**

> ### ⚠ Never `rm -rf media/` between renders
> Remotion writes its bookends to `media/<BeatID>.mp4` — the **same
> folder** Manim uses for its own render cache (`media/videos/...`).
> Wiping `media/` to force a clean Manim slate silently destroys the cold
> open, verdict, handoff and outro. If only Manim scenes changed,
> overwrite `manim/<BeatID>.mp4` in place and leave `media/` alone.

## Step 6 — compile

```bash
# fast preview
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 1080 --fps 30
# final master (4K UHD 3840x2160) — render Manim at -qk first (repeat Step 4 with -qk)
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 2160 --fps 30
```

**Read the retiming lines it prints.** The stretch factor must stay under
**~1.15x** — add `self.wait()` inside the Manim scene rather than let
compile.py paper over a large factor.

**Verify no beat silently slated:**

```bash
$PY -c "import json;m=json.load(open('clips/manifest.json'));print(m)" | tr ',' '\n' | grep -i slate
```

Any hit means that beat has no rendered clip — fix and re-render rather
than reaching for `--allow-slates`.

## Step 7 — visual QC (mandatory; the mp4 probe is not QC)

```bash
mkdir -p _qc/frames
ffmpeg -i "$REEL/how-do-you-know-it-worked.mp4" -vf fps=2 _qc/frames/%05d.png -y
```

**Read the PNGs** against the 8-point rubric in
`brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md`: edge bleed, title-safe
margins, container overflow, collision, offscreen anchors, legibility,
brand bug, aspect/letterbox. Sample mid-scene frames too, not just settled
final frames — B04's pooling-caveat diagram and B06's two-example
sequence both change composition mid-beat.

Watch specifically for: the three-mechanism legend width-clamped to the
title-safe span (B02-B09, mirrors STEM2's four-mode legend fix); B03's
three outcome chips not colliding when scaled to fit 12.4 units; B04's
pool-of-numbers row not overrunning the frame; B08's two-column divider
staying centered after both columns render at their real widths (measured
only at render time, not before).

## Step 8 — captions (last of all)

```bash
$PY "$TOOLKIT/runtime/scripts/align.py" "$REEL" --model base --language en
$PY "$TOOLKIT/runtime/scripts/make_srt.py" "$REEL"
```

Must run **after** audio is final and after the last compile.

## Step 9 — derive the 9:16 cut

```bash
$PY "$TOOLKIT/runtime/scripts/shorts.py" "$REEL"
```

Re-run `sheet_check.py` against the derived short's sheet (not this
16:9 sheet) — the `*916` Remotion patterns have sharply tighter text
limits (see `agents.md`'s 9:16 table). Re-run visual QC on the 9:16 render
separately; it is different geometry, not a guaranteed-clean crop.

## Step 10 — clean the folder

Only these survive: `beat_sheet.json`, the gate docs, this file,
`scenes.py`, `graphics_lib.py`, `manim/*.mp4`, `media/<BeatID>.mp4`, the
final `<slug>.mp4` and its `.srt`/subtitled variant, and the 9:16 outputs.
Everything else is regenerable scratch:

```bash
rm -rf "$REEL/_qc" "$REEL/media/videos" "$REEL/__pycache__"
```

Note `media/videos` — the Manim cache — **not** `media/` itself, which
holds the four rendered Remotion bookends.

## Never publish

Output stays in this folder for human review.
