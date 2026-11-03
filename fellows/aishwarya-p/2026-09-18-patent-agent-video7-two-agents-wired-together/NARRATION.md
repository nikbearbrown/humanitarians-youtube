# Video 7: The Two Agents, Wired Together — Extended Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video covers two real things: testing the Lineage Agent on patents it had never seen, and building the first real interface that runs both agents together.

## B00 — Cold open
Three citations on one patent. Two hundred and forty-two on another. The same parser, the same code, handling both without changing a line.

## B01 — Where the Lineage Agent actually started
Method: the Lineage Agent's first real test found a real bug — BigQuery returns empty strings, not null, for a missing citation field. A check written to look for a missing value never actually fired, because the value it was checking for genuinely never occurred. Fixed, and verified against the one patent that exposed it. But one patent is a small sample.

## B02 — Broadening the test, on purpose
Two new, deliberately different real patents this time, chosen specifically to stress a different part of the same logic: OpenAI's, and Shopify's — different domains, different real citation profiles than the original plant-biology filing.

## B03 — What the broader test actually found
OpenAI's patent came back with twenty citations, eighteen of them real patents — the opposite mix of the first one tested. It also included real citations from China and the WIPO international filing system, formats the parser had never been specifically built to handle, and it got every one right anyway. Shopify's patent came back with just three citations, the smallest count seen yet. One real, honest quirk turned up too: the same reissued patent showed up as two separate citation entries under two different kind codes — a real feature of how patent reissues get recorded, not a parsing bug.

## B04 — Wiring the two agents together
The real next step: one script, one real patent number in, both agents run, one combined answer out. Structural claims reading, citation lineage, and — if you want it — the actual scope classification, all in a single call. A flag to skip classification entirely keeps the common case free, since the BigQuery lookup costs nothing on a cached patent, but a fresh Claude call always costs something real, however small.

## B05 — Watching it run for real
This is the actual CLI, running against a real patent — one one one nine seven nine five two — live. Seventeen claims. One independent. Two hundred and forty-two citations, the largest this system has ever pulled, spanning seven real countries' patent office formats. No mock data. No pre-recorded output.

## B06 — Handoff
Your turn. Before trusting a script that wires two systems together, run it against something you've already verified by hand — if the combined output doesn't match what each piece gave you separately, that's the bug to chase first.

## B07 — Outro
The Two Agents, Wired Together. Built with Claude, for Humanitarians AI.
