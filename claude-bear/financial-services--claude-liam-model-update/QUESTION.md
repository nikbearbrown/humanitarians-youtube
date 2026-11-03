# QUESTION.md — financial-services--claude-liam-model-update

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-model-update`, a skill-teardown walk
through the Anthropic `model-update` Claude Skill from the `financial-services`
book's `earnings-reviewer` plugin) into the Plain register for
@HumanitariansAI, per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When a Claude Skill called "model update" runs, does it update Claude
> itself, or does it update a financial model with new data?

**The naive framing (what B00 types and corrects):** "Does a model update
mean Claude just got smarter?" — the newcomer's assumption is that "model
update" means Anthropic shipped a new Claude, the way "model update" reads
in most AI news. It doesn't. `model-update` is a Skill: given new data —
quarterly earnings, management guidance, macro changes, or a revised
assumption — Claude adjusts the estimates, recalculates the valuation, and
flags whatever changed enough to matter. Claude does not change. The
financial model does. That correction ("smarter" → "new numbers") is the
wrong-guess pedagogy per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-model-update/beat_sheet.json`):
a skill is a folder Claude reads before it works, containing one file
(SKILL.md) written in plain language, no hidden logic; the instructions
live in a Steps section, executed in order, no branching unless a step
says so; `model-update`'s specific job is to update financial models with
new data — quarterly earnings, management guidance, macro changes, or
revised assumptions — adjusting estimates, recalculating valuation, and
flagging material changes; it triggers on requests like "update model,"
"plug earnings," "refresh estimates," or "new guidance"; same input
produces the same output every run; the skill only handles what its file
specifies, and the investment call is not part of that file.
