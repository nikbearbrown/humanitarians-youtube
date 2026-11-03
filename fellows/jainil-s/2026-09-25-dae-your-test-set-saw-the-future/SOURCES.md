# SOURCES — dae-your-test-set-saw-the-future

The mechanism is standard, documented ML practice. The authoritative source is
scikit-learn's own documentation for the tool built to prevent this failure.

| # | Source | Verbatim wording relied on | Supports |
|---|---|---|---|
| S1 | [`TimeSeriesSplit` — scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | "Provides train/test indices to split time-ordered data, where **other cross-validation methods are inappropriate, as they would lead to training on future data and evaluating on past data**." | The whole thesis, stated by the library itself |
| S2 | [`TimeSeriesSplit` — scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | "Note that, unlike standard cross-validation methods, **successive training sets are supersets of those that come before them**." | How a correct split is constructed — train always precedes test |
| S3 | [`TimeSeriesSplit` — scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | "This cross-validation object is a variation of `KFold`. In the k-th split, it returns the first k folds as the train set and the (k+1)-th fold as the test set." | The fix is a drop-in replacement, not a rewrite |
| S4 | [`TimeSeriesSplit` — scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | "To ensure comparable metrics across folds, **samples must be equally spaced**." | The fix has its own precondition — stated, not glossed |

## Why the library's own docs are the source

The claim being made is *"the standard tool is wrong for this data"*. The
strongest possible evidence is the standard library saying so itself, which S1
does explicitly. No secondary commentary is needed and none is used.

## Deliberately NOT used

- Specific figures for how much offline accuracy inflates under temporal
  leakage. Widely quoted in blog posts, highly dataset-dependent, and not
  traceable to a source that would survive scrutiny. **No magnitude is claimed.**
- Named incidents of production failures attributed to this cause. The reel
  argues the mechanism, not a case study.

## Derived, not cited

The worked example — a shuffled timeline placing later rows in train and
earlier rows in test — is an illustration of S1's stated failure mode, labelled
as such on screen.
