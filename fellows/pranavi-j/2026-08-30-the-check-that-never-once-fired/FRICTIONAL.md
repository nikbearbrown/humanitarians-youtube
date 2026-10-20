# Frictional log — The Check That Never Once Fired

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This weekly report covers a third fix in Project 29's Layer 1 hardening pass: the pipeline's `identifySource()` CFTC-detection heuristic looked correct on paper but, tested against every real, live CFTC Regulations item on build day, matched 0 of 12. It was chosen over two other open bugs (source misclassification generally, and the bigger Google News link-unwrapping project) because it had a clean, fully measured before/after across all 5 live feeds and a sharp lesson: a safeguard never tested against real input isn't protecting anything. The plan was a 9-beat, ~2-minute report with every on-screen code/query string quoted verbatim from `B2-VERIFICATION.md`, and both fact-check open items resolved before Gate P: whether "tested live today" framing was sufficient (versus a stronger claim about the pipeline's full history), and confirming no downstream incident was implied anywhere in the script.

## Where it resisted

- Unlike several sibling reels, the first full 4K render of the long-form cut came back completely clean on GATE B and GATE V (0 errors on all 9 scenes, 0 BLOCKER/0 MAJOR on the true master) — the main friction in this build was concentrated in the 9:16 Short rather than the long cut.
- The Short's portrait redesign hit real GATE B layout failures on three restacked beats: a caption running off the bottom of the frame and a header sitting exactly on the safe ceiling (both from a vertical stack sized for the wider parent frame not fitting the portrait column's tighter y-budget), a results-table header and closing caption both crossing the safe ceiling/floor for the same reason, and a code block's last lines running past the safe floor — each fixed by measuring every element's real top/bottom edges and tightening buffs rather than guessing.
- GATE V on the Short's true master found three further real defects, not the watermark artifact: a "0 MATCHES" stamp box and a CFTC-row highlight box both edge-bled past the safe x-extent (one because inner text was capped to the full safe width with no allowance for the box's own padding, the other because a highlight box was centered on an off-center table row instead of the table's true center), and a statement card underfilled the safe area — all three fixed with direct measurement.
- After the long-form cut was already built, the fellow caught a real factual overstatement on review: B01's narration claimed the classifier sat in "the same regulatory pipeline from the last two weeks," a timeframe not supported by the source material. Because this toolkit is audio-first, the correction required a full mini-rebuild chain (regenerate the one beat's audio, retime its Manim scene's wait calls, clear the stale render slot, re-render, recompile both the 16:9 and 9:16 masters, and re-run GATE V by hand on both true masters) rather than a simple text edit.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, all 9 Manim scenes for both the long-form and portrait cuts, generated Kokoro audio, ran every GATE A/B/V pass, and found and fixed the real layout and edge-bleed defects in the Short through direct measurement. The fellow approved the plan and narration before any audio generation (Gate P), and resolved both fact-check framing questions explicitly — confirming the "tested live today" wording was sufficient without an additional on-screen date caption, and confirming the script should stay scoped to classifier behavior rather than implying any specific past bad alert or report. Critically, it was the fellow's own review of the finished video — not an automated gate — that caught the one real factual error that shipped in the first cut (the unsupported "last two weeks" timeframe claim), which was then corrected end-to-end.

## Still open / understood now

- `B2-VERIFICATION.md` and `SOURCES.md` are explicit that this measures classifier behavior on a single live test, not the fellow's actual historical n8n run log — the narration deliberately avoids generalizing "never once fired" into a permanent historical claim.
- The script deliberately leaves out two related open items (21 "Unknown Source" Google News items with no reliable classification signal, and the separate Google News link-unwrapping project) as candidates for a future report.
- Two MAJOR underfill findings remain on the Short's auto-generated endcard, outside this task's scope to fix without editing the shared toolkit.
- Publishing was not authorized for either the long-form or Shorts cut as of the last BUILD-LOG entry, including after the B01 factual patch.
