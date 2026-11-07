# Frictional Log — Guardrails and Evals

**Week of 2026-09-18** · Adwait Changan · Agentic AI playlist (Episode 7)
Topic: you can't read every run, so you must be able to score one.

**What I built this week**
- Priced manual review: ~90 seconds per run, which doesn't shrink with volume — 1,000 runs a day is 25 human-hours in a 24-hour day.
- Tested sampling honestly: 5% of a 2% failure rate still leaves 19 failures a day that nobody sees, and the sample looks clean.

**The one idea it teaches**
- Evals are the builder's *stopping rule*, not a quality badge. Change the question from "did a human read it?" to "would anything have noticed?" — because a check costs the same at any volume.

**Where it pushed back (and what I did)**
- QC: a code card only filled about a fifth of its panel. Fixed it in the toolkit (the beat now sizes its type and card to the content) instead of padding the beat — the arithmetic was correct, the panel was the defect.

**What I learned**
- Buying back missed failures by raising the sample just buys back the hours sampling was meant to save.

_Hours this week: ~20 (across the two videos built this week)._
