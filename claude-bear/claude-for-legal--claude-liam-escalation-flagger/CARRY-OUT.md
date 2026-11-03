# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **A flag isn't Claude's judgment call — it's a match against criteria
> written in a file. Same match, same flag, every time; no match, no flag,
> however it looks to a person.**

## The wrong guess it defeats

That an escalation flag means Claude decided this looks risky — some
instinct or judgment call, the way a person would eyeball something and
sense trouble. It doesn't work that way. The flag fires because the input
matched a criterion written into `SKILL.md`, checked step by step like
every other line in the file. Remove that criterion from the file, and
inputs that used to trigger it stop getting flagged — nothing hidden
notices on Claude's behalf. The file decides what gets flagged, not
Claude's read of the situation.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (the flag is a match
against a written file, not a judgment call) and it also carries the
guarantee's edge in the same breath: "no match, no flag, however it looks
to a person" is true of every Claude Skill's matching logic, not just this
one.

## What it deliberately does not say

- **Not a claim about what `escalation-flagger` specifically checks for.**
  The source's own narration never actually states this (see QUESTION.md's
  "source defect" note — four of seven source beats carry an unfilled
  template placeholder where that specific content should have been, and
  the real `SKILL.md` lives on a machine this build can't reach). This
  reel states only what's generically true of any Claude Skill's matching
  mechanism, using `escalation-flagger` as the name and its plain-language
  category of behavior (checks input, flags matches for a human), not as a
  source of invented criteria or escalation targets.
- **Not a verdict on the design.** The source's B03 called this "the
  Teardown moment" and framed it as "what it gets right / what it bites" —
  Teardown language. Plain keeps the same underlying mechanism (repeatable
  inside the spec, silent outside it) but states it as a boundary, not a
  critique of whoever wrote the file.
- **No accusation that the source's broken template was concealing
  something.** It reads as an ordinary batch-build substitution bug, the
  same class already found on this family's `auto-updater` and
  `amendment-history` siblings, and the reel treats it as one.

---
**GATE C — signed:** ______________________  (human)
