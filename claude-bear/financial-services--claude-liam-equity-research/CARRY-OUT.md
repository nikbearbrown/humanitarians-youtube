# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Equity-research isn't a trained analyst inside Claude — it's a written
> file of steps, and Claude only runs the steps that are written down.**

## The wrong guess it defeats

That when Claude produces an equity research snapshot, some specialized,
separately trained financial-analyst judgment is doing the work inside the
model. It isn't — `equity-research` is a Claude Skill: one file,
`SKILL.md`, written in plain language, that Claude reads before it acts.
The steps in that file — pull analyst consensus estimates, pull company
fundamentals, pull historical prices, pull macroeconomic context, assemble
a snapshot — are what actually runs, the same way for any company you name.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (written file of
steps, not trained judgment) and it also carries the boundary for free:
"only runs the steps that are written down" is why a question the file
never wrote — like whether to buy the stock — doesn't get answered, and why
a clean snapshot back doesn't mean the numbers were checked or judged.

## What it deliberately does not say

- **Not a verdict on the design.** The source's B03 framed this as "what
  it gets right: repeatable results. What it bites: anything outside the
  spec" — Teardown language, including an implicit judgment on the
  trade-off. Plain keeps the same underlying facts (repeatable because it's
  a spec; bounded to what the spec says) but states them as mechanism
  boundaries, not a critique of the skill file.
- **Not a claim about the specific numbers the skill returns.** The source
  narration never specifies an actual company, estimate, or price — neither
  does this reel. The one concrete case (research one company) is used to
  show *what runs*, not to assert *what number comes back*.
- **Not a claim that Claude in general can't reason about valuation
  questions.** The reel is explicit that a question outside this file's
  steps is uncovered by this skill, not beyond Claude's general capability
  — the boundary is the file, not the model.

---
**GATE C — signed:** ______________________  (human)
