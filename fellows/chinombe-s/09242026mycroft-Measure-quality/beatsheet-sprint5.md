# Beat Sheet — Mycroft Sprint 5: Measure Quality

**Channel:** claude-hai · **Persona:** Simba · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer, sprint report · Two cuts this build.

## 16:9 long cut — 4:01 (246.61s, Kokoro ground truth)

| Beat | Act | Timestamp | Duration | Pattern | Note |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 21.79s | `ClaudeComposerAsk` | Cold open — usable vs. good |
| B01 | SUMMARY | 0:21 | 12.14s | `ClaudeStatement` | BLUF — the split |
| B02 | STRUCTURE | 0:33 | 21.98s | `TwoWayCompare` | The judge — swap and compare |
| B03 | REASONING | 0:55 | 21.53s | `FactStack` | Why it's built this way |
| B04 | RESULTS | 1:17 | 16.70s | `DataTable` | The full sweep |
| B05 | RESULTS | 1:34 | 19.08s | `DataTable` | The cost split |
| B06 | REASONING | 1:53 | 21.60s | `FactStack` | A bug that isn't a mistake |
| B07 | FINDINGS | 2:14 | 17.81s | `FindingPair` | Same bug, second time |
| B08 | FINDINGS | 2:32 | 20.50s | `FindingPair` | What inconsistent actually looks like |
| B09 | SUMMARY | 2:53 | 25.46s | `ClaudeVerdictArtifact` | Verdict — measured, not assumed |
| B10 | REASONING | 3:18 | 26.35s | `FactStack` | What went wrong — the answer key |
| B11 | NEXT STEPS | 3:44 | 16.68s | `ClaudeComposerAsk` | Your Turn |
| B12 | OUTRO | 4:01 | 4.99s | `ClaudeTitleOutro` | Sign-off |

## 9:16 Shorts cut — 0:38 (38.54s, Kokoro ground truth)

THE SHORTS LAW derivative: single cycle, no revision, condensed subset (hook, the judge's swap-compare diagram, the cost-split finding, verdict, outro), pointing back to the long cut.

| Beat | Act | Timestamp | Duration | Pattern | Note |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 7.34s | `ClaudeComposerAsk916` | Condensed hook |
| B01 | STRUCTURE | 0:07 | 10.46s | `TwoWayCompare916` | Judge swap-compare, portrait |
| B02 | RESULTS | 0:17 | 9.29s | `DataTable916` | Cost split |
| B03 | SUMMARY | 0:27 | 6.89s | `ClaudeVerdictArtifact916` | Verdict |
| B04 | OUTRO | 0:33 | 4.56s | `ClaudeTitleOutro916` | Points back to the long cut |

## GATE L note

B02's judge mechanism (compare two answers, twice, order swapped, flag disagreement as inconsistent) doesn't match any existing loop/fan-out component in the library — it's neither a single-item loop (`AutoregressiveLoop`, built for decode) nor a fan-in/fan-out (`ParallelPass`, built for prefill). Rather than author a third bespoke diagram component for a shape used once in this script, `TwoWayCompare` (an existing, legitimate side-by-side compare component — not a text card standing in for a different mechanism) was reused, framed as Pass 1 vs. Pass 2 with an ok/not-ok row for the consistency check. This is a judgment call, documented rather than treated as equivalent to prefill-decode's from-scratch `ParallelPass`/`AutoregressiveLoop` builds. `TwoWayCompare916` (portrait composition) was added to `Root.tsx` for the Shorts cut — `TwoWayCompare` itself was already portrait-responsive, so no component code changed, only the composition registration. `tsc --noEmit` clean.

## Sources
Sprint 5 report (What the sprint was for / What was built / What was run / Results / Findings / What went wrong), as supplied by the user.
