# Frictional log — Vendor Intelligence update: Rate Limits, Fixed

## 2026-09-25 — weekly project-update reel (changelog), 16:9 + 9:16

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(8/12, gate PASS), `vendor-intel-ratelimit.mp4`, `short/vendor-intel-ratelimit-short.mp4`.
Source: my rate-limiting change log (collector stopped after 2 of 50 companies).
(YouTube / Drive: TBD.)

**What I was working on.** A changelog reel on six rate-limiting changes after a
collector run died after 2 of 50 companies: a token-budget pacer, a fixed retry-after
parser (2.79s matched instead of a 180s fallback), attempts 2 → 6, throttle-vs-wall at
300s, skip-one-headline instead of abort-all, and the verified run (10/10, 0 aborts).

**What I tried, and what I expected.**
* After the 236s stretch bug on the agent-harness reel, I expected running audio first
  and the Remotion render second (sequentially) to keep the timing correct.

**Where it resisted, and what I did next.**
* It mostly didn't resist — which is the point of logging a quiet build. The sequential
  render order held (final 140s matched the audio sum), the card generator already had
  the kinds I needed, and the one real friction was choosing which figures to put on
  screen vs in narration. The earlier reels' fixes paid off here.

**What Claude contributed, and what I did with it.**
* Mine: the change log (all the exact numbers), the neutral-framing choice.
* Claude's: built the reel from my log under DOUBLE-CHECK; applied the sequential render
  order; ran PROOF (8/12, the changelog floor), noting B04 (the verified run) as the
  strongest beat.

**What I understand now, and what I still do not.**
* Understood: the fixes from earlier reels (sequential render; the PIL card generator)
  turned what could have been a bumpy build into a clean one. Infrastructure compounds.
* Not resolved: the changelog teaching floor (8/12) — same genre caveat as every update.
