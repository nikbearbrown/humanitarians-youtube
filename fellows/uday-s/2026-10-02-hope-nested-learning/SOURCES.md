# SOURCES — Levels, Not Layers

Primary source is the paper. The announcement blog is used only for framing,
never for a number, because it presents its results as charts with no figures in
the text.

| On screen | Beat | Source |
|---|---|---|
| HOPE is a self-modifying architecture, a Titans variant | B01 | paper, section 8 |
| depth is the illusion; levels are the axis | B01 | the paper's title and section 1 |
| weights never update / attention holds one context | B03 | paper, section 1 |
| CMS: a spectrum of blocks, each on its own update frequency | B03 | paper, section 7 |
| the worked CMS example uses 4 levels of MLP blocks | B03 | paper, section 7 cost analysis |
| Wiki ppl 14.39 / 15.60 / 17.92 | B04 | Table 2, 1.3B params / 100B tokens |
| LAMBADA acc 51.0 / 49.1 / 42.6 | B04 | Table 2, same row block |
| avg ppl 12.24 -> 13.04, acc 58.1 -> 57.3 without CMS | B05 | Table 6 |
| S-NIAH-3 @16K: 4.0 / 5.8 / 21.2 / 24.8 / 40.8 | B06 | Table 1 |
| "comparing with other attention-free models, Hope achieves the best performance" | B06 | section 9.2, quoted |
| CTNL: ICL collapses, Hope-3 nearly recovers | B07 | section 9.1 |
| "catastrophic forgetting is not 'solved' in general" | B08 | conclusion, page 40 |
| "a roadmap rather than a destination" | B08 | same |

## Reference links

- Google Research announcement - https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/
- The paper (arXiv) - https://arxiv.org/abs/2512.24695
- Author's copy - https://alibehrouz.com/files/NL.pdf

## How the tables were read

`pdftotext` in READING ORDER, not `-layout`. The layout pass interleaved the
columns and shifted rows against their labels, which is exactly how a wrong
figure gets on screen. In reading order each model label is followed by its own
first four numeric cells, so Wiki ppl / LMB ppl / LMB acc / PIQA acc are
unambiguously attributable. Columns further right did not survive and were not
used.

## A source that was rejected

A web summary gave HOPE's 1.3B scores as 15.11 Wiki / 11.63 LMB. The paper says
14.39 / 10.08; 15.60 / 11.41 is the TITANS row. The summary had slid one row and
invented the decimals. It is recorded here because it is the exact failure mode
this reel's own rubric is about: a number quoted without its table.

## Claims NOT sourced here, and therefore not made

- Nothing about HOPE in any shipped Google product.
- Nothing about training cost, throughput, or inference speed.
- No comparison to any model outside the paper's own baseline tables.
