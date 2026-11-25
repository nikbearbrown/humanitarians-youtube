# Pedagogy Review

## Topic
The Check That Passed: a movie recommender whose gradient check passed while its training
objective was wrong, and the logQ correction that fixed it

## Learning Objective
A passing check answers only the question it asks. The viewer leaves able to name, for a
check they rely on, one question it answers and one it cannot.

## Audience
General audience with some interest in AI. Recommendation and "wrong answers in a batch"
are explained in plain words before the correction is named.

## Key Findings Reported
Measured in this session on MovieLens 25M with github.com/Kenny0bi/pulse-recsys:
- 6,198 test users, scored on films watched after the training cutoff.
- Recall at 10: popularity counter 5.8%, two-tower without logQ 3.1%, with logQ 8.6%
  (47% above the counter).
- Gradient check passes: max error 1.27e-06.
- Share of top-ten slots on the 100 most popular films: 1.2% without logQ, 25.5% with.

## Accuracy Gate
See FACTCHECK.md, which records that the repo README's no-logQ figure (0.018) did not
reproduce; the video uses the measured 0.031.

## Restraint Gate
- The README discrepancy is reported to the author, not presented as the video's claim.
- "47 percent above" compares recall at 10 on one temporal split only.
- The narration is an AI voice. The outro says so on screen.

## Takeaway
For any check you trust, write down one question it answers and one it cannot.

## VERDICT: PASS
