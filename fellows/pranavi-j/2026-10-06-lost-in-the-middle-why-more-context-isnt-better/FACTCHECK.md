# FACTCHECK — Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer

Status: **RESOLVED — fellow reviewed 2026-10-06. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | Language models are reliably better at using information near the start/end of a long context than information buried in the middle | PASS — this is a well-documented, widely-replicated finding in long-context LLM research (often called the "lost in the middle" / U-shaped retrieval-accuracy effect), not specific to any one vendor | General, well-known published research finding — kept generic per house style, no specific paper's numeric results quoted | — |
| 2 | B03 | Framed as uneven attention distribution across a long input, not a hard inability to "see" the middle | PASS — standard explanation for the effect; consistent with how the phenomenon is generally described, phrased qualitatively (no specific attention-weight numbers claimed) | — | — |
| 3 | B04/B05 | Moving the identical fact from the middle to the start/end of the same document changes whether a model reliably finds it | PASS — this is the defining shape of the documented effect, stated as an illustrative generic scenario, not a specific benchmarked test of a named model | — | Narration should not imply this always happens 100% of the time or to the same degree for every model — phrased as "might miss it" / "can be unreliable," not a universal guarantee |
| 4 | B06, B07 | The 3-question rubric and takeaway | PASS — editorial framework/takeaway, not a factual claim requiring external citation | — | — |

## Dramatization check

No beat names or benchmarks a specific real model, claims a specific product's current
long-context performance, or quotes a specific percentage/statistic from any paper. The
onboarding-document worked example is a fully generic, illustrative scenario, not a disclosed
test of a named system.

## Resolved 2026-10-06

1. Confirmed no beat drifts into citing a specific number (e.g. "accuracy drops by X%") — the
   draft is intentionally qualitative throughout.

Gate P (narration review) can proceed.
