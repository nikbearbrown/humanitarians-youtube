# QUESTION.md — financial-services--claude-liam-kyc-rules

**Mode:** redo. There is no literal asked question — this reel re-registers
an existing Teardown reel (`claude-liam-kyc-rules`, a skill-teardown walk
through the Anthropic `kyc-rules` Claude Skill from the `financial-services`
book's `kyc-screener` plugin) into the Plain register for @HumanitariansAI,
per hai-simple's redo contract.

**The question this reel answers**, framed as a newcomer would ask it:

> When Claude screens a new client's file for KYC/AML risk, does it decide
> whether to accept them, or just score the file against the rules?

**The naive framing (what B00 types and corrects):** "Does Claude approve a
new client's KYC file?" — the newcomer's assumption is that Claude makes the
accept/reject call. It doesn't. `kyc-rules` only applies the firm's KYC/AML
rules grid to an already-parsed onboarding record — it assigns a risk
rating, lists every rule outcome with the rule that produced it, and flags
what's missing or worth escalating. It decides nothing; it scores and
routes. That correction ("approve" → "score") is the wrong-guess pedagogy
per WRITER LAW.

**Source facts carried over unchanged** (from
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-kyc-rules/beat_sheet.json`):
a skill is a folder Claude reads before it works, containing one file
(SKILL.md) written in plain language, no hidden logic; the instructions
live in a Steps section, executed in order, no branching unless a step
says so; `kyc-rules`'s specific job is to apply the firm's KYC/AML rules
grid to a parsed onboarding record — assign a risk rating, list every rule
outcome with the rule cited, and flag what's missing or escalation-worthy;
it runs only after `kyc-doc-parse` has already produced that parsed record;
it decides nothing, it scores and routes; same input produces the same
output every run; the skill only handles what its file specifies.
