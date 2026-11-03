# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this
sentence survivable.

## The line

> **Before Claude proposes a fix, it isolates which layer actually broke —
> same order, every time, and nothing outside that list.**

## The wrong guess it defeats

That "debug it" means Claude looks at a broken Zoom integration and jumps
straight to a patch. It doesn't. `debug-zoom-integration` runs its steps in
a fixed order — checking auth, webhooks, SDK joins, MCP transport, and the
real-time media stream — and only proposes a fix once the failing layer is
actually confirmed. A fix offered before that isolation step is not what
the skill does.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still
true?*

Yes — it compresses the one distinction that matters (isolate first, fix
second, in a fixed order) without needing a second sentence.

## What it deliberately does not say

- **Not a verdict on whether isolate-then-fix is the right amount of
  process.** The source's B03/BVDT framed "what it gets right" / "what it
  bites" as a Teardown judgment. Plain keeps the same underlying mechanism
  (nothing proposed until the layer is confirmed) as a fact about
  sequencing, not a critique of the design choice.
- **Not a claim about what actually breaks in any real Zoom integration.**
  The "join button spins and never connects, and the break turns out to be
  MCP transport" scenario is this reel's own invented anchor, built to make
  the five layers and the isolate-first order visualizable — not a
  statement about what commonly fails.
- **Not that the skill covers every Zoom problem.** Outside its five named
  layers, the skill has nothing to add; the same steps just don't run.

---
**GATE C — signed:** ______________________  (human)
