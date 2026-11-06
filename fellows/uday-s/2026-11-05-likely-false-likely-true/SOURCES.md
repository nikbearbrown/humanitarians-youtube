# SOURCES — Likely False, Likely True

Two primary sources carry every figure. No aggregator, blog, vendor page or
summary sourced a number.

| On screen | Beat | Source |
|---|---|---|
| "most claimed research findings … are likely false" | B01 | NBER WP 20592 abstract, verbatim |
| "most claimed statistical findings … are likely true" | B01 | arXiv 2206.15365, the paper's title |
| 316 factors | B01, B03 | Harvey–Liu–Zhu PDF, extracted text |
| 313 articles, 250 published | B03 | same |
| ~1/yr, ~5/yr, ~18/yr discovery rates | B03 | same |
| 164 in nine years vs 84 in all prior years | B03 | same, quoted |
| t > 3.0 proposed; t > 2.0 the usual criterion | B04 | NBER WP 20592 abstract, verbatim |
| "the overwhelming majority of t-statistics exceed the 1.96 benchmark" | B04 | Harvey–Liu–Zhu PDF, quoted |
| FDR ≤ 25% in eight of nine prior studies | B05 | arXiv 2206.15365 abstract, verbatim |
| a more refined bound, FDR ≤ 9% | B05 | same abstract, verbatim |
| FDR ≤ 8.5% on the main specification; at least 91.5% true | B05 | arXiv 2206.15365 HTML v10, verbatim |
| the 2016 methods imply ~9%; the gap is definitional | B06 | same |

## Reference links

- Harvey, Liu, Zhu — Review of Financial Studies 29(1), 5–68 (2016), NBER WP 20592 — https://www.nber.org/papers/w20592
- Author-hosted PDF — https://people.duke.edu/~charvey/Research/Published_Papers/P118_and_the_cross.pdf
- Chen (Federal Reserve Board), arXiv 2206.15365 — https://arxiv.org/abs/2206.15365

## How the 2016 figures were read

The publisher copy is paywalled and the author-hosted PDF would not yield its
body to a plain fetch. The file was saved locally and run through
`pdftotext -layout`, and the counts were read out of the paper's own sentences:

> In total, we focus on 313 articles, among which are 250 published articles.
> We catalogue 316 different factors.

> In total, 164 factors were discovered in the past nine years, roughly
> doubling the 84 factors discovered in all previous years.

The t-ratio hurdle and the "likely false" phrasing are from the NBER abstract,
which was readable verbatim. Nothing in this reel rests on a search summary.

## Two sources that refused, and are therefore absent

- **ams.org returned HTTP 403** for the Notices of the AMS article on backtest
  overfitting. An author-hosted mirror 404'd, and an arXiv id that search
  results associated with it turned out to be an unrelated paper.
- **cmegroup.com timed out twice** on Harvey's "Backtesting".

The expected-maximum-Sharpe and minimum-backtest-length results from that
literature would have suited this reel. They appear nowhere in it. B07 makes the
adjacent point without a figure: the trial count is what nobody reports.

## A search result that was read and then not used for any number

An early search returned secondary summaries putting the Bonferroni threshold
for 316 tests near t = 3.8, and the share of false positives at "a third to a
half". Neither was confirmed in a primary source, so neither appears.

## Claims NOT sourced here, and therefore not made

- Nothing about any tradable instrument, strategy or system.
- No Sharpe ratio, return, or performance figure of any kind.
- No claim about which of the two papers is correct.
