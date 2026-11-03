# FACTCHECK — The Classifier That Learned When Not to Guess

Status: **RESOLVED — fellow reviewed 2026-10-06. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | 21 items fell through to "Unknown Source"; 13 already resolved by prior fixes; 8 remain | PASS — directly measured by re-running the live `identifySource()` function (extracted from the current `workflow.dev.json`) against the actual 21 DB rows, this session | `mycroft/scripts/regulatory-intel/B2-VERIFICATION.md` (2026-10-06 addendum) | — |
| 2 | B03 | The 8 residual example headlines (24-Hour Trading, KYC, etc.) are real | PASS — verbatim titles from `regulatory_feeds` table, `localhost:5431`, `mycroft_intelligence` DB | Live `psql` query, this session | — |
| 3 | B04 | New node only calls the LLM for `source_feed === 'Unknown Source'` items; fails open on error | PASS — confirmed by reading the shipped node code directly (`workflow.dev.json`, `Layer 2 - LLM Source Classification`) | `mycroft/scripts/regulatory-intel/workflow.dev.json` | — |
| 4 | B05 | 0 already-resolved items mutated; 1 of 8 resolved; 7 declined; 0 errors on this run | PASS — measured directly via a Node.js harness running the exact extracted shipped code against the real 21 DB rows, this session | `B2-VERIFICATION.md` live-verification section | — |
| 5 | B05 | Fail-open path (unreachable Ollama) leaves items unaffected | PASS — separately tested by pointing the extracted code at an unreachable port | `B2-VERIFICATION.md` | — |
| 6 | B06 | 1-of-8 is honestly framed as a correct outcome, not a shortfall | PASS — editorial framing, consistent with the measured result (model declined rather than mis-classified) | — | — |

## Dramatization check

No invented numbers. All counts (21/13/8, 0 mutated/1 resolved/7 declined/0 errors) are the exact
figures measured this session against the real local DB and the real shipped code — not
simulated, not rounded for effect.

## Resolved 2026-10-06

1. Confirmed the chosen headline examples (B03) and the resolved example (B05) are fine as
   verbatim text; any on-screen truncation for longer titles is a layout detail only, narration
   text unchanged.

Gate P (narration review) can proceed.
