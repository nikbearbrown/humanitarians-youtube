# PEDAGOGY — Every Image Earns Its Place

**Reel:** `weekly_updates/08-21/` · slug `claude-sai-every-image-earns-its-place`
**Kind:** weekly progress reel (loon detector / National Loon Center · "Immer")
**Register:** Teardown · **Voice:** Kokoro `am_onyx` · **Handle:** `@HumanitariansAI`
**Cuts:** 16:9 master at 3840×2160, and a 9:16 Shorts cut at 2160×3840 derived
by `shorts.py`.

> **GATE P is unsigned.** Audio will refuse to run until a human signs the line
> at the bottom of this file. Claude must not sign it.

---

## The ONE idea

**Before you train anything, you decide what is allowed in — and you write that
decision down as code.**

All three of this week's deliverables are the same move at different scales: the
repository decides *where* an image lives, the script decides *whether* it gets
in, and the mock shows the human review step that decides whether a detection
becomes data. The reel is ordered so that the model's absence reads as a choice,
not as a gap — the closing line is "no model yet, and that is the right order."

---

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open. "This is Sai." The week's ask typed on screen; three result lines are the three deliverables. |
| B01 | ONE PLACE | `DivergentFates` | The centralized repository, as two fates of an arriving image: one door, or scattered copies. |
| B02 | GATE ONE | `BinaryBranch` | The quality half of the script — sharp enough, and close enough. Resolver: the floor is written down. |
| B03 | GATE TWO | `ClaudeScienceChipGrid` | The duplicate half, and its honest limit: exact hashing catches one of four cases. |
| B04 | THE MOCK | `STILL` (ken burns) | The Immer landing page from Lovable, and the promise printed on it. |
| B05 | THE FLOW | `STILL` (hold) | The dashboard: analyze → review → dataset, with its figures declared placeholder. |
| B06 | VERDICT | `ClaudeVerdictArtifact` | The week on one page, four bare sentences. |
| B07 | HANDOFF | `ClaudeComposerAsk` | A prompt the viewer can paste: write your own admission rule. |
| B08 | OUTRO | `ClaudeTitleOutro` | Title restate, handle, sign-off "Sai." |

---

## ILLUSTRATE LAW check

The Claude UI appears at **B00, B06, B07, B08 only**. The five body beats each
illustrate their own concept, and no two consecutive body beats share a Remotion
pattern:

`DivergentFates` → `BinaryBranch` → `ClaudeScienceChipGrid` → `STILL` → `STILL`

**The one thing to look at:** B04 and B05 are both stills. That is deliberate —
they are a two-shot walkthrough of a single artifact, which is how you would
actually show someone an app — and they are differentiated by motion (a slow
push, then a hold). If on review they feel like two slides with a voiceover
rather than one movement, the fix is to cut B05 and fold the flow description
into B04's narration, not to add a third still.

---

## Evidence and honesty

**This reel asserts no numbers.** The author confirmed at intake that he has no
real counts this week. So there is no image count, no reject rate, no dedupe
total, and no threshold value anywhere in the narration or on any beat. B02
describes the quality gate by the *kind* of check it makes — sharpness, and
resolution/altitude — because the actual threshold values were not supplied and
inventing plausible ones is exactly what the DOUBLE-CHECK LAW forbids.

**The screenshots contain fake numbers, and the reel says so.** B05's plate is a
Lovable mock showing 1,248 images analyzed, 387 loons detected, 68% annotation
progress. None of that is measured. Two independent mitigations:

1. the narration says it out loud — "every figure on this screen is a
   placeholder that Lovable filled in; none of it is measured";
2. the plate itself is captioned `MOCK DATA · EVERY FIGURE ON THIS SCREEN IS A
   PLACEHOLDER`, burned in by `make_plates.py`, so a still lifted out of the
   video still carries the disclaimer.

B04's plate is captioned `LOVABLE MOCK · USER FLOW, NOT A BUILD` for the same
reason.

**The limitation is a beat, not a footnote.** The dedupe is exact file hashing
today. That catches a re-uploaded file and nothing else. B03 is built around the
three cases it misses — burst frames, the same bird on a second pass, the same
lake minutes later — because those are the ones that leak an individual bird
across a train/test split and quietly inflate a validation score. Claiming
"deduplication: done" would have been the dishonest version of this beat.

**Attribution.** Hosted by Sai in his own name. The IN-FOR-BEAR LAW of
`WEEKLY-VIDEO-GUIDE.md` is deliberately suspended for this series (established
2026-07-31 and carried forward): B00 says "this is Sai", B08 signs off "Sai",
and the handle is `@HumanitariansAI`. The Kokoro voice remains `am_onyx`.

---

## Human review checklist

Before signing, check each of these:

- [ ] **The week is described accurately.** Three deliverables: centralized
      repository, quality + dedupe script, Lovable mock. Nothing claimed as
      finished that is still in progress — the script is described as being
      built, and its dedupe half as incomplete.
- [ ] **The quality gate is right.** Sharpness floor and resolution/altitude
      floor, and nothing else. If the script also checks loon-presence or
      exposure, it is currently *missing* from B02 and should be added.
- [ ] **The dedupe is right.** Exact file hash only. If it has since become
      perceptual or embedding-based, B03 and B06's line 3 both overstate the
      gap and must be rewritten.
- [ ] **No invented figures.** Read B02, B03 and B06 and confirm nothing
      numeric is asserted anywhere.
- [ ] **The mock is framed as a mock** in B04 and B05, both spoken and on the
      plate.
- [ ] **"Immer" and "National Loon Center" are correct** as names, and it is
      acceptable to show this mock publicly.
- [ ] **The sign-off is right** — "Sai", `@HumanitariansAI`.
- [ ] **The next-week tease is real** — B08 promises the near-duplicate work. If
      that is not actually next, change the line.

---

## Reviewer signature

Change the blank below to the word PASS to unlock audio generation.

VERDICT: PASS  — reviewer: Sai Nikhil Kunapareddy date: 08/21/2026
