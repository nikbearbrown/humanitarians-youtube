# Feedback: "BLIP: Noisier Data, Better Model?" — Ritik B., film 3

**Verdict:** clear-for-public **once GATE P has a human signature**. Teaching score **12/12**.
Production gate **PASS** (both orientations).

One line: this film sets out to explain a vision-language architecture and instead explains
something more useful — how to audit a model that trains on data it wrote itself — and it
gets away with the bigger claim because all four axes of its rubric are ablations the paper
already ran.

> Reviewed from the rendered frames of both masters plus `NARRATION.md`. Self-review by the
> build agent, applying the PROOF rubric to its own cut. That is a conflict of interest and
> is named as one: the punch list below is the part worth reading, not the score.

## Where it improved vs film 2 ("Visual Question Answering, Blind?")

| Criterion | Film 2 | Film 3 |
|---|---|---|
| Explicit framework | 2 — four moves, shown first | 2 — four axes, shown first, **and each axis carries the table that proves it** |
| Reusable rubric | 2 — the blind test | 2 — survives leaving the domain (applies to any self-training paper, not just VLP) |
| Worked example | 2 — one image walked | 2 — one image walked **plus the published rate on a cohort** |
| Falsifiability | 2 — the benchmark's own numbers | 2 — **two** cases: the paper's stress test, and where the thesis fails |
| Active task | 2 — four measurements | 2 — four graded axes + "name the one it skips" |
| Friction | 2 — honest architecture, broken benchmark | 2 — noisier data wins, resolved on screen not in the voice |

**Film 2's punch list, self-applied:**

1. *"B05 is the one beat still asking for trust — an illustrative softmax rather than a real
   checkpoint's output."* → **Applied.** This film has exactly one illustrative element (B04's
   two caption strings) and it is labelled in frame. Every number on every beat is from a
   published table. There is no beat where the viewer is asked to take a figure on faith.
2. *"GATE P is self-signed and needs a human."* → **Not applied — same defect, same reason.**
   The operator instructed the agent to work without check-ins, so the signature is again the
   agent's. It is flagged in `PEDAGOGY.md`, this file, the README and the PR body. **This is
   now a recurring finding, and per PROOF's own rule about recurring problems it should stop
   being re-flagged per film and become a process fix: no reel in this series gets a
   non-provisional PASS until a human has read the narration.**

## Rubric

| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | structure shown before the examples | **2** — B02 lands at ~19s, before any BLIP figure except the cold open's preview. Four numbered axes, each with its receipt in mono at the right. |
| Reusable rubric | a viewer could score a new case | **2** — GENERATE / JUDGE / DIVERSITY / ABLATE are decisions any synthetic-data pipeline makes. Nothing in the four axes is BLIP-specific. |
| Worked example | one case walked live | **2** — B04 runs CapFilt on one image and shows the verdict *drawing* through the rejected caption, then scales to the published 25% as twenty tiles with five struck. |
| Falsifiability | stress-tested against a counter-case | **2** — B05 is the paper's own test of axis 2 (share the judge's weights → 25% falls to 8%, every metric drops). B07 states where the thesis **fails**: COCO captioning CIDEr 130.1 raw vs 129.7 bootstrapped. |
| Active task | structured, not "ask Claude" | **2** — B09: quote and grade four axes on a paper of the viewer's choosing, then name the unproven one. Output lines show what PASS and FAIL look like. |
| Friction | the viewer resolves a tension | **2** — B06 shows both wings growing together before the voice explains why. The contradiction is the graphic. |
| **Total** | | **12 / 12** |

## Production gate

**Legibility —** PASS. Every figure is a counter or a bar that reaches its value as the
number is spoken, sized from `safe` rather than from px guesses. Type floor is well clear of
~24px effective at 4K.

**Sources on screen —** PASS. `ReelKit.Stage` renders the citation under the artwork on
every illustration beat, so claim and source share the frame. B08 carries its `sourceNote`
in both orientations (the 9:16 verdict scene's dropped-citation bug was fixed in film 2's
patch and holds here).

**Side-by-side —** PASS. B05 holds both columns for its whole 12.5s. B06 holds both wings.
B07 holds five bars plus the reference line for ~5s, with the exception rendered beside the
claim rather than after it.

**Honesty devices —** worth calling out separately because they are the reason a two-point
spread can be plotted at all. B06 and B07 both truncate their accuracy axis, and both
declare it: B06 in its axis label, B07 with a drawn axis strip, a break glyph and both tick
values. A truncated axis that hides its floor would make this film self-refuting.

## The problem

**The one beat that could be stronger is B04.** It is the only beat carrying an invented
element — the two caption strings. The mechanism, the verdicts and the 25% rate are all the
paper's, and the beat says on screen which part is illustrative, so this is not a gate
failure. But the paper's Figure 4 contains real accepted and rejected captions, and a version
of this beat built on two of those strings would remove the last thing the viewer has to take
on trust. Figure 4 is raster text in the PDF and was deliberately not transcribed rather than
approximated — approximating it would have been the worse failure.

## Do X next week

1. **[RESHOOT/NEW SOURCE]** Transcribe two real caption pairs from BLIP Figure 4 (one
   accepted, one rejected) and rebuild B04 on them. One beat, ~12s, and the reel's last
   illustrative element disappears. Requires reading the figure, not re-rendering.
2. **[EDIT]** Get a human GATE P signature on `NARRATION.md`. Audio is Kokoro, so a change
   costs one regeneration and a conform.
3. **[PROCESS]** Add `check_clips.py` to the series' standing gates. This build shipped a
   handoff beat whose compiled clip started *after* the prompt had finished typing — eleven
   seconds of static card under narration that reads the prompt aloud. Every frame of it was
   legible, so GATE V passed it; the defect was the wrong eleven seconds, which a frame check
   structurally cannot see. A gate that reads frames needs a companion that reads durations.
4. **[PROCESS]** Stop re-flagging the GATE P gap per film. Make it a standing precondition
   of the series: a reel is `unlisted` until a human has read its eleven lines.
5. **[EDIT]** B05's two large rejection figures sit at the left and centre while the table's
   value columns sit at the right. Aligning each figure over its own column would tie the
   headline to the evidence. Cosmetic, not a finding.
6. **[EDIT]** Consider one beat on what CapFilt does **not** fix — the filter can only reject
   what its ITM head scores as mismatched, so a fluent-but-wrong caption that matches the
   image's gist survives. There is no published number for this, so it would have to be
   framed as an open question, which is legitimate but costs runtime the 2:00 cap does not have.

## What works

The receipts column on B02. Four framework axes that each name the table that proves them
turns a rubric from four assertions into four testable claims, and it costs one mono column.
That move should become standing template for every framework beat in this series.

And B06. A butterfly chart where both wings lengthen together is the whole argument in one
shape — the viewer sees the paradox before the narration names it, which is the correct order
and the hardest thing to get right in an explainer.
