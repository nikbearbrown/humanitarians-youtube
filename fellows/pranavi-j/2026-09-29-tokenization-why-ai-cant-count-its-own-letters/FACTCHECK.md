# FACTCHECK — Tokenization: Why AI Can't Count the Letters in Its Own Words

Status: **RESOLVED — fellow reviewed 2026-10-02. Cleared for Gate P (narration lock).**

| # | Beat | Claim (as spoken/shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02/B03 | Language models process text as tokens (sub-word chunks), not individual characters | PASS — this is a well-established, uncontested fact about how transformer-based language models are built (byte-pair-encoding/similar tokenizers), not specific to any one vendor | — | — |
| 2 | B03/B04 | A word can be split into tokens that don't align with its letter boundaries, causing character-counting errors | PASS — well-documented, widely-discussed class of behavior (the "how many Rs in strawberry"-style failure is publicly well known as an illustrative example of this mechanism) | — | — |
| 3 | B05 | Spelling a word out letter-by-letter (with separators) typically improves a model's character-level accuracy on it | PASS — follows directly from the mechanism in B03: if each letter becomes its own token, the model has direct access to individual letters; a generically-stated expected effect, not a specific benchmarked claim | Narration should not claim this works 100% of the time or for every model — phrase as "gets it right" for this illustrative case, not as a universal guarantee |
| 4 | B06, B07 | The 3-question rubric and takeaway | PASS — editorial framework/takeaway, not a factual claim requiring external citation | — | — |

## Dramatization check

No beat names or benchmarks a specific real model, claims a specific product's current tokenizer
behavior, or presents the worked example as a disclosed test of a named system. The "strawberry"
style example is treated as a well-known, generic illustration of the mechanism, not a live
benchmark result.

## Resolved 2026-10-02

1. **Worked example kept fully generic** — no specific real model named or benchmarked.

Gate P (narration review) can proceed.
