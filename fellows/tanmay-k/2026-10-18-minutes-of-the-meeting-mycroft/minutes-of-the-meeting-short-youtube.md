Who Fills in the Blank? What an AI Is Handed

An AI is about to give advice on a stock, and the last thing it's told is that its action plan must strictly match
a verdict. Who decides the verdict? In an open-source finance pipeline I contributed to, three simulators each read
one invented stock their own way: one says strong sell, one says enter a full position, one says the verdict is
fragile. A chair weighs them 45, 35 and 20 into a sell, and the AI is handed the minutes, not the meeting. The full
film follows the whole meeting, shows what the AI is handed, and shows the one place my own copy of the steps
disagreed with the original, and how I caught it.

The full film shows the whole meeting and the minutes the AI receives:
[FULL VIDEO LINK]
Search: Minutes of the Meeting: What an AI Is Handed

The contribution:
nikbearbrown/mycroft pull request #70 (merged): a Python port of six steps of the What-If Simulation Agent recipe,
checked against the original JavaScript, with a validator, a provenance check and a self-test. The recipe stays a
draft; nothing calls the AI or the database.

What this Short claims, and what it does not:

- The stock (Ironbridge Power) and every company, ticker and number are invented. Nothing here is investment advice,
  and the simulators' finance is shown as the workflow defines it, not judged.
- The three simulators: the first says strong sell (82% confidence); the second, for an aggressive investor, says
  enter a full position (four limits met exactly); the third finds the verdict fragile (stability 0.05 out of 1).
- The chair weighs them 45%, 35% and 20%; the pieces are 0.37, 1.75 and 0.05, together 2.17 out of 5, which falls in
  the workflow's SELL band (1.8 up to 2.8).
- The briefing the AI is handed is about 470 words, in five sections, and ends with the instruction shown at the top.
- "I show where my own copy disagreed" refers to my port of the six steps, which disagreed with the original on two
  requests and was fixed; the long film shows it.

Source: the merged repository (nikbearbrown/mycroft, main after PR #70). Every figure on screen is read from files in
it; the sources are named on screen.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animation: no third-party
images, recordings or music, and open-licence fonts only (EB Garamond, Inter, PT Mono).

Humanitarians AI — @HumanitariansAI
Tanmay Kulkarni, for Humanitarians AI

Tags: AI agents, LLM pipelines, prompt engineering, what-if simulation, open source finance, Mycroft, AI transparency,
Humanitarians AI
