# SOURCES — Counting The Wrong Words

One primary paper carries every figure, plus one quotation from the mycroft
repository. No aggregator, blog or summary sourced a number.

| On screen | Beat | Source |
|---|---|---|
| 73.8% of negative word **counts** | B03 | Loughran & McDonald 2011, body text |
| 121,217 filings | B03 | same |
| 1994–2008 | B03 | same, abstract |
| the seven words, and "more than one-fourth" | B04 | same, Table III discussion |
| costs = 4.61% of the total | B04 | same |
| *foreign* → international operations; *vice* → vice-presidents | B05 | same |
| *mine, cancer, crude, tire* identify an industry segment | B05 | same |
| Fin-Neg = 2,337 words including inflections | B06 | same |
| "about half as many words as the H4N-Inf list" | B06 | same |
| the attestation quotation | B08 | `mycroft @ b425b19`, `logs/attestations/market-sentiment-analysis-part-1-v0.2.0.md` |

## Reference

- Loughran, T. and McDonald, B., "When Is a Liability Not a Liability? Textual
  Analysis, Dictionaries, and 10-Ks", **The Journal of Finance LXVI(1),
  February 2011**.

## How the figures were read

A plain fetch of the PDF returned only its byte stream — FlateDecode streams and
font dictionaries, no readable text. The file was saved locally and run through
`pdftotext -layout`, and each figure was read from the paper's own sentences.
This is the same method used for the MuSiQue, HOPE and Harvey–Liu–Zhu reels, and
it is now the default whenever a publisher PDF will not yield its text.

## The correction this reel exists partly to make

The search that preceded the fetch reported the 73.8% figure as a share of
**distinct words**, and offered a separate ~50% figure as the "occurrences"
version. The paper says the opposite: 73.8% is of **word counts**. The ~50%
figure is a different, narrower result about the top 30 words minus five.

Both numbers were therefore re-read in context before either was used, and only
the first appears — with "of the counts, not of the list" stated on screen.
Had the search summary been trusted, this reel would have understated its own
central finding and attributed it to the wrong quantity.

## Claims NOT sourced here, and therefore not made

- Nothing about whether sentiment predicts returns — no source here addresses it.
- Nothing about any model, vendor, instrument or strategy.
- No figure for the Harvard list's size; only the ratio the paper states.
- Nothing about non-filing text beyond noting the result does not transfer
  automatically.
