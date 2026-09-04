# Claude, Salesforce API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:05.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone updates a Salesforce record with PATCH, gets an empty response back, and assumes it failed. It didn't — PATCH returns 204 No Content on success. So how do you tell a real failure apart?" | BrutalistHesitantWriter — types "An empty response from Salesforce means my update failed.", corrects "failed" → "worked" |
| B01 | 1 stakes / 2 wrong guess, falsified | PATCH a Salesforce record and a clean update comes back as 204, with nothing at all in the body — that emptiness is the success. Get a field name wrong instead, and the response carries a real body this time: a JSON array, with an errorCode inside it. Success stays silent. Failure always talks back — and never as a plain object. | a clean PATCH returns 204/empty; a bad-field PATCH returns a JSON array with an errorCode — same call shape, opposite bodies |
| B02 | 3 mechanism / **4 anchor planted** | Every call needs the org's own instance URL — its My Domain — plus the versioned data path; there's no shared endpoint across orgs. Before touching a field, Describe the object: field names, picklist values, and which fields are actually updateable. Query the open Opportunities closing this quarter, with Account name and owner, and pull the Id of the top match — that's the record about to change. | THE ANCHOR — instance URL + Describe confirm StageName is updateable, then the SOQL query returns the top Opportunity's Id |
| B03 | **4 anchor payoff / 5 both directions** | PATCH that Id's StageName to Closed Won, and the response comes back 204 — empty, and exactly what a successful update looks like. Chain several updates in one Composite call instead, and the outer response returning 200 doesn't mean every subrequest succeeded — each one carries its own httpStatusCode, and only checking those tells you which wrote and which didn't. A single failed subrequest doesn't undo the others either, unless allOrNone was set to true — otherwise the batch's partial writes stay. | THE ANCHOR RETURNS — the same Id's PATCH resolves 204; then a Composite batch of several PATCHes, outer 200, each subrequest's own status checked individually |
| **BCRY** | **6 carry-out** | An empty response from Salesforce isn't a failure — 204 with no body is what success looks like. Trust the status code, not the silence, and when a call carries several writes at once, check each one's own code, not just the one wrapping it. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Find all open Opportunities closing this quarter, with Account name and owner — then update the top one to Closed Won. Watch three things: does it set the org's real instance URL before making any call, does it Describe the Opportunity object to confirm StageName is updateable and Closed Won is a valid picklist value before writing, and does it check the actual status code afterward instead of treating an empty response as a failure. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Salesforce API. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the "silent success, loud failure" split as an observable fact; the instance-URL/Describe mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (empty response means failure); B01 falsifies it with a case — a clean PATCH returns 204/empty, a bad-field PATCH returns a JSON array with an errorCode, same call shape, opposite outcomes |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documented facts about the salesforce-api skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the open-Opportunities-closing-this-quarter query, Id pulled, then PATCHed to Closed Won and resolved 204) |
| Both directions | B03 — a Composite's outer 200 doesn't prove every subrequest succeeded (check each httpStatusCode, holds); one subrequest failing doesn't prove the batch was undone either (only `allOrNone: true` rolls it back, flips) |
| No design judgment | B03 states the Composite outer-200 fact and the allOrNone behavior as documented mechanism, never a verdict on whether the API's design is good |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the same facts
  as "what it gets right" / "where it bites" — Teardown language. Plain
  keeps the facts (204 means success, Composite's outer-200 caveat) but
  states them as mechanism and a documented boundary, never a judgment on
  the skill's design quality.
- **Not that status codes are the only rule.** SOQL's `FIELDS()`/`LIMIT
  200` requirement, SOSL's `-G` flag, the external-ID upsert codes (201/
  200/300), and the recycle-bin retention on DELETE are real parts of the
  skill; the reel picks the one habit that governs reading every response
  as the carry-out, not a full reference of every rule.
- **Not that every write needs Composite.** Only that the same
  "don't trust the outer result alone" habit applies the moment a call
  bundles more than one write.

## Handoff prompt (BHTF, read aloud)

> "Find all open Opportunities closing this quarter, with Account name and
> owner — then update the top one to Closed Won."

Why it's worth running: it forces three checks in one shot — does Claude
set the org's real instance URL before making any call, does it Describe
the Opportunity object to confirm `StageName` is updateable and `Closed
Won` is a valid picklist value before writing, and does it check the
actual status code afterward instead of treating an empty response as a
failure.

---
**GATE P — signed:** ______________________  (human)
