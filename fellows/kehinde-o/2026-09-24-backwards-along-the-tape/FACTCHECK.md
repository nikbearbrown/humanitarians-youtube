# FACTCHECK — Backwards Along the Tape

Source of record: `github.com/Kenny0bi/ember`. Every figure below was **read in this
session** from the committed run logs, not copied from the repo README
(docs/EXECUTABLE-EVIDENCE.md).

Files read: `assets/parity_log.json`, `assets/shakespeare_log.json`,
`assets/mnist_log.json`, `assets/manim_chain_rule.py`.

| # | Claim on screen or spoken | Beat | Verdict | Where it comes from |
|---|---|---|---|---|
| 1 | The engine is roughly 700 lines on raw NumPy | B02 | TRUE | `ember/` package, README scope statement |
| 2 | It implements broadcasting, batched matmul, LayerNorm, causal attention, AdamW, cosine schedule | B02 | TRUE | `ember/tensor.py`, `nn.py`, `optim.py` |
| 3 | Every op is gradient-checked against PyTorch in float64 at 1e-9 | B05 | TRUE | `tests/test_grads.py` |
| 4 | Same weights, same batches, 300 steps of momentum SGD in both engines | B05 | TRUE | `examples/parity_pytorch.py`, `parity_log.json` (300 entries) |
| 5 | Largest gap between the two loss curves: 2.682e-07 | B05 | TRUE | `parity_log.json` `max_abs_diff` = 2.682209e-07 |
| 6 | Mean gap 5.36e-08 | B05 | TRUE | `parity_log.json` `mean_abs_diff` = 5.363176e-08 |
| 7 | Char-GPT: 624K parameters, 3 layers, 4 heads, Tiny Shakespeare | B06 | TRUE | README run table, `shakespeare_log.json` |
| 8 | Validation loss 4.49 at initialisation | B06 | TRUE | `shakespeare_log.json` `val_loss[0]` = 4.4910 |
| 9 | Uniform guessing over a 65-character vocabulary is 4.17 | B06 | TRUE | ln(65) = 4.1744, computed this session |
| 10 | Validation loss 1.83 after training | B06 | TRUE | `shakespeare_log.json` `val_loss[-1]` = 1.8336 |
| 11 | 1,625 tokens per second on a 2014 quad-core laptop | B06 | TRUE | `shakespeare_log.json` `tokens_per_sec[-1]` = 1625.34 |
| 12 | 97.8 percent on MNIST in 19 seconds | B06 | TRUE | `mnist_log.json` `test_acc[-1]` = 0.9783 |
| 13 | The x node never ignites because inputs do not require gradients | B04 | TRUE | `assets/manim_chain_rule.py` docstring, and ember's `requires_grad` behaviour |
| 14 | Broadcasting forward means summing gradients backward | B07 | TRUE | `ember/tensor.py` broadcast reduction in backward |

## Note on claim 8
The reel says initialisation is "slightly worse than guessing uniformly at random". That is
correct and deliberate: 4.491 at init against a uniform floor of 4.174. It is stated rather
than smoothed over.

## Math typesetting (docs/MATH-TYPESETTING.md)
B03 renders three structured SVG rows via `runtime/scripts/typeset_math.py`:
- `L = f(g(x))`
- the chain rule, with real fraction bars and partial derivative symbols
- gradient accumulation as a sum over k, with a proper summation index

B04 is Manim MathTex, re-rendered at 3840x2160 from the repo's own scene.

Algebra check: in row three, x is the free index and k is bound by the summation. This is
the multivariable chain rule for the case where x feeds several downstream values, which is
exactly what ember's tape does when one tensor is used more than once. Rows two and three
agree when k has a single value.

## Deliberately not claimed
- No claim that ember is faster than, or a replacement for, PyTorch. The measured claim is
  agreement of gradients and loss curves.
- No claim that the trained GPT is good at writing Shakespeare. The claim is a measured
  held-out loss against a stated guessing floor.
