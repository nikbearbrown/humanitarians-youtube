# SOURCES — State Space Models and Mamba Architecture

Every claim made in narration or shown on screen, with where it comes from.
Nothing here is from memory: each row was checked against the paper's own
abstract or a published result before it was narrated.

| # | Claim (spoken / shown) | Beat | Source |
|---|---|---|---|
| 1 | Attention cost grows with the square of the sequence length | B01, B03 | Standard result for full self-attention (Vaswani et al. 2017); restated, not novel |
| 2 | An SSM keeps one fixed-size state, so cost is linear in sequence length | B01, B04 | Mamba abstract: "linear scaling in sequence length" — [arXiv:2312.00752](https://arxiv.org/abs/2312.00752) |
| 3 | SSM form: `h'(t) = A h(t) + B x(t)`, `y(t) = C h(t)` | B04 | Standard continuous-time state space formulation (control theory); as used by S4/Mamba |
| 4 | S4 = Gu, Goel & Ré, 2021 | B05 | "Efficiently Modeling Long Sequences with Structured State Spaces" — [arXiv:2111.00396](https://arxiv.org/abs/2111.00396) |
| 5 | S4 was the first architecture to get a non-trivial result on Path-X | B05 | Reported for S4 on the Long Range Arena Path-X task; Path-X had defeated all prior models |
| 6 | In S4 the matrices are the same for every token | B05 | Follows from S4's time-invariant (LTI) formulation — the property Mamba's selection removes |
| 7 | Mamba = Gu & Dao, submitted 1 Dec 2023 | B06 | [arXiv:2312.00752](https://arxiv.org/abs/2312.00752) v1 1 Dec 2023, v2 31 May 2024 |
| 8 | Selection = SSM parameters become functions of the input | B06 | Abstract: parameters become "functions of the input", letting the model "selectively propagate or forget information" |
| 9 | Mamba uses a hardware-aware parallel scan | B06 | Paper's hardware-aware algorithm, adopted because input-dependent parameters break the convolutional (LTI) training path |
| 10 | 5× higher inference throughput than a similar-size Transformer | B07 | Abstract: "5× higher throughput than Transformers" |
| 11 | Linear scaling in sequence length | B07 | Abstract, verbatim |
| 12 | Performance improves out to million-length sequences | B07 | Abstract: "performance improves on real data up to million-length sequences" |
| 13 | Mamba-3B outperforms Transformers its size and matches ones twice its size | B07 | Abstract, verbatim |
| 14 | Mamba drops attention and MLP blocks | B07 | Abstract: eliminates "attention or even MLP blocks" |
| 15 | SSMs cannot copy arbitrary strings unless state grows with the sequence | B08 | Jelassi et al. 2024, "Repeat After Me: Transformers are Better than State Space Models at Copying" — [arXiv:2402.01032](https://arxiv.org/abs/2402.01032) |
| 16 | This is not a Mamba design flaw — any fixed-memory model has the ceiling | B08 | Same paper: the limitation follows from fixed state size, not from Mamba specifically |

## Claims deliberately NOT made

- **No benchmark table, no leaderboard numbers, no accuracy percentages.** Only
  the four headline claims the Mamba abstract states in its own words appear on
  screen. Anything more would need the results tables re-read, which was not
  done for this cut.
- **No claim that Mamba beats Transformers in general.** The reel states the
  specific comparisons the abstract makes and then spends a full beat on where
  it loses.
- **No claim about Mamba-2, Jamba, or any successor.** Out of scope for this cut.
- **No throughput number of my own.** Nothing was benchmarked locally; the 5×
  is attributed to the paper on screen, not asserted as measured.

## Dating (DOUBLE-CHECK LAW)

Publication years are load-bearing here (2021 → 2023 → 2024 is the argument's
spine), so they stay. No model version numbers, product names, or "current
state of the art" phrasing appears anywhere — those rot.
