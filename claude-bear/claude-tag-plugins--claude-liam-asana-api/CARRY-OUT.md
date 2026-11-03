# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Every Asana call Claude makes turns on two habits — a gid instead of a
> name, and a response unwrapped from data — get those right and the ten
> operations take care of themselves.**

## The wrong guess it defeats

That Claude manages your Asana tasks by operating the app the way you
would — opening it, clicking into a project, pressing complete. It
doesn't: Claude calls Asana's REST API directly. Every object it touches
is addressed by a `gid` (a string global ID, never a name), and every
response — read or write — arrives wrapped under a top-level `data` key.
Skip either habit and a request can look like it worked while quietly
returning the wrong task, or nothing at all.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (Claude calls an API
with two fixed conventions, not an app with none) without overstating what
those two habits guarantee.

## What it deliberately does not say

- Not a verdict on whether the Asana API skill is well designed — that's
  Teardown territory; this reel states the mechanism and stops.
- Not a claim that gid and the data envelope are the *only* things that
  matter — `opt_fields`, rate limits, and the search cap are real, but the
  carry-out compresses the two habits that govern every single call, not
  the full reference.
- Not a claim that every Asana request needs the bundled script — only
  that a hand-rolled request still owes the same two habits.

---
**GATE C — signed:** ______________________  (human)
