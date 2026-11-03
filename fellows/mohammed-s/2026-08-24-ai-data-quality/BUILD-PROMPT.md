# BUILD-PROMPT — `ai-data-quality` · "The Rule, Not The Report."

Paste-ready. Builds **both** masters end to end — the 16:9 4K cut and the
full-length 9:16 4K cut — from a clean checkout. Run from the folder that
contains `brutalist.art/` and `mycroft-videos/`. Never publishes.

---

## Environment (Windows / Git Bash)

The toolkit's scripts all call `python3`. On this machine the system `python3`
does **not** have the dependencies; the venv does. Put the venv first on PATH
for the whole session, and set `ART_HOME` so the Kokoro model files resolve:

```bash
cd brutalist.art
export PATH="$PWD/venv/Scripts:$PATH"     # python3 → the venv (kokoro-onnx, manim, PIL, numpy)
export ART_HOME="$PWD"
REEL=../mycroft-videos/youtube/ai-data-quality
python3 -c "import kokoro_onnx, PIL, numpy; print('deps ok')"
```

---

## The prompt

> Build the reel at `mycroft-videos/youtube/ai-data-quality` to two finished
> 4K masters — 16:9 and full-length 9:16 — following its `beat_sheet.json`.
> `PEDAGOGY.md` is signed (GATE P: VERDICT PASS) and `FACTCHECK.md` declares
> every on-screen figure a worked example, so no new claims may be introduced.
> Do not publish; leave both masters in the reel folder.
>
> 1. **Audio is the clock.** Regenerate only if narration changed:
>    `python3 runtime/scripts/generate_audio_kokoro.py $REEL`. Never hand-fix
>    a duration — regenerate and recompile.
> 2. **Pin the compositions to the audio:**
>    `python3 $REEL/sync_durations.py $REEL` — copies each measured
>    `actual_duration_s` into the beat's `durationSeconds` prop, which
>    `calculateMetadata` in Root.tsx turns into `durationInFrames`. Skip this
>    and every Dq beat either freezes or gets trimmed.
> 3. **Render the 16:9 beats** (foreground, never hand-rolled `npx remotion`):
>    `python3 runtime/scripts/remotion_scenes.py $REEL`
> 4. **Compile the 4K master:** `bash runtime/scripts/run.sh $REEL --height 2160`
>    — this also runs GATE L (beat-mix lint) and GATE V (frame-level visual
>    QC). `scenes.py` defines no Scene classes on purpose, so the Manim gates
>    are correctly skipped.
> 5. **Derive the vertical cut:** `python3 $REEL/make_916.py --force`, then
>    `python3 $REEL/sync_durations.py $REEL/916`, then
>    `python3 runtime/scripts/remotion_scenes.py $REEL/916`, then
>    `python3 runtime/scripts/compile.py $REEL/916 --height 3840`.
>    Do **not** use `./art shorts` here — it enforces the 3:00 Shorts cap by
>    dropping beats, and this reel is 3:07. `make_916.py` keeps all twelve.
> 6. **VISUAL QC LAW — look at the frames, both aspects.** The mp4 probe is a
>    file check, not QC. Sample `ffmpeg -i <mp4> -vf fps=2 _qc/frames/%05d.png`
>    plus each beat at ~15/50/85% of its span, actually READ the PNGs, and
>    audit the 9-point rubric: edge bleed, title-safe margins, container
>    overflow, collision, offscreen anchors, legibility, brand bug, aspect,
>    and canvas fill. Log findings in `_qc/REPORT.md`. Fix root causes in
>    `runtime/remotion/src/scenes/DataQualityIllus.tsx` and re-render until
>    zero BLOCKER and zero MAJOR remain.
> 7. **Report** both output paths, both resolutions, and the QC verdict.

---

## Expected outputs

| File | Resolution | Notes |
|---|---|---|
| `ai-data-quality.mp4` | 3840×2160 | clean 16:9 master |
| `ai-data-quality-slate.mp4` | 3840×2160 | review cut, beat labels + timecode |
| `916/ai-data-quality-916.mp4` | 2160×3840 | clean 9:16 master, all 12 beats |
| `916/ai-data-quality-916-slate.mp4` | 2160×3840 | review cut |

Runtime 3:07 in both. Cost: **$0.00** — Kokoro is local, Remotion is local,
there is no API key anywhere in this pipeline.

---

## Things that will bite you (learned on the first build)

- **`python3` on PATH.** Every gate and script shells out to `python3`. If it
  resolves to a bare system Python, `generate_audio_kokoro.py` dies on
  `kokoro_onnx` and `final_frame_check.py` silently exits 3 (needs Pillow +
  numpy). Export the venv onto PATH once, at the top of the session.
- **Text encoding.** The toolkit's scripts were written for POSIX; several
  called `Path.read_text()` / `open()` with no encoding, which on Windows
  defaults to cp1252 and dies on this reel's own em dashes and arrows —
  sometimes *after* truncating the file it was writing. Fixed in
  `generate_audio_kokoro.py`, `shorts.py`, `qc/beat_lint.py` and
  `qc/final_frame_check.py`; the same pattern is worth checking in any script
  this reel starts using.
- **Never `npx remotion render` by hand.** `remotion_scenes.py` supplies
  `--scale=2` (true 4K from the 1920×1080 / 1080×1920 comps),
  `--image-format=png` (removes Remotion's JPEG-q80 ceiling on flat brand
  colour) and `--crf=16`, then reconciles the clip to the beat length. A hand
  render gets none of that.
- **`compile.py` center-cuts a clip that is LONGER than its beat.** That is
  why step 2 exists. A composition left at its default length loses its
  opening and its payoff, symmetrically, and it is not obvious in a thumbnail.
- **Never kill a render mid-beat, and verify if you did.** `render_beat()`
  finishes by writing `media/_ext_<BID>.mp4` and moving it over the target.
  Killed between those steps, the slot keeps the RAW composition render — full
  comp length, not beat length — and because `render_beat()` skips any beat
  whose output already exists, **a re-run will not repair it**. The wrong-length
  clip then flows into the cut and gets center-cut, losing both ends of the
  beat, and nothing flags it. Run `python3 verify_clips.py` after any
  interruption and before every compile; `--fix` deletes the bad clips so they
  rebuild.
- **Don't run `npx tsc` (or anything that loads the whole Root.tsx type graph)
  while renders are live.** Root.tsx is ~3,600 lines and ~600 compositions; on
  a 16 GB box with renders running, the typecheck is enough to push it into
  swap and get render workers killed. Typecheck between renders, not during.
- **Check for other sessions before killing processes.** More than one Claude
  session may be rendering into this same toolkit. `taskkill /F /IM node.exe`
  is machine-wide and will abort their work too — use `ListAgents` first, and
  prefer stopping your own task over killing by image name.
- **`ART_CONCURRENCY=4`** (env-gated in `remotion_scenes.py`, default 1) is a
  large speedup on an 8-core box. The default stays 1 because a 4K PNG frame
  pipeline is memory-hungry and one OOM-ed worker takes the beat with it.
