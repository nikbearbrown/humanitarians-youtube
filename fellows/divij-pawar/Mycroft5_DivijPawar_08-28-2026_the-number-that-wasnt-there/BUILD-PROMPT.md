# BUILD-PROMPT.md — the-number-that-wasnt-there

Paste-ready build for this reel, end to end. Never publishes; the master
stays in this folder. **15 beats (B00-B14)** — see CHECKS-REPORT.md
"Beat-count deviation" for why this isn't the ai-explainer default of 10,
and why it grew from this reel's own prior 11-beat build.

## Precondition — GATE P

`PEDAGOGY.md` currently reads **`VERDICT: PENDING`**. A human must read it,
resolve the open checklist items at its end (including the two new ones from
this rebuild — the runtime overrun and the five-test-card repetition risk),
replace that line with `VERDICT: PASS`, and sign it **before** running Step
2. Kokoro is free, so this is a quality gate, not a cost gate.

The signature also covers the deviations logged in PEDAGOGY.md / SOURCES.md:
the missing `the-other-agent-wasnt-real/` template (this build used
`three-files-twenty-one-tests/` instead), the source-verification gap
(several claims trace only to files absent from this checkout), the beat
count (15, not 10), the original B14 sign-off line not present in the
source script, the ~12:29 projected runtime against the script's own ~10:40
target, and whether the five near-identical test-card beats (B04-B08) need
more visual differentiation before render.

## Environment (every new shell)

`./art run` shells out to `python3`, which on this machine is a Microsoft
Store alias, not the real interpreter — it prints "Python was not found"
and silently no-ops. Use the explicit path below.

```bash
export PATH="/c/ffmpeg:$PATH"
export PYTHONUTF8=1
PY="/c/Users/divij/AppData/Local/Programs/Python/Python312/python"
TOOLKIT="/c/Users/divij/Desktop/mycroft/brutalist.art"
REEL="/c/Users/divij/Desktop/mycroft/accountability_layer/youtube/the-number-that-wasnt-there"
```

## Step 1 — re-verify the sheet (free, instant)

```bash
$PY "$TOOLKIT/runtime/qc/sheet_check.py" "$REEL" --strict
```

Expected: `clean — 15 beats, no findings`. This was already run during the
Chapter-3 rebuild (read-only) and came back clean with no findings at all —
re-run before spending time on renders in case the sheet is edited during
GATE P review.

## Step 2 — audio (the master clock)

```bash
$PY "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Writes `mp3/beat-B00.mp3` ... `beat-B14.mp3` and fills `actual_duration_s`
in `beat_sheet.json` for all 15 beats. Projected pre-audio total is ~12:29
(1,871 words at 150 wpm) against the script's own ~10:40 target — see
PEDAGOGY.md "Runtime — recomputed"; this is only a planning estimate, not
measured, and the two estimates disagree by design (this build did not
compress the narration to force-fit the script's header number — see that
section for why).

## Step 3 — RETIME the Manim scenes against real audio ⚠

**Do not skip this.** Every scene in `scenes.py` currently sets `TARGET` to
the pre-audio `estimated_duration_s` — a placeholder, not yet measured
against real Kokoro output for this reel. Once Kokoro reports real
durations, compare:

```bash
$PY - <<'EOF'
import json, pathlib
d = json.load(open('beat_sheet.json', encoding='utf-8'))
for b in d['beats']:
    m = b['shot'].get('manim')
    if m:
        est, act = b['estimated_duration_s'], b['actual_duration_s']
        print(f"{b['beat_id']}  {m['scene_class']:<32} est {est:>3}s  actual {act:6.2f}s  D{act-est:+6.2f}")
EOF
```

Any beat off by more than ~1.5s: adjust that scene's `TARGET` constant and
`self.wait(...)` holds in `scenes.py` before rendering. Per
`youtube/CLAUDE.md` §5, spread added/trimmed time across several of the
longer holds near a beat's end, not into one static dump — **B05 (Test 2,
100s) and B04/B06/B08 (Tests 1/3/5, ~90-92s each) are this reel's longest
beats and the most likely to need redistribution rather than a single large
`self.wait()`.**

## Step 4 — render Manim (B01-B13)

```bash
cd "$REEL"
declare -A S=( [B01]=B01_FixtureToRealGrader [B02]=B02_InputVsInvented
               [B03]=B03_ScorecardIntro [B04]=B04_Test1ClaimVerification
               [B05]=B05_Test2Determinism [B06]=B06_Test3ConsistencyProbe
               [B07]=B07_Test4GuardrailStress [B08]=B08_Test5Breadth
               [B09]=B09_ScorecardComplete [B10]=B10_ThreeFilesSynced
               [B11]=B11_ElevenToSeven [B12]=B12_TwoChipsHonestLedger
               [B13]=B13_CaughtByAHuman )
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13; do
  $PY -m manim -qh --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
```

**Then move the clips where compile.py actually looks** — it reads
`manim/<BID>.mp4` only, never Manim's own cache path. Skip this and every
beat compiles as a slate while the render reports success:

```bash
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13; do
  cp "media/videos/scenes/1080p30/$B.mp4" "manim/$B.mp4"
done
```

(Use `media/videos/scenes/2160p30/` instead if rendering `-qk` for the
final 4K pass — see Step 6.)

## Step 5 — render Remotion bookends (B00, B14)

```bash
for B in B00 B14; do
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
ffmpeg -i "$REEL/the-number-that-wasnt-there.mp4" -vf fps=2 _qc/frames/%05d.png -y
```

**Read the PNGs** against the 8-point rubric in
`brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md`: edge bleed, title-safe
margins, container overflow, collision, offscreen anchors, legibility,
brand bug, aspect/letterbox. Sample mid-scene frames too, not just settled
final frames — watch specifically:

- **B02's dashed question-mark box** next to the invented claim — confirm
  it doesn't collide with the claim box above it once both are on screen
  at 4K.
- **B04 through B08's six-field test card next to its bespoke visual** —
  these are new, denser layouts than any prior beat in this reel (a
  six-row label+value card sharing the frame with a regex pattern / bubble
  cluster / divergence flag / numeric readout / ticker grid). Confirm the
  card text doesn't collide with, or get crowded by, the adjacent visual at
  4K — this was authored without a render to check against (see
  CHECKS-REPORT.md's legibility-contract note).
- **B08's twelve-tile grid → single-tile push-in** transition — confirm the
  zoomed tile and its two-column close-up don't overlap the fading grid
  mid-transition.
- **B10's "does not fix" `checked()` chip** (uses `symbol="✕"`) — confirm
  the cross glyph actually renders (not a `.notdef` box); this is exactly
  the defect class the channel's own tips warn about.
- **B12's half-filled JUDGMENT chip** — confirm the fill line lands at
  visually half the box height, not skewed by the outline stroke width.
- **B04 through B09's scorecard row** — confirm the five slot chips stay
  legible and don't overlap each other as they transition color across
  beats (grey → amber/green/red), and that the "active, still-pending"
  terracotta-outline state (used in B04-B08 before that beat's own slot
  resolves) reads as visually distinct from an already-resolved slot.

## Step 8 — captions and final files (last of all)

**End state: exactly two final video files, both already carrying muxed
captions** — `the-number-that-wasnt-there.mp4` (4K, 16:9) and
`the-number-that-wasnt-there_shorts.mp4` (9:16) — per `youtube/CLAUDE.md`
§2/§3. There is no separate unsubtitled master and no separately-named
`_subtitled` copy at any point; captions are muxed **in place** into the
one file that ships.

```bash
# 1. generate the caption source (after audio is final and after the last 16:9 compile)
$PY "$TOOLKIT/runtime/scripts/align.py" "$REEL" --model base --language en
$PY "$TOOLKIT/runtime/scripts/make_srt.py" "$REEL"
# writes captions.srt — the source-of-truth subtitle file, not itself a delivered format

# 2. derive the 9:16 cut from the captioned-or-not-yet-captioned 16:9 master
$PY "$TOOLKIT/runtime/scripts/shorts.py" "$REEL"
# writes the-number-that-wasnt-there_shorts.mp4

# 3. mux captions.srt as a soft mov_text stream into BOTH final files, in place —
#    never burned in, never written to a new *_subtitled.mp4 or *_captioned.mp4 path
ffmpeg -i "$REEL/the-number-that-wasnt-there.mp4" -i "$REEL/captions.srt" \
  -map 0 -map 1 -c copy -c:s mov_text \
  -metadata:s:s:0 language=eng "$REEL/_tmp_master.mp4" \
  && mv "$REEL/_tmp_master.mp4" "$REEL/the-number-that-wasnt-there.mp4"

ffmpeg -i "$REEL/the-number-that-wasnt-there_shorts.mp4" -i "$REEL/captions.srt" \
  -map 0 -map 1 -c copy -c:s mov_text \
  -metadata:s:s:0 language=eng "$REEL/_tmp_shorts.mp4" \
  && mv "$REEL/_tmp_shorts.mp4" "$REEL/the-number-that-wasnt-there_shorts.mp4"
```

Re-run `sheet_check.py` against the derived short's own sheet (not this
16:9 sheet) before muxing — the `*916` Remotion patterns have sharply
tighter text limits (see `agents.md`'s 9:16 table). Re-run visual QC on the
9:16 render separately, before muxing captions into it; it is different
geometry, not a guaranteed-clean crop of the 16:9 pass.

**Do not skip the mux step or leave an intermediate file behind as if it
were a deliverable.** If the mux commands above are re-run, they overwrite
the same two filenames in place (via the `_tmp_*` → `mv` pattern) rather
than producing a third or fourth file — there should never be more than
these two `.mp4` files in the folder once this step completes.

## Step 9 — clean the folder

Only these survive: `beat_sheet.json`, the gate docs, this file,
`scenes.py`, `graphics_lib.py`, `manim/*.mp4`, `media/<BeatID>.mp4`, the
archival `the-number-that-wasnt-there.md`, `captions.srt` (the source
subtitle file, not a delivered format), and **exactly the two final
deliverables**: `the-number-that-wasnt-there.mp4` (4K 16:9, captions
already muxed in) and `the-number-that-wasnt-there_shorts.mp4` (9:16,
captions already muxed in). Everything else is regenerable scratch:

```bash
rm -rf "$REEL/_qc" "$REEL/media/videos" "$REEL/__pycache__"
```

Note `media/videos` — the Manim cache — **not** `media/` itself, which
holds the two rendered Remotion bookends.

**Verify the end state before calling this done:**

```bash
ls "$REEL"/*.mp4
# expected: exactly the-number-that-wasnt-there.mp4 and
# the-number-that-wasnt-there_shorts.mp4 — no unsubtitled master, no
# *_subtitled.mp4, no *_captioned.mp4, no third file of any kind.
```

If any other `.mp4` is present in the reel folder at this point (an
unsubtitled master, a separately-named subtitled copy, a leftover
`_tmp_*.mp4`), that means Step 8's mux-in-place didn't complete — fix it
there rather than deleting or renaming files here to paper over it.

## Never publish

Output stays in this folder for human review. Do not touch
`../the-other-agent-wasnt-real/` at any point in this process.
