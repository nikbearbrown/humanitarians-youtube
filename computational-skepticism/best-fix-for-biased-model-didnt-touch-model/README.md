# The Best Fix for a Biased Model Didn't Touch the Model

Three engineering teams are assigned to fix the exact same biased AI system. The first team rewrites the loss function with an algorithmic fairness penalty; the disparity drops slightly. The second team resamples the training data with costly underrepresented cohort collection; the disparity shifts shape, but persists. The third team touches neither the model nor the training data — they examine the downstream deployment room, restructure reviewer heuristics and appeal thresholds, and the disparity collapses by an order of magnitude.

How can the most effective fix for a biased AI leave the model completely untouched?

Because bias flows from the world to decisions along multiple causal paths. An intervention acts as a dam: it only stops what its specific path carries. When bias enters through proxy features that bypass the model directly into downstream human review, polishing the model's internal weights leaves that massive conduit wide open. Teams One and Two were not incompetent; they were low-leverage, intervening on real paths that carried very little of the bias.

In this episode of *Computational Skepticism for AI*, Liam (in for Professor Bear) unpacks the leverage analysis protocol: why engineers must map the full causal graph before writing code, and why the highest-leverage intervention often lives entirely outside the model.

---

### Key Takeaways & Carry-Out
- **The Parable of the Three Teams**: Honest, technically competent debiasing efforts inside the model produce marginal results if the primary bias-carrying conduit bypasses the algorithm.
- **The Dam Principle**: An intervention only removes what its causal path carries. A dam on model parameters cannot block bias flowing through downstream reviewer interpretation.
- **Leverage Analysis Protocol**:
  1. Map the complete graph from real-world inputs to final decisions.
  2. Trace every candidate path carrying bias flow through the system.
  3. Test prospective interventions as dams on specific candidate paths.
  4. Intervene at the bottleneck carrying the largest volume of bias.
- **Carry-Out Law**: "An intervention only removes what its causal path carries — and the highest-leverage path often bypasses the model entirely."
- **Direction A (Model Balance ⇏ Fair Outcome)**: Perfectly balanced internal weights do not guarantee fair real-world outcomes if downstream review paths leak bias.
- **Direction B (Outcome Disparity ⇏ Model Flaw)**: Discovering disparities in deployed decisions does not prove the model is the primary culprit; the dominant path may bypass it entirely.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take an AI model in your organization that assists real-world decisions. Map the causal path from real-world inputs to the final outcome: data collection, model scoring, and the human review process. If an unfair disparity appears, which path carries the most bias — and would retraining the model even touch it?
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Bias & Fairness
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 6: Bias: Where It Enters and Who Is Responsible)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **AI Disclosure**: Synthetic narration generated locally via Kokoro `am_onyx`. Visuals algorithmically rendered via Manim and Remotion. Zero generative video, zero paid APIs.
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/best-fix-for-biased-model-didnt-touch-model
