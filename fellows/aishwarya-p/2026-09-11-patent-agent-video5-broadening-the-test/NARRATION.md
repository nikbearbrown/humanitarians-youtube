# Video 5: Broadening the Test — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video covers what happened when the Claims Agent got tested on patents it had never seen before.

## B00 — Cold open
Three new patents. Mechanical, robotics, medical device. One of them came back with zero claims parsed — on a patent that had fourteen.

## B01 — The real gap
Method: every patent tested so far numbered its claims the same way — a digit, then a period, no space. The new patent used a space before the period. The regex required the period immediately after the digits, so it silently returned nothing, on real claims text that was genuinely there.

## B02 — Tracing it, verifying the fix
Pulling the raw text confirmed it: "1 ." instead of "1." One character of whitespace, one silent failure. The fix allowed optional space between the number and the period — verified against the new format, and against the original format, to make sure nothing broke that already worked.

## B03 — The real classifier results
Eight independent claims classified across four real patents in four different domains — semiconductor, mechanical, robotics, medical device — and zero refusals on this batch. Every reading came with a real, specific, checkable caveat.

## B04 — The honest open question
Every one of those eight readings came back "narrow" and "defensive." Six claims in a row, no "broad," no "offensive." That could be how these particular patents are actually drafted — or it could be the classifier's own bias toward the safer-sounding answer. Not concluded either way. Flagged, and left open for more real data.

## B05 — Handoff
Your turn. Before trusting a parser against a new patent, check that it actually returned something — a real patent with real claims coming back empty is a signal to inspect the raw text, not a signal that the patent had no claims.

## B06 — Outro
Broadening the Test. Built with Claude, for Humanitarians AI.
