# STATUS — Ep. 17, *scheduling-the-night*

**DELIVERED.** Both masters built, verified and sitting in this folder.
Nothing published, per house rule.

Updated 2026-11-13.

---

## Deliverables

| file | spec |
|---|---|
| `claude-for-astronomy_OmMali_13_11_2026.mp4` | **3840 × 2160**, 24 fps, 159.49 s |
| `scheduling-the-night-9x16.mp4` | **2160 × 3840**, 24 fps, 159.49 s |

Runtime **2:39.5** — under the 3:00 ceiling. The 9:16 is a separate build, not
a crop: Manim re-rendered at 2160×3840 and Remotion's own `*916` compositions.
Its working folder is `short/`.

**Total spend: $0.00.** Kokoro TTS local, Manim, Remotion, HiGHS via SciPy.

## The pipeline that ran

| phase | result |
|---|---|
| GATE P | **signed** — Om Mali, 11/13/2026 |
| audio, Kokoro `af_bella` | 14 MP3s, 159.49 s measured — the master clock |
| pacing solve | RT/HOLD per scene; **no `RT_PORTRAIT` needed** — every portrait branch plays the same 7–12 reveals as landscape |
| GATE A / W | 10/10 clean each, re-run after every edit |
| GATE B, `--curve-strict` | **20/20** clean, both aspects |
| 4K render | 20 clips, both aspects, each 0.19–0.22 s under its beat |
| compile | 14/14 slots filled, both cuts, no slates |
| **frames read** | **5 defect classes found that no gate caught** — see `VISUAL-QC.md` |
| GATE V | **exits 2 on both.** 0 BLOCKER. The remaining MAJORs are characterised with measurements in `VISUAL-QC.md` and are not text or layout faults |

## What GATE V still reports, and why it was not "fixed"

Five `low-contrast` MAJORs (16:9) and two (9:16) come from the gate averaging
**every** non-background pixel into one ink colour. Ep. 17's plates are pale
line-art on cream, so 61–78% of that average is plate. The type measures
**5.7:1 to 7.9:1** WCAG against the page — AA is 4.5:1.

Two `underfill` MAJORs on portrait B11 are an aspect mismatch: the 916 verdict
card reserves the platform-UI bands by design, and GATE V measures against a
16:9-derived safe area. 53% against a 55% floor.

Both were read at native 4K before being called artifacts. Nothing was run
with `--lenient`.

## Honest notes carried into the cut

- **B09 attacks the episode's own claim.** Paid 20× to care about finishing,
  greedy reaches 0.975 against the planner's 1.000 — by starting 43 fewer
  fields and giving up 2.3% of its rate. On screen, not omitted.
- **"Without machine learning" is scoped to the pointing decision** (FACTCHECK
  F14). SMTN-020 — the document describing the scheduler Rubin actually runs —
  contains zero occurrences of `reinforcement`, `machine learning` or `neural`,
  which contradicts `ideas.md`'s blurb for this topic.
- **The simulation is a toy.** Its airmass gap (1.7 vs 1.3) is wider than
  ZTF's real one (1.20 vs 1.11). No narration calls these numbers ZTF's.
- **The ILP does not prove optimality** — it stops on its 120 s wall clock.
  Nothing on screen or in narration claims it does.
