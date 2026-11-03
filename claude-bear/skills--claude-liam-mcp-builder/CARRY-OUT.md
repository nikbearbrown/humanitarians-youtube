# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this
sentence survivable.

## The line

> **A good MCP server isn't judged by how many endpoints it covers — it's
> judged by real tasks it can prove it completes. And that proof only
> reaches as far as read-only calls, checked directly against the real
> answer.**

## The wrong guess it defeats

That building a good MCP server is mostly a coding and coverage problem —
wrap every endpoint the API offers, ship it, done. It isn't: the skill
starts with research (protocol, language, tool list) before any code, and
its own proof standard — ten evaluation questions — only directly verifies
tools that are read-only. `github_list_repos` can be checked by calling it
and comparing the answer to the real repository list. `github_create_issue`
writes real state; a task built around it can't be one of the ten the same
way, even though creating an issue is exactly the kind of thing an agent
gets asked to do.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (coverage isn't the
measure; provable task completion is, and the proof itself has a hard
edge at read-only) without overstating the source: it doesn't say
write-tools are untested, only that the read-only evaluation standard
can't verify them the same direct way.

## What it deliberately does not say

- Not a verdict on whether requiring read-only, verifiable eval questions
  is the *right* standard, or whether mcp-builder *should* have a separate
  proof path for tools that write state — Teardown territory. Plain states
  the mechanism and the asymmetry, and stops.
- Not a claim that TypeScript-over-Python is a bad recommendation — it's
  stated as the skill's own default, not judged.
- Not a full accounting of all four phases in equal depth — this reel
  compresses to the research-first mechanism and the tool-anatomy/eval
  asymmetry the anchor needs, not a recitation of the MCP Inspector step
  or every implementation detail.

---
**GATE C — signed:** ______________________  (human)
