# Pedagogy Review

## Topic
Every Look Was Right: peeking at A/B tests, and a flaw I found in my own sequential test

## Learning Objective
Checking an experiment repeatedly and stopping at the first significant result inflates
false alarms even though each check is a valid test. A sequential test fixes this only
if its inputs are fixed in advance; treating a measured number as known breaks the
guarantee. The viewer leaves able to ask how many times a result was looked at.

## Audience
General audience. "False alarm" is used for false positive; significance is described
as "looks like a real difference" before the threshold is named.

## Key Findings Reported
Measured by driving github.com/Kenny0bi/product-analytics-engine's own
ABTestAnalyzer.frequentist_test and SequentialTester.compute_sprt through an in-memory
DuckDB: 1,000 A/A experiments, both arms converting at 10 percent, 2,000 users per arm,
checked at 10 looks.
- Check once at the end: 4.0 percent false alarms (promise: 5).
- Check all ten times, stop at the first significant result: 18.7 percent.
- The repo's sequential test (control rate re-estimated each look): 12.9 percent.
- The same test with the control rate fixed in advance at the true rate: 3.2 percent.

## Accuracy Gate
See FACTCHECK.md. Wald's walls computed from the formula match the repo's logged
boundaries to four decimals.

## Restraint Gate
- "Fixed in advance at the true rate" is stated as such; in practice the baseline comes
  from history, and a two-sample always-valid test is the general fix. The video does not
  claim fixing theta-zero is always available.
- The comparison is conservative toward the repo's test: it was checked at 10 looks, the
  textbook test after every user.
- The link to the textbook work is an analogy of lesson.
- The narration is an AI voice. The outro says so on screen.

## Takeaway
Before trusting a result, ask how many times it was looked at and whether the looking
stopped at the first answer someone liked.

## VERDICT: PASS
