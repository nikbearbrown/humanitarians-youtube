# QUESTION.md — financial-services--claude-liam-break-trace

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-break-trace`, a skill-teardown walk
through the Anthropic `break-trace` Claude Code Skill from the
`financial-services` book's `gl-reconciler` plugin) into the Plain register
for @HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude finds a break in the books — two records that should match and
> don't — does it fix the discrepancy, or just explain it?

**The naive framing (what B00 types and corrects):** "Does Claude fix a
break in the books?" — the newcomer's assumption is that Claude *resolves*
the discrepancy. It doesn't. `break-trace` only follows the audit trail back
to the original transaction or posting on each side and states what differs
and why; it runs *after* another skill (`gl-recon`) has already classified
the break, and it hands back a diagnosis, not a fix. That correction
("fix" → "trace") is the wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-break-trace/beat_sheet.json`):
a skill is a folder Claude reads before acting, containing one file
(SKILL.md) written in plain language; the instructions are steps, executed
in order, no branching unless a step says so; `break-trace`'s specific job
is root-causing a reconciliation break to its source transaction or posting
by following the audit trail back on each side and stating what differs and
why, used only after a break has already been classified; same input
produces the same output every run; the skill only handles what its file
describes.
