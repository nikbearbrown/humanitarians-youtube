# BUILD-PROMPT — `yatra-nobody-wrote-this`

Paste-ready prompt that rebuilds this reel end to end. Run it from
`~/Desktop/brutalist-reels/` (or anywhere — the reel path below is absolute).

> **Environment note, read first.** This machine's only system Python is 3.14,
> which has no wheels for the toolkit's pinned deps. The build runs inside
> `~/Desktop/brutalist.art-main/.venv` (CPython 3.12, created with `uv`), so every
> command below is prefixed by activating it. `manim` is NOT installed there and
> is not needed: this reel has zero Manim beats, so `run.sh` skips that stage
> cleanly. Kokoro, Remotion, Pillow, ffmpeg and the caption pipeline are all
> READY.

---

```
Rebuild the reel at ~/Desktop/brutalist-reels/youtube/yatra-nobody-wrote-this
end to end. Free path only — Kokoro + Remotion + ffmpeg, no paid API, never publish.

Read first, in this order:
  ~/Desktop/brutalist.art-main/skills/make/ai-explainer/SKILL.md   (doctrine)
  ~/Desktop/brutalist.art-main/CLAUDE-BRAND.md                     (fidelity palette)
  ./FACTCHECK.md   ./SOURCES.md   ./CHECKS-REPORT.md   ./SHOTLIST.md

HARD CONSTRAINTS — these are the ones this reel exists to protect:
  1. Every figure on screen was supplied verbatim by the human. Do not round,
     recompute, re-derive or "tidy" a single one. The ranges 25–29% and 4–13%
     stay ranges on screen.
  2. Never render the human-written share of LinkedIn posts. It is available by
     subtraction (100 − 41 − 4.3) and it was NOT supplied. LnkAllOrNothing has no
     remainder-bar prop by design — do not add one.
  3. Every figure-bearing scene REQUIRES its `source` string. A number without a
     citation beneath it is a build failure, not a style choice.
  4. B10's left block stays tagged INTERPRETATION. It is the narrator's read, not
     a finding, and the tag is what keeps the frame honest.

STEPS:

  cd ~/Desktop/brutalist.art-main && source .venv/bin/activate && export ART_HOME=$PWD

  # 1. audio is the master clock — regenerate ONLY if narration changed
  python3 runtime/scripts/generate_audio_kokoro.py \
      ~/Desktop/brutalist-reels/youtube/yatra-nobody-wrote-this

  # 2. if any duration moved, retarget durationInFrames in Root.tsx for the nine
  #    Lnk* compositions AND their 916 twins: frames = round(measured_seconds * 30).
  #    They must match, or the progress-mapped animation stops spanning its beat.

  # 3. render every Remotion beat, then compile both cuts + run GATE V
  bash runtime/scripts/run.sh \
      ~/Desktop/brutalist-reels/youtube/yatra-nobody-wrote-this --height 2160

  # 4. VISUAL QC LAW — the mp4 probe is a FILE check and never counts as QC.
  #    Sample frames and actually LOOK at the PNGs:
  ffmpeg -i .../yatra-nobody-wrote-this.mp4 -vf fps=2 _qc/frames/%05d.png
  #    Audit the 9-point rubric in CLAUDE-CODE-VISUAL-QC-CHECK.md, with extra
  #    attention to: the end-of-bar values in LnkLadder (they sit closest to
  #    SAFE.r), the citation line on every stat beat (it must be legible, not
  #    just present), and canvas fill on LnkStat/LnkBluf.
  #    Log every defect and fix in _qc/REPORT.md. Fix ROOT CAUSES in the scene
  #    source under runtime/remotion/src/scenes/NobodyWroteThis*.tsx and
  #    re-render until zero BLOCKER and zero MAJOR remain.

  # 5. the 9:16 derivative (Instagram / LinkedIn / Shorts)
  python3 runtime/scripts/shorts.py \
      ~/Desktop/brutalist-reels/youtube/yatra-nobody-wrote-this
  #    The reel is 2:48, under the hard 3:00 cap, so NO beats should be dropped —
  #    the whole thing reformats. If the planner proposes dropping beats, stop and
  #    say so: that means a narration edit pushed it over, and the fix is the
  #    script, not the cut.
  python3 runtime/scripts/compile.py \
      ~/Desktop/brutalist-reels/youtube/yatra-nobody-wrote-this/short --height 3840

  # 6. report: durations, gate results, QC verdict. Do NOT publish. The master
  #    stays in the reel folder.
```

---

## Deliverables this produces

| File | What it is |
|---|---|
| `yatra-nobody-wrote-this.mp4` | 16:9 master, 3840×2160 — YouTube |
| `yatra-nobody-wrote-this-slate.mp4` | review cut with beat markers |
| `short/yatra-nobody-wrote-this-short.mp4` | 9:16, 2160×3840 — Instagram / LinkedIn |
| `_qc/REPORT.md` + `_qc/frames/` | the frame-level visual QC pass |
| `mp3/` + `mp3/timings.json` | narration and the master clock |

## Scene source (edit here, never in the reel folder)

```
runtime/remotion/src/scenes/NobodyWroteThis.tsx      # 16:9 — nine components
runtime/remotion/src/scenes/NobodyWroteThis916.tsx   # 9:16 — re-banded, not scaled
runtime/remotion/src/Root.tsx                        # registrations + frame counts
```

---

## 9:16 exports at 4K (2160×3840)

The portrait beats already render at 2160×3840 — `remotion_scenes.py` uses
`--scale=2` on the 1080×1920 compositions. Only the compile step decides the
delivered resolution, so a 4K vertical needs **no re-render**, just:

```bash
python3 runtime/scripts/compile.py <REEL>/short --height 3840
```

`compile.py` derives width from `metadata.aspect_ratio` (`9:16`), so
`--height 3840` yields 2160×3840. Delete `<REEL>/short/clips/` first, or the
previously conformed 1080p clips get reused and you get an upscale.

**The endcard is the one thing that is NOT natively 4K.** `shorts.py` hardcodes
`W, H = 1080, 1920` in `endcard_png()`, so the generated `media/END.png` is
1080p and will be upscaled into a 4K timeline — visibly soft type on the final
card. Regenerate it at double size before compiling:

```python
from PIL import Image, ImageDraw, ImageFont
import shorts
W, H = 2160, 3840
img = Image.new("RGB", (W, H), shorts.INK)
d = ImageDraw.Draw(img)
fh = ImageFont.truetype(shorts.find_serif(), 128)      # 2x the 64px original
hb = d.textbbox((0, 0), handle, font=fh); hw = hb[2] - hb[0]
d.text(((W - hw) / 2, H * 0.30), handle, font=fh, fill=shorts.CREAM)
y = H * 0.30 + (hb[3] - hb[1]) + 52                    # 2x the 26px gap
d.line([((W - hw) / 2, y), ((W + hw) / 2, y)], fill=shorts.TERRA, width=8)
img.save("<REEL>/short/media/END.png")
```

`handle` must come from `metadata.channel_handle` — `shorts.py`'s `--handle`
defaults to `@nikbearbrown` and never reads the beat sheet.

## If a rebuild fails on `TimeoutError: [Errno 60]`

That is iCloud, not a corrupt file. These reels live under `~/Desktop`, which is
iCloud-synced; when the volume runs low macOS evicts rendered media to the cloud,
leaving files that report their full size in `ls` but hold zero bytes on disk.
`compile.py` then dies hashing one. Force them back:

```bash
brctl download <REEL>/short/media
```

Check for evicted files with `stat -f '%b'` — a block count of 0 against a
non-zero size means the data is not local.
