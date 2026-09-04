# Claude, Jira API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:40.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude can set a ticket's status directly, like dragging a card on a board. It can't — status moves through a transition, an ID Claude looks up first. What does that look like?" | BrutalistHesitantWriter — types "Claude must just set the ticket's status to Done to close it out.", corrects "set" → "transition" |
| B01 | 1 stakes / 2 wrong guess, falsified | Ask Claude to move a ticket to Done, and it can't just write that value — Jira has no direct status field to set. It first lists the issue's available transitions, matches the one named Done, and posts that transition's ID. And that ID isn't universal: the same-looking transition on a different ticket, in a different workflow, often carries a different ID. | a direct status-write guess struck through; the real path opens — list transitions, match by name, post by ID; the same ID fails on a second ticket |
| B02 | 3 mechanism / **4 anchor planted** | Two families split the work: Platform REST v3 handles issues, projects, and search — the default — while Agile REST v1 only covers boards and sprints, concepts the core issue model doesn't have. Say Claude searches PROJ for every open bug assigned to you: that search has to be bounded — at least one filter clause, or it's rejected — and it comes back a page at a time, a token pointing to the next page instead of a total count. Comment on the top result, and that comment can't be a plain string: it has to be a JSON tree — a doc, versioned, built from typed content blocks — or Jira sends back a 400. | THE ANCHOR — two API families; the bounded-search request traced through nextPageToken pagination, then the ADF comment |
| B03 | **4 anchor payoff / 5 both directions** | Get it right, and the loop stops the moment the token disappears — no total needed — and the comment posts clean as a typed JSON tree, not a sentence. Get it wrong, and it fails quietly two different ways: a loop written to expect a total from search never gets one, and can spin forever waiting; a comment sent as a plain string comes back a 400, but the error never mentions ADF, so it just looks broken. One more habit worth carrying: assignees and watchers take an account ID, never an email — Jira stopped accepting email lookups years ago. | THE ANCHOR RETURNS — pagination completing cleanly and the ADF comment posting, then the same request silently spinning or 400ing; accountId flagged |
| **BCRY** | **6 carry-out** | Every Jira write Claude makes turns on two habits — a transition ID instead of a status you set, and a JSON tree instead of a string you type — get those right, and the three pagination schemes are the only thing left to watch for. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Find all open bugs in PROJ assigned to me, then move the highest-priority one to In Progress and add a comment explaining why. Watch three things: does it list the issue's transitions and post by ID instead of trying to set status directly, does it send the comment as a JSON tree instead of a plain string, and does it keep paging through search results by token instead of stopping when it doesn't see a total. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Jira API. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the transition fact and falsifies the direct-write guess; the two-API-family and pagination mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (Claude sets status directly); B01 falsifies it with a case — the same transition ID posted to a second, differently-workflowed ticket fails, which only makes sense if IDs are per-workflow lookups, not a status value |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documented facts about the jira-api skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the bounded "every open bug in PROJ assigned to me" search, traced through nextPageToken pagination and the ADF comment, then paid off complete vs. quietly wrong) |
| Both directions | B03 — get the token-based pagination and ADF body right and the request completes cleanly (holds); skip either and the loop spins forever or the comment 400s with no clue why (flips) |
| No design judgment | B03 states the accountId rule and the under-explained 400 as documented facts to watch for, never a verdict on whether Jira's API was designed well |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the same facts
  as "what it gets right" / "where it bites" — Teardown language. Plain
  keeps the facts (the transition/ADF habits, the pagination gaps) but
  states them as mechanism and documented boundaries, never a judgment on
  the skill's design quality.
- **Not that transitions and ADF are the only rules.** `createmeta`,
  the sanity-check call, the 404-vs-403 access-control quirk, and
  `maxResults` clamping are real parts of the skill; the reel picks the
  two habits that govern every write as the carry-out, not a full
  reference of every rule.
- **Not that all three pagination schemes are equally risky.** JQL
  search's missing total is the one flagged, because it's the one most
  likely to make a hand-rolled loop spin forever; the other two schemes
  (offset-based lists, nested-key comments) are real but not dramatized
  here.

## Handoff prompt (BHTF, read aloud)

> "Find all open bugs in PROJ assigned to me, then move the
> highest-priority one to In Progress and add a comment explaining why."

Why it's worth running: it forces three checks in one shot — does Claude
look up the transition ID instead of trying to set status directly, does
it send the comment as a JSON tree instead of a plain string, and does it
keep paging by token instead of expecting a total that JQL search never
sends.

---
**GATE P — signed:** ______________________  (human)
