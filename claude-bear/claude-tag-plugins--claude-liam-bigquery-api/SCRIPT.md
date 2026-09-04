# Claude, BigQuery API. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude sends one API call and BigQuery hands back the rows. It doesn't — every query becomes a job, tracked and checked until it's ready. So what does that job actually look like?" | BrutalistHesitantWriter — types "Claude must just make one API call and hand back my rows. Is that it?", corrects "call" → "job" |
| B01 | 1 stakes / 2 wrong guess, falsified | Ask Claude to pull the top ten names in a public dataset and sometimes the rows come straight back — that's the synchronous mode, one request that blocks until it's done. But a slower query can't finish inside that window, so it submits instead: a job with its own ID, checked and paged until it's ready. | sync mode as one blocking call, falling through to async: a job card with an ID appears when the window runs out |
| B02 | 3 mechanism / **4 anchor planted** | That job runs inside a billing project — the project charged for the bytes scanned isn't necessarily where the data lives — and it's pinned to the location it ran in. Ask for the top ten names in California from the public names dataset, and every later check on that job has to carry the same location back, or it 404s. | THE ANCHOR — the "top 10 names, California" job traced: billing project pays, location pins it, every follow-up call carries that same location |
| B03 | **4 anchor payoff / 5 both directions** | Check that job again with the location attached and it comes back clean — but reaching `DONE` isn't proof it succeeded; the result can carry an error, so that gets checked before the rows are trusted. And a job still running isn't proof it's stuck — that's what the checking is for. One more thing worth knowing: the field name for "more pages" isn't the same everywhere — list endpoints use `nextPageToken`, but a query's own results use `pageToken` — read the wrong one and it comes back empty, silently, after page one. | THE ANCHOR RETURNS — the same job checked correctly, then DONE-but-failed flagged, then the pagination field-name split broken out as the one exception |
| **BCRY** | **6 carry-out** | Every BigQuery job Claude runs turns on two habits — carry the same location on every follow-up call, and check for an error before trusting a job marked done — get those right and both query modes take care of themselves. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Run a query against the BigQuery public dataset bigquery-public-data.usa_names.usa_1910_current and return the top five names for Texas. Watch three things: does it pass the same location on every follow-up call, does it check for an error before trusting a job marked done, and does it use the bundled script instead of a raw request that might miss a page. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, BigQuery API. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the sync/async split as an observable fact; the billing-project/location mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (one API call, rows back); B01 falsifies it with a case — a query too slow for the synchronous window has to fall through to a tracked job, which only makes sense if a call can't always finish in one round trip |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documented facts about the BigQuery API skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the "top 10 names, California" job, traced through billing project + location, then checked correctly vs. DONE-but-failed) |
| Both directions | B03 — a job marked DONE isn't proof it succeeded (check for an error first, holds); a job still running isn't proof it's stuck (that's what checking is for, flips) |
| No design judgment | B03 states the pagination field-name split as a documented fact to watch for, never a verdict on whether splitting the field name was the right call |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the same facts
  as "what it gets right" / "where it bites" — Teardown language. Plain
  keeps the facts (the two-habit rule, the pagination split) but states
  them as mechanism and a documented boundary, never a judgment on the
  skill's design quality.
- **Not that location and the error check are the only rules.** The eight
  operations, `totalRows`, and the write-heavy job types are real parts of
  the skill; the reel picks the two habits that govern every single job as
  the carry-out, not a full reference of every rule.
- **Not that every BigQuery request needs the bundled script.** Only that
  a hand-rolled request still owes the same two habits, and that
  pagination — which the script handles — is where a hand-rolled loop most
  often goes quietly wrong.

## Handoff prompt (BHTF, read aloud)

> "Run a query against the BigQuery public dataset
> bigquery-public-data.usa_names.usa_1910_current and return the top five
> names for Texas."

Why it's worth running: it forces three checks in one shot — does Claude
carry location on every follow-up call, does it check for an error before
trusting a job marked done, and does it reach for `bq_query.sh`'s pagination
instead of a single request that quietly misses rows past the first page.

---
**GATE P — signed:** ______________________  (human)
