# FACTCHECK — Gradient Descent, One Step at a Time

Verdicts: ✓ verified · minor (true with a qualifier) · CORRECTED (was wrong in draft, fixed) · WRONG.
"Executed" means the number was produced by `demo/gd_demo.py`; the run is in `demo/RUN-LOG.txt`.
Script hash: sha256 `b9bb39a3…4b15`. Evidence hash: `219f97b3…5d052`.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 1 | B01 | Training is repeated small steps against the slope, not a search for the best answer | ✓ | Gradient descent is a local first-order method (Cauchy 1847; Goodfellow, Bengio & Courville, *Deep Learning* §4.3) | — |
| 2 | B01 | Draft said "millions of times" | CORRECTED | Large-model runs are often about 10⁵ optimizer steps. The draft overstated it. | Now "step after step" |
| 3 | B02 | At any point the model can measure only the local slope | ✓ | Definition of a first-order method | — |
| 4 | B03 | θₜ₊₁ = θₜ − η ∇L(θₜ) | ✓ | Standard update rule (*Deep Learning* eq. 4.21) | — |
| 5 | B04 | L = θ², slope = 2θ | ✓ | d/dθ θ² = 2θ | — |
| 6 | B04 | θ: 3 → 2.4 → 1.92, factor 0.8 per step | ✓ executed | θₜ = θ₀(1 − 2η)ᵗ. The script asserts the closed form at every step. | — |
| 7 | B04 | Loss 9 → "just under one" after 5 steps | ✓ executed | L₅ = 0.9664 | — |
| 8 | B05 | θ₁₀ = 2.4512 / 0.3221 / 18.5752 for η = 0.01 / 0.1 / 1.1 | ✓ executed | 3·0.98¹⁰, 3·0.8¹⁰, 3·(−1.2)¹⁰ | — |
| 9 | B05 | "Every step overshoots… lands further out" at η = 1.1 | ✓ | Factor −1.2: the sign flips every step and \|θ\| grows by ×1.2 | — |
| 10 | BHTF | Convergence iff 0 < η < 1; η = 0.9 oscillates and converges | ✓ | \|1 − 2η\| < 1. At 0.9 the factor is −0.8. | — |
| 11 | B06 | Minima of θ⁴ − 3θ² + θ at θ = −1.3008 (L −3.5139) and 1.1309 (L −1.0702) | ✓ executed | Roots of 4θ³ − 6θ + 1, second derivative 12θ² − 6 > 0 | — |
| 12 | B06 | From θ = 2 the descent stops in the shallow valley; from −2 it reaches the deep one | ✓ executed | η = 0.02, 200 steps, end θ = 1.1309 and −1.3008 | — |
| 13 | B07 | Models have millions to billions of parameters | ✓ | Parameter counts of current published models span this range. No specific model is named, so the claim won't date. | — |
| 14 | B07 | Draft said real models run "this same rule" | CORRECTED | Most use variants such as momentum or Adam | Now "a version of this same rule" |
| 15 | B07 | Backpropagation computes every partial derivative in one backward pass | ✓ | Rumelhart, Hinton & Williams 1986; reverse-mode differentiation | — |
| 16 | B07 | A batch of 8 of 200 costs 1/25 per step | minor | 8/200 = 1/25 for the gradient computation. Fixed overhead is ignored. | Wording says "each step costs a twenty-fifth as much", which is true for the gradient |
| 17 | B07 | The mini-batch fit lands "within a few percent" | ✓ executed | MSE 0.1533 vs 0.1500 full-batch, a 2.2% gap. Full batch matches least squares (w 1.5008, b −0.5248). | — |

## Algebra checks (MATH-TYPESETTING.md)
- **Indices:** θₜ₊₁ is the new value and θₜ the current one. ∇L is evaluated at θₜ, not at θₜ₊₁.
- **Sign:** the minus applies to the whole product η∇L. Here η > 0.
- **"=" is assignment.** The narration reads it as "becomes".
- **Numeric case:** θ₁ = 3 − 0.1·6 = 2.4 ✓.
