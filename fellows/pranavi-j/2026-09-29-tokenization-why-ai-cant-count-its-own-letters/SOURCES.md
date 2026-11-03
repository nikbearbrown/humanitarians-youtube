# SOURCES — Tokenization: Why AI Can't Count the Letters in Its Own Words

This is a general AI/STEM topic explainer, not a report of real engineering work. All content is
an editorial framework plus a well-known, generic illustration of a widely-documented mechanism —
no external sources are used.

## Claim → source mapping

| Beat | Claim | Source | Notes |
|---|---|---|---|
| B02/B03 | Language models process text as tokens, not individual characters | General, uncontested description of how transformer-based tokenizers work | No specific model/vendor cited or needed |
| B04 | A word's token split can misalign with its letters, causing counting errors | Well-documented, widely-discussed class of LLM behavior (the "letter-counting" failure mode) | Illustrative, not a live benchmark of any named product |
| B05 | Spelling a word out letter-by-letter typically improves character-level accuracy | Follows directly from the tokenization mechanism in B03/B04 | Framed as an illustrative expected effect, not a universal guarantee |

## Citation status

- No external sources are used — the worked example and falsifiability case are original,
  generic illustrations of a well-known mechanism, not drawn from a specific real benchmark,
  disclosed test, or named model/vendor.
