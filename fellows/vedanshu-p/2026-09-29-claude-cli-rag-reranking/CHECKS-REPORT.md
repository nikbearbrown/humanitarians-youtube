# CHECKS-REPORT — Reorder Is Not Retrieve.

PROOF GATE, written before the first render (nopunt SKILL.md §"SHOW / HOLD / CARD").

```
12 SHOW / 0 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

Every OUTPUT beat is SHOW by definition here — the CLI spine requires motion,
never a still, and all three output beats (B04, B05, B08) animate their reveal
in narration order.

## Per-beat classification

| Beat | Pattern | Class | Why |
|---|---|---|---|
| B00 | ClaudeComposerAsk | SHOW | ask types, send arms, three output lines land — COLD OPEN LAW |
| B01 | RagExecutiveSummary | SHOW | the problem stated before any build; headline → subline → spark |
| B02 | ClaudeComposerAsk | SHOW | the cycle-1 prompt types in |
| B03 | ClaudeCodeBeat | SHOW | real source from `code/rerank.py` |
| B04 | TwoStageCascade | SHOW | corpus block fills, each stage arrow draws with its measured cost, the prohibitive figure lands |
| B05 | ShortlistReorder | SHOW | shortlist fills, connectors draw and cross, the absent answer lands last |
| B06 | ClaudeComposerAsk | SHOW | the revision prompt types, `runningText: "updating…"` |
| B07 | ClaudeCodeBeat | SHOW | real source from `code/rewrite.py` |
| B08 | RetrievalMatrix | SHOW | rows fill, then each column resolves; one cell flips |
| B09 | RagExecutiveSummary | SHOW | the lesson and its three declared limits |
| B10 | ClaudeComposerAsk | SHOW | handoff prompt types and holds while discussed |
| B11 | TitleOutroChannel | SHOW | title restates, signature settles |

No bare CARDs. No PUNTs — both bespoke visual needs were searched (GATE L),
missed, and discharged by **building** the component.

## Spine compliance (cli-explainer, mandatory in the 16:9 cut)

| Requirement | Where |
|---|---|
| PROBLEM beat after intro, before the CLI loop | B01 |
| Cycle 1: CLI → CODE → OUTPUT | B02 → B03 → B04 (+ B05, second result from the same run) |
| **At least one revision** (THE REVISION LAW) | B06 → B07 → B08 |
| SUMMARY | B09 |
| NEXT STEPS | B10 |
| OUTRO last | B11 |

The revision is motivated by cycle 1's *measured* result, not by a scripted
beat: B05 reports 0 promoted / 0 demoted and one answer absent from the
shortlist, and B06 changes approach because of it.

## Teaching arc detail

- **FRAMEWORK before examples ✓** — B01 establishes why a second pass exists
  (the query-independent score) before any code or result appears.
- **WORKED EXAMPLE ✓** — the chapter's own vague question is in the corpus, and
  B05 walks one concrete shortlist end to end.
- **FALSIFIABILITY ✓** — twice. B03's `prove_query_independence` is a check that
  could have failed and didn't (0.00e+00). And the cycle-1 result is a **null**:
  the reel reports that the re-ranker moved nothing rather than reaching for a
  corpus where it would.
- **SCAFFOLDED VIEWER TASK ✓** — B10 asks the viewer to split their own failures
  into "present but ranked low" vs "missing entirely", which is exactly the
  diagnostic that decides whether re-ranking is worth buying.
- **FOUR BOOKENDS ✓** — intro, problem, summary, handoff + outro.
- **NO-SOURCE-NO-VERDICT ✓** — every number on screen is captured stdout from
  `_run-rerank.txt` / `_run-rewrite.txt`; every concept carries its citation.

## Legibility contract

| Requirement | Status |
|---|---|
| Names its on-screen artifact in `shot.show` / `visual_intent` | ✓ all body beats |
| ~15–35% negative space | designed for; confirmed at QC |
| Un-highlighted elements never below ~40% opacity | ✓ — B05's non-gold connectors sit at 55% |
| Comparisons side-by-side, held ≥2s | ✓ B04 (corpus vs shortlist), B05 (before vs after), B08 (literal vs rewritten) |

## Honesty notes carried into the build

1. **Stage 2 is NOT a cross-encoder, and the reel says so on screen.** No
   cross-encoder checkpoint exists in this machine's model cache,
   `transformers` is absent, and there is no network. Stage 2 is late
   interaction (MaxSim) — a real joint query-document interaction, and a weaker
   stand-in for the mechanism Chapter 9 describes. Declared in B04's caption and
   in B09's narration.
2. **The rewrites are hand-written.** HyDE and Rewrite-Retrieve-Read both need a
   language model; this machine has none. The caveat appears in the source file
   shown in B07, not only in the voice.
3. **Six questions is a small test**, and B09 says so. The reel reports a
   direction, not a benchmark.
4. **The chapter's 27% figure is Nogueira & Cho's**, never presented as this
   reel's result. It does not appear on screen at all.
