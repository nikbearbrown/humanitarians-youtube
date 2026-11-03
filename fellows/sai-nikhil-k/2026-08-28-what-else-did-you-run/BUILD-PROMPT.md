# BUILD-PROMPT — What Else Did You Run? (16:9 4K + 9:16 4K)

Paste-ready. Run every command from the toolkit root
(`/Users/nikhilkunapareddy/Documents/brutalist.art`).
`<reel>` = `weekly_updates/08-28-2`.

Source: `~/Documents/manipulator/blog/how-to-lie-with-data.md`.
All-Remotion — no Manim, no plates, no paid anything.

---

## STEP 1 — GATE P (human)

Open `weekly_updates/08-28-2/PEDAGOGY.md`, work the review checklist, and change
the VERDICT line's blank to the word PASS. Save. Audio refuses to run until it
is signed, and Claude must not sign it.

## STEP 2 — narration audio (the master clock, free, ~30s)

```bash
.venv/bin/python runtime/scripts/generate_audio_kokoro.py weekly_updates/08-28-2
```

Kokoro needs the venv interpreter, not the system `python3`.

**Check the total before rendering.** The Shorts cap is 180s and this reel is
budgeted at ~165s (413 narration words). If Kokoro lands it over 180s, trim
`narration_text` on B00 and B03 and re-run — do not let `shorts.py` start
dropping beats, because the whole point of this build is that both cuts carry
identical content.

## STEP 3 — render the beats (true 4K, a few minutes)

```bash
python3 runtime/scripts/remotion_scenes.py weekly_updates/08-28-2
```

Foreground only. Never hand-roll `npx remotion render`. `scale_for` picks the
scale per composition, so the 1280x720 deck patterns render at `--scale=3` and
the 1920x1080 Claude UI scenes at `--scale=2` — every beat leaves at 3840x2160.

## STEP 4 — compile the 16:9 4K master + visual QC

```bash
./art run weekly_updates/08-28-2
```

→ `claude-sai-what-else-did-you-run.mp4` (clean 4K master, 3840x2160)
→ `claude-sai-what-else-did-you-run-slate.mp4` (labelled review cut)
→ `_qc/` — **look at the frames and the qc-sheet, not just the probe.**

Faster preview first: `./art run weekly_updates/08-28-2 --height 1080`

## STEP 5 — derive the 9:16 4K cut

```bash
python3 runtime/scripts/shorts.py weekly_updates/08-28-2
```

Read the printed plan and confirm it reports **no beats dropped** and **no outro
rewrite** before continuing. Every one of the eight beats is a REMOTION beat with
a registered `916` sibling, so all eight get rewired and re-rendered portrait;
nothing is centre-cut.

Then compile at **4K portrait** — note `--height 3840`, not the 1920 that
`shorts.py` prints in its own hint:

```bash
python3 runtime/scripts/compile.py weekly_updates/08-28-2/short --review --height 3840
```

`3840 x (1080/1920) = 2160`, so this lands 2160x3840. The portrait beats already
render at 2160x3840 (`scale_for` targets 2160 on the short edge for a 9:16
composition), so this compiles without upscaling. Passing `--height 1920` would
ship a 1080x1920 short — correct aspect, quarter resolution.

## STEP 6 — final masters

```bash
./art final weekly_updates/08-28-2
python3 runtime/scripts/compile.py weekly_updates/08-28-2/short --height 3840
```

Both stay in the reel folder. Never publish.

---

## If you change the words

Edit `narration_text` in `beat_sheet.json`, then STEP 2 → STEP 3 (`--force`) →
STEP 4 → STEP 5. **Never hand-edit durations** — audio is the clock.

## Known traps for this reel

- **`--height 3840` for the short.** `shorts.py` prints `--height 1920` in its
  own hint. That is the 1080p portrait preview, not 4K. See STEP 5.
- **The default weekly patterns would have blocked the 9:16 cut.**
  `ClaudeScienceLayerStack`, `ClaudeScienceSourceFlow` and `AttritionChain` have
  no `916` sibling in `Root.tsx`. Do not "improve" a body beat by switching to
  one — it will strand the portrait render with no composition to rewire to.
- **`typeScale` is set on B01 (1.6), B02 and B03 (1.4).** The `*916` siblings
  take `{data}` only and ignore it — expected, not a prop mismatch.
- **`ScaleComparison` labels must stay ≤ 8 characters.** They are right-aligned
  into ~136px at `x0 - 14`. The working precedent is `FP32`/`INT4`; this reel
  uses `DISTRICT`/`TRUTH`/`PRE-REG`/`SUBGROUP`/`ALLIANCE`/`OFFICE`. A longer
  label runs off the left edge of the frame.
- **`ScaleComparison` is `log10` — it cannot plot a negative value.** B01 shows
  claim magnitudes with the sign set aside and says so on screen. If you add an
  item, it must be positive.
- **Gate V may flag the outro or verdict cards as UNDERFILL.** Centred cards trip
  it routinely, and a 9:16 frame trips it harder. Look at the frame before
  treating it as a defect.
- **`scenes.py` must stay free of any Manim scene declaration**, including inside
  its docstring — GATE F scans it as text.
