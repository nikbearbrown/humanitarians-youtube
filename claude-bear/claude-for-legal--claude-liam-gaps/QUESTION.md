# QUESTION.md

**Question:** Claude picked up a "skill" called gaps — does that mean it can
now judge compliance risk on its own, or is that not what's going on?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-gaps`, a Teardown skill-explainer under
`anthropics/claude-for-legal/`). Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source-fidelity note:** unlike the sibling `claude-for-legal--claude-liam-
case-brief` redo (whose source beat sheet carried a literal unfilled `>`
placeholder), the `claude-liam-gaps` source beat sheet's narration DOES carry
the skill's real, specific description, verbatim, in four beats (B00, B03,
BVDT, BHTF): "Open gaps tracker — what's flagged and not yet closed. Use
when the user asks 'what gaps are open', 'gap tracker', 'remediation
status', or wants to close (--close GAP-ID) or risk-accept (--accept
GAP-ID) a tracked gap." That sentence is the real skill spec text and is
used here as-is. What is NOT reachable from this machine is the underlying
SKILL.md file itself
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/regulatory-legal/skills/gaps/SKILL.md`
— confirmed via `find` across the local `anthropics/claude-for-legal/` tree:
only `youtube/` exists locally; no `regulatory-legal/` directory). This redo
asserts nothing beyond what the source narration already states about
gaps's behavior (open a tracker, report what's flagged/unclosed, close or
risk-accept a tracked item) — no invented detail about how the file
internally decides what counts as a "gap."
