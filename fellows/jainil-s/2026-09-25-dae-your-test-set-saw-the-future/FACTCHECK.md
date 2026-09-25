# FACTCHECK — Your Test Set Saw the Future

Status: **GATE F CLOSED — 2026-09-25.** The central claim is quoted verbatim
from scikit-learn's own documentation for the tool built to prevent this
failure. No magnitude of accuracy inflation is claimed anywhere.

| # | Beat | Claim (as spoken / shown) | Verdict | Source |
|---|---|---|---|---|
| 1 | B00 | A model can score well offline and badly in production because of the split | ✅ PASS | Follows from S1 — the failure mode the library names |
| 2 | B01 | A random split is the sensible default for most data | ✅ PASS | Framing, not a claim. Stated as "for most data", and immediately qualified. |
| 3 | B01 | With time-ordered rows, shuffling lets the model train on later data and test on earlier | ✅ PASS | S1, verbatim: "they would lead to training on future data and evaluating on past data" |
| 4 | B02 | Under a random split, test points have training data later in time than themselves | ✅ PASS | Arithmetic property of random sampling from an ordered sequence; shown directly on the timeline |
| 5 | B03 | On-screen quote attributed to scikit-learn's `TimeSeriesSplit` docs | ✅ PASS | S1 + S2, **verbatim**. Attribution line names the page. |
| 6 | B03 | "The standard approach is documented as wrong for this case, by the people who ship it" | ✅ PASS | Fair characterisation of S1, which says other CV methods "are inappropriate" for time-ordered data |
| 7 | B04 | A chronological split puts every test row after every train row | ✅ PASS | S2: "successive training sets are supersets of those that come before them" |
| 8 | B05 | The failure is silent — no error, no warning | ✅ PASS | Follows from mechanism: a shuffled split is a valid operation; nothing in the library raises |
| 9 | B06 | `TimeSeriesSplit` is a drop-in for `KFold` | ✅ PASS | S3, verbatim: "This cross-validation object is a variation of KFold. In the k-th split, it returns the first k folds as the train set and the (k+1)-th fold as the test set." |
| 10 | B06 | It requires equally spaced samples | ✅ PASS | S4, verbatim: "To ensure comparable metrics across folds, samples must be equally spaced." |
| 11 | B06 | Grouped rows (same user, same device) leak the same way under a random split | ✅ PASS | Same mechanism as 4 — near-duplicates split across both sides. Stated as an extension, no figure attached. |

## Claims deliberately CUT

- **Any number for how much offline accuracy inflates.** Blog posts quote
  dramatic figures; they are dataset-specific and untraceable. The reel argues
  direction and mechanism only, and says so.
- Named real-world incidents attributed to temporal leakage. Not sourced to a
  standard anyone could check.
- Any claim about how common this mistake is in practice.

## Register check

B00 opens as a learning log — "this week I learned … and I had written the
cheat myself." That is a framing device in the narrator's voice, not a claim
about a specific project, and nothing downstream depends on it being literal.
