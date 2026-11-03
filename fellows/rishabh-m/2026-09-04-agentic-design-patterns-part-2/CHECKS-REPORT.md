# CHECKS-REPORT — agentic-design-patterns-part-2

Written BEFORE the first slate compiled, per ai-explainer PROOF GATE.

## Beat classification

**13 SHOW / 2 justified-HOLD / 0 PUNT-flagged**

| Beat | Class | Artifact named in `shot.show` |
|---|---|---|
| B00 | SHOW | composer ask types; running indicator; three output lines land |
| B01 | SHOW | writer types `agents`, corrects to `state` |
| B02 | SHOW | seven cards land, four across then three |
| B03 | SHOW | manager fans to three specialists; all converge on the shared store |
| B04 | SHOW | incoming splits into three memory tiers; long-term lights |
| B05 | SHOW | action → capture → denoise gate → update |
| B06 | SHOW | goal → KPIs → monitor → drift check at the σ threshold |
| B07 | SHOW | error splits three ways; critical branch lights |
| B08 | SHOW | confidence gate → pause & review (state suspended) → resume |
| B09 | SHOW | query → vector search → rerank (top-K) → ground |
| B10 | SHOW | four patterns compose across one conversation |
| B11 | HOLD | three conditions land, then one lights — a judgment beat; the cards ARE the claim |
| B12 | SHOW | artifact page; seven verdict lines land in order |
| B13 | SHOW | suggested prompt types itself into the composer |
| B14 | HOLD | title restate + rule + handle + credit — held card by OUTRO LAW |

No bare CARD beats. Every structural claim names its on-screen artifact.

## Teaching arc

| Item | Status | Where |
|---|---|---|
| FRAMEWORK before examples | ✓ | B02 presents all seven before B03–B09 explain any |
| WORKED EXAMPLE | ✓ | B10 — one customer conversation through four composed patterns |
| FALSIFIABILITY | ✓ | B11 — one task, one user, one session: skip all seven |
| SCAFFOLDED TASK | ✓ | B13 — audit YOUR system; name the state most likely to corrupt |
| BOOKENDS | ✓ | B00 cold open · B01 BLUF · B12 verdict · B13 handoff · B14 outro |
| NO-SOURCE-NO-VERDICT | ✓ | 20 claims traced in FACTCHECK.md; the thesis flagged as interpretation |

## Legibility contract

- Every SHOW beat names its artifact in `shot.show`.
- One terracotta moment per beat (`accentId`) — ACCENT LAW.
- `AgenticPatternDiagram` positions from the shared `SAFE` constant; the grid
  stretches to fill it, so Gate V's 55% ink floor is met by construction.
- Node labels kept to 1–2 words on the seven-card framework beat (B02), which
  runs four columns and therefore has the narrowest cards in the reel.

## Deviations logged

1. **B01 narration is 39 words**, above the EXECUTIVE-SUMMARY LAW's 20–35 range.
   Deliberate. The law's binding requirement is a ≥9s audio window; the real
   constraint is that Gate V samples at 50% of the beat and the hesitant-writer
   has a fixed ~5.3s typing floor for three lines. A 33-word take measured 9.94s,
   putting the 50% sample at 5.0s — mid-type, which fails `underfill`. Solved
   from both sides: text cut to three lines (lower floor) and narration grown to
   39 words → 12.0s, sampling at 6.0s. See HOUSE-RULES.local.md gotcha #1.

2. **ASK→RESULT LAW applied at the bookends, not per illustration** — same
   reading as Part 1. A composer micro-beat before each of the nine illustrated
   beats would add nine UI beats and violate ILLUSTRATE LAW's anti-wallpaper
   rule. The cold open is a true ask→result pair.

3. **`ClaudeTitleOutro` not used** — it hardcodes `@NikBearBrown`
   (OUTRO-LOCK.md). `HaiTitleOutro` carries the correct channel, no mascot.

4. **No new components.** GATE L found no reusable match for memory tiers, RAG
   or HITL, but `AgenticPatternDiagram` (built in Part 1) covers all seven
   topologies. Recorded because "no punt" here is a result, not an omission.
