# Does Claude Send Your Legal Replies, or Just Draft Them? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-legal-response`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude can answer a subpoena and send the reply itself. It can't. Liam is here to take you through what the skill actually does: draft a reply, then hold it for review." | writer types "What does the skill / do with a subpoena — / just send?", hesitates on "send", corrects to "draft it for review" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that legal-response handles the legal matter start to finish — reads the request, drafts a reply, and sends it. But the skill only works from configured templates, and it never sends anything on its own. Send it a request that doesn't fit any template — a subpoena with unusual terms, say — and it doesn't force a reply anyway. It flags the situation for escalation and stops. | a "reads → drafts → sends" pipeline, struck; a "template match → draft → hold for review" pipeline, lit |
| B02 | 3 mechanism / **4 anchor planted** | Here's what it actually does: read the SKILL.md, match the inquiry to one of its configured templates, assemble the draft, then run an escalation check before anything moves further. Watch the anchor: one data-subject request, walked step by step, landing as a held draft — not a sent reply. | THE ANCHOR — five stages (INQUIRY / TEMPLATE MATCH / DRAFT ASSEMBLED / ESCALATION CHECK / HELD FOR REVIEW), one request's data moving through all five |
| B03 | **4 anchor payoff** / 5 both directions | The request comes out the other side as a held draft — but a draft that's ready isn't a reply that's sent; a human still has to read it and decide. And a flagged escalation isn't a legal opinion either — it just means the skill declined to guess, so someone still has to write the actual response. Ready or flagged, the skill never makes the final call. | THE ANCHOR RETURNS — the five-stage pipeline, ending lit at HELD FOR REVIEW; splits into "ready is not sent" and "flagged is not answered" |
| **BCRY** | **6 carry-out** | legal-response doesn't decide how to handle a legal matter or send anything on its own — it drafts a reply from a template and holds it for human review, or flags the request when nothing fits. A finished draft means the words are ready, not that anyone approved sending it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Take a routine written request you get often — a scheduling ask, a data question, a standard vendor email. Ask Claude to draft a reply from a fixed template you give it, and to flag rather than answer if the request doesn't fit. Then send it something that clearly doesn't fit the template, and see whether it flags instead of guessing. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Does Claude Send Your Legal Replies, or Just Draft Them? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "reads the request, drafts a reply, and sends it"; falsified by "send it a request that doesn't fit any template... it flags the situation for escalation and stops" |
| Exactly one inference flag | none needed — every claim is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (one data-subject request walked through inquiry / template match / draft assembled / escalation check / held for review) |
| Both failure directions | B03: "ready is not sent" (a finished draft doesn't mean it went out) / "flagged is not answered" (an escalated request doesn't mean a human's legal question has been answered) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's BVDT in
  the source framed reliability and scope as a verdict recap ("know the
  limit: only what the file says"); Plain keeps only the mechanism and its
  two failure directions, no judgment on the design choice itself.
- **Not a claim about any specific client, law firm, or document format.**
  The anchor (one data-subject request moving through five pipeline
  stages) is a generic, unnamed example — no invented screen, dashboard,
  or output UI.
- **Not "the skill handles the legal matter for you."** The whole point of
  the both-directions beat (B03) is the opposite: it drafts from a
  template or flags for escalation — it never decides what should be said
  in an unusual case, and it never sends anything. Those stay a human's
  job.
- **Not a specific claim about what counts as an escalation trigger
  internally.** The source states only that the skill has "built-in
  escalation checks for situations that shouldn't use a templated reply" —
  the reel states that boundary without inventing the exact trigger logic.

## Handoff prompt (BHTF, read aloud)

> "Take a routine written request you get often — a scheduling ask, a data
> question, a standard vendor email. Ask Claude to draft a reply from a
> fixed template you give it, and to flag rather than answer if the
> request doesn't fit. Then send it something that clearly doesn't fit the
> template, and see whether it flags instead of guessing."

Why it's worth running: watching the drafter refuse to force a reply onto
a request that doesn't fit is the fastest way to see that assembling a
templated answer and deciding what to say about something unusual are two
different jobs.

---
**GATE P — signed:** ______________________ (human)
