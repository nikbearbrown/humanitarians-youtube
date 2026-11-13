# SCRIPT: the Short (9:16), *The Price That Wasn't There* (working title)

**Draft 2, 2026-10-10** (Short Gate P PASS; one later change approved by Tanmay: S01 "Five stocks, and one total" → "Five stocks. One total", because Kokoro blended it into "five stocks in one total"). Rewritten after Tanmay's note on draft 1 ("make sure the Short gives the right context and is
not something done in a hurry"). Draft 1 had passed Short Gate P, but draft 2 changes most lines, so **it needs a
fresh Short Gate P** before any audio. Approved shape unchanged (`ANGLE.md` §2): **one morning, the zero price**, one
continuous arc for someone who never sees the long film. Every shot is `MorningDashboardOFL916`.

## What was wrong with draft 1 (audited as a first-time viewer)

| # | Problem in draft 1 | Where | What draft 2 does |
|---|---|---|---|
| 1 | **No frame for the first 50 seconds.** The viewer saw "a portfolio dashboard" with no idea whose it is, where it comes from, or why I'm showing it. Mycroft only appeared in S04 | S01–S03 | S01 says who I am, what Mycroft is and what this dashboard is, before any numbers |
| 2 | **The idea came after the example.** "Hand-off" was introduced in S03, after the slip. A viewer can't know what to look for (the topic Short learned the same lesson: framework early) | S03 | New S02 names the idea and gives the video one question up front: "when a hand-off slips, does anything say so?" |
| 3 | **"Previous close" was never explained.** It's jargon to most viewers, and it's the whole point | S02 | S03 says it plainly: the price at the end of the last trading day |
| 4 | **The rule was code, not words.** `regularMarketPrice \|\| previousClose` on screen, and "a JavaScript 'or'" in the ear | S02 | The rule spoken in plain words ("use the current price, or if it's missing, the previous close"), then why zero counts as missing. The code stays on screen as the source |
| 5 | **Half the story was missing.** The merged record shows **two** of five prices came from the previous close: META (zero) and GOOGL (no current price at all). Draft 1 only told the first | — | S04: "Meta isn't the only one" (FACTCHECK W20, from `validated.json`) |
| 6 | **"What says so now" didn't show the record.** One label, `previousClose`, with nothing beside it | S04 | S05 shows the record for all five stocks, each appearing as it's spoken: two previous closes, three current prices |
| 7 | **The close was confusing.** Four hand-off boxes marked STOPS, none of them explained in the Short | S06 | S07 names the three other mornings and my own test, as a list headed "In the full video" |
| 8 | **The pictures barely changed.** Same dashboard, small evidence boxes, a large empty band | all | Each beat has a job on screen: the frame (S01), the hand-off box (S02), the zero turning into 590 (S03), the second flag (S04), the record (S05), the question (S06), what's next (S07) |

**Length:** 370 words, about 1:45 plus a 2 s pause (the long film's measured pace is 3.6 words/s). The limit is 180 s.

**Same rules as before:** numbers in words when spoken, digits only on screen. "Mycroft" keeps the override
`mˈaɪkɹɔft`. Every price is invented, said in S01 and labelled on every frame. The fallback is described as
how the workflow works, never as a fault. Facts come only from `../FACTCHECK.md` (W1, W3–W8, W16, W20, W21).

---

### S01 · WHO, AND WHAT THIS IS  _(warm, unhurried)_
> This is Tanmay Kulkarni, in for Humanitarians AI. This week I worked on Mycroft, which is both a book and a working repository of finance pipelines. One of those pipelines feeds this: a portfolio dashboard. Five stocks. One total, sixty-five thousand and ninety-eight dollars. Every price on it is invented, for testing.

*On screen:* heading "A portfolio dashboard, from Mycroft"; the five rows and the total. "Illustration · every price
invented". Evidence: "Mycroft: “both a book and a working agentic repository”" (README). *Refs:* W1, W4.

### S02 · THE IDEA, AND THE QUESTION  _(clear; the question is the hook)_
> Every number on a screen like this arrives through hand-offs, places where one part of the system takes another part's word for it. Here, the dashboard takes the quote service's word for every price. So here's the one question for this video. When a hand-off slips, does anything say so?

*On screen:* one hand-off box, "the price, from the quote service · ON TRUST". Evidence title "One question", line
"When a hand-off slips, does anything say so?" *Refs:* W2 (the price fetcher fetches the prices), framing.

### S03 · THE SLIP  _(slow down on "zero")_
> Look at Meta. The dashboard shows five hundred and ninety dollars. But the quote for Meta actually came back as zero. The workflow picks each price with one rule. Use the current price, or if it's missing, use the previous close, the price at the end of the last trading day. And in JavaScript, the language this step is written in, zero counts as missing. So the screen quietly shows the older price.

*On screen:* the META row lights, tagged "previous close". Three items appear as each is spoken: "The quote
came back · 0"; "The rule · current price, or if missing, previous close"; "The dashboard shows · 590.00 (previous
close)". Source: the code line `regularMarketPrice || previousClose`, Calculate Metrics. *Refs:* W5, W6.

### S04 · WHY NOTHING LOOKED WRONG
> The math is right. Nothing on the screen looks wrong. And Meta isn't the only one. The Google stock's quote had no current price at all, so it got the previous close too. Two of the five prices on this screen aren't the current quote, and the screen looks exactly the same either way.

*On screen:* the GOOGL row lights too, tagged "previous close", as it's spoken. Evidence "Two of five: META (0), GOOGL
(none)". The hand-off box stays ON TRUST. *Refs:* W5, W20.

### S05 · WHAT SAYS SO NOW  _(first person, plain)_
> My pull request to Mycroft, now merged, didn't change that rule. It's the workflow's choice, not mine, and the recipe notes it for the maintainers. What I added is a record. Before any math runs, a check now writes down which price each stock used. Meta, previous close. Google, previous close. The other three, the current price.

*On screen:* "Mycroft · PR #64, merged" on "My pull request". The hand-off box turns RECORDED on "What I added is a
record". The record itself, from `validated.json`, line by line as spoken: "META · price_source: previousClose", "GOOGL
· price_source: previousClose", "AMD, MSFT, NVDA · price_source: regularMarketPrice". *Refs:* W3, W7, W8, W20, W21.

### S06 · YOUR NUMBER  _(slower, then a 2 s pause)_
> Now pick one number you look at every morning. What is it quietly taking on trust? A good answer names the hand-off, and the thing that would tell you if it slipped. "It's always been right" doesn't count.

*On screen:* the dashboard dims. The question, with "Good answer: names the hand-off, and what would say so · Not an
answer: “it's always been right”". 2 s of silence held after. *Refs:* none.

### S07 · CLOSE
> The full video spends three more mornings with this dashboard. A stock the portfolio doesn't hold, a list written twice, and a call by name. And then the morning my own test passed when it shouldn't have. Tanmay Kulkarni, in for Humanitarians AI, signing off.

*On screen:* the dashboard with the one RECORDED box; a list headed "In the full video": "a stock the portfolio doesn't
hold · a list written twice · a call by name · the morning my own test passed". `@HumanitariansAI`. *Refs:* W9–W16
(pointers only).

---

## Does it carry its own context? (draft 2)

| A first-time viewer needs | Where | How |
|---|---|---|
| Who's speaking, and why | S01, S07 | Name at both ends; "this week I worked on Mycroft" |
| What Mycroft is | S01 | Its own words, a book and a working repository, with the README on screen |
| What the dashboard is, and that it isn't real money | S01 | "One of those pipelines feeds this"; "every price invented", said and labelled |
| The idea, before the example | S02 | Hand-offs, and the one question the video answers |
| What went wrong, in plain words | S03 | The zero, the rule in words, what "previous close" means, why zero counts as missing |
| That it's not a one-off | S04 | Two of five prices, from the merged record |
| What I did, and didn't do | S05 | Kept the rule (not mine to change), flagged it, added the record, shown line by line |
| The answer to S02's question | S05 | Yes: now the record says so, for every stock |
| Something to do | S06 | Your own number, with a good and a weak answer, and a pause to think |
| Where to go next | S07 | The three other mornings and my own test, named |

## For you to judge at the read

- **S01:** is the context enough without slowing the opening down?
- **S03:** the longest beat, and the heart of the Short. Does "the price at the end of the last trading day" and
  "zero counts as missing" land the first time you hear it?
- **S04:** "the Google stock". The ticker on screen is GOOGL. Is that clear spoken aloud?
- **S05:** does the record, read out line by line, feel like the answer to S02's question?
- **Not claimed**, as in the long film: why a quote service might send zero or no price.
