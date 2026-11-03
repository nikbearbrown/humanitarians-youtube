# Claude, Gl Recon.

Claude picked up a skill called gl-recon — does that mean it's now deciding
which ledger is right and fixing the books? No. It matches the general
ledger to the subledger at the trade date, position, or transaction level,
surfaces every place they disagree, and tags each disagreement with a
likely cause. Run it on a period with a known break and neither ledger
number moves — only a classified break sits between them. Say the GL shows
$104,000 for a position and the subledger shows $100,000: gl-recon flags
the $4,000 gap and tags it, say, a late trade. That makes it a matcher and
a classifier, not a fixer — the payoff is the same breaks caught the same
way, every run; the limit is that it never decides which ledger is
correct. And neither a tidy classification nor a clean reconciliation is
proof on its own: a break tagged "timing" doesn't prove it resolves itself,
and a period that reconciles clean doesn't prove nothing was wrong in it.

**Topic:** CLAUDE · SKILLS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-gl-recon

---

## Chapters

0:00 The naive framing: "Claude decides which ledger is right"
0:10 Sounds like an audit
0:18 Broken, with a case — run a known break, neither number moves
0:30 The anchor: a $4,000 break between GL and subledger
0:44 Match, surface, classify — in a fixed order
0:55 Matcher, not fixer — the payoff and the limit
1:06 The anchor returns — still open
1:16 Both directions — neither proves the other
1:30 Carry-out
1:40 Your turn
2:00 Outro

---

## YOUR TURN

Paste this into Claude: "I want to reconcile general ledger to subledger
for a trade date or period — match at the position or transaction level,
surface breaks, and classify each by likely cause. Read the gl-recon skill
and walk me through what you will do, before you do it."

Run that today, against a period you actually work with, and watch exactly
which fields it matches on before a single break gets classified.

---

## Deliberately not claimed

This reel does not describe gl-reconciler's SKILL.md internal instruction
text beyond what the source script itself states — that source file lives
in a partner plugin collection not reachable from this build. The source's
anatomy beat names exactly one file (SKILL.md, 2k), so this redo does not
invent a second one. The $104,000 / $100,000 / "late trade" figures are an
illustrative example built to visualize the source's own literal job line
(match, surface breaks, classify by likely cause) — not a claim about any
real reconciliation the skill has processed. See BUILD-LOG.md for the full
account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
