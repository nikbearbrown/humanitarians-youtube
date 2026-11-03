# Claude, Redshift API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes a 200 back from Redshift means their query worked. It doesn't — 200 only means the query began; whether it actually finished comes later. So did it really work?" | BrutalistHesitantWriter — types "A 200 from Redshift means my query worked. Right?", corrects "worked" → "began" |
| B01 | 1 stakes / 2 wrong guess, falsified | Submit a query and Redshift's Data API hands back an Id — not rows, not a result, just an Id to check later. Send SQL with a typo and ExecuteStatement still returns 200; only polling DescribeStatement later reveals Status FAILED — the failure never shows up in the response to the call that submitted it. | one clean query and one typo'd query both submit and both come back 200 + an Id; only the typo'd one later flips to FAILED on a second poll |
| B02 | 3 mechanism / **4 anchor planted** | Two things have to be set before any call: the region — baked into the endpoint hostname — and a connection target in one shape: a workgroup name for Serverless, a cluster plus a database user for provisioned access, or a secret for Secrets Manager. Set the workgroup and submit the real query — the top twenty events from the past month, grouped by name — and ExecuteStatement hands back exactly one thing: an Id. | THE ANCHOR — region + RS_TARGET set, the "top 20 events · past month" query submitted, ExecuteStatement returns one Id and nothing else |
| B03 | **4 anchor payoff / 5 both directions** | Poll that same Id with DescribeStatement until it reaches FINISHED, then check HasResultSet before calling GetStatementResult — a write statement can finish with nothing to page. But FINISHED alone doesn't mean the SQL was clean; that same field can read FAILED instead, and only DescribeStatement, never the original call, ever says so. A statement still sitting at STARTED isn't stuck either — that's what the poll loop is for. One habit that carries past this one query: decode each cell with to entries bracket zero dot value; a plain dot value silently returns nothing. | THE ANCHOR RETURNS — the same Id polled to FINISHED and paged, beside the same Id polled to FAILED instead; a decode card breaks out to the side |
| **BCRY** | **6 carry-out** | Every Redshift query Claude runs turns on two habits — poll DescribeStatement to a terminal state before ever calling GetStatementResult, and decode each cell with to entries bracket zero dot value instead of a naive dot value — get those right and a 200 from ExecuteStatement stops meaning anything it doesn't. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Query my Redshift Serverless workgroup — find the top twenty events from the past month, grouped by name. Watch three things: does it set the region and the workgroup before making any call, does it poll DescribeStatement to a terminal state before ever calling GetStatementResult, and does it read the result cells with to entries bracket zero dot value instead of a naive dot value that comes back empty. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Redshift API. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the "submission, not an answer" split as an observable fact; the region/RS_TARGET mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (a 200 means it worked); B01 falsifies it with a case — a typo'd query submits just as cleanly as a clean one, both return 200, and only a later poll on the typo'd one flips to FAILED |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documented facts about the redshift-api skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the "top 20 events, past month, grouped by name" query, submitted for its Id, then polled to a terminal state and decoded) |
| Both directions | B03 — FINISHED isn't proof the SQL succeeded (check for FAILED first, holds); a statement still at STARTED isn't proof it's stuck (that's what polling is for, flips) |
| No design judgment | B03 states the FINISHED/FAILED split and the cell-decode rule as documented facts to watch for, never a verdict on whether the API's design is good |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the same facts
  as "what it gets right" / "where it bites" — Teardown language. Plain
  keeps the facts (the two-habit rule, the cell-decode gotcha) but states
  them as mechanism and a documented boundary, never a judgment on the
  skill's design quality.
- **Not that polling and cell decoding are the only rules.** The three
  connection-target shapes, the six operations, the 3 TPS catalog cap, and
  the `ClientToken` idempotency gap are real parts of the skill; the reel
  picks the two habits that govern every single call as the carry-out, not
  a full reference of every rule.
- **Not that every Redshift request needs the bundled script.** Only that
  a hand-rolled request still owes the same two habits, and that cell
  decoding is where a hand-rolled reader most often goes quietly wrong.

## Handoff prompt (BHTF, read aloud)

> "Query my Redshift Serverless workgroup — find the top twenty events from
> the past month, grouped by name."

Why it's worth running: it forces three checks in one shot — does Claude
set the region and the workgroup before making any call, does it poll
DescribeStatement to a terminal state before ever calling
GetStatementResult, and does it decode result cells with
`to_entries[0].value` instead of a naive `.value` that comes back empty.

---
**GATE P — signed:** ______________________  (human)
