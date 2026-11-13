# SHOTLIST — You're Only Seeing Half the Curve

Typed work order. 9 beats, 2:22 at measured audio. All-Remotion reel: no Manim,
no stills, no human-supplied media, no open slots.

| Beat | Act | Component | Status | What is on screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | library | Composer on cream. Greeting `Namaste, Jainil`. The practitioner's question types in, send arms terracotta, two output lines answer it. Handle `@HumanitariansAI`, model chip `Fable 5`. |
| B01 | BLUF | `BrutalistHesitantWriter` | library | "The error curve dips once." typed, then `once` deleted and `twice` typed in its place. Seed `ai-only-half-the-curve-b01`. `lead_silence_s: 0.8`. |
| B02 | EVIDENCE | `DoubleDescentCurve` | **NEW** | Log x, **linear y** (`logY: false`), 11 points, p=2…90 only. The textbook U, bottoming at 60 with a terracotta callout. No threshold line yet — the classical picture stated fairly, on its own terms. |
| B03 | EVIDENCE | `DoubleDescentCurve` | **NEW** | Same figure, axes redrawn to fit, all 24 points. Terracotta dashed threshold at p=100, peak callout `111 — 159x worse`, dashed reference line at the classical best, end callout `0.29` visibly below it. |
| B04 | MECHANISM | `InterpolatorChoice` | **NEW** | Two panels, same six data dots. LEFT: one violently swinging curve. RIGHT: five faint candidates plus the smooth terracotta one that gets picked. |
| B05 | EVIDENCE | `DoubleDescentCurve` | **NEW** | Full test curve in ink plus a dotted training-error series that sinks to the floor before the threshold and runs flat to the right edge. Legend distinguishes them. |
| B06 | SOURCE | `FormACard` | library | Belkin et al. quotation verbatim on cream, citation line smaller beneath. `qc.sparse`. |
| B07 | HANDOFF | `ClaudeComposerAsk` | library | Greeting `Your turn.` — persona drops. The viewer's prompt types in full. `runningText: paste this into Claude…`. |
| B08 | OUTRO | `HaiTitleOutro` | library | Serif title restate, terracotta period, SUBSCRIBE pill, `@HumanitariansAI`. Never `ClaudeTitleOutro` (OUTRO-LOCK). `qc.sparse`. |

## Components built for this reel

Four new scenes, all registered in `Root.tsx` and indexed via `./art scene-index`
(627 renderable, up from 623).

| Component | Why GATE L was a miss |
|---|---|
| `DoubleDescentCurve` / `916` | `PositionCurve` was the near hit and is the wrong shape: it calls out a LOW point, has no threshold marker, no reference line, no staged reveal and a linear axis. This data spans 2–4000 on x and 0.29–111 on y and the argument lives in a PEAK. |
| `InterpolatorChoice` / `916` | Genuine miss — top candidate scored 5.5 and was a logo sting. Nothing in 623 scenes draws "many curves through the same points, one chosen". |

Both carry portrait variants with their schemas **declared in full rather than
re-exported** — the indexer reads the `z.object` literal in each file, and a
re-export leaves `./art scenes --check` reporting no props at all.

## Deliberate repetition

`DoubleDescentCurve` carries B02, B03 and B05. B02→B03 is one continuous figure
being revealed in two stages, which is the pedagogy: state the textbook rule on
its own axes, then redraw the axes to show what they could not contain. B04 sits
between that pair and B05 so no two consecutive beats share a visual scheme —
ILLUSTRATE LAW is about wallpaper, and this is a build.

## Axis change between B02 and B03 — deliberate, and narrated

B02 draws its y axis **linear**, topping out near 1.9; B03 switches to **log**,
topping out near 200. That is not a silent rescale: the
narration says *"the axis has to be redrawn to fit it"* on the cut, because the
textbook plot genuinely cannot contain the number. An unremarked rescale between
two shots of "the same" figure would be a cheat; a remarked one is the point.
