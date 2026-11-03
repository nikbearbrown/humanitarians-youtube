# The Dataset With Zero Errors That's Still Poison

A dataset has zero data-entry errors, 100% verified ground-truth labels, and perfect coverage — yet the machine learning model trained on it produces severe, systematic harm.

When historical bias is present, the training data faithfully records a world shaped by past discrimination. Because the data has no errors, the model learns the historical distribution with near-flawless accuracy. Its accuracy *is* the harm: it projects what was into what will be, and its automated decisions generate the next round of biased data, closing a self-reinforcing feedback loop.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam trace the five-node loop connecting past practices, faithful records, trained models, automated decisions, and the future world.

---

### Key Takeaways & Carry-Out
- **The Epistemic Mechanism**: Historical bias means the training data accurately reflects past disparities ($P(Y_{\text{historical}} \mid x) \neq P(Y_{\text{fair}} \mid x)$). Standard diagnostics come back green because the model learned history with complete fidelity.
- **The Feedback Loop**: Automated decisions filter future opportunities, causing future company records to reflect the model's own bias — now legitimized as machine-driven merit.
- **Carry-Out Law**: When a dataset faithfully records a discriminatory past, the model's accuracy is the harm — it projects what was into what will be, and calls the projection truth.
- **The Inheritance Trade-off**: Every algorithmic fix (reweighting, fairness constraints, proxy removal) trades away predictive fit on historical data to inherit less of the past.
- **Direction A**: Zero data-entry errors and clean labels do NOT guarantee an unbiased or fair model.
- **Direction B**: A biased prediction from such a model does NOT imply that the training data was corrupt, noisy, or mislabeled.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Identify an AI model in your organization that predicts success or risk based on historical records. Trace the feedback loop: does high predictive accuracy on past data reinforce historical selection patterns into future decisions?
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Bias & Fairness
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 6: Bias — Where It Enters and Who Is Responsible)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/dataset-with-zero-errors-thats-still-poison
