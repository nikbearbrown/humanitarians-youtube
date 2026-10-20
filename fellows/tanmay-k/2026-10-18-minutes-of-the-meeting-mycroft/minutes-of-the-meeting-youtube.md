Minutes of the Meeting: What an AI Is Handed

Before an AI writes anything, someone has already told it what to say about. In one open-source finance pipeline,
that someone is six small steps: three simulators that each read the same invented stock their own way, and a chair
that weighs them 45, 35 and 20 into one verdict. The AI never sees the original request. It sees the minutes. This
week I contributed to Mycroft so those six steps run on test data, with checks, and the minutes can be read before any
model sees them. The video follows one stock through the meeting, shows the one place my own copy of the steps
disagreed with the original, and ends on a question to take to your own pipelines: who had a vote, and how much?

Chapters:
0:00 The last line of the message
0:15 What this is
0:46 The chair opens
1:12 First voice: growth against sentiment
1:25 Second voice: the same stock, three investors
1:45 Third voice: how close to changing its mind
2:00 They disagree: the chair weighs the voices
2:33 The minutes: what the AI is handed
2:52 My minute-taker: where my copy disagreed
3:20 Adjourned: nothing was sent anywhere
3:33 Your turn

The contribution:
nikbearbrown/mycroft pull request #70 (merged): a Python port of six steps of the What-If Simulation Agent recipe,
checked against the original JavaScript on 23 requests; a data-shape validator; a provenance check; a self-test with
10 deliberate breaks; 25 invented sample requests. The recipe stays a draft: five items are still open, and nothing
calls the AI or the database.

What this video claims, and what it does not:

- The stock in the video (Ironbridge Power) and every company, ticker and number are invented. Nothing here is
  investment advice, and the simulators' finance is shown as the workflow defines it, not judged.
- The three voices: Sim 1 sorts a stock into one of nine boxes by growth and sentiment (this one: STRONG SELL, 82%
  confidence); Sim 2 judges the same stock for a conservative, a balanced and an aggressive investor (avoid, avoid,
  enter a full position; the aggressive investor's four limits are met exactly); Sim 3 nudges growth and sentiment six
  ways and finds three that change the verdict (stability 0.05 out of 1).
- The chair weighs the voices 45%, 35% and 20% on a one-to-five scale. The weighted pieces are 0.37, 1.75 and 0.05,
  together 2.17, which falls in the workflow's SELL band (1.8 up to 2.8). The scale puts strong sell at the bottom and
  enter a full position at the top, which is why a smaller weight on the top can outweigh a bigger weight on the bottom.
- The briefing the AI is handed is about 470 words and ends with an instruction to match the verdict. In it, a number
  someone typed and a number the workflow filled in by default print the same.
- My port and the original disagreed on two requests where a number was not a number (growth typed as "abc",
  sentiment left as empty text), because JavaScript's Math.min and Python's min treat NaN differently. I fixed it; the
  two now agree on all 23 requests. Whether the workflow itself should reject such values is the maintainers' call.
- Nothing was sent anywhere: the calls to the AI service and the database are recorded as not approved and never made.

Source: the merged repository (nikbearbrown/mycroft, main after PR #70). Every figure on screen is read from files in
it; the sources are named on screen and in the repository.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn slates and animations: no
third-party images, recordings or music, and open-licence fonts only (EB Garamond, Inter, PT Mono).

Humanitarians AI — @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: AI agents, LLM pipelines, prompt engineering, what-if simulation, open source finance, Mycroft, verification,
Python and JavaScript, AI transparency, Humanitarians AI
