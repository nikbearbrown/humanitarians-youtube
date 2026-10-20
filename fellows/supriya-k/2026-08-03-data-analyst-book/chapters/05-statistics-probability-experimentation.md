# Chapter 5 — Statistics, Probability & Experimentation

This round rarely wants a proof. It wants to see you **reason under uncertainty and state your assumptions** — and not fall for the classic traps.

> **What's tested here**
> Sound reasoning out loud, correct use of core concepts, and spotting a flawed experiment. Confidently *wrong* (especially about p-values) is worse than "let me state my assumptions."

## Hypothesis testing, in interview language

- **Null hypothesis (H₀):** the default — "no effect," or the parameter takes an obvious value. **Alternative (H₁):** its negation.[^hyp]
- **p-value:** the probability of a test statistic **at least as extreme** as observed, *assuming H₀ is true.*[^hyp]
- **Significance level (α):** the largest false-positive rate you'll accept; commonly 5% or 1%. If p < α, you reject H₀ at that level.[^hyp]

> ⚠️ **The trap.** A p-value is **not** the probability that the null (or your hypothesis) is true — a well-known source of confusion.[^hyp] Say "under the null, a result this extreme has a 3% chance," never "there's a 97% chance my hypothesis is right."

## A/B testing

An **A/B test is a randomized experiment comparing two or more variants** to see which performs better, applying hypothesis testing to the difference.[^ab]

Watch for these pitfalls:[^ab]
- **Too-small samples** — tests are sensitive to variance and need enough data to detect a real difference.
- **Biased splits** — unequal distribution across user segments skews results.
- **Vague outcomes** — the metric must be defined and measurable up front.
- **Peeking / early stopping** — checking daily and stopping when it looks significant inflates false positives.

## Probability questions

Common shapes: conditional probability, expected value, simple combinatorics. Method matters more than speed — define the sample space, state assumptions, then compute.

## Worked example

An invented food-delivery app tests a new checkout button. Conversion moves **4.0% → 4.3%** over a week.

Reason it through aloud:
1. **H₀:** the button doesn't change conversion. **H₁:** it does.
2. **Test:** compare conversion rates between groups (a proportions test).
3. **Trust check:** Was the sample big enough for a 0.3-point move? Were users split randomly? Did we fix the metric and duration *before* peeking?
4. **Before shipping:** confirm significance at a pre-set α, check for novelty effects, and look at guardrail metrics (e.g., did average order value drop?).

![Conversion 4.0% vs 4.3% with confidence intervals that overlap — reason to be cautious.](images/05-statistics-probability-experimentation-fig-01.png)

## Exercises

1. **(Warm-up.)** In plain language, what does a p-value of **0.03** mean — and what does it *not* mean?
2. **(Representative.)** A team ran an A/B test, checked results every day, and stopped the moment it hit significance. Name the flaw and its effect on the false-positive rate.
3. **(Stretch.)** A game pays \$10 on heads, costs \$4 to play, fair coin. Compute the expected value and say whether you'd play — narrating your reasoning.

---

*Next:* the tool interviewers still reach for — spreadsheets under time pressure.

[^hyp]: Wikipedia, "Statistical hypothesis test," https://en.wikipedia.org/wiki/Statistical_hypothesis_test (accessed 2026-07-15).
[^ab]: Wikipedia, "A/B testing," https://en.wikipedia.org/wiki/A/B_testing (accessed 2026-07-15).
