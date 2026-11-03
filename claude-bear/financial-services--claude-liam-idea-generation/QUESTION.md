# QUESTION.md

**Question:** Claude picked up a skill called idea-generation — does that mean
Claude itself is now creatively brainstorming new stock ideas, the way an
analyst free-associates in a pitch meeting?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-idea-generation`, a Teardown skill-explainer
under `anthropics/financial-services/`). Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json is fully filled in for
its job description and mechanism. The skill's job line survives verbatim in
the source's B00/B03/BVDT beats (with B03/BVDT truncating it mid-word to
"…thematic res." / "…quantitative s." — a template-truncation bug in the
source, not a fact to reproduce): "Systematic stock screening and investment
idea sourcing. Combines quantitative screens, thematic research, and pattern
recognition to surface new long and short ideas. Use when looking for new
ideas, running screens, or conducting thematic sweeps. Triggers on 'idea
generation', 'stock screen', 'find ideas', 'what looks interesting', 'screen
for', 'new ideas', or 'pitch me something'." The source's anatomy beat (B01)
lists exactly one real file: `SKILL.md` (3k, accented) — no second file is
ever named, so this redo does not invent one. The skill's own source file
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-
services/plugins/agent-plugins/market-researcher/skills/idea-generation/
SKILL.md`) is not reachable from this machine (confirmed via `find`) — same
class of gap documented on the `claude-liam-gl-recon` sibling redo — but
nothing here depends on reading it: the source beat_sheet.json already states
the job, the file count, the linear pipeline (read SKILL.md → execute →
return output), and the specification semantics (repeatable results, a limit
at the file's edge). The "FCF up + insider buying → 3 candidates" screen
figures in this redo are an illustrative example built to visualize the
source's own literal job line (quantitative screens, thematic research,
pattern recognition, surfacing long and short candidates) — not a claim
about any specific real screen, ticker, or account the skill has ever
processed.
