# BUILD-PROMPT.md — does-it-remember-or-just-pretend

Paste-ready build for this reel, end to end. Never publishes; the master
stays in this folder. **10 beats (B00-B09)**, 6 Manim (B01-B06) + 4
Remotion (B00, B07, B08, B09).

## Precondition — GATE P

`PEDAGOGY.md` currently reads **`VERDICT: PENDING`**. A human must read it,
replace that line with `VERDICT: PASS`, and sign it **before** running
Step 2. Kokoro is free, so this is a quality gate, not a cost gate.

The signature also covers the declared deviations logged in
PEDAGOGY.md/SOURCES.md: the illustrative examples (vegetarian preference,
poisoned-memory timeline), the beat count (10, fewer than STEM6's 12),
and the proactive narration-style rewrite applied without being asked.

## Environment (every new shell)

`./art run` shells out to `python3`, which on this machine is a Microsoft
Store alias, not the real interpreter — it prints "Python was not found"
and silently no-ops. Use the explicit path below.

```bash
export PATH="/c/ffmpeg:$PATH"
export PYTHONUTF8=1
PY="/c/Users/divij/AppData/Local/Programs/Python/Python312/python"
TOOLKIT="/c/Users/divij/Desktop/mycroft/brutalist.art"
REEL="/d/Code/humanitarians-youtube/fellows/divij-pawar/STEM7_DivijPawar_09-11-2026_does-it-remember-or-just-pretend"
```

## Step 1 — re-verify the sheet (free, instant)

```bash
$PY "$TOOLKIT/runtime/qc/sheet_check.py" "$REEL" --strict
```

Expected: `clean — 10 beats, no findings`. Exit 2 means a hard slate-rule
violation on a Remotion beat's props (B00, B07, B08, B09) — fix before
spending time on renders.

## Step 2 — audio (the master clock)

```bash
$PY "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Writes `mp3/beat-B00.mp3` ... `beat-B09.mp3` and fills `actual_duration_s`
in `beat_sheet.json` for all 10 beats. **Do not run until GATE P reads
PASS.**

## Step 3 — RETIME the Manim scenes against real audio ⚠

**Do not skip this.** Every scene in `scenes.py` is timed against
`estimated_duration_s` (a placeholder estimate, not yet measured against
real Kokoro output for this reel). Once Kokoro reports real durations,
compare:

```bash
$PY - <<'EOF'
import json
d = json.load(open('beat_sheet.json', encoding='utf-8'))
for b in d['beats']:
    m = b['shot'].get('manim')
    if m:
        est, act = b['estimated_duration_s'], b.get('actual_duration_s')
        print(f"{b['beat_id']}  {m['scene_class']:<26} est {est:>3}s  actual {act}")
EOF
```

Any beat off by more than ~1.5s: adjust that scene's `self.wait(...)`
holds in `scenes.py` before rendering. Spread added/trimmed time across
several of the longer holds near a beat's end, not into one static dump.

## Step 4 — render Manim (B01-B06)

```bash
cd "$REEL"
declare -A S=( [B01]=B01_OneWordTwoMechanisms [B02]=B02_HowRetrievalWorks
               [B03]=B03_StaleMemory [B04]=B04_PoisonedMemory
               [B05]=B05_SameBlindSpot [B06]=B06_TheFramework )
for B in B01 B02 B03 B04 B05 B06; do
  $PY -m manim -qh --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
```

**Then move the clips where compile.py actually looks** — it reads
`manim/<BID>.mp4` only, never Manim's own cache path:

```bash
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06; do
  cp "media/videos/scenes/1080p30/$B.mp4" "manim/$B.mp4"
done
```

(Use `media/videos/scenes/2160p30/` instead if rendering `-qk` for the
final 4K pass — see Step 6.)

## Step 5 — render Remotion bookends (B00, B07, B08, B09)

```bash
for B in B00 B07 B08 B09; do
  $PY "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --only "$B" --force
done
```

Needs Node.js. If one beat fails with an ffmpeg `create-silent-audio` /
`merge-audio-track` error, that is a transient temp-dir race — retry that
beat alone. **`--only` takes exactly ONE beat id per invocation.**

> ### ⚠ Never `rm -rf media/` between renders
> Remotion writes its bookends to `media/<BeatID>.mp4` — the **same
> folder** Manim uses for its own render cache. If only Manim scenes
> changed, overwrite `manim/<BeatID>.mp4` in place and leave `media/`
> alone.

## Step 6 — compile

```bash
# fast preview
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 1080 --fps 30
# final master (4K UHD 3840x2160) — render Manim at -qk first (repeat Step 4 with -qk)
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 2160 --fps 30
```

**Read the retiming lines it prints.** The stretch factor must stay under
**~1.15x**.

**Verify no beat silently slated:**

```bash
$PY -c "import json;m=json.load(open('clips/manifest.json'));print(m)" | tr ',' '\n' | grep -i slate
```

## Step 7 — visual QC (mandatory; the mp4 probe is not QC)

```bash
mkdir -p _qc/frames
ffmpeg -i "$REEL/does-it-remember-or-just-pretend.mp4" -vf fps=2 _qc/frames/%05d.png -y
```

**Read the PNGs** against the 8-point rubric in
`brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md`. Sample mid-scene frames
too, not just settled final frames — B04's two-query timeline and B05's
split-screen callback both change composition mid-beat. Watch
specifically for: B01's evaporating-box fade not lingering behind the
persistent-memory box; B02's dot field staying inside the title-safe
span; B05's vertical divider staying centered after both sides render at
their real widths.

## Step 8 — captions (last of all)

```bash
$PY "$TOOLKIT/runtime/scripts/align.py" "$REEL" --model base --language en
$PY "$TOOLKIT/runtime/scripts/make_srt.py" "$REEL"
```

Must run **after** audio is final and after the last compile. Mux as a
real `mov_text` stream into the compiled master in place — `compile.py`
does not do this automatically (confirmed on STEM6's build; re-mux
manually with `ffmpeg -c:s mov_text` after every recompile, since
recompiling drops any previously-muxed subtitle stream).

## Step 9 — derive the 9:16 cut

```bash
$PY "$TOOLKIT/runtime/scripts/shorts.py" "$REEL"
```

**Check the auto-drop plan before accepting it** — on STEM6, the
automatic "cheapest beats" plan opened the short mid-mechanism with no
setup and had to be manually overridden with `--drop`/`--keep` to keep a
self-contained arc (cold open + one fully-illustrated beat + verdict +
task + outro). Re-run `sheet_check.py` against the derived short's own
sheet, and re-QC the 9:16 render separately.

## Step 10 — clean the folder

Only these survive: `beat_sheet.json`, the gate docs, this file,
`scenes.py`, `graphics_lib.py`, `manim/*.mp4`, `media/<BeatID>.mp4`, the
final `<slug>.mp4` and its captioned variant, and the 9:16 outputs.
Everything else is regenerable scratch:

```bash
rm -rf "$REEL/_qc" "$REEL/media/videos" "$REEL/__pycache__"
```

## Never publish

Output stays in this folder for human review.
