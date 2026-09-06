# Script: The one-parameter fix that proves the confidence was decorative

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "real?", corrects to "decorative?".
**Narration**:
"When a deep neural network outputs ninety-nine percent confidence, you might assume that number reflects genuine certainty. But modern classifiers are notoriously overconfident. A single learned number can fix it without changing a single decision. Let's see why."

## B01 — stakes (The Ninety-Nine Percent Claim)
**Visual**: Manim `B01Scene`. Deep network output card: Dog 99.1%, Cat 0.8%, Fox 0.1%. Stated certainty vs actual empirical accuracy.
**Narration**:
"Deep neural networks routinely output extreme confidence scores. They say ninety-nine percent certain with crisp, unwavering precision."

## B02 — stakes (The Overconfidence Gap)
**Visual**: Manim `B02Scene`. 99% stated vs 85% empirical. The 14-point overconfidence gap highlighted in terracotta.
**Narration**:
"Yet when you evaluate thousands of predictions where the model claimed ninety-nine percent, the true empirical accuracy is often only eighty-five percent. The network is fundamentally miscalibrated."

## B03 — anchor planted (Logits & Softmax Bars)
**Visual**: Manim `B03Scene`. Unnormalized logits [z1=6.0, z2=3.0, z3=1.0] passing into standard Softmax. High bar at 95%, tiny residual bars.
**Narration**:
"To see where this comes from, look at the network's final layer. The model computes unnormalized scores called logits, then passes them through a softmax function to turn them into probabilities."

## B04 — wrong guess (Confidence Equals Correctness)
**Visual**: Manim `B04Scene`. Naive mental model: confidence and classification strength bound together in an unbreakable lock.
**Narration**:
"Intuition assumes that confidence and correctness are inseparable: that if a model is ninety-nine percent sure, flattening that number would break its ability to pick the right answer."

## B05 — mechanism (The Guo Discovery)
**Visual**: Manim `B05Scene`. Guo et al. (ICML 2017) finding: Classification ranking is preserved. Only the probability scale is distorted.
**Narration**:
"In 2017, Guo, Pleiss, Sun, and Weinberger proved that assumption wrong. A network's ranking of options is usually fine. It picked the right class; only its stated certainty was inflated."

## B06 — mechanism (Dividing by Temperature T)
**Visual**: Manim `B06Scene`. Formula: softmax(z / T). Scalar dial T > 1.0 inserted into the exponent denominator.
**Narration**:
"Their fix was surprisingly simple: temperature scaling. Before computing the softmax, you divide every logit by a single learned number, T. When T is greater than one, it gently cools the distribution."

## B07 — anchor payoff: slosh/spread (The Softening Bars)
**Visual**: Manim `B07Scene`. MANIM MOVE `slosh/spread`: As dial T turns from 1.0 up to 2.2, the tall 99% bar sloshes and spreads outward into adjacent bars, dropping down to an honest 85%.
**Narration**:
"Here is the visual payoff. As temperature T turns up, watch the probabilities slosh and spread. The peaked ninety-nine percent bar softens outward into neighbouring classes, settling right at eighty-five percent."

## B08 — mechanism (Monotonic Invariance)
**Visual**: Manim `B08Scene`. Strict monotonic invariance: Dividing all numbers by T > 0 keeps argmax(z/T) == argmax(z). Ranking unchanged.
**Narration**:
"Because dividing by a positive constant is strictly monotonic, it cannot alter the order of the logits. The highest score stays highest. Not a single decision or top-one classification changes."

## B09 — anchor payoff (Confidence Was Decorative)
**Visual**: Manim `B09Scene`. Decoupling card: Decision Track (100% stable) vs Confidence Track (re-scaled). The decorative layer stripped away.
**Narration**:
"That is the core insight. If you can fix the probabilities across an entire dataset with one global dial without changing a single decision, the original confidence score was decorative all along."

## B10 — one flag (The Calibration Diagonal)
**Visual**: Manim `B10Scene`. Reliability diagram: T=1.0 curve sagging far below diagonal vs T=2.2 curve hugging the 45-degree line.
**Narration**:
"One flag: check the reliability diagram before and after. At temperature one, the curve sags far below the diagonal in the overconfident tail. Scaled by T, the curve hugs the honest forty-five-degree line."

## B11 — direction A (Calibrated In-Distribution)
**Visual**: Manim `B11Scene`. Direction A: In-distribution honesty. Risk estimates now match actual empirical hit rates.
**Narration**:
"In one direction, temperature scaling delivers real value. On in-distribution data, it turns an arbitrary number into a calibrated probability you can use for risk management."

## B12 — direction B (The Distribution Shift Caveat)
**Visual**: Manim `B12Scene`. Direction B: Domain shift alert. Calibration holds in-distribution, but goes stale when the world drifts.
**Narration**:
"In the other direction, temperature scaling is not magic: if the deployment distribution drifts from your calibration set, that honest number goes stale silently."

## BCRY — carry-out (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"If dividing by one learned number fixes the probabilities without altering a single decision, the original confidence was decorative all along."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take a classifier in your pipeline with a softmax output. Measure its empirical accuracy in the top confidence bin. If your ninety-nine percent predictions only succeed eighty-five percent of the time, fit a single temperature parameter T on held-out logits and verify that the ranking never changes. Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"The one-parameter fix that proves the confidence was decorative. Liam, in for Bear."
