# Claude, Nav Tieout.

Claude picked up a skill called nav-tieout — does that mean it's now verifying
that the fund's NAV is correct? No. It assumes the NAV pack is right, and ties
an LP statement to it: recompute the LP's capital account from the NAV
components, then flag any line that doesn't agree. Run it on a period with a
known LP-statement error and the fund's NAV components are exactly what they
were before the run — only a flagged mismatch shows up on the LP side. Say
the NAV pack puts the account at $404,000 and the LP statement shows
$400,000: nav-tieout flags the $4,000 gap and leaves it there. That makes it
a checker, not an auditor of the fund — the payoff is the same mismatch
caught the same way, every time, before the statement goes out; the limit is
that it never questions whether the NAV pack itself is right. And neither
result is proof on its own: a flagged mismatch doesn't prove the LP statement
is wrong (the NAV pack could be the one with the error), and a clean tie-out
doesn't prove the NAV was calculated correctly — it only means the two
documents agree with each other.

**Topic:** CLAUDE · SKILLS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-nav-tieout

---

## Chapters

0:00 The naive framing: "Claude verifies the NAV is correct"
0:11 Sounds like an audit of the NAV itself
0:20 Broken, with a case — run a known LP error, the NAV pack doesn't move
0:33 The anchor: a $4,000 gap between the NAV pack and the LP statement
0:47 Recompute, compare, flag — in a fixed order
1:01 Checker, not auditor — the payoff and the limit
1:13 The anchor returns — still flagged
1:26 Both directions — neither proves the other
1:44 Carry-out
1:56 Your turn
2:11 Outro

---

## YOUR TURN

Paste this into Claude: "I want to tie an LP statement to the fund's NAV
pack — recompute the LP's capital account from the NAV components and flag
any line that doesn't agree. Read the nav-tieout skill and walk me through
what you will do, before you do it."

Run that today, against a statement and NAV pack you actually work with, and
watch exactly which NAV components it recomputes from before a single line
gets flagged.

---

## Deliberately not claimed

This reel does not describe statement-auditor's SKILL.md internal
instruction text beyond what the source script itself states — that source
file lives in a partner plugin collection not reachable from this build. The
$404,000 / $400,000 / $4,000 figures are an illustrative example built to
visualize the source's own literal job line (recompute the LP's capital
account from the NAV components, flag any line that doesn't agree) — not a
claim about any real fund, LP, or account the skill has processed. See
BUILD-LOG.md for the full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
