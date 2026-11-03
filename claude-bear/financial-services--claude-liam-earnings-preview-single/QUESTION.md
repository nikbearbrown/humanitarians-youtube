# QUESTION.md

**Question:** Claude picked up a skill called earnings-preview-single — does
that mean Claude itself is now analyzing the numbers and forming a view on
whether a stock is a buy?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-earnings-preview-single`, a Teardown
skill-explainer under `anthropics/financial-services/`). Not a live viewer
submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** the source's beat_sheet.json IS fully filled in —
unlike the sibling `claude-for-legal` redos, there is no unfilled `>`
placeholder here. The skill's job line survives verbatim across the source's
B00/B03/BVDT beats: "Generate a concise 4-5 page equity research earnings
preview for a single company. Analyzes the most recent earnings transcript,
competitor landscape, valuation, and recent news to produce a professional
HTML report." The source's anatomy beat (B01) lists three real files:
`LICENSE` (11k), `report-template.md` (44k, accented), `SKILL.md` (36k,
accented). The skill's own source file
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-
services/plugins/partner-built/spglobal/skills/earnings-preview-beta/
SKILL.md`) is not reachable from this machine (confirmed via `ls`) — same
class of gap documented on the `claude-for-legal` sibling redos — but nothing
here depends on reading it: the source beat_sheet.json already states every
fact this redo uses. No invented detail about the report-template's internal
structure or the SKILL.md's specific instructions beyond what the source
states.
