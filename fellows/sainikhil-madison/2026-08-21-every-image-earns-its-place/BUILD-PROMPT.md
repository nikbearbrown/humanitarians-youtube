# BUILD-PROMPT — Every Image Earns Its Place

Paste-ready end-to-end build for `weekly_updates/08-21/`. Run every command from
the toolkit root, `/Users/nikhilkunapareddy/Documents/brutalist.art`.

Produces two masters:

| Cut | File | Resolution |
|---|---|---|
| 16:9 long | `weekly_updates/08-21/claude-sai-every-image-earns-its-place.mp4` | 3840×2160 |
| 9:16 Shorts | `weekly_updates/08-21/short/claude-sai-every-image-earns-its-place-short.mp4` | 2160×3840 |

---

## Interpreter note (this bites every time)

Two different Pythons are needed, and neither is a drop-in for the other:

- **Kokoro TTS → `.venv/bin/python`.** The module is `kokoro_onnx`, and it is
  only installed in the venv. It does *not* need `soundfile`; it writes WAV via
  the stdlib and shells out to ffmpeg.
- **Pillow → system `python3`.** Pillow is *not* in the venv, so `make_plates.py`
  and anything else drawing images must use `python3`.

`./art doctor` reports audio as blocked when invoked under the wrong
interpreter. Ignore it; the commands below are correct.

---

## STEP 0 — the still plates (already built; re-run only after replacing a screenshot)

```bash
cd weekly_updates/08-21 && python3 make_plates.py && cd -
```

Writes `media/B04.png`, `media/B05.png` (3840×2160) and
`pantry/B04-916.png`, `pantry/B05-916.png` (2160×3840). The portrait pair is the
override slot `shorts.py` honours for user media — without it, both screenshots
would be centre-cut to a narrow vertical slice.

## STEP 1 — GATE P (human, not Claude)

Open `weekly_updates/08-21/PEDAGOGY.md`, work the review checklist, and change
the blank on the verdict line at the bottom to the word `PASS`. Save. Audio
refuses to run until that line is signed.

## STEP 2 — narration audio (the master clock) · free, ~30s

```bash
.venv/bin/python runtime/scripts/generate_audio_kokoro.py weekly_updates/08-21
```

## STEP 3 — render the seven Remotion beats · a few minutes

```bash
python3 runtime/scripts/remotion_scenes.py weekly_updates/08-21
```

Scale is chosen per composition so every beat lands at true 3840×2160 — 2× for
the 1920×1080 Claude UI scenes, 3× for the 1280×720 deck patterns. Add `--force`
(or `--only B0X`) to re-render after edits; beats with an existing `media/*.mp4`
are otherwise skipped.

## STEP 4 — compile the 4K master + visual QC

```bash
./art run weekly_updates/08-21 --crf 12
```

→ the clean 4K master, a `-slate.mp4` review cut, and `_qc/` frame samples.
**Look at `_qc/` and `qc-sheet.png`** — never trust the mp4 probe alone.
For a fast look first: `./art run weekly_updates/08-21 --height 1080`.

## STEP 5 — derive the 9:16 Shorts cut

```bash
python3 runtime/scripts/shorts.py weekly_updates/08-21
```

At 126s estimated the reel is under the 180s cap, so **no beats are dropped and
the outro is not rewritten** — meaning no narration is regenerated. The script
rewires each Remotion beat to its `*916` portrait sibling (all seven exist), picks
up the two `pantry/*-916.png` plates, and inherits the endcard handle from
`metadata.folder_chip` (`@HumanitariansAI`).

## STEP 6 — render + compile the short at vertical 4K

```bash
python3 runtime/scripts/remotion_scenes.py weekly_updates/08-21/short
python3 runtime/scripts/compile.py weekly_updates/08-21/short --height 3840 --crf 12
```

`--height 3840` is what makes the short 2160×3840; the portrait compositions are
registered at 1080×1920 and render at 2× . Add `--review` for a slated review
cut alongside the clean one.

---

## If you change wording

Edit `narration_text` in `beat_sheet.json`, then STEP 2 → STEP 3 `--force` →
STEP 4, and re-derive the short. **Never hand-edit durations** — audio is the
clock.

## Known QC noise (not defects)

- **GATE V underfill on B08 / B06.** Centred title and verdict cards trip the
  canvas-fill check every time. Look at the frame before re-rendering anything.
- **A stray `_ext_*` in `media/`** means a render was killed midway and that
  beat is unretimed. Delete it and re-render that beat with `--only`.
- **`./art doctor` / `./setup` crashing with `declare: -A: invalid option`** is
  stock macOS bash 3.2 and affects only the readiness table.
