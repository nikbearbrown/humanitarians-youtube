# BUILD-PROMPT — Ground Truth First (16:9 + 9:16)

Paste-ready. Run every command from the toolkit root
(`/Users/nikhilkunapareddy/Documents/brutalist.art`).
`<reel>` = `weekly_updates/08-28`.

---

## STEP 0 — plates (already done, re-run only if the source changes)

```bash
python3 weekly_updates/08-28/make_plates.py     # system python3 — needs Pillow
```

Writes `media/B03.png` (3840x2160) and `pantry/B03-916.png` (2160x3840), and
prints the box centroid in plate space. **If that centroid moves, update
`shot.focus` on B03 in `beat_sheet.json`** — it is currently `[0.488, 0.574]`.

## STEP 1 — GATE P (human)

Open `weekly_updates/08-28/PEDAGOGY.md`, work the review checklist, and change
the VERDICT line's blank to the word PASS. Save. Audio refuses to run until it
is signed, and Claude must not sign it.

## STEP 2 — narration audio (the master clock, free, ~30s)

```bash
.venv/bin/python runtime/scripts/generate_audio_kokoro.py weekly_updates/08-28
```

Kokoro needs the venv interpreter, not the system `python3`. This is the
reverse of STEP 0, which needs system `python3` for Pillow.

## STEP 3 — render the beats (true 4K, a few minutes)

```bash
python3 runtime/scripts/remotion_scenes.py weekly_updates/08-28
```

Foreground only. Never hand-roll `npx remotion render`.

## STEP 4 — compile the 16:9 master + visual QC

```bash
./art run weekly_updates/08-28
```

→ `claude-sai-ground-truth-first.mp4` (clean 4K master)
→ `claude-sai-ground-truth-first-slate.mp4` (labelled review cut)
→ `_qc/` — **look at the frames and the qc-sheet, not just the probe.**

Faster preview first: `./art run weekly_updates/08-28 --height 1080`

## STEP 5 — derive the 9:16 cut

```bash
python3 runtime/scripts/shorts.py weekly_updates/08-28
```

The reel is ~126s, under the 180s cap, so the plan should report **no beats
dropped** and **no outro rewrite** — read the printed plan and confirm that
before continuing. It rewires each Remotion beat to its `*916` sibling,
re-renders them portrait, and honours `pantry/B03-916.png` for the still.

Then:

```bash
python3 runtime/scripts/compile.py weekly_updates/08-28/short --review --height 1920
```

If `shorts.py` reports it rewrote the outro (it should not at this length), the
one regenerated mp3 is:

```bash
.venv/bin/python runtime/scripts/generate_audio_kokoro.py weekly_updates/08-28/short --only B07
```

## STEP 6 — final masters

```bash
./art final weekly_updates/08-28
```

Naming follows the series convention (`sainikhil_0828_1.mp4` for the long,
`sainikhil_0828_1_short.mp4` for the vertical) once both cuts pass QC.

---

## If you change the words

Edit `narration_text` in `beat_sheet.json`, then STEP 2 → STEP 3 (`--force`) →
STEP 4 → STEP 5. **Never hand-edit durations** — audio is the clock.

## Known traps for this reel

- **Gate V will likely flag `B03-916` as UNDERFILL.** A landscape photograph in
  a 9:16 frame is structurally short even after the composed crop. Check the
  frame before treating it as a defect; on the clean master it is a MAJOR, not
  a BLOCKER.
- **`typeScale: 1.4`** is set on B02 and B04. The `*916` siblings take `{data}`
  only and ignore it — that is expected, not a prop mismatch.
- **`ScaleComparison` is not usable for the 10% figure.** Its axis is `log10`,
  built for orders of magnitude. It was rejected during authoring; do not
  "improve" B04 by switching to it.
- **`scenes.py` must stay free of any Manim scene declaration**, including
  inside its docstring — GATE F scans it as text.
