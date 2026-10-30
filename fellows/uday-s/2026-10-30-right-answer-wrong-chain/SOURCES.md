# SOURCES — Right Answer, Wrong Chain

Four sources. Every figure on screen comes from a primary paper; no aggregator,
blog or summary sourced a number.

| On screen | Beat | Source |
|---|---|---|
| DiRe answer F1 — HotpotQA 68.8, 2Wiki 63.4, MuSiQue 37.8 | B03 | MuSiQue (TACL), Table 4, read from the PDF |
| "lower is harder to cheat" / bypassing reasoning steps | B03 | same paper, §8.1 |
| 57.9 / 47.9 / 28.1 across 2-, 3-, 4-hop | B04 | same paper, §8.1 — best model EX(SA) |
| "stays around 42% irrespective of the number of hops" | B04 | same paper, same paragraph — the EE model |
| 78% of a representative MATH test subset | B05 | Let's Verify Step by Step, abstract |
| "process supervision significantly outperforms outcome supervision" | B05 | same abstract, quoted |
| 800,000 step-level human labels (PRM800K) | B05 | same abstract |
| parity on grade-school maths | B06 | Uesato et al. 2022 |
| outcome supervision no more statistically difficult, up to polynomial factors | B06 | arXiv 2502.10581 |

## Reference links

- MuSiQue (Trivedi, Balasubramanian, Khot, Sabharwal), TACL — https://aclanthology.org/2022.tacl-1.31.pdf
- Let's Verify Step by Step (Lightman et al.) — https://arxiv.org/abs/2305.20050
- Do We Need to Verify Step by Step? — https://arxiv.org/abs/2502.10581
- DiRe probe, original paper (Trivedi et al., EMNLP 2020) — cited by the MuSiQue
  paper as the origin of the metric; supplies no figure used here

## How the DiRe numbers were obtained

The TACL PDF would not yield its body text to a plain fetch — only link
annotations and metadata came back. The file was saved locally and extracted
with `pdftotext -layout`, and the figures were read out of Table 4 and the
surrounding paragraph in §8.1:

> the DiRe answer scores of HQ and 2W (68.8 and 63.4) are high, indicating that
> even disconnected reasoning (bypassing reasoning steps) can achieve such high
> scores. In contrast, this number is significantly lower (37.8) for MuSiQue.

This is the same method used for the HOPE reel, where a search summary had
misread a results table. A summary describing DiRe was available here and was
not used for any figure.

## A source that was found but not cited

A survey encountered during research attributes to Xi et al. (2025) the point
that in agentic settings an individual action's correctness is not clear-cut and
must be estimated from eventual outcomes. **That paper was not retrieved
directly, so it is not cited and no figure from it appears.** B07 makes the
related argument from the verified contrast instead, and its citation strip says
on screen that the inference is reasoning rather than a cited finding.

## Claims NOT sourced here, and therefore not made

- Nothing about any deployed agent system or product.
- No compute, cost or training-time figures.
- No numeric margin for process over outcome supervision — the abstract gives
  none.
- No recommendation of a benchmark or a training method.
