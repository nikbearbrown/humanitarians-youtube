Four Mornings: What a Dashboard Takes on Trust

A portfolio dashboard shows one clean total. Behind it, every number arrives through quiet hand-offs:
places where one part of a system takes another part's word for it. This week I contributed to Mycroft,
which describes itself as both a book and a working repository for finance pipelines, and my pull request
(now merged) put a check at four of those hand-offs.

So this video spends four mornings with the same dashboard, and on each one, lets one hand-off slip. A
price of zero quietly becomes the previous close. A quote arrives for a stock the portfolio doesn't hold.
The portfolio turns out to be written twice in the same workflow. The dashboard finds the price workflow
only by its name. Each time, the question is what the reader would have seen, and what says so now. Then
there's the morning it was my own check: a test that passed when it should have failed, and what I changed
so it can't do that again.

Chapters:
0:00 A portfolio dashboard, over coffee
0:20 What this is: Mycroft and two recipes
0:44 Morning one: a price of zero
1:12 Morning two: a stock the portfolio doesn't hold
1:31 Morning three: one list, written twice
1:52 Morning four: the call by name
2:08 The morning it was my own check
2:32 The same dashboard, any morning
2:49 Your number
3:01 Outro

The contribution: nikbearbrown/mycroft pull request #64, merged
https://github.com/nikbearbrown/mycroft/pull/64
Mycroft: https://github.com/nikbearbrown/mycroft

Everything shown on screen comes from files merged into Mycroft's main branch (commit 5097a8f):

- recipes/portfolio-price-fetcher.md and recipes/portfolio-dashboard.md (the two recipes, their steps,
  "Notes from porting", status DRAFT)
- data/verified/portfolio-price-fetcher/clean/validated.json and portfolio-summary.json (the record of
  which price each stock used, and the sample summary)
- data/raw/portfolio-price-fetcher/sample/ (the invented test prices)
- logs/portfolio-price-fetcher-provenance-2026-10-10.json and logs/portfolio-dashboard-provenance-2026-10-10.json
- scripts/tools/portfolio-price-fetcher-self-test.py (sections A–D, including the comment about the first
  version of my test)
- the declared n8n workflows' Calculate Metrics and Call Portfolio Price Fetcher nodes

What this video claims, and what it doesn't:

- Every price is invented, for testing. The dashboard is an illustration of our verified sample summary,
  labelled as such on every frame. It isn't market data, and it isn't the workflow's own HTML.
- The zero-price fallback and the portfolio written twice are described as how the workflow works, not as
  faults. My port keeps both behaviours, and the recipe leaves them to the maintainers.
- In the sample, two of the five prices are the previous close: META (the quote said zero) and GOOGL (no
  current price at all). Both are tagged on screen.
- The video says only what each check does. It makes no claim about why a quote service might send zero,
  or how n8n resolves the placeholder workflow ID.
- Both recipes are still drafts, and the video ends on what still runs on trust: live prices, three more
  steps in one recipe and five in the other.
- The only mistake in this film is mine (my own test), shown with its fix.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animations: no
third-party images, recordings or music, and open-licence fonts only.

Humanitarians AI — @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: Mycroft, open source contribution, finance pipelines, portfolio dashboard, data validation, data
provenance, n8n, JavaScript truthiness, testing, self-test, AI agents, Humanitarians AI
