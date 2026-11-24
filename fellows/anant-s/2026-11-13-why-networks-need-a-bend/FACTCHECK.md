# FACTCHECK — Why Neural Networks Need a Bend

Verdicts: ✓ verified · minor (true with a qualifier) · CORRECTED (was wrong in draft, fixed) · WRONG.
"Executed" means the number was produced by `demo/nonlinearity_demo.py`; the run is in `demo/RUN-LOG.txt`, and the script `assert`s the key results.
Hashes (sha256): demo script `68df197a…09311`, evidence `415b148b…0bc7e`.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 1 | B01 | Depth alone does not make a network more expressive; the nonlinearity between layers does | ✓ | A composition of linear maps is linear. Goodfellow, Bengio & Courville, *Deep Learning* §6.1: if the hidden layer were linear, the whole network would remain a linear function of its input | — |
| 2 | B01 | Draft said "Stacking alone does nothing" | CORRECTED | Deep linear networks have the same function class as one matrix, but different training dynamics (Saxe, McClelland & Ganguli 2014). "Does nothing" overstated it | Now "Stacking alone isn't enough" |
| 3 | B02 | Draft said "Two moves build every network" | CORRECTED | Modern architectures add other operations (attention, normalization, gating). Layer + activation is the core of a plain multilayer perceptron | Now "Two moves build a plain neural network" |
| 4 | B02 | A matrix can stretch, rotate and shear; straight lines stay straight, parallel lines stay parallel | minor | True of every linear map. Qualifier: a singular matrix can flatten a line to a point (still not a curve) | none needed in narration |
| 5 | B02 | ReLU keeps positives and flattens negatives to zero: ReLU(z) = max(0, z) | ✓ | Nair & Hinton 2010; Glorot, Bordes & Bengio 2011 | — |
| 6 | B03 | W₁ = [[3,1],[1,−1]], W₂ = [[−1,−2],[−2,−2]], x = (−1, 2); W₁x = (−1, −3); W₂(W₁x) = (7, 8); W₂W₁ = [[−5,1],[−8,0]]; (W₂W₁)x = (7, 8) | ✓ executed | numpy `default_rng(0)` integers, first seed tried. Hand check below. The script asserts equality | — |
| 7 | B03 | "Seeded random matrices" | ✓ | Seed 0, integers drawn from [−2, 3]. Seeds 0–11 were previewed for legibility and seed 0 was kept unchanged | — |
| 8 | B04 | 1,000 random inputs through ten random layers equal the one multiplied-out matrix; largest gap 8.88×10⁻¹⁵ | ✓ executed | Seed 1. Relative gap 3.15×10⁻¹⁶ is float64 rounding (machine ε ≈ 2.2×10⁻¹⁶) | — |
| 9 | B04 | "In the fifteenth decimal place" | ✓ | 8.88×10⁻¹⁵ = 0.00000000000000888; the first nonzero digit is the 15th after the point | — |
| 10 | B04 | With biases it is still one matrix plus one shift | ✓ executed | W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂); max gap 8.88×10⁻¹⁶ | — |
| 11 | B04 | "Depth without a bend buys no new shapes" | minor | True of the function class (affine maps). Depth still changes training dynamics (see #2), which "shapes" sidesteps | — |
| 12 | B05 | XOR outputs one when exactly one input is on | ✓ | Definition | — |
| 13 | B05 | 115,560 lines tried; the best gets 3 of 4 | ✓ executed | 360 angles × 321 offsets. A sweep is a sample, so the general claim rests on the proof below | — |
| 14 | B05 | No line gets all four (the four-inequality contradiction) | ✓ | Algebra check below. Minsky & Papert (1969) made the single-layer limitation famous | — |
| 15 | B06 | A 2-2-1 network with no activation, trained 5,000 steps (lr 0.1, seed 0): loss 0.25, every output 0.5 | ✓ executed | `RUN-LOG.txt` §4 | — |
| 16 | B06 | That is exactly what the best single line predicts | ✓ executed | The least-squares affine fit to XOR is w = (0, 0), b = ½. It predicts ½ at every corner, MSE ¼. "Best" means least-squares | — |
| 17 | B06 | 100 seeds, same floor, none gets all four | ✓ executed | Over seeds 0–99 the lowest loss is 0.25, and no run gets 4 of 4 correct | — |
| 18 | B07 | Hand-set weights W = [[1,1],[1,1]], c = (0, −1), w = (1, −2), b = 0 come from the *Deep Learning* textbook | ✓ | Goodfellow, Bengio & Courville 2016, §6.1 "Example: Learning XOR". The script asserts the outputs are exactly (0, 1, 1, 0) | — |
| 19 | B07 | At (0, 0) the second unit reads −1 and ReLU flattens it to 0 | ✓ executed | z = (0, −1), h = (0, 0) | — |
| 20 | B08 | The first layer puts all four points on one line; the two ones land on the same spot, between the zeros | ✓ executed | z-points (0,−1), (1,0), (1,0), (2,1) all lie on z₂ = z₁ − 1. The ones sit at (1,0), between the zeros | — |
| 21 | B08 | After ReLU one line separates them; in the input square it becomes a band | ✓ | h₁ − 2h₂ = ½ gives −½, 1, 0 at the three hidden points. With s = x₁ + x₂: y = s on [0,1] and 2 − s on [1,2], so y > ½ ⇔ ½ < s < 3⁄2 | — |
| 22 | B09 | Trained from 100 seeds, the 2-unit ReLU net solves XOR 18 times | ✓ executed | Setup: W, v ~ N(0,1), c = d = 0, MSE, lr 0.1, 5,000 full-batch steps. Success means 4 of 4 correct and loss < 0.01. The rate depends on this setup | Narration says "Here, eighteen…"; the setup is printed on screen |
| 23 | B09 | Draft said "Eighteen find XOR" with no qualifier | CORRECTED | The rate is specific to the setup above (DOUBLE-CHECK: de-sensationalize) | Now "Here, eighteen find XOR" |
| 24 | B09 | 82 get stuck, most with a hidden unit that went flat and never woke up | ✓ executed | 69 of 82 end with a unit at z ≤ 0 on all four inputs. That unit gets zero gradient, so full-batch GD can never revive it. The other 13 stall at loss 0.125 or 0.1667 | — |
| 25 | B09 | With eight units, 91 of 100 succeed | ✓ executed | Same setup and seeds | — |
| 26 | B10 | Along the diagonal, the output is flat, then rises, then falls in straight lines, with kinks at t = 0 and t = ½ | ✓ executed | y = ReLU(2t) − 2 ReLU(2t − 1). Unit 1 switches on at t = 0, unit 2 at t = ½. The script asserts the closed form | — |
| 27 | B10 | At (3, 3) it says −4, and it never curves back | ✓ executed | For t ≥ ½, y = 2 − 2t, which is linear forever; at (10, 10) it is −18 | — |
| 28 | B10/BVDT | Draft said "a ReLU network is straight lines" | CORRECTED | ReLU networks are continuous piecewise-linear functions (Montúfar et al. 2014; Arora et al. 2018). In 2-D the pieces are flat planes, not lines | Now "is made of straight pieces" |
| 29 | B00 | Result line: "trained from 100 seeds, it finds it 18 times" | ✓ executed | Same as #22 | Qualified with "from 100 seeds" |
| 30 | BHTF | Rubric: linear runs never get all four on any seed | ✓ | Guaranteed by #14 | — |
| 31 | BHTF | Rubric: stuck ReLU runs often have a dead unit | minor | 69 of 82 here. The viewer's setup will differ, hence "often" and "look for" | — |

## Algebra checks (MATH-TYPESETTING.md)
- **Collapse (B03), checked by hand.**
  - W₁x = (3·−1 + 1·2, 1·−1 + −1·2) = (−1, −3).
  - W₂(W₁x) = (−1·−1 + −2·−3, −2·−1 + −2·−3) = (7, 8).
  - W₂W₁ = [[−1·3 + −2·1, −1·1 + −2·−1], [−2·3 + −2·1, −2·1 + −2·−1]] = [[−5, 1], [−8, 0]].
  - (W₂W₁)x = (5 + 2, 8 + 0) = (7, 8). ✓
- **Order of multiplication.** The matrix nearest x acts first, so the product is W₂W₁, never W₁W₂. On these matrices W₁W₂ = [[−5, −8], [1, 0]], which is a different matrix, so the order is visible on screen.
- **Ten-layer product.** M = W₁₀⋯W₂W₁, built as M ← L·M in layer order. The narration says "multiply the ten matrices into one" and makes no claim about the order.
- **Bias.** W₂(W₁x + b₁) + b₂ = W₂W₁x + W₂b₁ + b₂, by distributivity. "=" is an exact identity.
- **XOR, no separating line.** Suppose a line w·x + b puts the ones on the positive side. Then:
  - (0,0) gives b ≤ 0.
  - (0,1) gives w₂ + b > 0.
  - (1,0) gives w₁ + b > 0.
  - (1,1) gives w₁ + w₂ + b ≤ 0.
  - Adding the middle two: w₁ + w₂ + 2b > 0, so w₁ + w₂ + b > −b ≥ 0. This contradicts the last line.
  - The mirror case (ones on the negative side) flips every sign and fails the same way. ✓
- **Hand-set ReLU (B07).** For x = (0,0), (0,1), (1,0), (1,1):
  - z = (0,−1), (1,0), (1,0), (2,1).
  - h = (0,0), (1,0), (1,0), (2,1).
  - y = h₁ − 2h₂ = 0, 1, 1, 0. ✓
- **Without the ReLU.** The same weights give y = w·(Wx + c) = (−1, −1)·x + 2. That is one plane, with outputs 2, 1, 1, 0 (executed). This is not XOR.
- **"½" on screen.** It appears as a typeset fraction (MathTex `\tfrac12`), never as "1/2" on a text card.
