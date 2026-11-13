# BUILD-PROMPT — `hussain-snowshift-migration-overview` · "Compiling Is Not Migrating."

Paste-ready. Builds **both** 4K masters — 16:9 and full-length native 9:16 —
from this folder's `beat_sheet.json`. Never publishes.

## Environment (Windows / Git Bash)

```bash
cd C:/Users/Hussain/Desktop/Project/Brutalist/Brut/brutalist.art
export PATH="$PWD/venv/Scripts:$PATH"   # python3 → the venv (kokoro-onnx, PIL, numpy)
export ART_HOME="$PWD" PYTHONUTF8=1
REEL=../snowshift-videos/youtube/hussain-snowshift-migration-overview
python3 -c "import kokoro_onnx, PIL, numpy; print('deps ok')"
```

## The prompt

> Build the reel at `snowshift-videos/youtube/hussain-snowshift-migration-overview`
> to two finished 4K masters, 16:9 and full-length 9:16, following its
> `beat_sheet.json`. `FACTCHECK.md` lists every claim; introduce no new ones.
> Do not publish.
>
> 1. **Audio is the clock.** Only if narration changed:
>    `python3 runtime/scripts/generate_audio_kokoro.py $REEL [--only Bxx]`.
> 2. **Pin compositions to the audio:** `python3 $REEL/sync_durations.py $REEL`.
> 3. **Render the 16:9 beats:** `python3 runtime/scripts/remotion_scenes.py $REEL`
>    (foreground; never hand-roll `npx remotion render`). `--only Bxx --force`
>    re-renders one beat.
> 4. **Compile the 16:9 master:** `python3 runtime/scripts/compile.py $REEL --height 2160`.
> 5. **Derive the vertical companion:** `./art vertical $REEL` (all beats, no
>    shortening; every pattern has a `*916` twin), then
>    `python3 $REEL/sync_durations.py $REEL/vertical`,
>    `python3 runtime/scripts/remotion_scenes.py $REEL/vertical`,
>    `python3 runtime/scripts/compile.py $REEL/vertical --height 3840`.
> 6. **VISUAL QC LAW — read the frames, both aspects.** Sample each beat at
>    ~15/50/85% of its span and audit edge bleed, title-safe, overflow,
>    collision, legibility, brand mark, aspect and canvas fill. Fix root causes
>    in `runtime/remotion/src/scenes/SnowshiftIllus.tsx` and re-render.
> 7. **Report** both paths, both resolutions and the QC verdict in `QC-STATUS.md`.

## Things that bite

- `durationSeconds` must be on every beat (step 2), or late reveals are trimmed.
- Root.tsx registrations must be literal `id="Name"` / `id="Name916"`:
  `shorts.py` and the scene index grep for them.
- GATE V's underfill heuristic flags the B01 typing beat at mid-beat by
  construction (see the Cortex reel's QC-STATUS.md); `./art final` refuses on it.
- B09 says "not run live yet": re-record it after the first live deploy.
