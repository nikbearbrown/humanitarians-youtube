# SOURCES — Mixture of Experts

Brief supplied by the requester (Likhith); points checked against the primary sources below (abstracts retrieved 2026-09-28).

- Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer", 2017 — https://arxiv.org/abs/1701.06538 — "A trainable gating network determines a sparse combination of these experts to use for each example."
- Jiang et al. (Mistral AI), "Mixtral of Experts", 2024 — https://arxiv.org/abs/2401.04088 — "each layer is composed of 8 feedforward blocks (i.e. experts). For every token, at each layer, a router network selects two experts"; "each token has access to 47B parameters, but only uses 13B active parameters during inference".
- DeepSeek-AI, "DeepSeek-V3 Technical Report", 2024 — https://arxiv.org/abs/2412.19437 — "671B total parameters with 37B activated for each token".

## Corrections / de-sensationalising
- "Experts" are the feed-forward blocks inside each layer, not whole separate models; B04 shows the split *inside one layer* and the verdict says so.
- Experts are not topic specialists in a human sense; the reel never claims an expert "knows" a subject. Router scores and token words (B05/B06) are illustrative and labelled on screen.
- Active ≠ 2/8 of the model: attention and other shared weights always run, which is why Mixtral's active count is 13B, not 47B × 2/8. B07/B08 show the published 13B, not a derived ratio.
- B03's "double the size, double the cost" is the standard per-token compute scaling of dense transformers (≈ proportional to parameter count); shown qualitatively, no measured numbers.
- No model version/speed claims beyond the published parameter counts.
