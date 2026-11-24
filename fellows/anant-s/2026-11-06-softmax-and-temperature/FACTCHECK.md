# FACTCHECK — Softmax and Temperature, Explained

Verdicts: ✓ verified · minor (true with a qualifier) · CORRECTED (was wrong in draft, fixed) · WRONG.
"Executed" means `demo/softmax_demo.py` produced the number; the run is in `demo/RUN-LOG.txt`. `make_sheet.py` also carries a CLAIMS block that asserts every spoken number against `evidence.json`.
Script sha256 `06547eb0…8a8ad0`. Evidence sha256 `009e3ad1…5009e`. Python 3.12.13, numpy 2.5.5, seed 2. The numbers are identical under numpy 2.3.5.

**Constructed inputs.** The logits for "The cat sat on the ___" and for "The capital of Australia is ___" are made up for illustration. No real model produced them. Every frame that shows them carries a label saying so (B02 and B09). The softmax, the temperatures, the samples and the counts are all executed.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 1 | B01 | A chat model samples its next word from weighted odds; it does not simply pick the likeliest word | minor | True under sampling decoding (T > 0), the usual default for chat use. Greedy decoding does pick the likeliest token, and B08 covers it. | B01 says "rolls weighted dice". B08 gives the greedy exception its own beat. |
| 2 | B01 | Drafted as "picks the likeliest **token**" | CORRECTED | B01 is for a lay viewer and "token" is not yet defined there | B01 says "word". From B02 on the film says "token". Tokens are often pieces of words; the film does not dwell on this. |
| 3 | B02 | The model outputs a score (logit) for every token in its vocabulary, not a word | ✓ | Language-model output layer: one logit per vocabulary entry, followed by softmax (Goodfellow et al., *Deep Learning* §6.2.2.3) | — |
| 4 | B02 | "Here are five of them" | minor | The demo applies softmax over 5 candidates only, which renormalizes over that subset. A real model divides by a sum over its whole vocabulary. | On-screen caption: "logits (constructed): 5 of the whole vocabulary" |
| 5 | B02 | The sampler appends the token and the loop repeats | ✓ | Autoregressive decoding | — |
| 6 | B03 | pᵢ = e^(zᵢ/T) / Σⱼ e^(zⱼ/T) | ✓ | Softmax (Bridle 1990) with temperature (Hinton, Vinyals & Dean 2015, eq. 1) | — |
| 7 | B03 | Every term turns positive; the shares add up to exactly one | ✓ | eˣ > 0, and Σᵢ pᵢ = Σᵢ e^(zᵢ/T) / Σⱼ e^(zⱼ/T) = 1. The demo asserts the sum. | — |
| 8 | B03 | "A bigger logit always means a bigger share" | ✓ | For T > 0, z ↦ e^(z/T) is strictly increasing | — |
| 9 | B04 | e^3.2 ≈ 24.5, e^0.3 ≈ 1.35, sum ≈ 48 | ✓ executed | 24.53, 1.35, Σ = 48.07 | — |
| 10 | B04 | 51 / 23 / 14 / 9 / 3 percent | ✓ executed | 51.0, 22.9, 13.9, 9.3, 2.8. The spoken values are rounded to whole numbers and the screen shows one decimal. | — |
| 11 | B05 | At T = 0.2 every gap grows five times | ✓ | z/T with T = 0.2 multiplies every logit, and so every difference, by 5 | — |
| 12 | B05 | mat 98% at T = 0.2 and 35% at T = 2; roof goes from almost nothing to 8% | ✓ executed | 98.0 / 35.0. Roof is 0.0 (about 5·10⁻⁷) at T = 0.2 and 8.2 at T = 2. | — |
| 13 | B05 | The order never changes | ✓ executed | Follows from #8. The demo asserts `order_preserved` at all three temperatures. | — |
| 14 | B06 | Inverse-CDF sampling: the token whose segment of [0, 1) contains u wins | ✓ | Standard method for categorical sampling. `sample()` in the demo uses `searchsorted` on the cumulative sum. | — |
| 15 | B06 | The same 20 rolls give 1 / 4 / 5 distinct words at T = 0.2 / 1 / 2; mat 20 of 20 at T = 0.2; roof appears at T = 2 | ✓ executed | Seed 2, the same uniforms reused at every temperature. Counts are in RUN-LOG §4. | — |
| 16 | B07 | 10,000 rolls at T = 1: predicted 51.0% mat, counted 51.3% | ✓ executed | RUN-LOG §5 | — |
| 17 | B07 | "Nothing misses by even one point" across 3 temperatures × 5 tokens | ✓ executed | Largest gap is 0.76 points (T = 1), at most 2.09 σ across 15 comparisons. That is ordinary sampling noise. | — |
| 18 | B07 | The 10,000-draw test used separate generators per temperature with `rng.choice` | CORRECTED (method) | That first scheme gave a 3.4 σ miss at T = 2 (mat 33.4 vs 35.0). Re-running the same draw with seeds 3, 4, 5 and [2, 21] landed within 0.3 points, so it was a seed outlier, not a softmax error. | Switched to the sampler the film shows (inverse CDF) on one seeded stream, the same 10,000 uniforms at each temperature. **This change was made after seeing the outlier**; see BUILD-LOG. The narration claims only what the new run shows. |
| 19 | B08 | mat 76% at T = 0.5 and 99.97% at T = 0.1 | ✓ executed | 76.19 / 99.97 | — |
| 20 | B08 | T = 0 means greedy (argmax); the formula itself cannot use T = 0 | ✓ | z/T is undefined at T = 0. T → 0⁺ gives a one-hot on argmax when the maximum is unique. APIs treat 0 as greedy by convention. | — |
| 21 | B08 | Drafted as "Same prompt, same answer" | CORRECTED | Serving systems do not promise bit-exact determinism. The OpenAI API reference (retrieved 2026-11-22) says of its `seed` parameter: "Determinism is not guaranteed." | Now "Same prompt, same answer, at least in principle". The on-screen caption carries "(in principle)". |
| 22 | B09 | At T = 1 the hypothetical model is wrong two times in three; at T = 0.2 wrong more than four in five; greedy wrong every time | ✓ executed (constructed logits) | 66.7%, 81.8%, Sydney always | Labelled on screen "hypothetical model · constructed logits". Canberra is the real capital. |
| 23 | B09 | Drafted as "Canberra barely moves" at T = 2 | CORRECTED | It falls from 33.3% to 30.5% | Now "Canberra actually slips" |
| 24 | B09 | Melbourne and Perth take the extra at T = 2 | ✓ executed | Melbourne 15.0 → 20.4, Perth 6.7 → 13.7 | — |
| 25 | B05/B09 | T = 2 is a real setting | minor | One major API documents temperature "between 0 and 2" (OpenAI reference, retrieved 2026-11-22). Anthropic's Messages API page, read the same day, showed no `temperature` entry. | The narration names no product and no API range, so the film doesn't date. T = 2 is used only as math. |
| 26 | BHTF | At T = 1 mat ≈ 51%; 1,000-draw counts land near, not on, the probabilities | ✓ | One σ at N = 1,000 and p = 0.51 is about 1.6 points | — |
| 27 | Verdict | Six lines | ✓ | Each line restates a checked claim: #3, #7, #11–12, #15, #20, #13/#22 | — |

## Algebra checks (MATH-TYPESETTING.md)
- **Indices.** i is free (the token being scored). j is bound by the sum and runs over the same candidate set. The numerator uses zᵢ and the denominator uses zⱼ.
- **Domain.** T > 0, and the demo raises an error for T ≤ 0. "T = 0" in B08 is a rule, typeset as a limit (T → 0⁺), never substituted into z/T.
- **Equality versus limit.** B08's MathTex uses "→", not "=". Strictly, the one-hot limit needs a unique maximum. With a k-way tie, T → 0⁺ splits evenly 1/k each. The film has no ties (3.2 is the strict maximum).
- **T → ∞.** zᵢ/T → 0 for every i, so p → uniform (1/5 each). This is not claimed on screen; T = 2 is only "flatter".
- **Shift invariance.** Adding a constant c to every logit cancels: e^((zᵢ+c)/T) / Σ e^((zⱼ+c)/T) = pᵢ. The demo asserts it, and it justifies the max-shift used for numerical stability. Not narrated.
- **Ratio check.** p_mat / p_floor = e^((3.2 − 2.4)/1) = e^0.8 = 2.2255, and 24.53 / 11.02 = 2.226 ✓.
- **Numeric case.** p_mat = 24.53 / 48.07 = 0.5103 ✓ (the demo asserts the worked table equals `softmax()`).
- **Gap scaling.** At T = 0.2 the scaled logits are 16, 12, 9.5, 7.5, 1.5. The mat–floor gap goes from 0.8 to 4.0, five times larger ✓. At T = 2 it goes to 0.4, half ✓.
