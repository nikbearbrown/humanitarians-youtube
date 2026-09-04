# QUESTION.md — knowledge-work-plugins--claude-liam-customer-pulse-check

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-customer-pulse-check`, a
skill-teardown walk through the Anthropic `customer-pulse-check` Claude
Skill) into the Plain register for @HumanitariansAI, per hai-simple's redo
contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude runs customer-pulse-check on a pile of complaints, does it
> send the replies itself, or does it just find the pattern and draft them?

**The naive framing (what B00 types and corrects):** "Does Claude send
replies to unhappy customers?" — the newcomer's assumption is that Claude
resolves the complaints itself, end to end. It doesn't. `customer-pulse-check`
synthesizes themes from PayPal disputes, HubSpot tickets, and review
exports into a top-3 fixable issues list with drafted response templates —
it drafts the replies, it never sends them. That correction ("send" →
"draft") is the wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-customer-pulse-check/beat_sheet.json`,
whose `beats[*].narration_text` served as the locked script — no SCRIPT.md
existed on the source, and its `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/customer-pulse-check/SKILL.md`)
is not present on this machine, same situation as prior redo siblings; the
source sheet's own narration is intact and specific — not a truncated
batch placeholder — so it carries the facts needed directly): a skill is a
folder Claude reads before it works, containing one file (SKILL.md)
written in plain language, no hidden logic; the instructions live in a
Steps section, executed in order, no branching unless a step says so;
`customer-pulse-check`'s specific job is to synthesize themes from PayPal
disputes, HubSpot tickets, and review exports into a top-3 fixable issues
list with drafted response templates, and it accepts an optional
since-date argument; same input produces the same output every run; the
skill only handles what its file specifies, including deciding which
drafted reply actually gets sent.
