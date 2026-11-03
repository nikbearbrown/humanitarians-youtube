# BUILD-PROMPT.md — when-two-agents-disagree

Paste-ready build for this reel, end to end. Never publishes; the master
stays in this folder. **12 beats (B00-B11)** — see CHECKS-REPORT.md
"Beat-count deviation" for why this isn't the ai-explainer default of 10.

## Precondition 0 — `scenes.py` does not exist yet

Before Step 1 will fully pass, `scenes.py` needs one Manim `Scene` class
per Manim beat in `beat_sheet.json`: `B01_OneVoiceThenMany`,
`B02_TheNaiveFix`, `B03_DetectingDivergence`, `B04_ArbitrationSetup`,
`B05_ArbitrationOutcomes`, `B06_UnresolvedHandling`,
`B07_SharedContamination`, `B08_TheFramework` — built against each beat's
`show[]` timeline and using `graphics_lib.py`'s helpers (`label()`,
`title()`, `serif()`, `mono()`) unchanged, per `youtube/CLAUDE.md` §3/§5.
This is unwritten as of this file. Do not run Step 2 (audio) before
`scenes.py` exists **and** GATE P is signed — per `youtube/CLAUDE.md` §5
Step 1, the beat sheet, gate docs, and `scenes.py` are authored together,
before audio generation, not after.

## Precondition — GATE P

`PEDAGOGY.md` currently reads **`VERDICT: PENDING`**. A human must read it,
replace that line with `VERDICT: PASS`, and sign it **before** running
Step 2. Kokoro is free, so this is a quality gate, not a cost gate.

The signature also covers the declared deviations logged in
PEDAGOGY.md/SOURCES.md: the illustrative financial scenario (Agent A/B,
margins improving/declining), the beat count (12, not the 10-beat
default), and the scope finding that no arbitration/multi-agent module
currently exists in `accountability_layer/` (so this reel is checked
against general practice, not this project's own code).

## Environment (every new shell)

`./art run` shells out to `python3`, which on this machine is a Microsoft
Store alias, not the real interpreter — it prints "Python was not found"
and silently no-ops. Use the explicit path below.

```bash
export PATH="/c/ffmpeg:$PATH"
export PYTHONUTF8=1
PY="/c/Users/divij/AppData/Local/Programs/Python/Python312/python"
TOOLKIT="/c/Users/divij/Desktop/mycroft/brutalist.art"
REEL="/d/Code/humanitarians-youtube/fellows/divij-pawar/STEM6_DivijPawar_09-05-2026_when-two-agents-disagree"
```

## Step 1 — re-verify the sheet (free, instant)

```bash
$PY "$TOOLKIT/runtime/qc/sheet_check.py" "$REEL" --strict
```

Expected: `clean — 12 beats, no findings`. Exit 2 means a hard slate-rule
violation on a Remotion beat's props (B00, B09, B10, B11) — fix before
spending time on renders. Also expect this to flag missing Manim scene
classes until Precondition 0 is resolved.

## Step 2 — audio (the master clock)

```bash
$PY "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Writes `mp3/beat-B00.mp3` ... `beat-B11.mp3` and fills `actual_duration_s`
in `beat_sheet.json` for all 12 beats. **Do not run until GATE P reads
PASS.**

## Step 3 — RETIME the Manim scenes against real audio ⚠

**Do not skip this.** Every scene in `scenes.py` will be timed against
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
        est, act = b['estimated_duration_s'], b.get('actual_duration_s')
        print(f"{b['beat_id']}  {m['scene_class']:<26} est {est:>3}s  actual {act}")
EOF
```

Any beat off by more than ~1.5s: adjust that scene's `self.wait(...)`
holds in `scenes.py` before rendering. A scene shorter than its audio
freeze-frames on its last shot; a scene longer gets cropped and loses its
ending. Per `youtube/CLAUDE.md` §5, spread added/trimmed time across
several of the longer holds near a beat's end, not into one static dump.

## Step 4 — render Manim (B01-B08)

```bash
cd "$REEL"
declare -A S=( [B01]=B01_OneVoiceThenMany [B02]=B02_TheNaiveFix
               [B03]=B03_DetectingDivergence [B04]=B04_ArbitrationSetup
               [B05]=B05_ArbitrationOutcomes [B06]=B06_UnresolvedHandling
               [B07]=B07_SharedContamination [B08]=B08_TheFramework )
for B in B01 B02 B03 B04 B05 B06 B07 B08; do
  $PY -m manim -qh --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
```

**Then move the clips where compile.py actually looks** — it reads
`manim/<BID>.mp4` only, never Manim's own cache path. Skip this and every
beat compiles as a slate while the render reports success:

```bash
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06 B07 B08; do
  cp "media/videos/scenes/1080p30/$B.mp4" "manim/$B.mp4"
done
```

(Use `media/videos/scenes/2160p30/` instead if rendering `-qk` for the
final 4K pass — see Step 6.)

## Step 5 — render Remotion bookends (B00, B09, B10, B11)

```bash
for B in B00 B09 B10 B11; do
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
ffmpeg -i "$REEL/when-two-agents-disagree.mp4" -vf fps=2 _qc/frames/%05d.png -y
```

**Read the PNGs** against the 8-point rubric in
`brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md`: edge bleed, title-safe
margins, container overflow, collision, offscreen anchors, legibility,
brand bug, aspect/letterbox. Sample mid-scene frames too, not just settled
final frames — B06's real-vs-ghosted report pair and B08's four-rule grid
both change composition mid-beat.

Watch specifically for: B03's gauge and two signal cards not colliding
once both are on screen at once; B04's crossed-out unbounded-debate ghost
staying legible against the "1 ROUND ONLY" stamp rather than overlapping
it; B08's 2×2 rule grid staying centered and title-safe after all four
icons render at their real widths (measured only at render time, not
before).

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
