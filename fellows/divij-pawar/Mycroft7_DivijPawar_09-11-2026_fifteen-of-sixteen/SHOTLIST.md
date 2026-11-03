# SHOTLIST.md — fifteen-of-sixteen (GATE F)

This file satisfies the toolkit's GATE F requirement. It is the per-beat
shot list for this reel's 18 beats (B00–B17). No beat uses a stock/generic
stand-in; every shot is either a live UI bookend or a diagram that enacts a
real, sourced claim (see `FACTCHECK.md`).

| Beat | Shot type | Scene / pattern | On-screen artifact |
|---|---|---|---|
| B00 | REMOTION | `ClaudeComposerAsk` | Cold-open composer card: 15/16 killed, the fix-verification finding |
| B01 | MANIM | `B01_OpenThreads` | Recap of last week's open threads (16/31 false positives, 0 real conflicts) |
| B02 | MANIM | `B02_NumberTagging` | Concept tagging excludes tagged numbers from comparison |
| B03 | MANIM | `B03_ThreeBugs` | Three specific tagging bugs, each caught by a named test, marked FIXED |
| B04 | MANIM | `B04_ReplayThroughGate` | Replay against the same 16 real runs, not new synthetic examples |
| B05 | MANIM | `B05_CheckedTwice` | Module-direct and production-API routes, both independently 15/16 |
| B06 | MANIM | `B06_TruePositivePreserved` | 15/16 killed; the 1 survivor labeled TRUE POSITIVE, PRESERVED |
| B07 | MANIM | `B07_SharedContextFork` | Same-evidence test: 4 live runs, role-swap control, shared SEC data fork |
| B08 | MANIM | `B08_ZeroRealNumbers` | Real vs. fabricated context box, showing mistral-7b's real fabricated quote + struck-out real URL (queried from `accountability.db`, run `09cc72b6`) |
| B09 | MANIM | `B09_SignAndMagnitude` | 4th run: real net income vs. wrong-sign, 1000x-magnitude fabricated figure |
| B10 | MANIM | `B10_ModelScoreboard` | Model A (4/4 correct, +1 unsupported) vs. Model B (0/4 grounded) scoreboard |
| B11 | MANIM | `B11_RouteRewire` | Same-day production wiring; `concept_aware` now the default rule |
| B12 | MANIM | `B12_RegexFix` | Comma-grouped number regex bug, fixed and reconfirmed against the historical case |
| B13 | MANIM | `B13_VerificationRateZero` | Claim verification wired into `/api/compare`, real fabrication replayed, `verification_rate = 0.0` |
| B14 | MANIM | `B14_TrueNowList` | "True now" callback list to prior confirmed beats |
| B15 | MANIM | `B15_StillNotTrueAndUncommitted` | Honest-ledger warning list, commit hash, growing file counter |
| B16 | MANIM | `B16_FifteenKilledReprise` | Cold-open counter reprise + dense end-card stats |
| B17 | REMOTION | `ClaudeTitleOutro` | Title restate, handle, subline — kept simple per OUTRO-LAW |

B08 is this reel's highest-attention beat for render-time QC (real fabricated
text swapped in during this build's re-render pass, replacing illustrative
placeholder text) — confirmed clean against rendered frames at 1080p with no
overlap against the adjacent REAL CONTEXT / FABRICATED boxes.
