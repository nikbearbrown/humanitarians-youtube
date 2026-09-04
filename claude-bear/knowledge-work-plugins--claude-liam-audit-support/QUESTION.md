# QUESTION.md — knowledge-work-plugins--claude-liam-audit-support

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-audit-support`, a skill-teardown
walk through the Anthropic `audit-support` Claude Skill from the
`knowledge-work-plugins` book's finance plugin set) into the Plain register
for @HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude runs SOX 404 control testing, does it decide whether the
> company's controls pass, or does it just test the sample and write it up?

**The naive framing (what B00 types and corrects):** "Does Claude pass a
company's SOX 404 audit?" — the newcomer's assumption is that Claude renders
the audit opinion itself. It doesn't. `audit-support` only picks the sample
using the firm's sampling methodology, tests each item against the
control's stated criteria, and classifies what it finds. It decides
nothing about the company overall; it tests and writes up. That correction
("pass" → "support") is the wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-audit-support/beat_sheet.json`,
whose `beats[*].narration_text` served as the locked script — no SCRIPT.md
existed on the source, and its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/finance/skills/audit-support/SKILL.md`)
is not present on this machine, same situation as prior redo siblings; the
source sheet's own narration and its `_std/AUDIT.md` carry the facts
needed): a skill is a folder Claude reads before it works, containing one
file (SKILL.md) written in plain language, no hidden logic; the
instructions live in a Steps section, executed in order, no branching
unless a step says so; `audit-support`'s specific job is to support SOX 404
compliance with control testing methodology, sample selection, and
documentation standards — used when generating testing workpapers,
selecting audit samples, classifying control deficiencies, or preparing
for internal or external audits; same input produces the same output every
run; the skill only handles what its file specifies.
