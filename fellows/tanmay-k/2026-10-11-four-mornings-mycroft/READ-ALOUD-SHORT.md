# READ-ALOUD: Short Gate P sheet, draft 2

*The Price That Wasn't There* (working title) · 9:16 · voice `am_onyx`

Draft 2 of the Short, rewritten for context (what changed and why: the audit table at the top of
`SCRIPT-SHORT.md`). Your draft 1 PASS doesn't carry over, because most lines are new. Read it aloud, top to
bottom, in one sitting, as someone who has never seen the long film. Then reply **"Short Gate P PASS"**
or list the beats that tripped you.

Say-it-right: **Mycroft** = MY-croft (the audio uses the override). **Meta** = MEH-tuh.

## Mechanical pass, already run

- Sentences over 22 words: 1
  - S02: Every number on a screen like this arrives through hand-offs, places where one part of the system takes another part's word for it.
- Digits in narration: 0
- Stills: portrait zones 7/7, Gate V 0 BLOCKER / 0 MAJOR, and every frame looked at (S03 and S05 overlaps fixed)

## The script

### [0:00] S01 · WHO, AND WHAT THIS IS  _(tone: warm, unhurried)_

This is Tanmay Kulkarni, in for Humanitarians AI. This week I worked on Mycroft, which is both a book and a working repository of finance pipelines. One of those pipelines feeds this: a portfolio dashboard. Five stocks, and one total, sixty-five thousand and ninety-eight dollars. Every price on it is invented, for testing.

<sub>**On screen:** A portfolio dashboard, from Mycroft · “both a book and a working agentic repository” · This dashboard: 5 holdings · total 65,098.13</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:14] S02 · THE IDEA, AND THE QUESTION  _(tone: clear; the question is the hook)_

Every number on a screen like this arrives through hand-offs, places where one part of the system takes another part's word for it. Here, the dashboard takes the quote service's word for every price. So here's the one question for this video. When a hand-off slips, does anything say so?

<sub>**On screen:** Every number arrives through hand-offs · When a hand-off slips, does anything say so?</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:28] S03 · THE SLIP  _(tone: slow down on "zero")_

Look at Meta. The dashboard shows five hundred and ninety dollars. But the quote for Meta actually came back as zero. The workflow picks each price with one rule. Use the current price, or if it's missing, use the previous close, the price at the end of the last trading day. And in JavaScript, the language this step is written in, zero counts as missing. So the screen quietly shows the older price.

<sub>**On screen:** One price isn't what it looks like · The quote for META came back: 0 · The rule · code: regularMarketPrice || previousClose: current price, or if missing, previous close · The dashboard shows: 590.00 (previous close)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:48] S04 · WHY NOTHING LOOKED WRONG

The math is right. Nothing on the screen looks wrong. And Meta isn't the only one. The Google stock's quote had no current price at all, so it got the previous close too. Two of the five prices on this screen aren't the current quote, and the screen looks exactly the same either way.

<sub>**On screen:** Not just one · META: the quote said 0 · GOOGL: the quote had no current price · Both shown at the previous close. The screen looks the same.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:03] S05 · WHAT SAYS SO NOW  _(tone: first person, plain)_

My pull request to Mycroft, now merged, didn't change that rule. It's the workflow's choice, not mine, and the recipe notes it for the maintainers. What I added is a record. Before any math runs, a check now writes down which price each stock used. Meta, previous close. Google, previous close. The other three, the current price.

<sub>**On screen:** What says so now · META · price_source: previousClose · GOOGL · price_source: previousClose · AMD, MSFT, NVDA · price_source: regularMarketPrice</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:19] S06 · YOUR NUMBER  _(tone: slower, then a 2 s pause)_

Now pick one number you look at every morning. What is it quietly taking on trust? A good answer names the hand-off, and the thing that would tell you if it slipped. "It's always been right" doesn't count.

*(2 s silence)*

<sub>**On screen:** Your number · What is it quietly taking on trust? And what would tell you if it slipped? · Good answer: names the hand-off, and the thing that would say so · Not an answer: “it's always been right”</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:32] S07 · CLOSE

The full video spends three more mornings with this dashboard. A stock the portfolio doesn't hold, a list written twice, and a call by name. And then the morning my own test passed when it shouldn't have. Tanmay Kulkarni, in for Humanitarians AI, signing off.

<sub>**On screen:** Four mornings, one dashboard · a stock the portfolio doesn't hold · a list written twice · a call by name · the morning my own test passed · @HumanitariansAI</sub>

> ☐ reads cleanly   ☐ note: ______________________

**Total: about 1:44.**
