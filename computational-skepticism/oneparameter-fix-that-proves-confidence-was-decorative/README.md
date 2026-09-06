# The One-Parameter Fix That Proves the Confidence Was Decorative

Deep neural networks routinely output extreme confidence scores. They output 99% certainty with crisp, unwavering precision. Yet when evaluated on real test benchmarks, models making 99% claims are often correct only 85% of the time.

Why does a single learned number prove that original 99% was decorative all along?

The answer lies in temperature scaling—a post-processing calibration technique highlighted by Guo et al. (ICML 2017). Modern deep networks achieve high accuracy because their unnormalized output scores (logits) rank classes correctly. But during training with cross-entropy and negative log-likelihood, logits grow excessively large, causing the standard softmax function to squash probabilities into extreme, overconfident spikes near 1.0.

By introducing a single learned scalar $T > 1.0$ and dividing every logit by $T$ before exponentiation ($\text{softmax}(z / T)$), the probability distribution gently sloshes and spreads outward, bringing stated confidence directly into alignment with empirical reality. Crucially, because division by a positive constant scalar is strictly monotonic, the relative order of logits is completely unchanged: $\text{argmax}(\text{softmax}(z / T)) \equiv \text{argmax}(z)$. Not a single classification decision changes or flips.

If dividing by one learned number fixes the probabilities without altering a single decision, the model's original confidence was never an intrinsic measure of certainty—it was decorative all along.

In this episode of *Computational Skepticism for AI*, Liam (in for Professor Bear) explores the separation of confidence and correctness, how temperature scaling diagnoses decorative probabilities, and the vital caveat of distribution shift.

---

### Key Takeaways & Carry-Out
- **The Overconfidence Gap**: High classification accuracy does not imply honest probabilistic calibration. Modern neural nets are consistently overconfident in their highest probability bins.
- **Strict Monotonic Invariance**: Dividing logits by scalar $T$ preserves class rank order identically for every single input. Top-1 predictions remain 100% invariant.
- **The Epistemic Proof**: Because accuracy remains identical while probabilities soften to match ground truth, stated confidence was separable from decision-making all along.
- **Carry-Out Law**: "If dividing by one learned number fixes the probabilities without altering a single decision, the original confidence was decorative all along."
- **Direction A (In-Distribution Calibration)**: On in-distribution validation data, temperature scaling turns an arbitrary score into a well-calibrated, risk-usable probability.
- **Direction B (The Distribution Shift Caveat)**: Calibration is not robust to domain shift; when data drifts from the calibration set, the temperature-scaled confidence goes stale silently.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take a classifier in your pipeline with a softmax output. Measure its empirical accuracy in the top confidence bin. If your ninety-nine percent predictions only succeed eighty-five percent of the time, fit a single temperature parameter T on held-out logits and verify that the ranking never changes.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Uncertainty & Probability
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 2: Probability, Uncertainty, and the Confidence Illusion)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **AI Disclosure**: Synthetic narration generated locally via Kokoro `am_onyx`. Visuals algorithmically rendered via Manim and Remotion. Zero generative video, zero paid APIs.
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/oneparameter-fix-that-proves-confidence-was-decorative
