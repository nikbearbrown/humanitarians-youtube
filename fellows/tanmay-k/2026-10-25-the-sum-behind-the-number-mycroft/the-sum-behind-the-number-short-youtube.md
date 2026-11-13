Minus Seventy-Eight: where a stress-test number comes from

A stress test says an invented portfolio of three chip stocks would lose 78% in a tech crash. Where does a number like that come from? From adding: the workflow's own list of named shocks, added up one holding at a time. One chip stock takes -15, then -35, then -40, which makes -90; a second takes the same; a third, off the AI list, takes -50. Give each its share of the book and it comes to 36 + 27 + 15 = 78. I wrote a Python copy of the adder, ran it beside the original code on 24 requests, and every number matched.

The full video takes the number apart block by block and ends on a question for any stress test: what was added?
[FULL VIDEO LINK]
Search: The Sum Behind the Number: Taking Apart a Stress Test

The contribution:
nikbearbrown/mycroft pull request #74 (merged): the Scenario Stress Testing Agent recipe, steps 1, 3 and 5 closed in sample mode.
https://github.com/nikbearbrown/mycroft/pull/74

What this Short claims, and what it does not:

- Every portfolio is invented. The tickers on screen come from the workflow's own sector list; the numbers are scenario arithmetic, not predictions, and not investment advice.
- Tech Sector Crash: market -15%, technology sector -30%, semiconductors -35%, AI stocks -40% (and a volatility number). For the first chip stock the engine adds market, semiconductors and AI list: -15 - 35 - 40 = -90. The workflow's README prints this sum as its worked example.
- Weighted 40%, 30% and 30%, the book's loss is 36 + 27 + 15 = 78, a drawdown of 78%.
- The Python copy matched the original code on 24 of 24 requests.
- Nothing was sent anywhere: no model, market-data service or database is called.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animation: no third-party images, recordings or music, and open-licence fonts only (EB Garamond, Inter).

Humanitarians AI - @HumanitariansAI
Tanmay Kulkarni, for Humanitarians AI

Tags: stress testing, scenario analysis, portfolio stress test, how stress tests work, open source finance, Mycroft, finance explained, Humanitarians AI, shorts
