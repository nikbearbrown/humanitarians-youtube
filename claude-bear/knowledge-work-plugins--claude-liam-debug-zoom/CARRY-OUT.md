# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **debug-zoom doesn't fix your Zoom integration. It isolates where it broke
> and hands you a ranked list of what to check, in order.**

## The wrong guess it defeats

That asking Claude to "debug" a broken Zoom integration means Claude goes and
fixes it. It doesn't — the skill's own stated job is to isolate the failure
point and route to the right reference, producing a ranked hypothesis list
plus verification steps. That's diagnosis handed to the person, not a repair
performed on their behalf.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (diagnosis, not repair)
and it survives being repeated because the skill's actual behavior, in every
run, is exactly this: a ranked list, not a fix.

## What it deliberately does not say

- **Not a verdict on the design.** The source's B03/BVDT framed this as
  Teardown's "what it gets right / what it bites" — a judgment on the
  skill's design. Plain keeps the same underlying facts (ranked-list output;
  scoped to five failure categories) but states them as mechanism, not a
  critique of the skill file.
- **Not that the skill covers every Zoom failure.** It's scoped to five
  named categories — auth, API, webhook, SDK, MCP. A failure outside that
  scope, or a problem that isn't actually a Zoom-integration bug, gets no
  help from this file — the reel states that as the both-directions beat,
  not an editorial complaint.
- **No invented specifics beyond what the source states.** The ranked
  order used for the anchor (secret, then tolerance, then URL) is an
  illustrative worked example built to visualize "ranked hypothesis list
  plus verification steps," not a claim about the actual skill file's
  internal ranking logic, which this redo cannot read (source_skill path is
  unavailable locally). The reel treats it as an example, never as a quote
  from the file.

---
**GATE C — signed:** ______________________  (human)
