# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **contact-research doesn't make Claude know a person. It makes Claude
> look them up, the same way every time — only when your words match what
> it was built to hear.**

## The wrong guess it defeats

That Claude already knows who a specific person is and what they're up to
right now, the same way it knows general facts, because it's a
knowledgeable general assistant. It doesn't — a contact's live signals (a
recent reply, a meeting booked, a title change, a shift in "warm lead"
status) are dated today, and nothing dated today lives in anything Claude
was trained on. The skill isn't a memory Claude checks; it's a file Claude
reads, and it only reads it when the request's words match one of the
triggers it was written for.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a skill is instructed
lookup, not recall) and it also carries the trigger-matching gotcha in the
same breath: match the words, and you get the repeatable pipeline; miss
them, and you're back to Claude answering from what it already knows, which
is the exact thing the reel opens by questioning.

## What it deliberately does not say

- **Not a verdict on the design.** The source's B03 framed the trigger spec
  as an "interesting constraint" and quoted "what it gets right" (repeatable
  results) against "what it bites" (anything outside the spec) — Teardown
  language, including an implicit judgment about the trade-off. Plain keeps
  the underlying fact (matching triggers get you the pipeline; anything else
  doesn't) but states it as a mechanism boundary, not a critique of the
  skill's design.
- **Not a claim that Claude has no general knowledge of people.** Claude
  plainly does, for public figures and well-documented ones. The reel's
  point is narrower: general knowledge is frozen at training time, and a
  contact's *current* signals are not — so a live research question needs a
  lookup step, not a memory.
- **Not that every phrasing outside the trigger list fails loudly.** The
  source doesn't describe an error state for a non-matching request; it
  simply never starts the pipeline. The reel states that as silence, not
  breakage.

---
**GATE C — signed:** ______________________  (human)
