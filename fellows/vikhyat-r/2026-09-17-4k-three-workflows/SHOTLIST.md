# SHOTLIST.md — hai-4k-three-workflows

Typed work order. Every beat is machine-renderable; no human-supplied slots, so
nothing here is owed by a person and no beat should fall to a slate.

Landscape renders at 3840x2160. Manim beats render via run.sh at `-r 3840,2160`
(`runtime/scripts/run.sh:203-205`); Remotion beats render at `--scale=2` from a
1920x1080 composition, which is 3840x2160 natively.

| Beat | Type | Owner | Renderer | Target |
|---|---|---|---|---|
| B00 | REMOTION | pipeline | ClaudeComposerAsk | `media/B00.mp4` |
| B01 | GRAPHIC | pipeline | Manim `B01_ThreeNamed` | `manim/B01.mp4` |
| B02 | GRAPHIC | pipeline | Manim `B02_WorkflowA` | `manim/B02.mp4` |
| B03 | GRAPHIC | pipeline | Manim `B03_WorkflowB` | `manim/B03.mp4` |
| B04 | GRAPHIC | pipeline | Manim `B04_WorkflowC` | `manim/B04.mp4` |
| B05 | GRAPHIC | pipeline | Manim `B05_WhatSeparates` | `manim/B05.mp4` |
| B06 | GRAPHIC | pipeline | Manim `B06_TheOrder` | `manim/B06.mp4` |
| B07 | GRAPHIC | pipeline | Manim `B07_YouTubeCaveat` | `manim/B07.mp4` |
| B08 | REMOTION | pipeline | ClaudeComposerAsk | `media/B08.mp4` |
| B09 | GRAPHIC | pipeline | Manim `B09_Outro` | `manim/B09.mp4` |

## Scene intent, one line each

- **B01_ThreeNamed** — three lanes, each with the one verb it owns. The verbs
  arrive last, because they are the point.
- **B02_WorkflowA** — a left-to-right flow with a refusal that loops back. The
  loop is the scene: the wrong file never reaches the end.
- **B03_WorkflowB** — a funnel. Wide cheap pass at the top, narrow expensive
  pass below, one sheet at the bottom. Width carries the cost argument.
- **B04_WorkflowC** — B's verdict arrives settled, then routes into two folders,
  with the move log as a rail underneath.
- **B05_WhatSeparates** — three rows, one line each: the thing only that
  workflow does. Nothing else on screen.
- **B06_TheOrder** — A above B above C on a single spine, not three columns.
  The spine is the argument.
- **B07_YouTubeCaveat** — what stays on one side, what goes on the other. The
  staying half is drawn first and stays put.
- **B09_Outro** — title restate, terracotta period against the last word,
  `@HumanitariansAI` beneath. Silent by design.

## Consistency with the companion reel

Same palette, same title treatment, same outro form, same two bookends. The
pair should read as one piece in two parts. Lessons carried forward from the
first reel's gate failures, applied before the first render here:

- `_title` uses `to_edge(UP, buff=0.65)` — 0.55 lands the box top at 3.45
  against Gate B's 3.4 safe edge.
- Cards are outline only. A white fill on cream collapses Gate V's
  ink-vs-background separation to near zero.
- Content stays inside x +/-6.3, y +/-3.4.
- Bottom-of-frame content arrives early, because Gate V samples at 50% of the
  beat and `compile.py` retimes Manim clips ~1.5x, so the sample lands
  mid-build.
- Every scene changes shape, not just text. Gate A rejects a static
  shape-state as a text slide.
- The outro period is paired with its own final line, not the whole block.

## Portrait note

The 9:16 companion gets its own `scenes.py` under `vertical/`, with
`config.frame_width = 4.5` forced — Manim does not derive a portrait frame from
a portrait pixel canvas. Portrait safe area is x +/-1.95, y +/-3.4, measured
from Gate B rather than derived. Every horizontal arrangement here stacks there.
