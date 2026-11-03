# SOURCES — You're Only Seeing Half the Curve

## Primary evidence (ships in this folder)

**`double_descent_evidence.py`** — pure numpy, no scikit-learn, no data
download, fixed seeds, runs in a few seconds. **Every number spoken or shown in
the reel comes out of this file**, and anyone can rerun it.

What it does: ridgeless (minimum-norm) least-squares regression on `p` random
Fourier features, with `n = 100` training examples held fixed and `p` swept from
2 to 4000. The random feature directions are drawn ONCE and reused as `p` grows,
so the 200-feature model literally contains the 100-feature model's features —
only capacity changes along the x axis. Reported figures are the **median over
12 seeds**.

Output used in the reel:

| Quantity | Value |
|---|---|
| Best test error below the threshold (`p = 60`) | 0.700 |
| Test error at the interpolation threshold (`p = n = 100`) | 111.263 |
| Ratio — peak vs classical best | 159× |
| Best test error far past the threshold (`p = 4000`) | 0.293 |
| Ratio — peak vs modern best | 380× |
| Training error at `p ≥ 100` | ~1e-27 (zero to machine precision) |
| Seeds where the modern regime beats the classical best | 12 / 12 |
| Median improvement over the classical best, per seed | 52% |
| Worst seed's improvement | 18% |

## Published sources

**Belkin, M., Hsu, D., Ma, S., & Mandal, S. (2019).** *Reconciling modern
machine-learning practice and the classical bias–variance trade-off.*
Proceedings of the National Academy of Sciences, **116**(32), 15849–15854.
doi:[10.1073/pnas.1903070116](https://doi.org/10.1073/pnas.1903070116) ·
PMID 31341078 · PMCID [PMC6689936](https://pmc.ncbi.nlm.nih.gov/articles/PMC6689936/) ·
preprint [arXiv:1812.11118](https://arxiv.org/abs/1812.11118)

- Supports: the existence and the name of the double-descent curve; the claim
  that capacity past the interpolation point improves performance.
- Quoted verbatim on B06.
- **Why this paper and not another:** its experiments are run on *random Fourier
  features*, the same model family as our evidence script (they used an MNIST
  subset; we use a synthetic target so the script needs no download). The reel's
  local experiment is a reproduction in the paper's own family, not an analogy.

**Nakkiran, P., Kaplun, G., Bansal, Y., Yang, T., Barak, B., & Sutskever, I.
(2020).** *Deep Double Descent: Where Bigger Models and More Data Hurt.*
ICLR 2020. Preprint [arXiv:1912.02292](https://arxiv.org/abs/1912.02292)
(submitted 4 Dec 2019).

- Supports: the same shape appears in modern deep networks, and along the
  *training-time* axis as well as the model-size axis.
- Paraphrased on B06. Verbatim from the abstract: *"double descent occurs not
  just as a function of model size, but also as a function of the number of
  training epochs."*
- Also introduces **effective model complexity**, which is why the reel never
  equates "model size" with raw parameter count for deep networks — see the
  deliberate omissions below.

## Deliberate omissions — claims that were available and were NOT made

Recorded because leaving them out was a decision, not an oversight.

1. **No numeric claim about deep networks.** The 159×, the 58%, the `p = n`
   threshold are properties of *this* linear experiment. In a deep network the
   peak sits at the effective model complexity, not at a parameter count you can
   read off the architecture. Stating our numbers as if they transferred would
   be the exact error the reel is about. The reel shows the shape and names the
   mechanism; it quantifies only what the script quantifies.

2. **No "just make it bigger" advice.** The second descent is real and is not a
   licence to scale blindly: it needs enough capacity to get *well* past the
   threshold, and sitting near `p ≈ n` is the worst place on the curve. The
   handoff asks the viewer to measure where they are, not to assume.

3. **No claim that regularisation is unnecessary.** This experiment is
   deliberately *ridgeless* — the effect is cleanest with no explicit
   regularisation. Properly tuned ridge regression can flatten the peak
   substantially. The reel does not mention this for time, and it is the first
   thing a careful viewer should read about next. Logged here rather than
   implied away.

4. **"Smallest coefficients ⇒ smoothest curve"** is stated in the reel as the
   mechanism. It is exactly true that min-norm least squares picks the
   smallest-norm coefficient vector; "smoothest" is the honest reading of what
   that means for random Fourier features, where coefficient norm controls how
   much high-frequency content the fit carries. It is an interpretation of a
   theorem, not a theorem, and is marked as such in `FACTCHECK.md`.
