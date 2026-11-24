# FACTCHECK — Backpropagation, One Error at a Time

Verdicts: ✓ verified · minor (true with a qualifier) · CORRECTED · WRONG.

"Executed" means the number comes from `demo/bp_demo.py`, whose run is logged in `demo/RUN-LOG.txt`. The script's asserts check the chain-rule product and agreement with finite differences.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 1 | B01 | Backprop isn't per-weight trial and error; it's one backward pass of the chain rule | ✓ | Rumelhart, Hinton & Williams 1986; reverse-mode differentiation (Goodfellow et al., *Deep Learning*, §6.5) | — |
| 2 | B02 | The network is z = w₁x, h = tanh z, y = w₂h, L = (y − t)² | ✓ | definition in `bp_demo.py` | — |
| 3 | B03 | ∂L/∂w₁ = ∂L/∂y · ∂y/∂h · ∂h/∂z · ∂z/∂w₁ | ✓ executed | chain rule; the script asserts the product equals dL/dw1 to 1e-12 | — |
| 4 | B03 | ∂y/∂h = w₂; ∂h/∂z = 1 − tanh²z; ∂z/∂w₁ = x | ✓ | d/dz tanh z = 1 − tanh² z | — |
| 5 | B04 | z = 0.5, h = 0.4621, y = 0.9242, L = 0.5245 ("about zero point five two") | ✓ executed | tanh(0.5) = 0.46212 | — |
| 6 | B05 | ∂L/∂y = 1.4485, ∂L/∂h = 2.8969, tanh slope 0.7864, ∂L/∂w₁ = 2.2783, ∂L/∂w₂ = 0.6694 | ✓ executed | — | — |
| 7 | B05 | One step at η = 0.1 drops the loss 0.5245 → 0.0983 ("just under zero point one") | ✓ executed | w₁ 0.5 → 0.2722, w₂ 2 → 1.9331 | — |
| 8 | B06 | Backprop and central differences agree to 8 decimal places | ✓ executed | 2.27828974 vs 2.27828974, \|Δ\| = 2.7e-10 (ε = 1e-5) | — |
| 9 | B06 | Central differences cost 2 forward passes per weight, so 2,000,000 for a million weights; backprop needs one backward pass | minor | A backward pass costs a small constant multiple of a forward pass, not literally the same | The narration says "Backprop needs one" (pass); accepted as a simplification |
| 10 | B07 | Sigmoid's slope is at most 0.25 | ✓ | σ′ = σ(1 − σ), maximised at σ = ½ | — |
| 11 | B07 | Each of 10 sigmoid layers (w = 1) multiplies the gradient by about 0.22; it reaches layer 1 at 3.48e-7 | ✓ executed | local slopes 0.235 → 0.2247 | — |
| 12 | B07 | Vanishing gradients are one reason deep nets moved to ReLU | minor | Hochreiter 1991; Bengio et al. 1994; Glorot, Bordes & Bengio 2011. Initialization, normalization and residual connections also matter | The wording says "one reason", not "the reason" |
| 13 | BHTF | At w₁ = 5 the tanh slope is 1.8e-4, so dL/dw₁ collapses to 1.3e-3 | ✓ executed | `saturated_w1_5` in `evidence.json` | — |

## Algebra checks (MATH-TYPESETTING.md)
- **Partial derivatives:** each ∂ factor is evaluated at the current forward values, not at the updated weights.
- **Sign:** gradient descent subtracts η·∂L/∂w, and both gradients are positive here, so both weights decrease. That matches the executed update.
- **Numeric case:** 1.4485 × 2 × 0.7864 × 1 = 2.2783 ✓.
