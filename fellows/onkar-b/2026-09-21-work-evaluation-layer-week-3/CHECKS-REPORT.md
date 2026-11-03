# CHECKS-REPORT.md — hai-liam-evaluation-layer

Written BEFORE the first compile, per the ai-explainer PROOF GATE.

```
9 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

Measured runtime **2:43.1** against a 2:45 target, first audio pass, no
re-cut needed (narration written to the measured 3.29 words/sec rate).

## Per-beat classification

| Beat | Class | Why it is SHOW, not a card |
|---|---|---|
| B00 | SHOW | The match is performed in the interface and then undercut by its own output lines. The viewer watches a success that proves nothing. |
| B01 | SHOW | The misconception is typed, marked terracotta, deleted, replaced. The correction is the motion. |
| B02 | SHOW | Three axis rows snap in on the spoken axis, each carrying a worked claim-vs-truth pair that appears with it. |
| B03 | SHOW | Typing beat (one of the three legal ones): the prompt that produces B04. |
| B04 | SHOW | The payload physically travels the loop — n8n, FastAPI, ChromaDB, verdict — and the ledger row docks as it passes. |
| B05 | SHOW | Two sentences stack with one word differing in colour while the similarity bar fills underneath; the viewer sees *why* the search passes it. |
| B06 | SHOW | Scoreboard rows land one per spoken item, then RESULT fills. |
| B07 | SHOW | Typing beat: the cURL command types as it is read aloud, then the expected verdict lands as output. |
| B08 | SHOW | Mark, title restate with terracotta period, rule, handle, credit — sequenced. |

No beat is a headline-plus-paragraph slide, so none fails THE PPT TEST. The
composer appears at B00, B03 and B07 only, separated by illustration beats
(ILLUSTRATE LAW). No two consecutive beats share a visual scheme.

## Teaching arc

- **FRAMEWORK before examples** ✓ — B02 (three axes) precedes B04/B05.
- **WORKED EXAMPLE** ✓ — B04, one claim through the real contract.
- **FALSIFIABILITY** ✓ — B05 names and shows the case that defeats similarity search.
- **SCAFFOLDED TASK** ✓ — B07, one cURL request, with a stated expected result so the viewer can tell pass from fail.
- **BOOKENDS** ✓ — cold open (B00), BLUF (B01), verdict (B06), handoff (B07), title outro (B08).
- **NO-SOURCE-NO-VERDICT** ✓ — every claim traces to the author's script (FACTCHECK.md); the one metric that would have needed a citation was removed rather than invented.

## Legibility contract

| Requirement | How it is met |
|---|---|
| Names its on-screen artifact | Every beat carries `shot.visual_intent` plus an ordered `show` list. |
| ~15–35% negative space | Series components are built to the house safe-area rules; verified in the frame-level QC pass, not assumed. |
| Un-highlighted elements ≥ ~40% opacity | No element is faded below the components' own dim tier. |
| Comparisons held ≥ 2s | B05's claim/ledger pair and B02's three rows complete well before their cuts and hold. |

## Known timing notes (checked, not assumed)

- **B01** — `BrutalistHesitantWriter` is registered at 606 frames but the beat is 11.8s, and the conform *trims*. Typing is set to `charMs: 13` so the correction lands and holds; verified by still-render on the sibling reel with text of the same length. Re-verified in the QC pass below.
- **B04** — narration was cut from 27.3s to 17.6s so it fits `GatekeeperVerifyLoop`'s 18s registration; otherwise the clip would freeze-hold for 9 seconds. Time moved to B07, which is a bookend and exempt from the body word budget.
- **B07** — 35.2s against a 30s registration, so the last ~5s freeze-holds. `ClaudeComposerAsk` is frame-absolute (everything lands by ~4s), so the held frame is the intended end state, not a truncation.

## Open items

None. Nothing is punting and no beat waits on a human-supplied asset.
