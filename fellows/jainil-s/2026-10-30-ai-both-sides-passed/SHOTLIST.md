# SHOTLIST — Both Sides Passed

Typed work order. 8 beats, 2:19.9 at measured audio. All-Remotion reel: no
Manim, no stills, no human-supplied media, no open slots.

| Beat | Act | Component | Status | What is on screen |
|---|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | library | Composer on cream. `Selam, Jainil`. Two output lines answer the question. |
| B01 | BLUF | `BrutalistHesitantWriter` | library | "validated on both sides." typed, then `sides` corrected to `sides, but never between them`. 14.8s window. |
| B02 | SETUP | `StageRail` | **reuse** | Producer → The boundary → Consumer. The middle card fills terracotta with "nobody owns this" beneath it. |
| B03 | EVIDENCE | `ClaudeBarChart` | **reuse** | Three bars: 1 / 6 / 7 out of seven defects caught. The last accented. |
| B04 | LAND | `CardSet` | **reuse** | Two cards on the defect that got through: what a range check sees (0.001%, "fine") against what a shape check sees (TVD 0.42, "not the same data"). |
| B05 | SOURCE | `FormACard` | library | Reference card, explicitly labelled as paraphrase. `qc.sparse`. |
| B06 | HANDOFF | `ClaudeComposerAsk` | library | `Your turn.` The viewer's prompt types in full. |
| B07 | OUTRO | `HaiTitleOutro` | library | Title restate, SUBSCRIBE, `@HumanitariansAI`. `qc.sparse`. |

## GATE L outcome — nothing new built, second week running

Three body beats, three existing generics, no modifications:

- **`StageRail`** (2026-10-09) — a three-stage rail with the *middle* marked is
  a use the component was not written for, and needed no change: `activeIndex`
  does not care whether the marked stage is a step or a gap.
- **`ClaudeBarChart`** (2026-10-16) — three bars with a `" / 7"` unit suffix.
- **`CardSet`** (2026-10-16) — two cards, prose lines, one accented.

Palette verified before use (gotcha A15):

```
StageRail        tokens/claude
ClaudeBarChart   tokens/claude
CardSet          tokens/claude
FormACard        tokens/claude
```

## B05 is a reference card, not a quotation

Every other source beat this channel has shipped quotes its paper verbatim.
This one does not: the Breck et al. abstract could not be retrieved in full,
and the single verbatim sentence available carries none of the relevant
content. The card is labelled `REFERENCE (paraphrased, not quoted)` on screen
and the narration says "described" rather than "wrote". Wrapping a paraphrase
in quotation marks would have been indistinguishable, to a viewer, from the
verbatim cards in every other reel — which is exactly why it was not done.

## Honesty note carried in the narration

The 7/7 figure is against a catalogue of defects written by the same person who
wrote the checks, and the shape check only works because the synthetic data was
given a daily rhythm. Both limits are stated — the first in `SOURCES.md` and
`FACTCHECK.md`, the second in B04's narration, which says the events "have a
daily rhythm" as the reason the check can see anything at all.
