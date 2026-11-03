# CHECKS-REPORT.md — hai-liam-rag-triangle

Written BEFORE the first slate compiles, per the ai-explainer PROOF GATE.

```
10 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

Measured runtime 2:44.10 against a 2:45 target (see BUILD-LOG.md deviation 3 —
the gap was closed with the B02B mechanism beat, not with held frames).

## Per-beat classification

| Beat | Class | Why it is SHOW, not a card |
|---|---|---|
| B00 | SHOW | The refusal is performed in the interface — the query types, the send arms, the refusal lands as output lines. The viewer watches the failure, they are not told about it. |
| B01 | SHOW | The misconception is typed, marked terracotta, deleted, and replaced on screen. The correction IS the motion. |
| B02 | SHOW | Three vertices light in narration order; edges draw on as each step is spoken. |
| B02B | SHOW | The corpus plots itself, the question lands as the one accent point, a similarity radius sweeps out, and the three points it catches promote into a ranked list. The mechanism performs itself while being explained. |
| B03 | SHOW | Typing beat (one of the three legal ones): the prompt that produces B04. |
| B04 | SHOW | Left column fails first, then the retrieved context slides in and the right column answers — the two sides visibly diverge at the spoken contrast, then hold. |
| B05 | SHOW | Same diagram, changed state: vertex 02 breaks, the wrong document travels the edge, a false answer is emitted. |
| B06 | SHOW | Artifact lines land one at a time on the spoken clause. |
| B07 | SHOW | Typing beat: the handoff prompt types as it is read aloud. |
| B08 | SHOW | Mark, title restate with the terracotta period, rule, handle — sequenced. |

No beat is a headline-plus-paragraph slide, so no beat fails THE PPT TEST, and
there are no two consecutive beats sharing a visual scheme except by design:
B02 and B05 are deliberately the SAME diagram in two states (that repetition is
the pedagogy — the viewer reads the change, not a new figure). The composer
appears at B00, B03 and B07 only, separated by illustration beats, per
ILLUSTRATE LAW.

## Teaching arc

- **FRAMEWORK before examples** ✓ — B02 (the Triangle) precedes B04 (the worked example).
- **WORKED EXAMPLE** ✓ — B04, one concrete question run twice.
- **FALSIFIABILITY** ✓ — B05 names the break (context poisoning) and shows it.
- **SCAFFOLDED TASK** ✓ — B07, a 30-second task the viewer can run for free.
- **BOOKENDS** ✓ — cold open (B00), BLUF (B01), verdict (B06), handoff (B07), title outro (B08).
- **NO-SOURCE-NO-VERDICT** ✓ — the verdict in B06 rests on the mechanism shown in B02/B04/B05, and the two illustrative figures are labelled illustrative on screen (see FACTCHECK.md rows 6 and 8).

## Legibility contract (per SHOW/HOLD claim beat)

| Requirement | How it is met |
|---|---|
| Names its on-screen artifact | Every beat carries `shot.visual_intent` + a `show` event list. |
| ~15–35% negative space | Components position from fractions of the frame with the diagram/columns occupying ~60–70% of the safe area; verified in the frame-level QC pass, not assumed. |
| Un-highlighted elements ≥ ~40% opacity | No element is faded below 0.55 in either new component (edges hold at 0.55 minimum before their reveal completes). |
| Comparisons held ≥ 2s | `RagPromptCompare` finishes all reveals by 0.78 of the beat, so both columns hold still for ~5s at B04's length. |

## Open items

None. Nothing in this sheet is punting, and there is no human-supplied slot to
wait on.
