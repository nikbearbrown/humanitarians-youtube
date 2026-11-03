# SHOTLIST — The Tails Go First

Typed work order. 9 beats, 2:21.7 at measured audio. All-Remotion reel: no
Manim, no stills, no human-supplied media, no open slots.

| Beat | Act | Component | Status | What is on screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | library | Composer on cream. `Annyeong, Jainil`. The question types in; two output lines answer it. `@HumanitariansAI`, `Fable 5`. |
| B01 | BLUF | `BrutalistHesitantWriter` | library | "Train on your own output, and nothing is lost." typed, then `nothing` deleted and `the rare things are` typed. 13.3s window. |
| B02 | SETUP | `DistributionShape` | **NEW** | The density silhouette draws left to right: one big ordinary lump, then a small far bump that fills terracotta and is labelled "the rare 5%". |
| B03 | TURN | `StageRail` | **reuse** | Real data → Generation 1 → Generation 2 → Generation n. The first card is terracotta with "never seen again" beneath it. |
| B04 | EVIDENCE | `PositionCurve` | **reuse** | The rare share every fifth generation, falling to the axis and staying there. The extinction point lights terracotta. |
| B05 | LAND | `DistributionShape` | **NEW** | Generation 40, with generation 0 behind it as a dashed ghost. The bump is absent and the absence is visible. Three stat cells: mean, std dev, "the rare 5% — gone". |
| B06 | SOURCE | `FormACard` | library | Shumailov et al. verbatim, citation smaller beneath. `qc.sparse`. |
| B07 | HANDOFF | `ClaudeComposerAsk` | library | `Your turn.` The viewer's prompt types in full. |
| B08 | OUTRO | `HaiTitleOutro` | library | Title restate, SUBSCRIBE, `@HumanitariansAI`. Never `ClaudeTitleOutro` (OUTRO-LOCK). `qc.sparse`. |

## GATE L outcome — two reuses, one build

This is the first reel where the library carried more of the load than it
demanded. `StageRail` and `PositionCurve` were both built for earlier videos
and both fit without modification:

- **`StageRail`** (built 2026-10-09 for the weekly report's publish flow) takes
  its stages as data, so "Drive → Review → Queue → Published" and "Real data →
  Gen 1 → Gen 2 → Gen n" are the same component with different props.
- **`PositionCurve`** (built 2026-10-02 for "Lost in the Middle") plots a value
  against position and calls out the lowest point. A share decaying to zero and
  staying there is exactly that shape, and the low callout lands on the
  extinction point for free.

| Built | Why GATE L was a miss |
|---|---|
| `DistributionShape` / `916` | Nothing generic draws a density silhouette, and critically nothing could draw a **ghost** of a previous shape behind the current one. "There used to be something here" cannot be shown by a curve that simply does not go there. Top GATE L hits were single-reel figures exposing only a `sparkLine` prop. |

## Deliberate repetition

`DistributionShape` carries B02 and B05, separated by B03 and B04. They are the
same figure before and after, which is the argument — the ghost outline in B05
only means something because B02 established the shape.

## Portrait notes

Both new 916 variants re-lay-out rather than scale. A density curve is
inherently wide and the entire argument sits at its right-hand end, so a centre
crop would delete the subject. Portrait keeps the full x axis, takes a taller
plot, and stacks the stats readout as rows instead of a horizontal strip.
