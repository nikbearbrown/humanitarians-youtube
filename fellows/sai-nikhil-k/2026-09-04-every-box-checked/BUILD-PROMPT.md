# BUILD-PROMPT — Every Box, Checked

Paste-ready build for `weekly_updates/09-04-01/`
Slug **`claude-sai-every-box-checked`** · 8 beats · Kokoro `am_onyx`, free/local
Two masters: **16:9 at 3840×2160** and **9:16 at 2160×3840**

Run every command from the toolkit root
(`/Users/nikhilkunapareddy/Documents/brutalist.art`).

---

## STEP 0 — the plates (already built, rerun only if the source changes)

```bash
python3 weekly_updates/09-04-01/make_plates.py
```

Writes `media/B02.png` (3840×2160, all 16 cells) and `pantry/B02-916.png`
(2160×3840, 8 cells re-tiled as a scale ramp). Needs **Pillow on system
python3**, not `.venv`.

## STEP 1 — sign GATE P (human)

Open `weekly_updates/09-04-01/PEDAGOGY.md`, read the narration and the review
checklist, and replace the blank on the `VERDICT:` line at the very bottom with
the word `PASS`. Save. Audio should not be generated before this.

## STEP 2 — narration audio (the master clock)

```bash
.venv/bin/python runtime/scripts/generate_audio_kokoro.py weekly_updates/09-04-01
```

**Use the `.venv` interpreter.** Kokoro is not importable from the default
`python3`; `./art doctor` reporting audio as blocked is that interpreter
mismatch, not a missing model. (Pillow is the reverse — see STEP 0.)

## STEP 3 — render the 16:9 beats

```bash
python3 runtime/scripts/remotion_scenes.py weekly_updates/09-04-01
```

Seven Remotion beats; B02 is a still and is skipped. `--scale` is chosen per
composition so every beat lands at true 3840×2160. Add `--force` (or
`--only B0X`) to re-render after an edit — beats whose `media/*.mp4` exists are
skipped otherwise.

> If a render is interrupted, delete any stray `media/_ext_*` before rerunning:
> a leftover means that beat is double-length and the next run will skip it.

## STEP 4 — compile the 16:9 master + visual QC

```bash
./art run weekly_updates/09-04-01 --height 2160
```

→ `claude-sai-every-box-checked.mp4` (clean 4K master)
→ `claude-sai-every-box-checked-slate.mp4` (labelled review cut)
→ `_qc/` frame samples + `REPORT.md`, and `qc-sheet.png` — **look at these.**

Fast preview first, optionally: `./art run weekly_updates/09-04-01 --height 1080`.

## STEP 4b — outro audio is speed-corrected (already done)

B07 uses **`LogoOutro`**, a 120-frame (4.0s) card that fades out at its end,
while `remotion_scenes.py` freeze-extends a short render by cloning the final
frame — which is **black**. So B07's audio is generated at `--speed 1.06` to
land at 3.9s, inside the card:

```bash
.venv/bin/python runtime/scripts/generate_audio_kokoro.py weekly_updates/09-04-01 \
  --only B07 --speed 1.06
```

If you re-edit B07's line, keep it to ~10 words and re-apply that flag, or the
tail grows into seconds of black. The last ~3 frames are black regardless —
that is the card's own designed fade-out.

## STEP 5 — derive the 9:16 beat sheet

```bash
python3 runtime/scripts/shorts.py weekly_updates/09-04-01
```

Writes `short/beat_sheet.json` with `aspect_ratio: "9:16"` and rewires each beat
to its `*916` sibling. Expect it to report **B02 taking the `pantry` override** —
that is `pantry/B02-916.png`, not a centre cut. If any beat reports a missing
`*916` composition, stop: every pattern in this reel has one.

## STEP 6 — render the portrait beats

```bash
python3 runtime/scripts/remotion_scenes.py weekly_updates/09-04-01/short
```

## STEP 6b — REQUIRED: rebuild the endcard at 4K

`shorts.py` draws `END.png` on a canvas hardcoded to **1080×1920** and
**rewrites it on every run**, so a 4K compile upscales it and `compile.py`
warns `WARNING END: still 1080x1920 under output 2160x3840`. Re-fix it as the
LAST step before compiling, every time you re-run STEP 5:

```bash
python3 - <<'PY'
import importlib.util, pathlib
import PIL.ImageFont as PF
from PIL import Image
spec = importlib.util.spec_from_file_location("shorts", "runtime/scripts/shorts.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
out = pathlib.Path("weekly_updates/09-04-01/short/media/END.png")
m.W, m.H = 2160, 3840          # canvas
_tt = PF.truetype               # ...and the type, or it renders half-size
PF.truetype = lambda p, size, *a, **k: _tt(p, size * 2, *a, **k)
try:    m.endcard_png(out, "@HumanitariansAI", "", dark=True)
finally: PF.truetype = _tt
print(Image.open(out).size)     # expect (2160, 3840)
PY
```

## STEP 6c — compile the 9:16 master at 4K

```bash
python3 runtime/scripts/compile.py weekly_updates/09-04-01/short --height 3840
```

→ `short/claude-sai-every-box-checked-short.mp4` at **2160×3840**.

> **`--height 3840`, not 1920.** `shorts.py` prints a `--height 1920` hint,
> which is 1080p portrait. `compile.py` derives width from the sheet's
> `aspect_ratio`, so 3840 × 9/16 = 2160 — a true 4K vertical master.

## STEP 7 — verify both

```bash
for f in weekly_updates/09-04-01/claude-sai-every-box-checked.mp4 \
         weekly_updates/09-04-01/short/claude-sai-every-box-checked-short.mp4; do
  ffprobe -v error -select_streams v:0 -show_entries stream=width,height,nb_frames \
          -of default=nw=1 "$f"; done
```

Expect **3840×2160** and **2160×3840**. Then open both and watch them, and skim
`_qc/` for each — the probe alone is not verification.

---

## Editing

Change wording or pacing by editing `narration_text`, then rerun
**STEP 2 → STEP 3 (`--force`) → STEP 4**, and **STEP 5 → STEP 6** for the
vertical cut. Never hand-edit a duration; the audio is the clock.

If you change B02's plate, rerun STEP 0 first. The B02 narration carries **no
positional reference** ("top left", "two rows down") on purpose — the same mp3
plays over both plates and the cell order differs between them, so keep it that
way.

## Known false positives in `_qc/`

- **Gate V underfill** on the centred title and verdict cards. Expected — they
  are centred by design.
- **Edge bleed on the 9:16 cut.** Check the clean master before believing it.
- **`./art doctor` / `./setup` crashing** with `declare: -A: invalid option` on
  stock macOS bash 3.2 — harmless, it is only the readiness table.
