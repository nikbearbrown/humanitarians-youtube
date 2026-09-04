# Scenes

The Remotion components that render these five episodes. **These are reference copies —
they will not build inside this repository.**

They live in the toolkit at `runtime/remotion/src/scenes/` and import from its modules
(`../tokens/layout`, `../tokens/claude`, `../deckPatterns`), so they only compile inside
`brutalist.art`. They are here so the code that made the videos sits next to the beat
sheets that describe them.

## Files

| File | What it renders |
|---|---|
| `claudeStage.tsx` | Shared stage furniture — cream ground, safe-area mapping, the `@Yatra` corner bug, eyebrow+title block. Everything else builds on this. |
| `BottleneckMoved.tsx` | The Bottleneck Moved. — ordinal bars, ordinal funnel, threshold zones |
| `JudgmentIsTheJob.tsx` / `…916.tsx` | The Judgment Is the Job. — ledger, concept wall, stakes list |
| `EveryToolEveryWeek.tsx` / `…916.tsx` | Every Tool, Every Week. — the per-tool loop, week strip, document status |
| `AssistedNotAutomated.tsx` / `…916.tsx` | Assisted, Not Automated. — the cited-statistic scenes, act cards, sources card |
| `OneToolAWeek.tsx` / `…916.tsx` | One Tool a Week. — tool/article card, proposed-team card |
| `Root.registrations.tsx` | The 57 `<Composition>` registrations for the above, extracted from the toolkit's shared `Root.tsx`. Not standalone. |

`…916.tsx` files are the 9:16 portrait variants. They are **re-banded, not scaled**: the
Shorts law's composition logic is that 16:9 lays out side by side while 9:16 stacks top and
bottom, so two ledger columns become two stacked sections, a 4x3 grid becomes 3x4, and
splayed branches stack vertically. They also hold content clear of the platform UI overlay
(above y≈1440, left of x≈960) and move the corner bug to the lower left.

## The constraint that shaped most of these components

Four of the five episodes were built under an instruction not to invent statistics. Rather
than rely on remembering that while authoring, the components were written so that a figure
is **not renderable**: `YtwWeeks` shows one named week and an open-ended run of unnamed ones
and so cannot express a count; `YtwStatus` is a fixed done/not-done pair and cannot imply a
date; `RcpCard` takes `lines: string[]` rendered verbatim with no "summary" or "findings"
field, because a field like that is an invitation to fill it.

`AssistedNotAutomated.tsx` inverts this deliberately, because that episode was supplied
seven verified figures to cite. There, `SeoStat`, `SeoCompare`, `SeoDrop` and `SeoShare`
each take a **required** `source` string — a statistic cannot be rendered without its
citation — and values are typed as strings printed verbatim, never parsed or recomputed.
Citations render in muted ink rather than the accent colour: a source is provenance, not
emphasis.

`RcpTeam` applies the same idea to status: it requires a `status` string, rendered in the
accent as the loudest element on the card, so a proposed initiative cannot be displayed as
though it were underway.

## Rendering

Render only through the toolkit's `runtime/scripts/remotion_scenes.py`, never by
hand-rolling `npx remotion render` — the script handles props, the 4K supersample, and
conforming each clip to its beat's measured audio length.
