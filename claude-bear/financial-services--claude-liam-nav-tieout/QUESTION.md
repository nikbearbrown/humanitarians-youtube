# QUESTION.md

**Question:** Claude picked up a skill called nav-tieout — does that mean
Claude itself is now verifying that the fund's NAV is correct?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-nav-tieout`, a Teardown skill-explainer
under `anthropics/financial-services/`). Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json is fully filled in for
its job description and mechanism — no unfilled `>` placeholder. The skill's
job line survives verbatim in the source's B00/B03/BVDT beats: "Tie an LP
statement to the fund's NAV pack — recompute the LP's capital account from
the NAV components and flag any line that doesn't agree. Use before LP
statements are distributed." The source's anatomy beat (B01) describes the
skill as one file, SKILL.md, containing "the full instruction set — plain
language, no hidden logic," read then executed in a fixed linear pipeline
(read SKILL.md → execute each step in order → return output), and its design
tell states the specification semantics: repeatable results are the payoff,
anything outside the spec is the limit. The skill's own source file
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-
services/plugins/agent-plugins/statement-auditor/skills/nav-tieout/SKILL.md`)
is not reachable from this machine (confirmed via `find`) — the same class of
gap documented on other `financial-services` sibling redos (e.g. `gl-recon`)
— but nothing here depends on reading it: the source beat_sheet.json already
states the job, the linear pipeline, and the specification semantics. The
"NAV pack $404,000 / LP statement $400,000 / flagged $4,000 gap" anchor
figures in this redo are an illustrative example built to visualize the
source's own literal job line (recompute the LP's capital account from the
NAV components, flag any line that doesn't agree) — not a claim about any
specific real fund, LP, or account the skill has ever processed.
