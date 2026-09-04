# Video 3: The Real Cost of a Query — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video covers something that doesn't usually make it into a demo: what it actually costs, in real dollars, to query a real, massive dataset — and what happens when that cost shows up mid-project.

## B00 — Cold open
Nine test runs in. One error. Your project exceeded quota for free query bytes scanned. The free tier was gone.

## B01 — The real error
Method: BigQuery gives 1 TiB of free query processing a month. Past that, it's real, billed usage — and the exact error, word for word, said to upgrade to a paid billing account to continue.

## B02 — The investigation
The first assumption was wrong: that a wildcard search was the expensive part. Checking the actual job history told a different story — an exact match on one single patent scanned 116.58 gigabytes. Same result on a repeat of that exact query: zero bytes, fully cached. The real cost wasn't the query style. It was the table itself — a hundred million rows, no clustering on the field being searched.

## B03 — Doing the real math, and paying for it
At six dollars twenty-five cents per terabyte, that's about seventy cents a lookup. Real money, so a real decision: add a billing account. Set one up, linked it to the project, and kept going — with the discipline to reuse cached results instead of re-querying blindly.

## B04 — A real dead end, checked honestly
Before spending more, a cheaper table looked promising — a third the size, with fields that looked like a pre-built dependency parser. Checking it directly: last updated 2017. It didn't cover any of the patents this project actually needed. A real, honest dead end, not a shortcut.

## B05 — The other real investment
Classifying a claim's protection scope needed real judgment, not a regex — so the Anthropic API came in too. A real key, a real per-token cost, tiny per call, but real. Real money and effort on two separate fronts, both times because the cheap option was tried first and genuinely didn't hold up.

## B06 — Handoff
Your turn. Before trusting any dataset's cost, check the actual job history — the bytes processed, the caching, the size of the table you're touching — rather than assuming based on how the query reads.

## B07 — Outro
The Real Cost of a Query. Built with Claude, for Humanitarians AI.
