# BUILD-LOG — "Testing AI Video Editors, and a Setup Guide for New Fellows"

What broke, what it cost, and what changed because of it.

## 1 — The narration contradicted itself

B05's first draft: "the other three tools haven't had a hands-on test yet." That
counted Remotion — which every Brutalist video, including this one, is built on.
Corrected to "OpenReel and DaVinci Resolve", the beat re-voiced (18.03 s →
18.92 s), `align.py` + `sync_cues.py` re-run, before any render.

## 2 — Frames had to be chosen, not grabbed

A 6×6 contact sheet of the HyperFrames output (one frame per 8 s) was read before
picking. Excluded: ~1:36–2:05, where the Suno workspace mockup hard-codes real
Suno users' handles (the known `SunoL1Interface` issue), and the end card at
~4:03, whose caption and credit carry the presenter's surname. Four frames kept
(t = 2, 12, 44, 78 s), staged to `runtime/remotion/public/agentic-editing-progress/`.

## 3 — `voice_policy` would have switched on the wrong workflow

The fellows skill records a fellow's persistent voice with
`metadata.voice_policy: "persistent-fellow-selected"` — but `build_safety.py`
treats that flag as "this is a fellow-REPORT reel", which makes B04 a
pass-through source video and B05/B06 Professor Bear's notes requiring his
signed approval. Neither is true here. The voice (`af_bella`) is recorded in the
fellow README and in every episode's `metadata.voice_kokoro` instead, which is
what FELLOWS-SUBMISSION asks for, and the flag is not set.

## 4 — Two library components ignored the narration

`HaiProgressOverturned` (B04) settles all its rows by ~frame 150 (5 s) and strikes
the left column faint; against 21.6 s of narration the four problems were struck
out before they were spoken, and hard to read. `HaiProgressSignupChain` (B06)
likewise lands its cards on a fixed stagger. Both gained **opt-in** `cues` +
`durationSeconds` props (landscape and portrait): with them, each row / card lands
on its spoken phrase and B06's guide sheet arrives first, on "setup guide", so the
frame is never empty; without them the original timing is unchanged, so earlier
reels re-render identically. In cue mode the struck text stays legible (INK_SOFT,
not GHOST).

## 5 — GATE T: terracotta text is below WCAG

The first `./art final` was blocked by GATE T on B02, B03, B06 (contrast §8.3) and
B05 (min-size §8.1). The brand spark #D97757 is 2.74:1 on cream — below 4.5:1 —
and several new scenes used it as a TEXT colour, and as the background of chips
carrying white text (3.1:1). The fix is real, not an exemption: a text-safe step,
`SPARK_TEXT` #A9482B (5.5:1 on cream, 5.8:1 under white), added to `cueKit`, used
for every readable accent glyph and text-bearing chip; strokes, rules and fills
keep #D97757. `HaiProgressSignupChain`'s doc label and status chip got the same
fix. The smallest chip in B05 went from 19 to 22 px (1080-scale) for the §8.1 floor.

## 6 — The first 9:16 cuts failed GATE T and Gate V

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

_Appended after the final pass._
