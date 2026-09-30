# CHECKS-REPORT — Every Fix Has A Ceiling.

PROOF GATE, written before the first render (nopunt SKILL.md §"SHOW / HOLD / CARD").

```
9 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

| Beat | Pattern | Class | Why |
|---|---|---|---|
| B00 | ClaudeComposerAsk | SHOW | ask types, send arms, four output lines land — COLD OPEN LAW |
| B01 | BrutalistHesitantWriter | SHOW | the misconception is typed, caught and corrected on screen |
| B02 | FaultSignatureTable | SHOW | four fault rows fill, four signature columns resolve, verdict lands |
| B03 | GroundingDrift | SHOW | two sentences land; one draws an anchor, one has none to draw |
| B04 | ShortlistReorder | SHOW | shortlist fills, connectors draw and cross, the absent answer lands |
| B05 | EvidenceTiers | SHOW | two rows fill, their evidence bars resolve visibly unequal |
| BVDT | ClaudeVerdictArtifact | SHOW | verdict lines land in sequence |
| BHTF | ClaudeComposerAsk | SHOW | handoff prompt types and holds while discussed |
| BOUT | TitleOutroChannel | SHOW | title restates, signature settles |

No bare CARDs. No PUNTs — and no new components, because the whole point of
this cut is that it replays figures the viewer has already been shown.

## GATE L — nothing was authored that already existed

This reel builds **zero** new components. Every body beat reuses the figure its
source reel already shipped, with that reel's measured data passed verbatim:

| Beat | Component | From |
|---|---|---|
| B02 | `FaultSignatureTable` | Ch. 7 reel, B07 |
| B03 | `GroundingDrift` | Ch. 8 reel, B05 |
| B04 | `ShortlistReorder` | Ch. 9 reel, B05 |
| B05 | `EvidenceTiers` | Ch. 8 reel, B04 — new content, existing component |

Only `sparkLine`, `verdict`, `caption` and `citation` differ from the sources:
the sparkline carries the ceiling framing, and the citation names which video
the figure came from so a viewer can go back to it.

## Teaching arc detail

- **FRAMEWORK before examples ✓** — B01 states the whole idea (three fixes, each
  bounded) before any chapter is replayed.
- **WORKED EXAMPLE ✓** — three of them, each the source chapter's own worked case.
- **FALSIFIABILITY ✓** — B05. The beat exists to say which half of these videos
  is measurement and which half is a declared stand-in. A summary is exactly
  where that distinction gets lost.
- **SCAFFOLDED VIEWER TASK ✓** — BHTF: write down what each layer can and cannot
  fix, then attribute the last ten wrong answers to a layer.
- **FOUR BOOKENDS ✓** — cold open, BLUF, verdict, handoff + outro.
- **NO-SOURCE-NO-VERDICT ✓** — every figure carries the video it came from in its
  citation line; every number is that reel's captured stdout.

## Legibility contract

| Requirement | Status |
|---|---|
| Names its on-screen artifact in `shot.show` / `visual_intent` | ✓ all body beats |
| ~15–35% negative space | designed for; confirmed at QC |
| Un-highlighted elements never below ~40% opacity | ✓ — inherited from the source components, all previously QC'd |
| Comparisons side-by-side, held ≥2s | ✓ B02 (four fault rows), B04 (before vs after), B05 (two tiers) |

## Honesty notes carried into the build

1. **No new claims.** Every measured figure in B02–B04 is passed verbatim from
   the source reel's beat sheet. If a number here disagrees with the video it
   came from, this reel is wrong.
2. **B05 is the reason this summary exists.** Two of the three reels ran a
   declared stand-in at the centre of their demo — a deterministic reader
   instead of an LLM (Ch. 7), and late interaction instead of a cross-encoder
   (Ch. 9). A recap that replays their clean results without repeating that
   declaration would quietly promote both to facts.
3. **The title is a claim about limits, not a criticism of the techniques.**
   B02–B04 each show the technique working before naming where it stops.
