# FACTCHECK — Likely False, Likely True

Status: **GATE F SIGNED — 2026-11-05. 11 rows PASS, 1 title CORRECTED,
2 sources REFUSED and recorded as unused.**

Commissioned as **"Algorithmic Trading"**, with permission to retitle.

## Scope: not investment advice

This is a **research-methodology explainer about the statistics of published
return predictors.** It names no tradable instrument, describes no trading
system, recommends no strategy, and says nothing about what anyone should buy,
sell or hold. Nothing in it is personalized financial advice. The citation strip
on the verdict beat says so on screen.

## The title, corrected

"Algorithmic Trading" is a **field**, not a claim — there is nothing in it to
verify, and a reel about a field would have to either survey it or pick
something arbitrary. The decidable question inside it is: *when a paper reports
a signal that predicted returns, should you believe it?*

On that question the literature contains two peer-reviewed answers whose titles
are near-exact opposites, and the retitle takes its words from them. That
disagreement is checkable, and resolving it produces a rubric.

## Verified claims

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B01, B03 | the 2016 paper catalogues **316 different factors** | PASS | the paper's own text: "We catalogue 316 different factors" |
| 2 | B03 | from **313 articles**, of which **250 published** | PASS | "In total, we focus on 313 articles, among which are 250 published articles" |
| 3 | B03 | discovery rate ~1/yr (1980–91), ~5/yr (1991–2003), ~18/yr in the last nine years | PASS | the paper's own text, same section |
| 4 | B03 | **164 factors** in those nine years, "roughly doubling the 84 factors discovered in all previous years" | PASS | quoted from the paper |
| 5 | B04 | the paper proposes a **t-ratio greater than 3.0** for a newly discovered factor | PASS | NBER WP 20592 abstract, verbatim: "a newly discovered factor needs to clear a much higher hurdle, with a t-ratio greater than 3.0" |
| 6 | B04 | the customary criterion it replaces is **t > 2.0** | PASS | same abstract: "the usual significance criteria for a newly discovered factor, e.g., a t-ratio greater than 2.0" |
| 7 | B01 | the 2016 paper argues "most claimed research findings in financial economics are likely false" | PASS | same abstract, verbatim |
| 8 | B04 | "The overwhelming majority of t-statistics exceed the 1.96 benchmark for 5% significance" | PASS | the paper's own text, quoted |
| 9 | B05 | the rebuttal bounds the false discovery rate at **≤ 25%** in eight of nine previous studies | PASS | arXiv 2206.15365 abstract, verbatim: "FDR ≤ 25%" … "in eight out of nine previous studies" |
| 10 | B05 | "A more refined bound finds **FDR ≤ 9%**" | PASS | same abstract, verbatim |
| 11 | B05, B06 | for the main specification the bound is **≤ 8.5%**, i.e. "at least 91.5% … are true"; and the rebuttal states the 2016 paper's own methods imply ~9% | PASS | arXiv 2206.15365 HTML (v10), verbatim |

Publication details: Review of Financial Studies **29(1), 5–68** (2016), NBER WP
20592. The rebuttal is by **Andrew Y. Chen, Federal Reserve Board**, arXiv
2206.15365, v10 revised November 2025.

## Two sources refused automated fetch, and are NOT used

- **ams.org** (Bailey, Borwein, López de Prado, Zhu, *"Pseudo-Mathematics and
  Financial Charlatanism"*, Notices of the AMS 2014) returned **HTTP 403**. An
  author-hosted mirror returned **404**, and an arXiv id that search results
  associated with it turned out to be an unrelated paper.
- **cmegroup.com** (Harvey, *"Backtesting"*) **timed out twice**.

That paper's well-known results — the expected maximum in-sample Sharpe ratio
from N trials, and the minimum backtest length — would have fitted this reel
well. **None of them appears in any frame**, because I could not read the
source. B07 makes the related point without a number: the trial count is the
figure nobody reports.

## How the 2016 figures were obtained

The publisher copy is paywalled. The author-hosted PDF at Duke redirected once
and returned 200, but its body was not readable through a plain fetch. The file
was saved locally and extracted with `pdftotext -layout`, and the counts were
read out of the paper's own text. This is the same method used for the MuSiQue
and HOPE reels.

The t-ratio and "likely false" wording come from the **NBER abstract**, which
was readable verbatim — not from the PDF extraction and not from any summary.

## Precision notes

- **B05's three bounds measure different things and the beat says so**: 25% is
  across eight of nine prior studies' summary statistics, 9% is a refined bound,
  8.5% is the main specification. They are not three estimates of one quantity.
- **"False discovery rate" direction is stated on screen** — lower means more of
  the findings are real — because an unlabelled percentage here reads backwards.
- **B06 does not claim the rebuttal is correct.** It reports what the rebuttal
  says about the gap, and attributes the ~9% figure to the rebuttal's reading of
  the 2016 methods, not to the 2016 authors.
- **The t > 3.0 hurdle is a proposal**, not an adopted standard, and the reel
  says "what they propose".
- **No Sharpe ratio, return, or performance figure appears anywhere**, because
  none was verified.

## Claims deliberately NOT made

- **No investment advice, and no instrument named.**
- **No claim that any particular published factor is real or spurious.**
- **No claim about which paper is right.** The reel's verdict is about what to
  ask, not which side to join.
- **No backtest-overfitting figures**, for the sourcing reason above.
- **No claim about the profitability of anything.**
