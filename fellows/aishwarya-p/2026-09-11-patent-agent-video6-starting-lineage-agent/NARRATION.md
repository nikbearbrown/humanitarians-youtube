# Video 6: Starting the Lineage Agent — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video covers the real start of the second agent — the one that traces a patent's citation lineage, not just its claims.

## B00 — Cold open
Twelve real citations on one patent. The summary said one patent, eleven papers. The summary was right — but only after a real bug got caught first.

## B01 — Checking the schema, for free
Method: before writing anything, check what's actually there. The citation field is a real, repeated record — publication number, application number, free text for non-patent literature, a type, a category, a filing date. Free to look at. No query cost to check a schema.

## B02 — Scoping it honestly
Two directions exist: backward, what a patent cites, and forward, who cites it back. Backward is a field on the row already being pulled. Forward means searching every other patent's citations for this one's number — a different, untested, likely expensive query. Backward first.

## B03 — The real bug
The first real test ran clean — twelve citations parsed, one patent, eleven papers. But the field that was supposed to say "this is non-patent literature" wasn't checking for empty text. It was checking for missing text. On this table, missing text isn't missing — it's an empty string. Every single citation was passing that check, whether it had a real patent number or not.

## B04 — Verifying the fix actually mattered
Fixed the check, re-ran it. Same twelve, same one, same eleven. Not because the fix did nothing — because this patent's real split genuinely was one patent citation and eleven real academic papers, verified by hand against every single line of raw text. The fix was correct. It just didn't change this particular patent's answer.

## B05 — Handoff
Your turn. Before trusting a field's absence to mean anything, check what an empty value actually looks like in real output — a missing string and an empty string are not automatically the same thing, and assuming they are can pass a bug through completely unnoticed.

## B06 — Outro
Starting the Lineage Agent. Built with Claude, for Humanitarians AI.
