# QUESTION.md — knowledge-work-plugins--claude-liam-compliance-check

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-compliance-check`, a skill-teardown
walk through the Anthropic `compliance-check` Claude Skill from the
`knowledge-work-plugins` book's legal plugin set) into the Plain register
for @HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude runs a compliance check on a proposed feature or initiative,
> does it clear the feature as compliant, or does it just surface what
> applies and leave the call to a person?

**The naive framing (what B00 types and corrects):** "Does Claude clear my
feature for launch?" — the newcomer's assumption is that Claude itself signs
off on the feature. It doesn't. `compliance-check` surfaces the applicable
regulations, the required approvals, and the risk areas — it decides nothing
about whether the feature ships. That correction ("clear" → "flag") is the
wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-compliance-check/beat_sheet.json`,
whose `beats[*].narration_text` served as the locked script — no SCRIPT.md
existed on the source, and its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/legal/skills/compliance-check/SKILL.md`)
is not present on this machine, same situation as the
`knowledge-work-plugins--claude-liam-audit-support` sibling; the source
sheet's own narration carries the facts needed): a skill is a folder Claude
reads before it works, containing one file (SKILL.md) written in plain
language, no hidden logic; the instructions live in a Steps section,
executed in order, no branching unless a step says so; `compliance-check`'s
specific job is to run a compliance check on a proposed action, product
feature, or business initiative, surfacing applicable regulations, required
approvals, and risk areas — used when launching a feature that touches
personal data, when marketing or product proposes something with regulatory
implications, or when the applicable approvals and jurisdictional
requirements need to be known before proceeding; same input produces the
same output every run; the skill only handles what its file specifies.
