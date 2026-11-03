# BUILD-PROMPT.md — How the Tutor Stays Grounded in Your Textbook

**Build / reproduction record. Everything below ran between 2026-09-24 and 2026-09-29, except where marked.**

- **Environment:** WSL Ubuntu, plain `python3` (3.10.12). `brutalist.art/.venv` is not used.
- **Repos:** `brutalist.art`, `medhavi-cancer` and `medhavi-hub` were not modified. The only toolkit side effect is the git-ignored render index `runtime/remotion/_bench/consumers.json`, which was accepted.
- **Git:** no git command was run during production. GitHub upload of source and docs is Prarthana's manual step. The videos are on Google Drive.

```bash
cd /mnt/c/Users/prart/HumanitarianAI/MedhavyAITutorVideo/brutalist.art
REEL=/mnt/c/Users/prart/HumanitarianAI/MedhavyAITutorVideo/humanitarians-youtube/fellows/prarthana-s/how-the-tutor-stays-grounded
W=$REEL/capture/capture_masked.py      # reel-local redaction wrapper (built + self-tested)
export PYTHONDONTWRITEBYTECODE=1       # never write __pycache__ into brutalist.art
```

## 1. Wrapper (ran)

```bash
python3 $W --self-test          # offline, file:// pages, dummy term "Testname": 11/11 PASS
```

The wrapper loads the toolkit's `capture_admin.py` as a module and extends its `MASK` JavaScript in memory. It then calls the unmodified `main()`. The design and the leak-check layers are in CAPTURE.md.

## 2. Captures (ran)

Prarthana did these steps herself:
- signed in with `save_session.py`
- set the mask term privately with `read -rs MW_MASK_TEXT && export MW_MASK_TEXT`
- ran each signed-in capture in her own shell, then ran `unset MW_MASK_TEXT`

```bash
python3 skills/make/medhavy-walkthrough/scripts/save_session.py
python3 $W $REEL --run run-signin        --plan $REEL/capture/plan-signin.json        --css-size 1600x900 --dpr 2.4 --no-session
python3 $W $REEL --run run-pilot         --plan $REEL/capture/plan-book.json          --css-size 1600x900 --dpr 2.4   # pilot plan version; discovery only
python3 $W $REEL --run run-book          --plan $REEL/capture/plan-book.json          --css-size 1600x900 --dpr 2.4   # corrected plan; landscape source
python3 $W $REEL --run run-portrait-test --plan $REEL/capture/plan-portrait-test.json --css-size 1280x720 --dpr 3     # no tutor requests
python3 $W $REEL --run run-portrait      --plan $REEL/capture/plan-portrait.json      --css-size 1280x720 --dpr 3     # portrait source
```

- **Plan edits.** `plan-book.json` was edited between the pilot and `run-book`:
  - the 5.4.2 card was confirmed
  - a scroll-to-bottom step and early screenshots were added before the follow-up
  - the "Thanks!" steps were removed
- **Redaction review.** After each run, frame contact sheets were built with `python3 $W --review-sheet $REEL --run <run>`, reviewed, and deleted.
- **Not run:** `run-signin-916src`.
- **Tutor memory:** never cleared.

## 3. Narration (ran)

```bash
python3 runtime/scripts/generate_audio_kokoro.py $REEL                         # landscape, am_onyx
python3 runtime/scripts/generate_audio_kokoro.py $REEL/vertical --only B11     # vertical-only B11 wording
```

Durations are the master clock. The vertical B11 take (15.53 s) was padded with silence to its 22.0 s window. The raw take is kept at `vertical/mp3/beat-B11.take.mp3`.

## 4. Landscape media (ran)

**Frame-exact footage cuts.** The toolkit's `prepare_media.py` calls `hashlib.file_digest`, which needs Python 3.11, and WSL has 3.10. So it was run unmodified, with an in-memory backport:

```bash
python3 -c "
import hashlib, runpy, sys
if not hasattr(hashlib, 'file_digest'):
    def file_digest(f, name):
        h = hashlib.new(name)
        for c in iter(lambda: f.read(1<<20), b''): h.update(c)
        return h
    hashlib.file_digest = file_digest
s = 'skills/make/medhavy-walkthrough/scripts/prepare_media.py'
sys.argv = [s, '$REEL']
runpy.run_path(s, run_name='__main__')"
```

**Library bookends** (B00, B01, B13, B14, B15) use the Playwright Chromium already installed in WSL:

```bash
export ART_CHROME=$HOME/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome ART_CHROME_MODE=chrome-for-testing
python3 runtime/scripts/remotion_scenes.py $REEL
```

## 5. Reel-local Remotion scenes (built and rendered)

**Project:** `remotion/` in this folder.
- **Source files:** `src/index.ts`, `src/Root.tsx`, `src/theme.ts`, `src/GroundingFlow.tsx` (`GroundingFlow`, `GroundingFlow916`), `src/PanelFocus916.tsx`, plus a stub `package.json`.
- **Symlinks (read only, not in the upload):** `remotion/node_modules` points to `brutalist.art/runtime/remotion/node_modules`, and `remotion/public/fonts` to `brutalist.art/runtime/fonts`. `remotion/public/capture` points to `../../capture`. Recreate them with:
  ```bash
  cd $REEL/remotion && ln -sfn $PWD/../../../../../brutalist.art/runtime/remotion/node_modules node_modules
  mkdir -p public && ln -sfn $PWD/../../../../../brutalist.art/runtime/fonts public/fonts && ln -sfn ../../capture public/capture
  ```
- **Render command** (one render at a time: parallel 4K renders exhausted memory once). Retry once on the known intermittent "Timed out … trying to connect to the browser" start-up failure.
  ```bash
  B=$HOME/.cache/ms-playwright/chromium-1243/chrome-linux64/chrome
  npx remotion render src/index.ts <Comp> <out.mp4> --props=<props.json> --scale=2 --image-format=png --crf=16 \
      --concurrency=2 --bundle-cache=false --browser-executable=$B --chrome-mode=chrome-for-testing
  ```

| Output | Composition | Props |
|---|---|---|
| `media/B10.mp4` | `GroundingFlow` | `{"durationSeconds": 17.133}` |
| `pantry/B10-916.mp4` | `GroundingFlow916` | the same |
| `pantry/B02-916.mp4`, `pantry/B03-916.mp4` … `pantry/B12-916.mp4` (every SCREEN beat) | `PanelFocus916` | each beat's `panelfocus_props` in `vertical-windows.json` |

## 6. Landscape final (ran)

```bash
python3 skills/make/medhavy-walkthrough/scripts/limit_audio.py $REEL
./art medhavy-walkthrough --check $REEL                  # PASS
./art final $REEL --height 2160 --fps 30 --out $REEL/exports/landscape
```

**Output:** `exports/landscape/claude-liam-medhavy-how-the-tutor-stays-grounded.mp4` (3840×2160, 167.93 s). GATE T PASS; Gate V clean.

## 7. Vertical final (ran, via the documented direct-compile exception)

```bash
./art vertical $REEL                                      # plans vertical/ with its own beat sheet
for f in $REEL/pantry/B??-916.mp4; do b=$(basename $f -916.mp4); cp -f $f $REEL/vertical/media/$b.mp4; done   # portrait clips into the vertical slots
python3 runtime/scripts/remotion_scenes.py $REEL/vertical         # *916 bookends
python3 skills/make/medhavy-walkthrough/scripts/limit_audio.py $REEL/vertical
python3 runtime/scripts/compile.py $REEL/vertical --height 3840 --fps 30 --out $REEL/exports/vertical
```

**Output:** `exports/vertical/claude-liam-medhavy-how-the-tutor-stays-grounded-vertical.mp4` (2160×3840, 167.93 s).

- **Why not `art final`:** it runs GATE T first with no bypass. GATE T fails only on B15, the locked `ClaudeTitleOutro916` handle, which can't be changed.
- **What still ran:** `compile.py` still runs Gate V on the candidate and writes the `.verified.json` receipt.
- **Approval and waivers:** approved by Prarthana on 2026-09-29. B01 and B13 carry `qc.sparse_by_design` underfill waivers. See QC-REPORT.md.

## 8. Handoff

Prarthana uploaded both finals to Google Drive. She is uploading the source and docs to GitHub manually. Nothing was published to YouTube.
