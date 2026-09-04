# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Debug never jumps straight to a fix. It runs reproduce, isolate, diagnose,
> then fix — the same order every time, but only for the kinds of breakage
> it's built to recognize.**

## The wrong guess it defeats

That asking Claude to "debug" is the same request as asking it to "fix" —
a single command that returns a patch. It isn't: invoking the skill commits
Claude to a fixed session with four ordered stages, and a fix only ever
comes last, after reproduce, isolate, and diagnose have already run.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters: this is an ordered,
repeatable procedure, not an ad hoc patch, and its guarantee stops at the
edge of what it's built to recognize.

## What it deliberately does not say

- Not "Claude can debug anything." The skill only fires on its stated
  triggers — an error message or stack trace, "works in staging but not
  prod," "broke after the deploy," or unexplained divergence from expected
  behavior. Outside that list, the skill has nothing to say.
- Not a claim that reproduce/isolate/diagnose/fix is the only valid
  debugging method — it's what this specific Skill's SKILL.md specifies.
- No design judgment on whether this is the "right" way to debug — Plain
  register describes the mechanism and stops.

---
**GATE C — signed:** ______________________  (human)
