# Frictional log — Lost in the Middle: Why More Context Doesn't Guarantee a Better Answer

*Reconstructed 2026-10-20 from this folder's BUILD-LOG.md and FACTCHECK.md.*

## What was tried and expected

This general-AI-topic explainer teaches a reusable 3-question rubric for noticing when a long-context prompt has put an important fact in a position a model is less reliable at using — the well-documented "lost in the middle" U-shaped retrieval-accuracy effect. The plan was a 9-beat explainer: a real plotted U-shaped attention-strength curve (not just asserted in narration) shown before any example, a worked example where a buried mid-document fact is missed, a falsifiability case where the identical fact repositioned near the start is reliably found, and a closing task — kept deliberately qualitative throughout, with no specific real model named or benchmarked and no fabricated percentage or statistic.

## Where it resisted

The BUILD-LOG documents fourteen distinct real issues found and fixed during this build:

- A semi-transparent decorative curve fill produced a real, hand-confirmed low-contrast failure; fixed by dropping the fill entirely and switching the curve's stroke color rather than trying to tune the wash's opacity.
- Inline document-caption labels repeatedly collided with panel edges or neighboring text across multiple beats in both aspect ratios — resolved with different strategies depending on the specific layout (moving labels into open space between panels, or dropping inline labels entirely in favor of a highlight box alone).
- One beat's label landed inside a bar shape's own fill area when placed below a curve's dip point — fixed by moving it above instead, where it cleared both the bar and the curve.
- The portrait redesign needed genuine structural changes, not just narrowing, across several beats: tags overflowing the safe width were moved inside a panel's own bounds after shortening header text; tick labels and notes needed repositioning after a first safe-area fix cascaded into a different collision; one beat's vertical budget couldn't fit a mini diagram inset alongside a closing line, resolved by dropping the inset from the portrait layout only, since the diagram's teaching job was already covered once, clearly, elsewhere; and a title/panel collision took two rounds to fix because an intermediate-sized correction still clipped on a second line of text before the real constraint (the panel, not the title) was identified.
- A frame edge-bleed defect in the portrait exec-summary card was found only by manually reconstructing the exact final-export command by hand and running the verification tool directly with full output visible — the normal error wrapper only surfaces a partial error stream and hid the real diagnostic output. The same manual-reconstruction technique then surfaced several further genuine underfill findings on both landscape and portrait beats that had been invisible through the normal review process, because the review cut's own debug overlay produces unrelated noise that masks real signal during casual inspection.
- A "cannot inspect" crash on the automated final-export verification step, on both aspect ratios, was root-caused not to a tool bug but to an exact duration mismatch: an initial manual reconstruction attempt used the wrong duration value for the export command, producing an artificially short file whose last frame landed just before a late sample point — using the pipeline's actual frame-quantized total duration instead made the crash disappear and surfaced the real (minor) underfill findings documented above.
- A stale render-cache issue recurred on every one of eleven rounds across both aspect ratios — the render pipeline doesn't detect scene-source changes, requiring a full cache-and-artifact deletion and a modification-time verification before trusting any render as current, every single time.
- The review-cut's debug timecode overlay produced the same uniform false-positive edge-bleed finding on every beat, every round, in both aspects — confirmed repeatedly as a slate-only artifact that never affected the true final export.

## What Claude contributed, what was accepted/changed/rejected

Claude (via Claude Code) authored the beat sheet, narration, and both the landscape and native-portrait Manim scenes (including new curve-plotting and document-stack visual helpers built specifically for this reel), generated Kokoro audio, and found and fixed all fourteen issues above — notably by refusing to accept an uninformative tool error message and instead manually reconstructing the exact pipeline commands to get at the real underlying diagnostic, which is what ultimately surfaced several defects the normal review workflow was masking. The fellow approved the beat sheet and narration before any audio was generated (Gate P), and in the fact-check review confirmed the entire mechanism and worked example should stay fully qualitative and generic — explicitly requiring that no beat imply the effect happens 100% of the time or to the same degree for every model, and confirming no beat drifts into citing a specific unfounded statistic.

## Still open / understood now

- This video is explicitly not a benchmark of any real model's long-context behavior, and the README notes the exact shape and severity of the effect varies by model and has shifted over time as providers have worked to mitigate it.
- Fact-check required the narration avoid implying the effect is a universal guarantee rather than a general tendency — phrased throughout as "might miss it" / "can be unreliable."
- Both masters were personally re-inspected frame-by-frame from the shipped deliverables as a final check, with no text-rendering artifacts, clipping, or low-contrast text found.
- Publishing is marked ready-for-review in the beat sheet's gate record, not approved — it requires separate fellow/PM sign-off per the toolkit's submission spec.
