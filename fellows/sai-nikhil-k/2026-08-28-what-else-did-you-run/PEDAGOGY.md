# PEDAGOGY — What Else Did You Run?

**Reel:** `weekly_updates/08-28-2/` · slug `claude-sai-what-else-did-you-run`
**Source:** "How to Lie with Data — and How to Catch It" (blog post, 2026-08-25)
**Register:** Teardown · **Host:** Sai · **Voice:** Kokoro `am_onyx`
**Formats:** 16:9 4K master + 9:16 4K Shorts cut derived from it

> GATE P. A human reads this and signs the line at the very bottom before any
> audio is generated. Claude does not sign it.

---

## The ONE idea

**A number is a claim about a procedure — and the procedure is the part that
isn't shown.**

The reel is not "data can lie." It is the narrower, more useful claim the post
actually makes: manipulation almost never touches a value. It works by choosing
rows, windows, denominators, averages, axes — each choice individually
defensible, each one sayable out loud in a meeting. So the question that
actually protects you is never "is this number real?" It is **"what else did
you run?"**

The post can prove this because the dataset is synthetic. We wrote the
data-generating process, so we know the true effect is $1,400/year. That is the
whole method, and B00 says so — with real data, ground truth is precisely the
thing you don't have, which is exactly why the tricks work in the wild.

## Why this scope, out of a 6,000-word post

The post carries twelve tricks, eleven questions, and a specification curve. A
sub-three-minute reel cannot teach twelve tricks; attempting it would produce a
list, not an argument. So the reel takes the post's own closing thesis and uses
three of its assets as evidence: the ground truth (§1), the two press releases
(§13), and the specification curve (§14). The twelve tricks appear once, as the
*menu of choices* in B04 — named as a class, not taught one by one.

What is deliberately left out: every individual trick walk-through (§2–§12), the
figures, and the "try it yourself" exercises. Those are what the post is for.
The reel's job is to make someone want to run the eleven questions.

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open. The rare version vs. the common version. Sets up the known answer. |
| B01 | THE GROUND | `ScaleComparison` | Every published claim on one log axis, against the true effect. |
| B02 | TWO PRESS RELEASES | `DivergentFates` | The narrative machine — same rows, opposite conclusions. |
| B03 | THE ONE CHOICE | `BinaryBranch` | Selection. The single fork that decides the answer. |
| B04 | THE MENU | `ClaudeScienceChipGrid` | The six degrees of freedom the twelve tricks exploit. |
| B05 | VERDICT | `ClaudeVerdictArtifact` | The specification curve, and the procedural fix. |
| B06 | HANDOFF | `ClaudeComposerAsk` | Three of the eleven questions, aimed at the viewer's own chart. |
| B07 | OUTRO | `ClaudeTitleOutro` | The thesis restated. |

## ILLUSTRATE-LAW check

- Claude UI (`ClaudeComposerAsk`) appears **only** at B00 and B06, plus the
  verdict/outro cards. ✅
- Body beats B01–B04: `ScaleComparison` → `DivergentFates` → `BinaryBranch` →
  `ClaudeScienceChipGrid`. **No two consecutive body beats share a pattern.** ✅
- Every body beat has an ordered `show` block; none would survive as a static
  slide with a voiceover. ✅

## Both-formats check (why these seven patterns)

The weekly guide's default body patterns — `ClaudeScienceLayerStack`,
`ClaudeScienceSourceFlow`, `AttritionChain` — have **no `916` sibling
registered in `Root.tsx`**, so a reel built on them cannot produce a 9:16 cut
without new Remotion code. Every pattern used here has a portrait sibling, and
each `916` schema is a re-export of its landscape schema, so one beat sheet
drives both orientations and `shorts.py` can rewire the patterns untouched.

Length is budgeted so the 9:16 is a **straight reformat, not a re-edit**:
~397 narration words ≈ 2:35–2:45, under the hard 3:00 Shorts cap. No beats are
dropped and no outro is rewritten, so both cuts carry identical content.

## Evidence and honesty

Every number is traced in `SOURCES.md`. Three things a reviewer should
specifically check:

1. **B01 shows magnitudes with the sign set aside, and says so on screen.** The
   Alliance claim is negative (participants earn $5,647 *less*), and a log axis
   cannot plot it. The slide meta states the omission and the narration says two
   of the figures point in opposite directions. If this reads as sleight of hand
   in the render, cut the Alliance item rather than soften the label — a reel
   about misleading charts cannot quietly drop a sign.
2. **`DivergentFates` renders the Program Office as `good` and the Alliance as
   `warn`.** That is the pattern's up/down layout requirement, not a judgment.
   Both packets are misleading. Confirm the narration and B05 make that
   unmistakable.
3. **Nothing was computed for the video.** No statistic appears on screen that
   is not already in the post.

The post is `draft: true` and the notebook is unpublished, so the reel names no
URL and shows no repo chip.

## Human review checklist

- [ ] The ONE idea survives: you finish the reel with "what else did you run?", not "charts lie."
- [ ] B00 makes clear the dataset is synthetic **and why that is the method**, not an apology.
- [ ] B01's six labels are legible at 4K and the terracotta TRUTH marker reads as the anchor.
- [ ] B02 does not appear to endorse either press release.
- [ ] B03's resolver lands: more data does not fix the wrong comparison.
- [ ] B05's four lines are bare sentences, and the interval genuinely covers $1,400.
- [ ] B06's prompt is something a viewer could actually paste and use tomorrow.
- [ ] Total runtime is under 3:00 so the Shorts cut needs no beats dropped.
- [ ] No number on screen is absent from `SOURCES.md`.

---

Sign below only when every box above is checked. Write the word PASS in the
blank to unlock audio generation.

VERDICT: PASS   — reviewer: Sai Nikhil Kunapareddy  date: 08/28/2026
