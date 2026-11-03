# BUILD-PROMPT.md — the-agent-that-was-told-what-to-do

Paste-ready build for this reel, end to end. Never publishes; the master
stays in this folder. **11 beats (B00-B10)**, 7 Manim (B01-B07) + 4
Remotion (B00, B08, B09, B10).

## Precondition — GATE P

`PEDAGOGY.md` currently reads **`VERDICT: PENDING`**. A human must read it,
replace that line with `VERDICT: PASS`, and sign it **before** running
Step 2. Kokoro is free, so this is a quality gate, not a cost gate.

The signature also covers the declared deviation logged in PEDAGOGY.md:
the outro closes the series reflectively rather than teasing a next
episode, since no STEM10 is currently scripted.

## Environment (every new shell)

```bash
export PATH="/c/ffmpeg:$PATH"
export PYTHONUTF8=1
PY="/c/Users/divij/AppData/Local/Programs/Python/Python312/python"
TOOLKIT="/c/Users/divij/Desktop/mycroft/brutalist.art"
REEL="/d/Code/humanitarians-youtube/fellows/divij-pawar/STEM9_DivijPawar_09-25-2026_the-agent-that-was-told-what-to-do"
```

## Step 1 — re-verify the sheet (free, instant)

```bash
$PY "$TOOLKIT/runtime/qc/sheet_check.py" "$REEL" --strict
```

Expected: `clean — 11 beats, no findings`.

## Step 2 — audio (the master clock)

```bash
$PY "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Writes `mp3/beat-B00.mp3` ... `beat-B10.mp3` and fills `actual_duration_s`
in `beat_sheet.json`. **Do not run until GATE P reads PASS.**

## Step 3 — RETIME the Manim scenes against real audio ⚠

```bash
$PY - <<'EOF'
import json
d = json.load(open('beat_sheet.json', encoding='utf-8'))
for b in d['beats']:
    m = b['shot'].get('manim')
    if m:
        est, act = b['estimated_duration_s'], b.get('actual_duration_s')
        print(f"{b['beat_id']}  {m['scene_class']:<28} est {est:>3}s  actual {act}")
EOF
```

Any beat off by more than ~1.5s: adjust that scene's `self.wait(...)`
holds. Spread added/trimmed time across several of the longer holds near
a beat's end, not into one static dump.

## Step 4 — render Manim (B01-B07)

```bash
cd "$REEL"
declare -A S=( [B01]=B01_DataAndInstructions [B02]=B02_WorkedExample
               [B03]=B03_NotTheAutonomyQuestion [B04]=B04_LockTheInstructions
               [B05]=B05_CrossExaminationHole [B06]=B06_ApprovalRealLimit
               [B07]=B07_SittingWithIt )
for B in B01 B02 B03 B04 B05 B06 B07; do
  $PY -m manim -qh --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06 B07; do
  cp "media/videos/scenes/1080p30/$B.mp4" "manim/$B.mp4"
done
```

(Use `media/videos/scenes/2160p30/` instead if rendering `-qk` for the
final 4K pass — see Step 6.)

## Step 5 — render Remotion bookends (B00, B08, B09, B10)

```bash
for B in B00 B08 B09 B10; do
  $PY "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --only "$B" --force
done
```

**`--only` takes exactly ONE beat id per invocation.** Never `rm -rf
media/` between renders.

## Step 6 — compile

```bash
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 1080 --fps 30   # fast preview
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 2160 --fps 30   # final master (render Manim at -qk first)
```

Verify no beat silently slated:

```bash
$PY -c "import json;m=json.load(open('clips/manifest.json'));print(m)" | tr ',' '\n' | grep -i slate
```

## Step 7 — visual QC (mandatory; the mp4 probe is not QC)

```bash
mkdir -p _qc/frames
ffmpeg -i "$REEL/the-agent-that-was-told-what-to-do.mp4" -vf fps=2 _qc/frames/%05d.png -y
```

Sample mid-scene frames too. Watch specifically for: B02's zoomed hidden
text staying legible against the background; B03's two doors staying
symmetric at their real rendered widths; B05's reprised nameplate
diagram not colliding the way the original STEM6 version once did before
its own fix; B06's two contrasted screens staying clearly separated.

## Step 8 — captions (last of all)

```bash
$PY "$TOOLKIT/runtime/scripts/align.py" "$REEL" --model base --language en
$PY "$TOOLKIT/runtime/scripts/make_srt.py" "$REEL"
```

Mux as a real `mov_text` stream into the compiled master **manually**
after every recompile — `compile.py` does not preserve a previously-muxed
subtitle stream:

```bash
ffmpeg -y -i the-agent-that-was-told-what-to-do.mp4 -i captions.srt -c:v copy -c:a copy -c:s mov_text \
  -map 0:v -map 0:a -map 1:s -metadata:s:s:0 language=eng the-agent-that-was-told-what-to-do_capt.mp4
mv the-agent-that-was-told-what-to-do_capt.mp4 the-agent-that-was-told-what-to-do.mp4
```

## Step 9 — derive the 9:16 cut

```bash
$PY "$TOOLKIT/runtime/scripts/shorts.py" "$REEL"
```

**Check the auto-drop plan before accepting it** — on STEM6 and STEM7,
the automatic plan opened the short with a dangling reference to a
dropped beat's content. Check whether the kept beat's opening line
references anything from a dropped beat. Re-run `sheet_check.py` against
the derived short's own sheet, and re-QC the 9:16 render separately.

## Step 10 — clean the folder

```bash
rm -rf "$REEL/_qc" "$REEL/media/videos" "$REEL/__pycache__"
```

## Never publish

Output stays in this folder for human review.
