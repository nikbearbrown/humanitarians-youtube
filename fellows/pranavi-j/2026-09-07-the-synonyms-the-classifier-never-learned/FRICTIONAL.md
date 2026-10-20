# Frictional log — The Synonyms the Classifier Never Learned

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

Fourth report in the Layer 1 hardening series: after a prior week's `dc:creator` fix, 18 real items across two Google News feeds still fell into "Unknown Source" because those feeds carry no `dc:creator` field at all. The fellow read all 18 titles by hand, split them into recoverable (missing a synonym the classifier didn't check for — "adviser," "RIA," "Reg BI") and genuinely not recoverable (no named regulator, or a regulator entirely out of scope like the UK's FCA), and added two feed-agnostic synonym checks. The plan was a 9-beat, ~2-minute report that recovered 10 of 18 (56%) with zero unexpected reclassifications, reporting the remaining 8 honestly as a deliberate, reasoned stopping point rather than an unsolved bug — with that exact framing locked by fact-check before narration.

## Where it resisted

- GATE A caught one real "shapes never change" error (only one distinct shape-state across a beat's hold) — fixed with a second real shape, the same pattern used across this fellow's other reels.
- The first full 4K render came back with six real MAJOR underfill defects — on the title card, the honest-limit beat, and the takeaway — each requiring iterative real-measurement fixes rather than one-shot guesses: a first attempt to fix the title card's underfill pushed its handle text off-frame entirely, requiring a second, smaller buff adjustment that cleared both the out-of-frame error and the underfill floor in the same pass; similarly the takeaway beat needed two rounds of font/buff increases before clearing the floor.
- Building the 9:16 Short required three genuine top/bottom-stack or one-column redesigns (a field comparison, a two-title comparison, a five-feed results table), and the portrait-aware layout checker caught three further real bugs: a closing caption running past the safe floor on two different beats, and a highlighted total number's own box padding intruding into the text above it once a strict curve check was applied.
- GATE V on the Short's true master found one beat landing exactly at the 55% canvas-fill floor — a marginal fail from float rounding — requiring one more small font/buff bump to clear it with margin.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, all 9 Manim scenes for both cuts, generated Kokoro audio, ran every GATE A/B/V pass, and found and fixed every real layout and underfill defect through direct Manim measurement rather than guesswork. The fellow drove the substance of the report itself: she did the actual investigative work of reading all 18 real titles by hand and deciding which were recoverable, and in the fact-check review she explicitly preserved the "deliberate tradeoff" framing for the remaining 8 items rather than letting it read as an open bug or implied future fix, and confirmed the "eighteen" count needed no additional on-screen date qualifier. Both the plan and narration were approved (Gate P) before any audio generation.

## Still open / understood now

- The source investigation document explicitly flags a fuzzier NLP/content-based approach to the remaining 8 unrecovered items as a candidate for a future report — an explicit tradeoff (lower confidence for more coverage) not pursued here, and the on-screen framing is fact-check-locked as "LEFT OPEN — BY DESIGN" specifically to avoid any "coming soon" implication.
- The fact-check table notes the live item count naturally drifts day to day (an earlier snapshot recorded 21, this build measured 18) and treats that as expected drift, not an error.
- Two MAJOR underfill findings remain on the Short's auto-generated endcard, outside this task's scope to fix without editing the shared toolkit.
- Publishing was not authorized for either the long-form or Shorts cut as of the last BUILD-LOG entry.
