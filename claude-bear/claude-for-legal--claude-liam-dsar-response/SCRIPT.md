# Claude, Dsar Response — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats
≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks what data a company holds on them, and the easy move is to check the one database with their name in it. That's not enough. The real question: which systems, under which name?" | BrutalistHesitantWriter — types "What's in\nour database\nabout them?", corrects "database" → "systems" |
| B01 | 1 stakes / 2 wrong guess, falsified | A person asks a company what personal data it holds on them, and where that shows up first is whichever system holds the obvious record — the customer database, say. Ask only that one system, and the file looks complete. But someone's data rarely lives in just one place — it scatters across support tickets, mailing lists, and old accounts a single database was never built to see. | a customer-record card, fully lit; three system chips (support tickets, mailing list, old account) slide past it, dim and disconnected, never touching it |
| B02 | 3 mechanism / **4 anchor planted** | Responding to that kind of request means searching every system that could hold a record, under every name and address the person has used — not just the one you thought of first. Follow one requester through the search: the customer database lists them under their current email. Support tickets mention them by name only, no email at all. The mailing list still has their account under an email they closed two years ago. | THE ANCHOR — three cards revealing the same requester under three different identifiers: current email / name-only / closed-out email |
| B03 | **4 anchor payoff / 5 both directions** | Search under only the current email, and the mailing-list record never turns up — it's filed under an address that's gone. The complete file needs all three, matched by name, both emails, and the ticket history. A system that returns nothing under one identifier hasn't ruled the person out — it's only ruled out that identifier. And a record that does turn up isn't automatically theirs to send: a support ticket that names a coworker too has to be cut back to their information alone before it goes out. | THE ANCHOR RETURNS — the three cards collapse into one complete file; then split into two: "no hit on one identifier ≠ no data" and "a hit ≠ ships as-is, redact the rest" |
| **BCRY** | **6 carry-out** | The response isn't complete until every system's been searched under every name and address the person has used — and what goes back is their data, and only their data. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. List every system your organization stores customer or user data in, plus every name, email, and account identifier one specific person has used. Ask: build a search checklist covering every system and identifier, and flag anywhere a shared record — like a support ticket naming someone else too — would need redacting before it goes out. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Dsar Response. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the request and the natural single-system read; the search mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (one database is enough); the B02→B03 anchor falsifies it directly — searching only the current email misses the mailing-list record entirely |
| Exactly one inference flag | none needed — the account describes the generic shape of a DSAR search-and-redact obligation, not a specific product's undocumented behavior; see QUESTION.md for why the source carried no facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (one requester, found under three different identifiers across three systems) |
| Both directions | B03 — a system returning nothing under one identifier hasn't ruled out the person, only that identifier; a record turning up isn't automatically ready to ship, since it may carry someone else's information too |
| No design judgment | B01–B03 state what a DSAR search-and-redact obligation requires and why one system alone can't answer it, never a verdict on any specific skill's or team's design choices |

## Deliberately not claimed

- **Not that every DSAR is this simple.** The reel doesn't claim redaction
  or search scope is always this clean — it states the ordinary requirement:
  search broadly, ship narrowly.
- **Not a specific Claude product feature.** Because the source sheet's
  actual facts were never written (see QUESTION.md), this script describes
  the generic mechanics of a data-subject access request rather than citing
  any particular tool's UI or output format.
- **No accusation that anyone searched carelessly.** Checking the one
  obvious system first is presented as an ordinary, understandable
  shortcut, not a failure by any named person or team.

## Handoff prompt (BHTF, read aloud)

> "List every system your organization stores customer or user data in,
> plus every name, email, and account identifier one specific person has
> used. Build a search checklist covering every system and identifier, and
> flag anywhere a shared record — like a support ticket naming someone else
> too — would need redacting before it goes out."

Why it's worth running: the exercise surfaces the same distinction the
reel is built around — a checklist that covers every identifier catches
every place a single-system search would have missed a record, or shipped
one that wasn't only the requester's.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
