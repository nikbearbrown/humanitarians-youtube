# BUILD-PROMPT.md — fifteen-of-sixteen

Paste-ready build for this reel, end to end. Never publishes; the master
stays in this folder. **18 beats (B00–B17)** — see CHECKS-REPORT.md
"Beat-count deviation" for why this isn't the ai-explainer default of 10.

## Precondition — GATE P

`PEDAGOGY.md` currently reads **`VERDICT: PENDING`**. A human must read it,
resolve the open checklist items at its end, replace that line with
`VERDICT: PASS`, and sign it **before** running Step 2. Kokoro is free, so
this is a quality gate, not a cost gate.

## Environment (every new shell)

`./art run` shells out to `python3`, which on this machine is a Microsoft
Store alias, not the real interpreter — it prints "Python was not found"
and silently no-ops. Use the explicit path below.

```bash
export PATH="/c/ffmpeg:$PATH"
export PYTHONUTF8=1
PY="/c/Users/divij/AppData/Local/Programs/Python/Python312/python"
TOOLKIT="/c/Users/divij/Desktop/mycroft/brutalist.art"
REEL="/d/Code/humanitarians-youtube/fellows/divij-pawar/Mycroft7_DivijPawar_09-11-2026_fifteen-of-sixteen"
```

## Step 1 — verify the sheet (free, instant)

```bash
$PY "$TOOLKIT/runtime/qc/sheet_check.py" "$REEL" --strict
```

Not yet run against this reel (see CHECKS-REPORT.md "Slate rules audit") —
run this before spending any time on renders. If it flags a soft
over-length finding (as happened on Mycroft6's B00 `output[2]`), shorten
that field and re-run — don't reach for `--allow-slates` or skip the check.

## Step 2 — audio (the master clock)

```bash
$PY "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Writes `mp3/beat-B00.mp3` ... `beat-B17.mp3` and fills `actual_duration_s`
in `beat_sheet.json` for all 18 beats. Projected pre-audio total is ~8:50
(1,323 words at 150 wpm) — see PEDAGOGY.md "Runtime"; this is only a
planning estimate. Mycroft6's real Kokoro output came in ~35% faster than
estimated across nearly every beat — expect a similar gap here, not a
1:1 match.

## Step 3 — RETIME the Manim scenes against real audio ⚠

**Do not skip this.** Every scene in `scenes.py` currently sets `TARGET` to
the pre-audio `estimated_duration_s` — a placeholder, not yet measured
against real Kokoro output for this reel. Once Kokoro reports real
durations, compare:

```bash
$PY - <<'EOF'
import json
d = json.load(open('beat_sheet.json', encoding='utf-8'))
for b in d['beats']:
    m = b['shot'].get('manim')
    if m:
        est, act = b['estimated_duration_s'], b['actual_duration_s']
        print(f"{b['beat_id']}  {m['scene_class']:<32} est {est:>3}s  actual {act}")
EOF
```

Update each affected scene's `TARGET` constant in `scenes.py` to the real
`actual_duration_s` — per this series' own precedent (zero-for-sixteen),
every scene's actual choreographed elapsed time was already comfortably
below even the shortened targets, so `hold_to()`'s own padding absorbed
the retiming without needing to touch individual `self.wait()` calls. Spot
check the same is true here before assuming it: sum each scene's `run_time`
+ `wait()` calls and confirm it's well under the new `TARGET`.

## Step 4 — render Manim (B01–B16)

```bash
cd "$REEL"
declare -A S=( [B01]=B01_OpenThreads [B02]=B02_NumberTagging
               [B03]=B03_ThreeBugs [B04]=B04_ReplayThroughGate
               [B05]=B05_CheckedTwice [B06]=B06_TruePositivePreserved
               [B07]=B07_SharedContextFork [B08]=B08_ZeroRealNumbers
               [B09]=B09_SignAndMagnitude [B10]=B10_ModelScoreboard
               [B11]=B11_RouteRewire [B12]=B12_RegexFix
               [B13]=B13_VerificationRateZero [B14]=B14_TrueNowList
               [B15]=B15_StillNotTrueAndUncommitted
               [B16]=B16_FifteenKilledReprise )
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14 B15 B16; do
  $PY -m manim -qh --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
```

**Then move the clips where compile.py actually looks** — it reads
`manim/<BID>.mp4` only, never Manim's own cache path:

```bash
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14 B15 B16; do
  cp "media/videos/scenes/1080p30/$B.mp4" "manim/$B.mp4"
done
```

(Use `media/videos/scenes/2160p30/` instead for the final 4K pass — see
Step 6. Render Manim twice, once at `-qh` for preview/QC, once at `-qk`
for the final master, exactly as zero-for-sixteen did — do not skip the
1080p preview-and-QC pass and go straight to 4K.)

## Step 5 — render Remotion bookends (B00, B17)

```bash
for B in B00 B17; do
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
> open and outro. If only Manim scenes changed, overwrite
> `manim/<BeatID>.mp4` in place and leave `media/` alone.

## Step 6 — compile

```bash
# fast preview
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 1080 --fps 30
# final master (4K UHD 3840x2160) — render Manim at -qk first (repeat Step 4 with -qk)
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 2160 --fps 30
```

**Read the retiming lines it prints.** The stretch factor must stay under
**~1.15x** — add `self.wait()` inside the Manim scene rather than let
compile.py paper over a large factor. **Verify no beat silently slated:**

```bash
$PY -c "import json;m=json.load(open('clips/manifest.json'));print(m)" | tr ',' '\n' | grep -i slate
```

Any hit means that beat has no rendered clip — fix and re-render rather
than reaching for `--allow-slates`.

## Step 7 — visual QC on REAL rendered frames (mandatory; the mp4 probe is not QC)

```bash
mkdir -p _qc/frames
ffmpeg -i "$REEL/fifteen-of-sixteen.mp4" -vf fps=2 _qc/frames/%05d.png -y
```

**Actually read the PNGs** against the 8-point rubric in
`brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md` — do not skip this or
assume the code is correct because it parses. zero-for-sixteen's own build
found two real defects this exact way (a tile pile landing on a label's
text, a ⚠ glyph silently failing to render) that no amount of code review
would have caught; both were only visible in actual rendered pixels. Watch
specifically:

- **B15's stacked layout** (5-line warning list + git panel + file-count
  chip + closing caption, all uncleared) — confirm nothing collides at 4K.
- **B16's end-card bullet list beneath the reprise card** — confirm it
  stays legible and doesn't compete visually with the card above it.
- **B08's two side-by-side context boxes + stamp beneath** — confirm the
  stamp doesn't crowd either box.
- **B03's strike-through + FIXED stamp sequence** — confirm each stamp
  lands clear of its own card's strike line, not overlapping it.
- **Any use of `warn_icon()`** — none is used in this reel's `scenes.py`
  as authored, but if one gets added during retiming/QC fixes, confirm it
  renders as an actual triangle+"!", never a raw `Text("⚠", ...)` — that
  glyph silently fails on this machine (see `scenes.py`'s own docstring).
- **Re-render and re-check any beat you touch to fix a defect** — verify
  the fix against a fresh rendered frame, never assume it worked from the
  code change alone (this caught a second-order issue in
  zero-for-sixteen's own B08 fix, where the first coordinate guess still
  needed a follow-up correction).

## Step 8 — captions and final files (last of all)

**End state: exactly two final video files, both already carrying muxed
captions.** Generate the caption source, mux into the 16:9 master:

```bash
$PY "$TOOLKIT/runtime/scripts/align.py" "$REEL" --model base --language en
$PY "$TOOLKIT/runtime/scripts/make_srt.py" "$REEL"
# writes captions.srt

ffmpeg -i "$REEL/fifteen-of-sixteen.mp4" -i "$REEL/captions.srt" \
  -map 0 -map 1 -c copy -c:s mov_text \
  -metadata:s:s:0 language=eng "$REEL/_tmp_master.mp4" \
  && mv "$REEL/_tmp_master.mp4" "$REEL/fifteen-of-sixteen.mp4"
```

## Step 9 — clean the folder

```bash
rm -rf "$REEL/_qc" "$REEL/media/videos" "$REEL/__pycache__"
```

Note `media/videos` — the Manim cache — **not** `media/` itself, which
holds the two rendered Remotion bookends.

## Step 10 — rename to the channel's Mycroft delivery convention

**The pipeline's own output filename is the slug (`fifteen-of-sixteen.mp4`)
— that is not the final delivery name.** Per this channel's actual
convention (confirmed against every prior Mycroft reel's shipped files,
e.g. `Mycroft_DivijPawar_08-28-2026.mp4`), rename before calling this done:

```bash
mv "$REEL/fifteen-of-sixteen.mp4" "$REEL/Mycroft_DivijPawar_09-11-2026.mp4"
```

This reel's folder date (09-11-2026) already matches this week's STEM
sibling (`STEM7_DivijPawar_09-11-2026_...`), so no date correction is
needed here — unlike Mycroft6, whose folder was dated by period-end
(09-07) while the channel's actual weekly delivery slot was 09-05, which
needed a rename after the fact. Confirm the date still matches before
running this step; if a STEM7 delivery date changes, use that date instead
of assuming 09-11 unchanged.

**Verify the end state before calling this done:**

```bash
ls "$REEL"/*.mp4
# expected: exactly one file, Mycroft_DivijPawar_09-11-2026.mp4 —
# no leftover slug-named file, no unsubtitled master, no *_subtitled.mp4.
```

## Shorts (9:16) — decide before starting, don't default to the auto-plan

zero-for-sixteen's own build found that `shorts.py`'s auto-plan (drops the
longest beats first, no content-protection awareness beyond hook/hero/
outro) will very likely propose dropping **B14 and/or B15 — Chapter 5**,
the one section this script's own production notes say to never cut. Given
this reel's runtime (~8:50, similar to Mycroft6's post-cut length) against
the Shorts 3:00 cap, expect the same conflict. Do not accept the
auto-plan's drop list without checking it against PEDAGOGY.md's protected
beats first. If Chapter 5 is in the drop list, either explicitly `--keep
B14 B15` (and drop more elsewhere to compensate) or skip the Shorts
derivative for this reel — the same three options Mycroft6's build
surfaced. Also pass `--handle @DivijPawar` explicitly — the script's own
default (`@nikbearbrown`) is wrong for this channel, caught on
zero-for-sixteen's build.

## Never publish

Output stays in this folder for human review.
