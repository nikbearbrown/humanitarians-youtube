# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **A context window is a workspace, not memory — when it fills, the session
> ends, and what carries over is whatever got written to a file and a git
> commit, not anything the agent remembers.**

## The wrong guess it defeats

That an agent picking up a long task across two sessions must "remember" where
it stopped — some continuity carried in the model or the conversation itself.
It doesn't. Session two opens with an empty context. What lets it resume
correctly is a plain external file, `feature_list.json`, holding one entry per
feature with a status of `incomplete` or `passing`, plus a git commit per
completed feature as an immutable ledger. The new session rereads the file,
finds the first entry still marked incomplete, and starts exactly there.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (progress lives in a file
and a commit log, not in the agent's memory) without smuggling in a claim about
how the feature list gets written in the first place, or how tests decide pass/fail.

## What it deliberately does not say

- Not that the agent has any persistent memory of its own — the file is
  external, and B01 states plainly that a new session is completely blank.
- Not a claim about how the initial 200-item feature list gets generated, or
  what makes a test "pass" — B04 states directly that both are out of scope.
- Not a verdict on whether this checkpoint design is the best way to do it —
  that would be a Teardown-register judgment, which this redo removes from the
  source entirely; Plain states the mechanism and stops.

---
**GATE C — signed:** ______________________  (human)
