# QUESTION.md — knowledge-work-plugins--claude-liam-legal-risk-assessment

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-legal-risk-assessment`, a skill-
teardown walk through the Anthropic `legal-risk-assessment` Claude Skill
from the `knowledge-work-plugins` book's legal plugin set) into the Plain
register for @HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude runs a legal risk assessment on a contract or matter, does it
> render a legal verdict on how risky it is, or does it just sort the issue
> by severity and likelihood and flag when a lawyer needs to look at it?

**The naive framing (what B00 types and corrects):** "Does Claude score my
contract's legal risk?" — the newcomer's assumption is that Claude produces
a single risk score or verdict of its own. It doesn't. `legal-risk-
assessment` classifies each issue against a severity-by-likelihood
framework and applies escalation criteria — it decides nothing about the
legal question itself. That correction ("score" → "sort") is the
wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-legal-risk-assessment/beat_sheet.json`,
whose `beats[*].narration_text` served as the locked script — no SCRIPT.md
existed on the source, and its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/legal/skills/legal-risk-assessment/SKILL.md`)
is not present on this machine, same situation as the `compliance-check`
and `audit-support` siblings; the source sheet's own narration — undamaged,
not a truncated `>` placeholder — carries the facts needed): a skill is a
folder Claude reads before it works, containing one file (SKILL.md)
written in plain language, no hidden logic; the instructions live in a
Steps section, executed in order, no branching unless a step says so;
`legal-risk-assessment`'s specific job is to assess and classify legal
risks using a severity-by-likelihood framework with escalation criteria —
used when evaluating contract risk, assessing deal exposure, classifying
issues by severity, or determining whether a matter needs senior counsel or
outside legal review; same input produces the same output every run; the
skill only handles what its file specifies.
