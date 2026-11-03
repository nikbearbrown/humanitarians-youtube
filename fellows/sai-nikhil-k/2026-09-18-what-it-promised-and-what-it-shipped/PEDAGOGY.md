# PEDAGOGY — What It Promised, And What It Shipped

**Reel:** `weekly_updates/09-18-1/`
**Slug:** `claude-sai-what-it-promised-and-what-it-shipped`
**Week:** 2026-09-18 · loon-detector project · hosted by Sai
**Voice:** Kokoro `am_onyx` (free, local, no account) · channel `claude-liam` · chip `@HumanitariansAI`

> **This file is the human review gate. It is UNSIGNED.** Read the narration
> below, then put the word on the signature line at the very bottom and save.
> Claude does not sign this file. Audio is generated after you do.

---

## The ONE idea

Last week's reel ended on a promise: *"real precision and recall come from the
model, before the meeting."* This week those four numbers exist — and they are
not in a notebook or a chat message. They are on a card **inside the artifact
that uses them**, in an application a colleague can install and open.

The through-line is therefore not "we shipped an app." It is **the promise being
checked**: what was owed last week, and what actually arrived. That is why the
title pairs *promised* against *shipped*, and why the reel does not end on the
good numbers — it ends on the one that is still open.

## Act structure, and what each beat has to earn

| Beat | Act | Pattern | Has to earn |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Quotes last week's promise back, then says an application exists. Cold open, "This is Sai." |
| B01 | THE BUNDLE | `ClaudeScienceChipGrid` | That it is a real installable thing, and that nothing in it reaches for a server. |
| B02 | THE APP | STILL (held plate) | That it runs. The author's own capture — the still IS the evidence. |
| B03 | THE PROMISE KEPT | `ExecutedData` | The four numbers, off the shipped card. Precision high, recall visibly short of it. |
| B04 | THE ARITHMETIC | `TypesetMath` | *Why* those two numbers are a trade — one term apart in the denominator. |
| B05 | THE FORK | `BinaryBranch` | That 0.800 recall is a decision to make, not a bug to fix. |
| B06 | VERDICT | `ClaudeVerdictArtifact` | One page: promise kept, model inside, prototype, one loon in five still unseen. |
| B07 | HANDOFF | `ClaudeComposerAsk` | A prompt a viewer can paste: ship the card with the model. |
| B08 | OUTRO | `LogoOutro` | Title restate, sign-off "Sai." |

## ILLUSTRATE-LAW check

Claude UI appears at **B00, B06, B07** only (ask, verdict artifact, handoff).
Body beats run `ChipGrid → STILL → ExecutedData → TypesetMath → BinaryBranch`.
**No two consecutive beats share a pattern.** Every body beat carries a `show`
block of ordered visual events; none would survive as a static slide with a
voiceover — B03's bars fill in sequence so the precision/recall gap is a visible
distance, and B04 sets three expressions in stages rather than all at once.

## Evidence and honesty

- **Every number on screen came out of the DMG you supplied**, not from prose
  and not from git. `loon_v1.json` (the model card inside the bundle) supplies
  precision, recall, mAP50, mAP50-95, the thresholds, the architecture and the
  training run. `Info.plist` supplies the version, bundle id and minimum OS.
  Sizes were measured locally. See `SOURCES.md` for the line-by-line map.
- **The shipped backend was actually run** rather than described: it reported
  `CPUExecutionProvider`, a 0.128 s model warm-up, and 0.124–0.143 s per
  detection over five calls. Its own `--help` says *"Loopback by default; this
  is not a network service."* That is quoted, not paraphrased, on B06.
- **One derived figure, labelled as derived.** F₁ = 0.860 is computed here from
  the card's P and R; the card does not print it. B04's note says *"ours, not the
  card's"* and the narration says *"I computed it from the two it does."*
- **The conflation this reel must never make:** the 82% and 89% in your screen
  captures are **per-image detection confidences**, not model metrics. mAP50
  being 0.894 is a coincidence. B02 speaks about 82% strictly as the score on one
  box in one photograph, and its portrait plate says so in type.
- **Kept out on your instruction:** the model card's `"spdx": "AGPL-3.0-only"`,
  inherited from Ultralytics YOLO11. No beat, no on-screen text, no narration,
  not in the description. Logged in `SOURCES.md` as an item for you to settle.
- **A claim deliberately not made:** a crop of the loon taken from your own
  screen capture was fed to the shipped backend and returned zero detections.
  That is an artifact of re-compressing an already-displayed image, not a miss by
  the model — the original photograph was not supplied. It is nowhere in the reel.
- **No teammate is named**, carried forward from 09-11-1: collaborators appear as
  "we" and "the team" only.

## The narration, in full — this is what gets voiced

**B00 · ASK** (55 words)
> Last week I told you the real numbers would come from the model itself, before
> the meeting. They did. And they are printed on a card inside an application
> that now runs on a laptop, with no server and no account. This is Sai. Here is
> what it promised, and here is what it shipped.

**B01 · THE BUNDLE** (55 words)
> So what is it? A desktop application. Eighty-four megabytes to download, a
> hundred and seventy-six once it is installed. Apple silicon, macOS ten fifteen
> and up. Inside there is a Rust shell, a Python service, the onnx runtime, and
> the detector itself — thirty-six megabytes of weights. Nothing in that list
> reaches for a server.

**B02 · THE APP** (57 words)
> And it behaves the way a field tool should. One image in. A box drawn where the
> bird is, eighty-two percent on that box, and a line underneath saying
> highlighted areas show where a loon was found. Not a score on its own — a
> place. The history page keeps the earlier checks, on your own disk.

**B03 · THE PROMISE KEPT** (51 words)
> Here is the card the promise was about. Precision, ninety-three percent — when
> it calls something a loon, it is almost always right. Recall, eighty. Mean
> average precision at fifty, eighty-nine. And the strict one, fifty through
> ninety-five, sixty-one. Four numbers, off the checkpoint itself. Not a hand
> count this time.

**B04 · THE ARITHMETIC** (60 words)
> Two of those four are a trade, and the trade has a shape. Precision divides the
> true finds by everything it called a loon. Recall divides the same true finds
> by every loon that was really there. One number balances them — the harmonic
> mean, eighty-six. The card does not print it. I computed it from the two it does.

**B05 · THE FORK** (62 words)
> But eighty percent recall has a plain meaning. One loon in five, the model says
> nothing about. And there is a dial for it in the card — confidence threshold,
> zero point two five. Drop it and you find more birds and more reed beds. Hold
> it and the misses stay. That is a decision to make, not a bug to fix.

**B06 · VERDICT** (46 words)
> So: one page. The promise is kept — four numbers, from the checkpoint, inside
> the app. The detector left the notebook and runs on a laptop. It calls itself a
> prototype on every screen. And one loon in five is still unreported. That is
> next week.

**B07 · HANDOFF** (62 words)
> Your turn. If you have a model that only works in a notebook, try this before
> you demo it again. Put it in something a colleague can open with no terminal
> and no account. Then make the build write the model's own numbers into the
> bundle. If you cannot state recall on the way out the door, it is not shipped yet.

**B08 · OUTRO** (8 words)
> What it promised, and what it shipped. Sai.

**Total: 456 words → ~140 s at am_onyx's slow end (÷3.25).** Comfortably inside
the 180 s Shorts cap for the 9:16 cut, including the endcard shorts.py appends.

## Human review checklist

- [ ] The B00 claim that last week's promise was *"before the meeting"* is a fair
      quote of what you said in 09-11-1. If the meeting already happened and the
      numbers were presented there, B00 should say so instead.
- [ ] **Precision 0.930 / recall 0.800** are the numbers you want public. They
      come from the card in the bundle, not from a run you narrated to me.
- [ ] You are content for the reel to end on **one loon in five unreported**
      rather than on the good numbers. This is the register of the series, but it
      is your call.
- [ ] B05 frames the 0.25 threshold as an open decision. If the team has already
      decided, that beat should state the decision instead of the fork.
- [ ] B05's resolver argues a missed loon costs more than a boxed reed bed,
      grounded in the app's own "review the result with your own expertise" note.
      Confirm that matches how the tool is actually meant to be used.
- [ ] "Nothing in that list reaches for a server" (B01) and the loopback quote
      (B06) are accurate for v0.1.0 and you are happy to say them on camera.
- [ ] No teammate is named anywhere.
- [ ] AGPL stays out, per your instruction this session.

Durations in `beat_sheet.json` are estimates only and are replaced by the
measured mp3 lengths. If a beat runs long, change the words and regenerate —
never hand-edit a duration.

---

VERDICT: PASS    — reviewer: SAI NIKHIL KUNAPAREDDY  date: 09-18-2026
