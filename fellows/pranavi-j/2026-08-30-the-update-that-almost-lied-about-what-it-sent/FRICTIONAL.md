# Frictional log — The Update That Almost Lied About What It Sent

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This weekly report covers a continued Layer 1 hardening fix in Project 29's regulatory-intel pipeline: a "Mark email sent" Postgres node that re-derived its own copy of the high-priority rule instead of reading what the email step had actually sent, which could silently flip rows to `email_sent = TRUE` that were never actually emailed. It was chosen over two other open bugs (source misclassification, and a Google News link-unwrapping task confirmed this week to be a bigger project) for having a clean, measured before/after and a sharp general lesson. The plan was a 9-beat, ~2-minute `ai-explainer`, with every on-screen code/query string quoted verbatim from `A7-VERIFICATION.md`, and both open fact-check questions resolved before Gate P: whether to narrate the 12 affected rows as something that already happened or as a forward-looking conditional, and whether to re-verify the "12" count live at build time rather than ship the original snapshot.

## Where it resisted

- GATE A/W static pre-flight caught genuine "shapes never change" errors on three beats (only one non-text shape existing for the whole hold) — fixed each time by adding a second real shape, consistent with the pattern already established in this fellow's sibling reels.
- The first GATE B pass caught several real layout bugs before rendering into the master: an unfit SQL line overhanging its panel and crossing the border, a caption sitting past the safe-area floor, a fixed-length divider extending through text below it, and a header/count group spilling past the safe walls because its combined span was off-center. Each was fixed with real measured positioning rather than guesswork.
- GATE V's automated pass against the review cut's watermark produced the same documented false-positive edge-bleed as this fellow's prior reels; checking the true clean master directly found 10 real MAJOR underfill defects, closed with real measured font/buff/width increases (in a couple of cases redesigning sparse beats as bigger poster-style type rather than just widening gaps).
- Building the 9:16 Short surfaced a toolkit limitation: the static checker has no portrait awareness and produced a false-positive "coordinate outside the frame" on one beat, confirmed as a stub artifact (not a real defect) by importing Manim directly and measuring the actual scene's real portrait geometry — documented rather than silently suppressed. The real portrait-aware layout checker then had to be run manually, bypassing the bundled gate trio, since there was no way to skip just the one false positive.
- That manual portrait check caught four real layout bugs: a panel never repositioned off the frame origin that cascaded a whole downstream stack off the bottom of the frame; a mismatch-text line centered exactly on a divider's own y-coordinate; a floating caption tag that collided with trailing code lines the portrait redesign hadn't accounted for (fixed by dropping the tag rather than patching its position); and a text block poking past its own panel's stroke.
- The Shorts scaffolding tool defaulted to the wrong channel handle (`@nikbearbrown`) and an empty teaser on the first run — caught and fixed by re-running with the correct handle and a substantive tease line.
- Two final underfill MAJORs remained on the Short even after fixes: both tied to the toolkit's own auto-generated silent endcard, not editable without touching the shared `brutalist/` repo — flagged as a human design call, not forced or silently accepted.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, all 9 Manim scenes (and the 9 portrait re-layouts for the Short), generated Kokoro audio, ran every GATE A/W/B/V pass, diagnosed the false-positive watermark and static-checker issues, and found and fixed the real layout and underfill defects through direct measurement. The fellow made the two substantive calls flagged in the fact-check: she approved the forward-looking "would have" framing for the 12 affected rows exactly as written (rather than overclaiming that they had already been mis-marked), and she chose to re-run the live query at build time to re-verify the "12" count rather than ship the original document's snapshot as-is. Both the plan (beat selection) and narration were approved (Gate P) before any audio generation.

## Still open / understood now

- `A7-VERIFICATION.md` explicitly does not prove the 12 identified rows were ever actually mis-marked in the fellow's live hand-built n8n workflow (its run history isn't tracked against the reference `workflow.dev.json`) — the narration deliberately keeps conditional framing rather than asserting it already happened.
- The fact-check table explicitly flags that several of the 12 rows are known low-signal noise (procedural exemptive-relief orders, routine meeting notices) and the beat sheet was written to avoid implying all 12 are equally significant, naming only one unambiguous example.
- Two MAJOR underfill findings remain on the Short's auto-generated endcard, outside this task's scope to fix without editing the shared toolkit.
- Publishing was not authorized for either the long-form or Shorts cut as of the last BUILD-LOG entry.
