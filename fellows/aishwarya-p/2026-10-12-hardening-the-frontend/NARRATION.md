# Video 10: Hardening the Frontend — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video covers two real improvements to last week's frontend: what happens when something goes wrong, and what happens while something is taking time.

## B00 — Cold open
A generic "Failed to fetch" error tells you nothing. Whether the backend isn't running, the publication number is wrong, or the server crashed — the original UI said the same thing every time.

## B01 — Distinct error states
Method: three real, different failures deserve three real, different messages. A 404 means the publication number format is wrong — the error now says so explicitly, with a real example. A 500 means the server itself crashed — the error now points at the API key as the likely cause. A network failure means the backend isn't reachable at all — the error now says to check if the server is running.

## B02 — Real loading states
The classify path can take several real seconds — a BigQuery fetch plus a Claude API call. The original UI just disabled the button and said "Reading...". The real improvement: a visible spinner, a contextual hint explaining why it's slow when classify is on, and disabled inputs during the fetch so nothing can be resubmitted mid-flight.

## B03 — One more honest change
Classify now defaults to off. The free path — structural claims reading plus citation lineage, no Claude API cost — is the sensible default. Classification is still one checkbox away, but opting in is now a real, deliberate choice rather than a silent default.

## B04 — Handoff
Your turn. Pick one real interaction in an app you've built and ask what happens in the three most likely failure modes — if all three give the same generic error, that's the real thing to fix first.

## B05 — Outro
Hardening the Frontend. Built with Claude, for Humanitarians AI.
