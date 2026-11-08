# STATUS — *Aim Where It's Going.*

Ep. 16 · `predictive-adaptive-optics` · **COMPLETE** · 2026-11-07

## Delivered

| Cut | File | Spec |
|---|---|---|
| 16:9 master | `claude-for-astronomy_OmMali_06_11_2026.mp4` | 3840×2160 @ 24 · 160.82 s · 15.5 MB · −21.0 LUFS |
| 9:16 master | `predictive-adaptive-optics-9x16.mp4` | 2160×3840 @ 24 · 160.82 s · 17.3 MB · −21.0 LUFS |

Both carry all 14 beats at 3859 frames. 2:40.8, **19.2 s inside the 3:00 cap**.
The 9:16 is a re-layout, not a crop.

| Stage | State |
|---|---|
| research | done — 6 primary sources, `SOURCES.md` |
| experiment | done — `assets/ao.py` + `assets/gen_ao.py`, seed 1616, 8 asserted claims |
| plates | done — 5 plates, imagery only |
| beat sheet | done — 14 beats, 428 words |
| paperwork | done — F complete |
| GATE L | PASS |
| GATE A | PASS 10/10 |
| GATE W | PASS 10/10 |
| GATE B | PASS 20/20, re-run with `--curve-strict` |
| visual pre-flight | done — 20 frames read, 5 defects fixed |
| **GATE P** | **signed — `VERDICT: PASS`, Om Mali, 11/06/2026** |
| audio | done — Kokoro `af_bella`, 160.82 s measured |
| pacing | done — all 20 clips land under beat, worst −0.220 s |
| render | done — 20 Manim clips at 4K + 8 Remotion bookends |
| GATE V | PASS — 28 frames · 0 BLOCKER · 0 MAJOR on **each** cut |
| frames read | done — both cuts, `_qc/VISUAL-QC.md` |
| 9:16 | done |

## What looking at frames caught that no gate did

A strikethrough centred on the glyph **bounding box** rather than the
x-height, so it struck through the **tops of the letters** on B01's
"where the answer came from" — the one struck string in the episode with no
descender. B10's strike measured correct by accident because "sky" descends,
which is why the 20-frame pre-flight passed it. Now centred on the median
glyph top and bottom; both measure 0.500 of the x-height band.

GATE B could not have caught it: `_strike` is marked `_qc_intentional`, which
exempts deliberate strikethroughs from the TEXT-ON-CURVE rule, so a strike
through the heads and a strike through the middle are the same case to the gate.

## Known deviation

`compile.py` warns `reveal` carries 7/14 beats (50%), over the ~40% motion
pantry cap. Recorded in `BUILD-LOG.md` rather than silently cleared — fixing
it would mean re-authoring beats whose content was already signed.

## Cost

**$0.00.** Fellow Tier throughout — Kokoro local, no image model, no API keys.

## Not published

Nothing was uploaded anywhere. Both masters stay in this folder.
