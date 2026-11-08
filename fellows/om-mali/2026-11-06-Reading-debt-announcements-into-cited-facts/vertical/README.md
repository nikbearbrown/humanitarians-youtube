# vertical/ — the 9:16 cut

`reading-debt-announcements-into-cited-facts-916.mp4` · **2160×3840**, 24fps, 202.12s — the
same length as the 16:9 master, to the frame.

## It is a re-layout, never a crop

Every scene in `ReadingIntoCitedFacts.tsx` lays itself out natively at both sizes through one
helper:

```tsx
const { f } = useStage();     // f(landscape, portrait)
const BAR_W = Math.min(SAFE.w - BESIDE, f(700, 470));
```

Each component is registered twice in `Root.tsx` — once at 1920×1080 and once at 1080×1920
under its `<pattern>916` name — so there is one component and two registrations, not two
components. Nothing is cropped, letterboxed or scaled down; rows that sit side by side in
16:9 stack in 9:16, B01's three steps turn from a row with `→` into a column with `↓`, and
B05's 24 refusal cells go from 12 per row to 8.

## The audio is the same audio

`make_vertical.py` derives `vertical/beat_sheet.json` from the landscape one and **copies the
twelve mp3s across**. Narration is never regenerated for this cut, so no number, no word and
no duration can differ between the two masters.

It matches the registration tuple shape in `Root.tsx`, not a naming convention — do not
"simplify" that regex back to a `W<digits>` pattern, which has silently missed a whole series
twice before.

## The body beats needed no rescale this week

A first for this series. The chassis arrives with week 3's portrait values already raised,
and the two bar beats compute the width given up by everything sitting *beside* the track
separately per orientation:

```tsx
const BESIDE = f(330 + 24 + 112 + 150 + 28 + 150 + 60, 108 + 146 + 150 + 28 + 60);
```

In landscape the label column sits beside the track and pays for the percentage, the
fraction and the extras scale. In portrait it stacks *above* the track and pays for nothing —
which is precisely what clipped every figure on week 3's B04 (`593` drew as `59`). Writing it
into the component instead of rediscovering it in QC is the whole of the saving.

## What portrait did break

The **bookends**, not the body. B00 and B10 threw four `edge-bleed` BLOCKERs: the segment
title wrapped to three lines and line 2 — "Announcements into Cited" — ran to the frame edge.
The title block in the shared `scenes/ClaudeComposerAsk.tsx` set `left: PAD_X` and no right
bound, so the box ran to the viewport and wrapped there. Fixed; see `../BUILD-LOG.md` §8 for
why no earlier reel re-wraps under the new bound.

## Gates

```
GATE V (explicit --mp4):  frames=24  BLOCKER=0  MAJOR=0
```

Check `_qc/REPORT.md` and `_qc/contact_sheet.png` here, not the landscape ones — GATE V can
pass 16:9 and fail 9:16 on the very same scene, and this week it did.
