# Research — Ch. 5: Statistics, Probability & Experimentation

*Phase 1 notes and sources. No chapter prose.*

## Key claims & sources

- **Null hypothesis (H₀):** a default hypothesis that the effect studied has no effect, or a parameter takes an "obvious" value. **Alternative hypothesis (H₁):** its negation.
  Source: Wikipedia, "Statistical hypothesis test," https://en.wikipedia.org/wiki/Statistical_hypothesis_test (accessed 2026-07-15). *Tertiary/secondary reference.*
- **P-value:** the probability that a test statistic at least as extreme as the one observed would occur under the null hypothesis. **It does NOT give the probability that the null (or its opposite) is true** — a common misinterpretation to warn readers about.
  Source: Wikipedia, "Statistical hypothesis test" (as above).
- **Significance level (α):** the maximum acceptable false-positive rate; common values are 5% and 1%. A result is "statistically significant" when p < α (reject H₀ at that level).
  Source: Wikipedia, "Statistical hypothesis test" (as above).
- **A/B testing** is a randomized experiment comparing two or more variants to see which performs better; it applies statistical hypothesis testing to user-response differences.
  Source: Wikipedia, "A/B testing," https://en.wikipedia.org/wiki/A/B_testing (accessed 2026-07-15). *Tertiary/secondary reference.*
- **A/B test considerations/pitfalls:** requires adequate sample size (sensitive to variance); results must show differences aren't chance; pitfalls include biased/unequal segment distribution, heterogeneous responses, insufficient samples, and poorly defined outcomes. (Common tests: Welch's t-test for continuous metrics; Fisher's exact test for click-through.)
  Source: Wikipedia, "A/B testing" (as above).

## Interview-craft (editorial)
- Teach reasoning aloud: state assumptions, then check them.
- Warn about "peeking"/optional stopping (checking results daily and stopping early inflates false positives) — widely known experimentation pitfall; framing/example is original.
- Probability question shapes: conditional probability, expected value, simple combinatorics.

## Original worked example
- Invented food-delivery checkout A/B test (4.0% → 4.3% conversion) — fully invented numbers.

## [UNVERIFIED] list
- Specific numeric sample-size formulas, if included, should be sourced to a statistics reference (not just Wikipedia) at draft time — mark any formula's source explicitly.
