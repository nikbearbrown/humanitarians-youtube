# Does Claude "Approve" a KYC Packet — or Just Parse It? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-kyc-doc-parse`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone asks whether Claude approves a client's KYC packet — decides if they pass. It doesn't. Liam is here to take you through what the skill actually does: turn the packet into structured fields." | writer types "What does the skill / do with a KYC packet — / approve it?", hesitates on "approve", corrects to "parse it into fields" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that kyc-doc-parse decides whether a client passes — clears them, or flags them as risky. But the skill only extracts what's already on the page into structured fields: identity, ownership, control, source of funds, and document inventory. Feed it a packet where the beneficial-owner section is left blank, and it doesn't raise an alarm — it records that field as missing and returns the rest of the packet, parsed, exactly as instructed. | a "clear / flag" decision box, struck; a five-field extraction, lit |
| B02 | 3 mechanism / **4 anchor planted** | Here's what it actually does: read one onboarding packet, then sort what's in it into five categories — identity, ownership, control, source of funds, and document inventory. Watch the anchor: one packet's data landing in all five buckets. Nothing here judges the client; it only structures what the document says, so the rules engine downstream has something clean to screen. | THE ANCHOR — five cards (IDENTITY / OWNERSHIP / CONTROL / SOURCE OF FUNDS / DOCUMENT INVENTORY), one packet's data filling all five |
| B03 | **4 anchor payoff** / 5 both directions | The packet comes out the other side as five filled-in fields — but a full set of fields isn't a cleared client, it's captured data waiting on the rules engine to actually screen it. And a field marked missing isn't proof of fraud either — the document might simply not have been submitted yet. Complete or incomplete, the parse itself never renders the verdict. | THE ANCHOR RETURNS — the five-field set, filled; splits into "captured is not cleared" and "missing is not fraud" |
| **BCRY** | **6 carry-out** | kyc-doc-parse doesn't decide whether a client passes KYC — it turns a messy onboarding packet into five structured fields a rules engine can actually screen. A complete parse means the fields were captured, not that the client was cleared. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Take a messy document — a lease, an invoice, an onboarding form, whatever you have on hand. Ask Claude to read it and sort the information into a fixed set of categories you specify in advance. Then hand it a version with one section blank, and see whether it flags the gap as a missing field rather than guessing what was probably there. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Does Claude Approve a KYC Packet, or Just Parse It? Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "decides whether a client passes — clears them, or flags them as risky"; falsified by "feed it a packet where the beneficial-owner section is left blank, and it doesn't raise an alarm — it records that field as missing" |
| Exactly one inference flag | none needed — every claim is stated directly from the source sheet's own facts (no inference leap) |
| One anchor, planted early, paid off late | B02 -> B03 (one onboarding packet's data landing in all five field buckets: identity, ownership, control, source of funds, document inventory) |
| Both failure directions | B03: "captured is not cleared" (a complete set of fields doesn't mean the client passed) / "missing is not fraud" (a field marked missing doesn't mean the client is suspicious) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03 in
  the source framed strengths/limits as a design-tell verdict ("gets
  right: repeatable results... bites: anything outside the spec"); Plain
  keeps only the mechanism and its two failure directions, no judgment on
  the design choice itself.
- **Not a claim about any specific client, institution, or document
  format.** The anchor (one onboarding packet filling five field buckets)
  is a generic, unnamed example — no invented screen, dashboard, or output
  UI.
- **Not "the skill screens the client for you."** The whole point of the
  both-directions beat (B03) is the opposite: it structures what's on the
  page, it doesn't judge risk — that's the rules engine's job, a separate
  step the skill only feeds.
- **Not a specific claim about what the rules engine checks internally.**
  The source states only that the skill's output feeds the rules engine as
  the first step of KYC screening — the reel states that boundary without
  inventing what the rules engine examines.

## Handoff prompt (BHTF, read aloud)

> "Take a messy document — a lease, an invoice, an onboarding form,
> whatever you have on hand. Ask Claude to read it and sort the
> information into a fixed set of categories you specify in advance. Then
> hand it a version with one section blank, and see whether it flags the
> gap as a missing field rather than guessing what was probably there."

Why it's worth running: watching the parser mark a gap as missing instead
of inventing a plausible fill is the fastest way to see that structuring a
document and judging its contents are two different jobs.

---
**GATE P — signed:** ______________________ (human)
