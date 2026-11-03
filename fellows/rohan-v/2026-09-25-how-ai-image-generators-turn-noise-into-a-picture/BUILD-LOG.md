# BUILD-LOG — "How AI Image Generators Turn Noise Into a Picture"

What broke, what it cost, and what changed because of it.

## 1 — The toolkit was updated before anything was authored

`origin/main` had two new commits (SEIS skills + NEU brand kit; godot/riff/repoloop +
MATH-TYPESETTING and EXECUTABLE-EVIDENCE). The local tree carried two weeks of
uncommitted scene work, so it was committed first (`ba942db`, backup tag
`backup/pre-merge-2026-09-25`) and then merged (`11f51b0`). Five conflicts, all
additive, all resolved by keeping both sides; `scenes.json` regenerated rather
than hand-merged. Two pre-existing type errors arrived with upstream
(`SeisSongReadAlong`, `ChatReplyMock`) — not touched; esbuild does not typecheck.

## 2 — The first topic overlapped earlier videos

Rohan's instinct was right. "How music generators turn sound into tokens" had no
earlier video, but its bitrate beat repeated *What MP3 Throws Away* and its
takeaway repeated *Sample Rate and the Nyquist Limit*. Dropped before any work.

## 3 — No GPU framework, a full C: drive

No torch; C: at 97% with 8.7 GB free. Rather than install a deep-learning stack,
the model was written in plain numpy (MLP denoiser with two residual blocks,
hand-written backprop, Adam, EMA, classifier-free guidance). 1,626,880
parameters, 24,000 steps, **1862 s** on CPU. Final loss 0.0664.

## 4 — The house math renderer had no matplotlib

`typeset_math.py` imports matplotlib; no Python on the machine had it. The rule
forbids a text fallback, so it was installed with
`pip install --no-cache-dir --target <toolkit>/.pydeps "matplotlib==3.10.*"` —
on D:, no pip cache on C:, `.pydeps/` gitignored. pip also pulled numpy 2.5.3 and
Pillow into that folder; they were deleted and the folder is **appended** to
`sys.path`, so the numpy (2.5.2) and Pillow the model was trained with always win.

## 5 — Seed 7's music note was faint

B05 needs one seed to make a clear heart AND a clear note. Seed 7's note scored
18.21 (mean pixel distance to its nearest training note; median over 40 seeds
13.46). `scan_seeds.py` scored seeds 1–40 under both prompts by a written rule
(nearest-class check under both prompts, then best worse-of-two score) and kept
every result. All 40 seeds produced both prompts recognisably; **seed 38** was
chosen (heart 11.53, note 10.76). The frame labels it SEED 38. B01/B04 keep
seed 7's heart (14.45), which is clear.

## 6 — Importing the training script emptied its log

`train_toy_diffusion.py` opens `evidence/run.log` for writing at module level,
so `scan_seeds.py` and `export_toy_data.py` truncated it when they imported the
module for its functions. Nothing was lost: every logged line was also printed,
and the run's stdout was captured in `evidence/_stdout.txt`; `run.log` was
restored from it. The training script was **not** edited — its SHA-256
(`7d515850…`) is recorded in `toy_diffusion.json` and still matches. The two
importers now save and restore `run.log` around the import.

## 7 — The replay is verified, not assumed

`export_toy_data.py` does not re-train. It replays all six recorded runs from the
saved weights with denser snapshots (every 20 steps) and **refuses to export** if
any final picture differs from the training-time record; it also rebuilds the
training set from the same seeded draws and checks it against the recorded
forward picture. All matched.

## 8 — Layout, found on low-res stills before the 4K render

A throwaway bundle-once still renderer (deleted afterwards; finals go through
`remotion_scenes.py`) rendered every new scene at 15/50/85/99% in both
orientations. Found and fixed before any 4K frame:

- B01: `--seed` chip over the picture; spark line crowding the TOY MODEL label; portrait loop caption under the spark line
- B02: shares shown as percentages that summed past 100% — changed to multipliers (see PEDAGOGY); strip too high in landscape
- B03: equation centred against a left-aligned grid; portrait "the noisy picture" clipped and colliding with "part picture"; empty lower half before the readout (now shown at step 0 from the start)
- B04: near-empty first 15%; "12000" without a separator
- B05: right third of the landscape frame unused; grid pinned right, caption moved under the fork

## 9 — A caption contradicted Rohan's own captures

B05's caption said "like your grid of four". The week-03 captures established
Midjourney's web app shows **one row of four**, not a 2×2 grid. Corrected to "the
four images Midjourney hands back"; the toy's four seeds stay 2×2 for space only.

## 10 — GATE T: terracotta text is below WCAG

The first `./art final` was blocked by GATE T on B04 (contrast §8.3): the brand
spark #D97757 is 2.74:1 on the cream page, under WCAG's 4.5:1, and the new scenes
used it for readable text (labels, the step readout, the "part noise" bracket
label). Fixed properly rather than exempted: `SPARK_TEXT` #A9482B (5.5:1 on cream)
in `cueKit` for every readable accent glyph and text-bearing chip; strokes, rules
and fills keep #D97757. On B01's dark TV screen the deep step would be too dark
(2.7:1), so the on-screen step counter uses a light terracotta tint (#F4B49A,
> 8:1) instead. B01–B05 re-rendered.

## 11 — The first 9:16 cuts failed GATE T and Gate V

`./art vertical` rewired every beat to its `916` composition, but the first
`./art final --height 3840` was blocked. **GATE T §8.1**: the floor is 1.9% of the
*physical* frame height — 72 px at 3840 — and at 2160 × 3840 every portrait label
and most body text fell under it. The kerning type spec
(`skills/make/kerning/reference/type-spec.md` §1) states the 9:16 scale outright:
title 5.5vh, body 4.0vh, hard floor 3.2vh, and "if a string can't fit at the floor,
that's a content problem (shorten the string)". Last week's portrait cuts had never
been through GATE T at all (no TYPECHECK.md in `short/`).

What changed:

- `cueKit` gained `PHONE(height)` — the 9:16 scale as numbers — plus opt-in
  `titleSize` on `BeatHead` and `fontSize` on `SparkLine`. Every new scene's portrait
  branch was rebuilt on it as a *show-less* layout: title, one hero visual, at most two
  large lines, the spark line. Secondary text (loop captions, credit lines, the
  training mosaic, eyebrows) is landscape-only.
- Library scenes got opt-in `phoneType` (`HaiApplyCard916`, `HaiProgressOverturned916`,
  `HaiProgressSignupChain916`); `HaiTitleOutro916`'s handle and subline were raised to
  the floor. Without the flag, earlier reels render unchanged.
- Shortened strings live only in `vertical/beat_sheet.json` (e.g. "ONE SEED, TWO
  PROMPTS", "captions, 0 overlaps"). Each was checked against FACTCHECK: "no new
  visuals" was rejected as inaccurate (the agent did add captions and an intro) and
  replaced with "no new diagrams".
- **Gate V** then failed on underfill: the 9:16 safe box is y 96–1824, not the
  230–1440 band these layouts had been sized to. Layouts were spread to fill it, spark
  lines moved to 80% of the height, placeholders drawn visibly enough to count, and
  `compile.py`'s `@HumanitariansAI` chip moved from 40 px above the bottom (outside the
  9:16 title-safe box) to 80% of the height in portrait.
- A throwaway probe rendered the exact frame each gate samples at full 4K and ran the
  gates' own functions on it (`type_check.check_min_size` / `check_contrast`,
  `final_frame_check.analyze_frame`), so each iteration cost minutes, not a 40-minute
  render. All 16 portrait beats passed both before the final render.
- `HaiFootageShowcase(916)` joined two documented exemption sets in `type_check.py`
  (per-blob contrast, bbox overlap): its monitor plays the fellow's own recorded output,
  and the detectors were reading that footage's dark caption bar as our typography.

## Render

_Appended after the 4K pass._
