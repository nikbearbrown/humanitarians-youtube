# Why Three Reasonable Fairness Definitions Cannot All Be True

In 2016, journalists analyzed the COMPAS risk assessment tool and discovered that innocent Black defendants were falsely flagged as high-risk at nearly twice the rate of innocent white defendants — a clear violation of equalized odds. The algorithm's creator responded that the tool was unbiased: within every risk bucket, the actual re-arrest rate was identical across racial groups — a clean satisfaction of calibration parity.

Both sides were mathematically correct. They were not having a factual disagreement that a larger dataset or a better algorithm could resolve. They were encountering a four-line theorem of Bayes' rule: when underlying base rates differ between groups, calibrating predictive scores mathematically forces their error rates apart.

In this episode of *Computational Skepticism for AI*, Liam (in for Professor Bear) derives the odds identity that connects calibration to error rates, demonstrates why the two definitions cannot simultaneously hold, and explains why choosing a fairness metric is always a values decision disguised as an engineering parameter.

---

### Key Takeaways & Carry-Out
- **The COMPAS Puzzle**: ProPublica and Northpointe evaluated the exact same tool and reached contradictory conclusions; both were arithmetically accurate because they measured different properties.
- **The Three Fairness Properties**:
  1. *Calibration Parity (Score Honesty)*: Stated probabilities mean the same empirical frequency regardless of group membership ($P(Y=1 \mid \hat{P}=s, \text{Group } A) = s$).
  2. *False-Positive Rate Parity*: Innocent individuals face the same probability of wrongful accusation across groups ($FPR_A = FPR_B$).
  3. *True-Positive Rate Parity*: Positive individuals face the same detection rate across groups ($TPR_A = TPR_B$).
- **The Odds Identity Balance**:
  $$\frac{v}{1 - v} = \frac{p}{1 - p} \cdot \frac{t}{f}$$
  Precision odds equal base-rate odds multiplied by the error-rate ratio.
- **The Four-Line Impossibility Theorem**: Calibration locks precision odds across groups. Taking the ratio between two groups binds the error-rate ratio directly to the ratio of base rates:
  $$\frac{t_A / f_A}{t_B / f_B} = \frac{p_B(1 - p_A)}{p_A(1 - p_B)}$$
  If base rates differ ($p_A \neq p_B$), the error-rate ratio cannot equal 1.0. Equalized odds and calibration parity are mutually exclusive.
- **The Two Theoretical Escapes (The One Flag)**: The theorem admits only two escapes — identical base rates across groups or clairvoyant prediction with zero errors ($t=1, f=0$). In real-world social evaluations, neither escape ever happens.
- **Direction A (Calibration ⇏ Equal Errors)**: Proving that risk scores are perfectly calibrated across groups guarantees that false-positive rates will diverge when base rates differ.
- **Direction B (Equal Errors ⇏ Calibration)**: Enforcing identical false-positive and true-positive rates across groups with different base rates guarantees that identical scores mean different probabilities for different groups.
- **Carry-Out Law**: "Calibrating scores across groups with different base rates forces their error rates apart — the conflict is Bayes' rule, not a tooling gap."

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take a predictive model evaluated across demographic groups in your organization. Measure the base rate of the positive outcome in each group, and inspect both the false-positive rate and the positive predictive value. When the base rates differ, which definition of fairness did the team choose to satisfy — and who signed off on the definition that had to break?
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Bias & Fairness
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 7: Fairness Metrics: Choosing a Definition and Defending It)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **AI Disclosure**: Synthetic narration generated locally via Kokoro `am_onyx`. Visuals algorithmically rendered via Manim and Remotion. Zero generative video, zero paid APIs.
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/why-three-reasonable-fairness-definitions-cannot-all-be
