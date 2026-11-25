# Fact check

All narration claims map to the primary-source ledger. Exact short excerpts and source passage locations appear in [research/sources.md](research/sources.md).

| Beat | Claims checked | Ledger IDs |
| --- | --- | --- |
| B00INTRO | Presenter, topic and AI disclosure. | C0 |
| B01GREEDY | Greedy top-token choice, token definition, removal of its sampling draw, computation of scores. | C1, C4 |
| B02ROUNDING | Finite precision and rounding, changed sum from order, possible near-tie flip and later divergence. | C2, C3 |
| B03BATCH | Batched requests, batch-dependent arithmetic and changing load. | C4 |
| B04HARDWARE | Fixed-batch determinism differs from batch invariance, CPU/TPU scope, concurrency alone is insufficient. | C5 |
| B05FIX | Batch-invariant computation, identical completions in the tested setup, timing cost and its partial reduction. | C6, C7 |
| B06CONTROLS | Deterministic algorithm selection or error, cross-release/platform/CPU–GPU limits. | C8, C9 |
| B07TAKEAWAY | Controlled configuration and repeat-testing advice. | C10 |
| B99CREDIT | Presenter and channel. | C0 |

The headline is a question about repeatability under temperature zero. It does not claim that every inference run changes. The near-tie explanation is explicitly a possibility. The exact larger-model completion test and the separate smaller-model timing test stay distinct in the ledger.
