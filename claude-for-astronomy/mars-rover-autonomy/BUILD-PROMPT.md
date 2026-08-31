# BUILD-PROMPT — rebuilding *Nobody Is Coming to Approve It.*

Everything needed to rebuild this reel from the folder, for $0.00, on a clean
machine with `brutalist.art` and its `.venv`.

## 0. Environment (Windows — this is not optional)

```bash
export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8
export PATH="E:/NEU/Jobs/Humanitarians_AI/brutalist.art/.venv/Scripts:$PATH"
```

`run.sh`'s inline Python reads `beat_sheet.json` without an explicit encoding
and dies on cp1252 without these. Unpatched in the toolkit; set them every time.

## 1. Plates

```bash
python assets/gen_mars.py
```

Deterministic — same seeds in, byte-identical PNGs out. Seeds are in
`SOURCES.md`. Read `_qc/asset_sheet.png` before trusting them; three separate
rendering defects in this generator were caught by looking, not by a gate.

**If you re-tune a plate, delete `media/videos` before re-rendering.** Manim
caches partial movie files keyed on scene *code*, and its cache key does not hash
the contents of images the scene loads. Deleting `manim/*.mp4` is not enough.

## 2. GATE P

`PEDAGOGY.md` carries the full narration. A human reads it and changes the
verdict line from PENDING. Audio will not generate until they do.

**Do not write the passing verdict string anywhere else in that file.**
`generate_audio_kokoro.py` matches it as a plain substring anywhere in the
document, so quoting it in an explanatory sentence silently unlocks the gate —
which is exactly what happened to the first draft of this reel's PEDAGOGY.md.

## 3. Audio — the clock

```bash
python runtime/scripts/generate_audio_kokoro.py <reel>
```

Kokoro `af_bella`, local, $0.00. Measured mp3 durations become the master clock.
**Never fix timing by hand — change the narration, regenerate, recompile.**

## 4. The 16:9 cut

```bash
bash runtime/scripts/run.sh <reel>            # 4K native (HEIGHT=2160)
python runtime/scripts/compile.py <reel> --height 2160     # or ./art final <reel>
```

`run.sh` runs GATE A → GATE W → the Manim stage → GATE B → compile. At 4K the
whole thing exceeds a 10-minute call for a 10-scene reel, so run the Manim stage
separately if you are on a call budget:

```bash
for S in B01_Presenter B02_OneBreath B03_LightTime B04_WhatItSees B05_TheFan \
         B06_Aegis B07_Snowdrift B08_TheProfile B09_Result B10_TwoLimits; do
  manim -qk --fps 24 -r 3840,2160 scenes.py "$S"
done
```

Re-entry is safe: `run.sh` skips any beat whose slot is already filled.

## 5. The 9:16 cut

```bash
python runtime/scripts/shorts.py <reel> --drop --no-endcard
python runtime/scripts/remotion_scenes.py <reel>/short     # FOREGROUND
bash runtime/scripts/run.sh <reel>/short --height 3840
python runtime/scripts/compile.py <reel>/short --height 3840
```

`--drop` with no values is a **manual plan that drops nothing** — that is what
makes this a full-length 9:16 cut of the same 14 beats rather than a 3:00 Short.
Because nothing is dropped, the outro is not rewritten and no audio is
regenerated; the short's `mp3/` are copies of the parent's.

Two things make this work:

- **`scenes.py` is aspect-aware.** It reads `PORTRAIT` from the frame and lays
  out accordingly, and it repeats Manim's portrait frame-sync itself (Manim CE
  sets pixel dims from `-r` but does not recompute `frame_width`). Copy it into
  `short/` — it needs no edits.
- **The Remotion bookends have `…916` compositions** already registered in
  `runtime/remotion/src/Root.tsx`, so `shorts.py`'s ONDA CHECK rewires them and
  nothing is centre-cut.

`shorts.py` was patched during this build to fall back to `shutil.copy2` when
`symlink_to` fails; on Windows it raises `OSError 1314` without developer mode
and used to kill the whole derivative.

## 6. Render Remotion only through the wrapper

```bash
python runtime/scripts/remotion_scenes.py <reel>     # FOREGROUND — never background
```

Never hand-roll `npx remotion render`. The wrapper renders `--scale=2`, so the
1920×1080 compositions land at true 3840×2160 and the 1080×1920 ones at
2160×3840, with supersampled text.

## 7. Verify by LOOKING

```bash
./art todo <reel>
```

Then read `_qc/contact_sheet.png` and `_qc/REPORT.md`. **An mp4 probe is not
verification.** Every defect that mattered in this build — the shadowless
plates, the invisible contours, the path that hugged obstacles, the signature on
the card border, the label on the closing line — was found by reading a picture.
None of them would have failed a probe.

Render final-frame stills in both aspects before committing to a 4K pass:

```bash
manim -s -r 960,540 --format=png --disable_caching scenes.py <Class>   # 16:9
manim -s -r 540,960 --format=png --disable_caching scenes.py <Class>   # 9:16
```

## 8. Gates, and what each one caught here

| Gate | Command | What it caught |
|---|---|---|
| L | `runtime/qc/beat_lint.py <reel>` | nothing — clean first run |
| A | `runtime/qc/static_scene_check.py scenes.py --class <C>` | nothing — clean first run |
| W | `runtime/qc/wcag_margin_check.py scenes.py --class <C>` | nothing |
| B | `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict [--portrait]` | nothing — but only because the stills pass had already fixed eight layout defects |
| V | run by `compile.py --review` | *(see `_qc/REPORT.md`)* |
| P | human signature on `PEDAGOGY.md` | a false-open on a substring match |

`ART_STRICT=0` relaxes GATE V. **It was not used.**

## 9. Never publish

There is no publishing machinery here. Both masters stay in this folder.
