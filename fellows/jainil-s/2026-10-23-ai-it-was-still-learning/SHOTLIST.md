# SHOTLIST — It Was Still Learning

Typed work order. 8 beats, 2:23.3 at measured audio. All-Remotion reel: no
Manim, no stills, no human-supplied media, no open slots.

| Beat | Act | Component | Status | What is on screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | library | Composer on cream. `Vanakkam, Jainil`. Two output lines answer the question. |
| B01 | BLUF | `BrutalistHesitantWriter` | library | "It has finished learning." typed, then `finished` deleted and `barely begun` typed. 15.5s window. |
| B02 | SETUP | `CardSet` | **reuse** | Two cards: the task (mod 23, 317/212 split, chance 4.3%) and the model (96 units, squared activation, decay 0.8). |
| B03 | EVIDENCE | `DoubleDescentCurve` | **reuse** | Both curves on a log-x, linear-y plot. Dashed training snaps to 100% at step 500; solid held-out crawls the floor, then climbs past the dashed 95% line. Terracotta threshold marks step 500. |
| B04 | MECHANISM | `ClaudeBarChart` | **reuse** | Four bars, held-out accuracy by weight decay: 0.9 / 10.4 / 86.3 / 99.5%. The last bar accented. |
| B05 | SOURCE | `FormACard` | library | Two ellipsis-led verbatim fragments from Power et al. `qc.sparse`. |
| B06 | HANDOFF | `ClaudeComposerAsk` | library | `Your turn.` The viewer's prompt types in full. |
| B07 | OUTRO | `HaiTitleOutro` | library | Title restate, SUBSCRIBE, `@HumanitariansAI`. `qc.sparse`. |

## GATE L outcome — nothing new built

The first reel this project has produced without building a single component.
All three body beats are carried by existing generics:

- **`CardSet`** (built 2026-10-16 for the weekly report's two-videos beat) —
  here it holds the task and the model. Same shape, unrelated content.
- **`DoubleDescentCurve`** (built 2026-10-09) — its optional `trainPoints`
  second series was added for "training error goes blind"; here it carries the
  training curve against the held-out one, which is the same two-series shape
  with the opposite meaning. `logY: false` for a 0–100% axis.
- **`ClaudeBarChart`** (built 2026-10-16, the day the vox-palette `BarChart`
  was caught) — its second outing, and the reason the earlier fix was worth
  doing properly rather than patching one reel.

## Palette check — now part of GATE L

Every component was checked for its token import before use (gotcha A15):

```
DoubleDescentCurve     tokens/claude
ClaudeBarChart         tokens/claude
CardSet                tokens/claude
FormACard              tokens/claude
```

## B03 axis note

`logY: false` because accuracy is a 0–100% quantity and a log axis would
distort the floor where the held-out curve spends its first 1,500 steps. The x
axis stays logarithmic: the interesting range spans steps 250 to 20,000, and on
a linear x the entire grokking transition would be squeezed into the left
quarter of the frame. `floorY: -1` so the 0.0% point sits on the linear scale
rather than being pinned to the axis.
