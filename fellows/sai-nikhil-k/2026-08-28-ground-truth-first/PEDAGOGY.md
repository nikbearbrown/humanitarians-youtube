# PEDAGOGY — Ground Truth First

**GATE P.** Audio does not run until a human signs the last line of this file.
Claude must never sign it.

Reel: `claude-sai-ground-truth-first` · weekly progress · loon detector ·
week of 2026-08-28 · 8 beats · ~126s estimated.

---

## The ONE idea

**Nothing in a detector runs until the ground truth exists.**

Week one of the loon detector bought three things, and none of them was model
code: places for the material to live, a written reason for the architecture,
and the first hand-drawn labels. The reel's argument is that this ordering is
deliberate rather than slow — a detector inherits whatever its dataset believes,
so the dataset's meaning has to be settled first. The 10% mark is presented as
the cheapest moment to be strict, not as a disappointing number.

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open. "This is Sai." The week's three headlines as `output` lines. |
| B01 | THE GROUND | `ClaudeScienceChipGrid` | The thesis: four things that had to exist before training could start. |
| B02 | THE DOCUMENT | `BinaryBranch` | The real fork — read and record the architecture choice, or reach for the familiar. Resolver is the guideline doc. |
| B03 | THE BOXES | `STILL` (ken burns) | The evidence. The author's own annotated frame. |
| B04 | TEN PERCENT | `DivergentFates` | The argument for fixing the labelling standard now rather than at 80%. |
| B05 | VERDICT | `ClaudeVerdictArtifact` | One page, four bare sentences. |
| B06 | HANDOFF | `ClaudeComposerAsk` | A prompt the viewer can paste, read aloud and discussed. |
| B07 | OUTRO | `ClaudeTitleOutro` | Title restate, handle, sign-off. |

## ILLUSTRATE LAW check

Claude UI appears at **B00, B06, B07** only (B05's verdict artifact is the
permitted verdict slot). The four body beats run:

> ChipGrid → BinaryBranch → STILL → DivergentFates

No two consecutive body beats share a pattern. No body beat is a static slide
with a voiceover: B01 lands its chips in sequence, B02 forks and resolves, B03
pushes toward a subject you have to hunt for, B04 diverges into two endpoints.
Every body beat carries an ordered `show` block.

## ATTRIBUTION — the IN-FOR-BEAR LAW is suspended here

`WEEKLY-VIDEO-GUIDE.md` requires B00 to say "this is Liam, in for Bear" and the
outro to sign off the same way. **That law is deliberately suspended for this
series** (established 2026-07-31, carried forward every week since). These
weekly reels are hosted by Sai in his own name: B00 says "This is Sai," B07
signs off "Sai," the greeting slot is "Hello, Sai," and the chip is
`@HumanitariansAI`. The Kokoro voice stays `am_onyx`. This is intentional, not a
drift from the guide.

## Evidence and honesty

Full log in `SOURCES.md`. The four things a reviewer should specifically
confirm:

1. **The 10% is project-wide.** The author's phrasing was ambiguous; he was
   asked and confirmed it means the whole project. The reel says "about ten
   percent of the project" and never attaches the figure to images, footage or
   annotation.
2. **No architecture is named anywhere.** The author did not say which
   architectures his guideline document surveys, so B02 is about the act of
   choosing and recording, not about a candidate. No model, backbone, framework
   or paper is named on screen or in narration.
3. **"Two instances boxed by hand" counts one frame**, not a dataset. No image
   counts, class counts, accuracy or mAP figures appear anywhere in this reel.
4. **B04 is editorial.** The cheap-to-fix-early argument is judgment the voice
   makes, not a decision the author reported. It is phrased as reasoning
   throughout and is absent from the verdict card's list of deliverables.

## Human review checklist

- [ ] The ONE idea is the idea you actually want this week to say.
- [ ] **Repository count:** the reel says three — two footage, one code. Correct?
- [ ] B00's three `output` lines are a fair headline of the week.
- [ ] B02 does not overstate the guideline document's completeness — it says
      "started this week."
- [ ] B03's narration matches what is visibly in the frame.
- [ ] B04 reads as an argument you endorse, not as a claim about what you did.
- [ ] The 10% is stated as project-wide everywhere it appears.
- [ ] Nothing numeric appears that you did not supply.
- [ ] The handoff prompt at B06 is one you would actually want a viewer to run.
- [ ] Sign-off is "Sai," not "Liam, in for Bear."

## Rendering note (both formats)

The 16:9 master is the source of truth. The 9:16 cut is **derived** from it by
`runtime/scripts/shorts.py` — same narration, same mp3s, no re-authoring. At
~126s the reel is well under the 180s Shorts cap, so the whole thing reformats
with **no beats cut and no outro rewrite**. Every Remotion pattern used here has
a registered `*916` portrait sibling, and B03 — the only piece of user media —
is covered by a hand-composed `pantry/B03-916.png` so it is never centre-cut.

---

Sign below to release audio. Leave the blank if this needs another pass.

VERDICT: PASS     — reviewer: Sai Nikhil Kunapareddy date: 08/28/2026
