# B04 — Interpretable Attention

- Encoded past steps and future prediction blocks split by a "now" divider
- Attention lines connect each prediction to the past steps it focused on
- Short-horizon forecasts attend to recent quarters
- Long-horizon forecasts attend to same-quarter-last-year
- A heatmap makes the attention weights readable at a glance
