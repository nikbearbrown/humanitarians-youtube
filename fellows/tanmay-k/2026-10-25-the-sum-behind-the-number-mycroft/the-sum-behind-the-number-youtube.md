The Sum Behind the Number: Taking Apart a Stress Test

A stress test says an invented portfolio of three chip stocks would lose 78% in a tech crash. Where does a number like that come from? In one open-source finance workflow, it comes from adding: a scenario is a short list of named shocks, and the engine adds up the shocks that belong to each holding. This video takes the number apart block by block (minus 15, minus 35, minus 40 for one holding, then the whole book), shows a milder scenario using the same rule, and ends on a question to take to any stress test: what was added, from which lists, and has anyone run the adder beside the original? This week I contributed to Mycroft so those steps run on sample data, with checks: a data-shape validator, a provenance check, and a Python copy of the engine that matches the original code on every request I tried.

Chapters:
0:00 Where does −78% come from?
0:13 What this is
0:37 A scenario is a list
1:03 One holding, one block at a time
1:25 The same crash, different holdings
1:45 A milder scenario, the same rule
2:09 Run beside the original
2:29 What the checks protect
2:52 A good list for next time
3:07 Ask what was added

The contribution:
nikbearbrown/mycroft pull request #74 (merged): the Scenario Stress Testing Agent recipe, steps 1, 3 and 5 closed in sample mode. A provenance check, a data-shape validator with the workflow's own rules, a Python port of four code nodes checked against the original code on 24 requests, a self-test with 12 deliberate breaks, and 22 invented sample portfolios. The recipe stays a draft: five items are still open, and nothing calls a model, a market-data service or a database.
https://github.com/nikbearbrown/mycroft/pull/74

What this video claims, and what it does not:

- Every portfolio is invented. The tickers on screen come from the workflow's own sector list, and the numbers are scenario arithmetic, not predictions about any company. Nothing here is investment advice.
- The scenario: Tech Sector Crash names five items: four price shocks (market -15%, technology sector -30%, semiconductors -35%, AI stocks -40%) and a volatility number. For each holding the engine adds the price shocks that belong to it. The first chip stock belongs to the market, to semiconductors and to the AI list: -15, -35 and -40 make -90. The workflow's own README prints this same sum as its worked example.
- The book: a second chip stock also takes -90; a third, off the AI list, takes -50. Weighted 40%, 30% and 30%, the three come to 36 + 27 + 15 = 78, a drawdown of 78% (10,000 down to 2,200). The workflow labels losses above 30% "critical".
- A milder case: an aggressive rate hike (market -10%, growth stocks -20%, technology sector -15%) on four equal growth names gives -30 for three of them and -45 for the one also filed under the technology sector; the book loses 33.75%.
- The check: a Python copy of the engine and its first steps, run beside the original code taken from the workflow file, matched on all 24 requests (every number, label and message). A self-test of 27 checks, including 12 deliberate breaks, caught every break.
- The validator accepts portfolios whose weights total 0.6 or 1.2 (the workflow rescales weights to 1) and stops each of 10 deliberately flawed portfolios with its reason.
- Nothing was sent anywhere: the call to a model, the market-data request and the reply to a caller are recorded as not approved and never made.

Source: the merged repository (nikbearbrown/mycroft, main after PR #74). Every figure on screen is read from files in it; the sources are named on screen and in the repository.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animations: no third-party images, recordings or music, and open-licence fonts only (EB Garamond, Inter, PT Mono).

Humanitarians AI - @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: stress testing, scenario analysis, portfolio stress test, how stress tests work, open source finance, Mycroft, verification, Python, data validation, explainer, Humanitarians AI
