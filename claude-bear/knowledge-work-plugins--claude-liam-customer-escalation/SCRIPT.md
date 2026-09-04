# Claude, Customer Escalation. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet — see
QUESTION.md). Register: **Plain**. 7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone tells Claude to escalate a customer bug, expecting it to just forward the complaint along. It doesn't — first it builds the case. So what actually happens before anything reaches engineering?" | BrutalistHesitantWriter — types "Escalate this bug to engineering — just forward it, right?", corrects "forward" → "package" |
| B01 | 1 stakes / 2 wrong guess, falsified / 4 anchor planted | Take a real example from the skill itself: API returning 500 errors intermittently for Acme Corp. Claude doesn't send that anywhere yet. It runs a fixed checklist first — what's broken, who's affected, how long it's been going on, what's already been tried — and checks that against its own rules for when an issue actually needs to escalate at all. | THE ANCHOR — the Acme-500-errors line types in over a checklist of four questions, each ticking off one at a time; nothing points anywhere yet |
| B02 | 3 mechanism | Only then does it decide who the case goes to — and that follows a fixed ladder, not a guess. Support escalations move up to senior support. Confirmed bugs go to engineering. Feature gaps go to product. Anything touching data exposure or access skips the ladder entirely and goes straight to security. And high-revenue churn risk, or a breached SLA on a critical account, goes to leadership. | a five-rung ladder card (Support / Engineering / Product / Security / Leadership); a marker climbs the first three rungs in order, then jumps a rung to Security, then a separate line reaches Leadership from outside the ladder |
| B03 | 4 anchor payoff / 5 both directions | Back to Acme: the brief gets built — severity, impact, exact reproduction steps — and it lands with engineering, the right tier for a confirmed bug. But even then, Claude doesn't post it or message the customer on its own — it asks first. And the same checklist can go the other way: if the fix is already documented, the issue never escalates at all — it stays in support. | THE ANCHOR RETURNS — the Acme checklist from B01, now all four checks lit, feeding a brief card that lands on the Engineering rung; a dashed "waiting on your yes" box sits over it; a second branch shows the same checklist landing on "documented fix" and stopping in a support lane, no brief at all |
| **BCRY** | **6 carry-out** | Ask Claude to escalate a customer issue, and it doesn't forward anything — it builds the full case, picks the target by fixed tier rules, and waits for you to say go. | the sentence, alone, serif, large |
| BHTF | handoff (generalized — see QUESTION.md) | Your turn. Here's the prompt — read it with me. Describe a real support issue to Claude — a bug, a slow response, an angry customer — and ask it to run the customer-escalation checklist before doing anything else. Then watch: does it build a full brief and ask before sending or posting it, or does it just react? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Customer Escalation. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the checklist and the escalate-or-not gate before B02's tier-by-tier detail |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude just forwards it); B01 falsifies it directly — a fixed checklist runs, and nothing is sent yet |
| Exactly one inference flag | none needed — every mechanism claim (the six-step workflow, the fixed tier ladder, Security bypassing the ladder, the offer-next-steps gate, the Handle-in-Support exit) is read directly off the real `SKILL.md`, verified present in this workspace; the Acme-500-errors scenario is the skill's own documented usage example, flagged in QUESTION.md/CARRY-OUT.md as illustrative, not an invented claim |
| One anchor, planted early, paid off late | B01 → B03 (the Acme 500-errors example, planted with the checklist, paid off showing the brief land on Engineering and the confirm-before-send gate) |
| Both directions | B03 — a confirmed bug follows the checklist to a brief on the Engineering tier (holds); a documented fix follows the same checklist to no escalation at all (flips whether anything gets built, not the checklist itself) |
| No design judgment | B03 states the tier choice and the confirm gate as facts about sequencing, never a verdict on whether the checklist is the right amount of process |

## Deliberately not claimed

- **Not a design verdict.** The source's B03/BVDT framed "what it gets
  right" / "where it bites" as Teardown judgment. Plain keeps the same
  underlying mechanism (checklist first, brief second, send only after a
  yes) as a sequencing fact, not a critique.
- **Not that every issue gets escalated.** The skill's own "Handle in
  Support When" criteria mean the checklist can just as easily conclude
  no escalation happens at all.
- **Not a real Acme Corp incident.** The 500-errors example is lifted
  verbatim from the skill's own documented usage examples — it is not a
  claim about an actual customer, ticket, or outcome.

## Handoff prompt (BHTF, read aloud)

> "I have a customer issue: [describe it]. Read the customer-escalation
> skill and walk me through what you'd check before deciding whether to
> escalate — and don't send or post anything until I say go."

Why it's generalized: the skill's own brief template names a support
platform, a CRM, and a project tracker as optional connected sources a
given viewer may not have wired up. The same lesson — checklist first,
brief second, confirm before anything goes out — runs on any support
issue a viewer describes, connected tools or not.

---
**GATE P — signed:** ______________________  (human)
