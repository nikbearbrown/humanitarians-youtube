The Price That Wasn't There #Shorts

A portfolio dashboard shows Meta at $590. But the quote for Meta came back as zero. The workflow's rule
is "use the current price, or if it's missing, the previous close", and in JavaScript, zero counts as
missing. The math is right and nothing looks wrong, and in this sample it happened to two of the five
stocks. My merged pull request to Mycroft didn't change that rule. It added a record: before any math
runs, a check writes down which price each stock used.

Your turn: pick one number you look at every morning. What is it quietly taking on trust, and what would
tell you if it slipped?

Full video, with three more mornings on the same dashboard and the morning my own test passed when it
shouldn't have: [FULL VIDEO LINK: added once the long form is live]

Contribution: nikbearbrown/mycroft pull request #64 (merged)
https://github.com/nikbearbrown/mycroft/pull/64
Source on screen: data/verified/portfolio-price-fetcher/clean/validated.json · Mycroft main @ 5097a8f

Every price is invented, for testing, and the dashboard is a labelled illustration of our sample summary.
"Previous close" means the price at the end of the last trading day. Narration is a synthetic voice
(Kokoro, run locally). Visuals are original code-drawn animations.

Humanitarians AI — @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: Mycroft, portfolio dashboard, JavaScript, data validation, open source, testing, Shorts,
Humanitarians AI
