# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this
sentence survivable.

## The line

> **Flagging a variance isn't Claude's judgment call — it checks the
> numbers against a rule someone already wrote, the same way every
> single time.**

## The wrong guess it defeats

That "material variance" is a judgment call — the kind of read an
experienced accountant makes by feel, and that Claude is doing something
similar when it flags one. It isn't. `financial-statements` is a written
spec: a file Claude reads before it works, telling it to build the income
statement, balance sheet, and cash flow statement, compare each period to
the last, and flag what crosses a threshold the file sets — not a
judgment Claude applies on its own.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it
still true?*

Yes — it compresses the one distinction that matters (variance flagging
is a written rule Claude checks against, not accounting judgment Claude
exercises) into a sentence that doesn't overstate what the skill
guarantees.

## What it deliberately does not say

- **Not the specific threshold, GAAP line items, or output layout.** The
  source states the skill's job (three statements, period comparison,
  variance analysis, GAAP presentation lookups) but never the exact
  numeric threshold for "material" or the precise output format. No local
  copy of `financial-statements`'s `SKILL.md` exists on this machine to
  recover that level of detail. This reel does not invent it.
- **Not a verdict on whether this design is good.** That's Teardown
  territory; this reel states the mechanism and stops.
- **Not that every skill's judgment calls are this simple in practice.**
  Only that the mechanism — read the file, run the steps in order, check
  against a written rule, same input same output — is what every Agent
  Skill guarantees, regardless of how elaborate its Steps section gets.

## Why no ONE-FLAG beat

Every claim in this reel is the source's own confirmed statement about
how the skill works: a folder/file Claude reads, not a judgment module;
the documented job (three statements, comparison, variance analysis, use
cases); linear step execution; same-input-same-output; the limit is only
what the file says. None of it is this reel's inference. The one thing
genuinely unconfirmed — the exact variance threshold or output format —
is never asserted, so there is nothing to flag.

---
**GATE C — signed:** ______________________  (human)
