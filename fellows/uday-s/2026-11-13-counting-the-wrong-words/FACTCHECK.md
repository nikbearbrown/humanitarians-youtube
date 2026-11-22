# FACTCHECK — Counting The Wrong Words

Status: **GATE F SIGNED — 2026-11-13. 10 rows PASS, 1 title CORRECTED,
1 secondary-source misreading CAUGHT AND CORRECTED.**

Commissioned as **"how to perform market sentiment analysis using AI for
predicting stocks"**, with permission to retitle.

## Scope: not investment advice

A **measurement-methodology explainer.** It names no tradable instrument,
describes no strategy, reports no return or performance figure, and makes **no
claim that sentiment predicts prices** — B07 exists specifically to separate
that claim from the one the evidence supports. The verdict beat's citation strip
says "not investment advice" on screen.

## The title, corrected

The commissioned phrase bundles a **method** with a **promised outcome**.

- The method half is routine — get text, count negatives, score, act. Teaching
  it as a tutorial would be filler.
- The outcome half — *predicting stocks* — is a separate claim, and nothing in
  the primary literature used here establishes it. Last week's reel was about
  exactly how hard that claim is to establish.

So the retitle names the step the evidence is actually about: the decision
upstream of the model, where the published failure is large, measured, and
fixable.

## Verified claims

Every figure read from the paper's own text, extracted with `pdftotext -layout`.

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B03 | **73.8%** of Harvard-list negative **word counts** in 10-Ks come from words not typically negative in a financial context | PASS | "we find that almost three-fourths (73.8%) of the negative word counts according to the Harvard list are attributable to words that are typically not negative in a financial context" |
| 2 | B03 | the sample is **121,217** filings | PASS | "sample of 121,217 10-Ks by 44,822 firms" |
| 3 | B03 | over **1994 to 2008** | PASS | abstract: "In a large sample of 10-Ks during 1994 to 2008" |
| 4 | B04 | the first seven words — tax, costs, loss, capital, cost, expense, expenses — account for **more than one-fourth** of the total negative count | PASS | "The first seven words (tax, costs, loss, capital, cost, expense, and expenses) account for more than one-fourth of the total count of 'negative' words" |
| 5 | B04 | **costs** alone is **4.61%** of the total | PASS | "the word costs accounts for 4.61% of the total count of all the H4N-Inf negative words" |
| 6 | B05 | *foreign* usually denotes international operations; *vice* usually denotes vice-presidents | PASS | the paper's own examples |
| 7 | B05 | *mine, cancer, crude, tire* identify an industry segment rather than a negative event | PASS | "are more likely to identify a specific industry segment than reveal a negative financial event" |
| 8 | B06 | the finance list, **Fin-Neg**, contains **2,337 words including inflections** | PASS | "Fin-Neg consists of 2,337 words, including inflections" |
| 9 | B06 | it is about **half the size** of the list it replaces | PASS | "the Fin-Neg list has only about half as many words as the H4N-Inf list" |
| 10 | B08 | the mycroft market-sentiment attestation states nobody has checked whether the score means anything, and that weights/thresholds/keyword lists were inherited with no derivation, backtest or author | PASS | quoted verbatim from the committed attestation at `b425b19`; still present today |

Publication: **The Journal of Finance, Vol. LXVI, No. 1, February 2011.**

## The misreading this reel caught

A search summary reported the 73.8% figure as the share of **distinct words** in
the Harvard list that are not negative in finance, and separately reported a
~50% figure, guessing that *that* one was about occurrences.

**Both guesses were wrong.** The paper's sentence makes 73.8% a share of **word
counts**, i.e. of the score itself — a considerably stronger claim. And the ~50%
figure is a narrower sub-result: after removing the five words that also appear
on the finance list, *the remaining 25 of the top 30* still account for almost
half the Harvard negative count.

B03 therefore labours the distinction on screen — "not 73.8% of the word list;
73.8% of the score" — because the weaker reading is the one in circulation. The
~50% sub-result is **not used**, since stating it without its "top 30 minus 5"
scoping would mislead.

## Precision notes

- **The paper's own abstract is looser than its body.** The abstract says
  "almost three-fourths of the words identified as negative"; the body says
  "almost three-fourths (73.8%) of the negative word **counts**". The reel uses
  the body's formulation, which is the precise one.
- **"More than one quarter" is the paper's wording**, not a computed figure, and
  the reel keeps the qualifier rather than inventing a decimal.
- **B06's two bars are schematic.** The finance list is drawn at about half the
  length of the other, which is what "about half as many words" states; the
  Harvard list's exact size is not shown, because only the ratio is quoted.
- **B08's quote is from a project record, not a paper**, and is attributed on
  screen as such.

## Claims deliberately NOT made

- **No claim that sentiment predicts returns.** B07 states the opposite: this
  settles measurement, not prediction.
- **No claim that any model or vendor is good or bad.**
- **No instrument, ticker, strategy, or performance figure anywhere.**
- **No claim that the finance list is correct**, only that it was built for the
  domain and is smaller.
- **No claim about non-filing text** — headlines, posts, calls — beyond noting
  the result does not automatically transfer.
