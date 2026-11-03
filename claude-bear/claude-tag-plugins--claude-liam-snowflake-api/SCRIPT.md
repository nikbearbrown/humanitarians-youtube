# Claude, Snowflake Api. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:15.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone submits SQL to Snowflake and expects their answer to come straight back. It doesn't — the first thing back is only a handle to check later. So what actually comes back first?" | BrutalistHesitantWriter — types "I submit SQL to Snowflake and get my answer back. Right?", corrects "answer" → "handle" |
| B01 | 1 stakes / 2 wrong guess, falsified | Submit a query to Snowflake's SQL API and the first response back is a statement handle — not rows, not an error, just a handle to check later. Submit SQL with a typo and the API still hands back a handle just the same; only polling that handle afterward reveals the statement failed — the failure never shows up in the response to the call that submitted it. | one clean query and one typo'd query both submit and both come back with a handle; only the typo'd one later flips to FAILED on a second poll |
| B02 | 3 mechanism / **4 anchor planted** | Before any query runs, Claude needs a warehouse to run it on — compute picked from what's browsable: warehouses, databases, schemas, and tables. Choose one, then submit the real question — what tables are in this schema — and the SQL API hands back exactly one thing: a statement handle. Not the table list. Just a handle to check later. | THE ANCHOR — a warehouse chosen from the browsable list, the "what tables are in this schema" query submitted, the API returns one handle and nothing else |
| B03 | **4 anchor payoff / 5 both directions** | Poll that same handle until it reaches a terminal state, then fetch the result — but it can arrive in more than one partition, so one fetch isn't always the whole answer. Reaching a terminal state isn't proof the query succeeded either; that same status can read failed instead, and only the poll ever shows it, never the original submit. A handle still shown as running isn't stuck — that's what polling is for, and it's also what you'd cancel if you needed to stop it early. The habit that carries past this one question: expect the table list in partitions, and check status before you trust any of them. | THE ANCHOR RETURNS — the same handle polled to a finished, partitioned result, beside the same handle polled to failed instead; a cancel option and a "more partitions remain" note break out to the side |
| **BCRY** | **6 carry-out** | Every Snowflake query Claude runs turns on one habit — treat the submit call as a receipt, not an answer: poll the handle to a terminal state, then fetch the result one partition at a time — get that right and a response from the SQL API stops meaning anything it doesn't. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. List the tables in a schema I have access to in Snowflake. Watch three things: does it treat the first response as a handle to check, not a finished answer, does it poll that handle to a terminal state before trusting it, and does it fetch more than one partition if the table list is long. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Snowflake Api. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the "submission, not an answer" split as an observable fact; the warehouse/browse mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (submit SQL, get the answer back); B01 falsifies it with a case — a typo'd query submits just as cleanly as a clean one, both return a handle, and only a later poll on the typo'd one flips to FAILED |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documented description of the snowflake-api skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the "what tables are in this schema" query, submitted for its handle, then polled to a terminal state and fetched in partitions) |
| Both directions | B03 — a terminal state isn't proof the query succeeded (check for failed first, holds); a handle still shown as running isn't proof it's stuck (that's what polling is for, flips) |
| No design judgment | B03 states the terminal-state/partition rules as documented facts to watch for, never a verdict on whether the API's design is good |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03 framed the same facts
  as "what it gets right" / "where it bites" — Teardown language. Plain
  keeps the one confirmed fact (submit is async; the response is a handle,
  not an answer) but states it as mechanism, never a judgment on the
  skill's design quality.
- **Not specific field names, header names, or terminal-state strings.**
  The source (a thin batch build whose `source_skill` path does not exist
  on this machine) never gets more specific than "submit statements, poll
  async handles, fetch result partitions, cancel, and browse warehouses/
  databases/schemas/tables" — this reel states exactly that shape and adds
  nothing invented beyond it.
- **Not that polling and partitioned fetching are the only rules.**
  Cancelling and browsing warehouses/databases/schemas/tables are real
  parts of the skill; the reel picks the one habit that governs every
  single query as the carry-out, not a full reference of every operation.

## Handoff prompt (BHTF, read aloud)

> "List the tables in a schema I have access to in Snowflake."

Why it's worth running: it forces three checks in one shot — does Claude
treat the first response as a handle to check rather than a finished
answer, does it poll that handle to a terminal state before trusting it,
and does it fetch more than one partition if the table list is long.

---
**GATE P — signed:** ______________________  (human)
