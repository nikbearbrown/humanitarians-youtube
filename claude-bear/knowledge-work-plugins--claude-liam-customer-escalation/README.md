# Claude, Customer Escalation.

Ask Claude to escalate a customer issue, and it doesn't just forward the
complaint. The real `customer-escalation` skill runs a checklist first —
what's broken, who's affected, how long, what's been tried — and checks
that against its own rules for when something actually needs to escalate
at all. Only then does it decide who the case goes to, following a fixed
tier ladder: support, engineering, product, security (which bypasses the
ladder entirely), or leadership. Even after the brief is built, Claude
doesn't send or post it on its own — it asks first. And the same checklist
can just as easily conclude that nothing gets escalated: a documented fix
stays in support.

**Topic:** SKILLS · CUSTOMER-ESCALATION
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-customer-escalation

---

## Chapters

0:00 Escalate this bug to engineering — just forward it, right?
0:11 Checklist first, no target yet
0:29 A fixed ladder, not a guess
0:57 Brief built — then it asks
1:24 Carry-out
1:33 Your turn
1:52 Outro

---

## YOUR TURN

"I have a customer issue: [describe it]. Read the customer-escalation
skill and walk me through what you'd check before deciding whether to
escalate — and don't send or post anything until I say go."

Describe a real support issue to Claude — a bug, a slow response, an
angry customer — and watch: does it build a full brief and ask before
sending or posting it, or does it just react?

---

## Deliberately not claimed

This reel's source was a Teardown-register batch build. Unlike some
`knowledge-work-plugins` siblings whose real `SKILL.md` lives only on a
separate machine, this skill's real source file IS present in this
workspace, so every mechanism claim here — the six-step workflow, the
fixed tier ladder, Security bypassing the ladder entirely, the
offer-next-steps gate, the Handle-in-Support exit — is read directly off
the real skill file, not guessed at. "API returning 500 errors
intermittently for Acme Corp" is the skill's own documented usage
example, used here as the anchor scenario — not a claim about a real
customer or incident. Not a verdict on the skill's design: the checklist
and confirm gate are stated as sequencing facts, never a critique of how
much process the skill asks for.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudeCode #Plugins #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
