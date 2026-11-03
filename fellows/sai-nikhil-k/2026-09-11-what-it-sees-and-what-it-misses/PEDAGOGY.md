# PEDAGOGY — What It Sees, And What It Misses

**Reel:** `weekly_updates/09-11-1/` · slug `claude-sai-what-it-sees-and-what-it-misses`
**Week:** 2026-09-11 · LoonNet, first iteration
**Gate:** this file is GATE P. Audio will not generate until a human signs the
line at the bottom. **Claude must never sign it.**

---

## The ONE idea

**The seven failures are not one failure.** A first detector trained on 106
images returns 19 clean frames out of 26 — a real result. The seven that fail do
so for four different reasons, and only some of those reasons are fixed by more
data. A single averaged score would hide that distinction; the reel refuses to
compute one and goes frame by frame instead.

---

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Cold open. The week's question, not its summary. Three headline result lines. |
| B01 | THE SET | `ClaudeScienceChipGrid` | What went in: 106 trained, 26 held out, four capture paths, two classes. |
| B02 | THE EVIDENCE | STILL (`media/B02.png`) | The full prediction mosaic, held. The scale range is the argument. |
| B03 | RIGHT AND WRONG | `DivergentFates` | 19 clean vs 7 defective — and the 7 split further. |
| B04 | FOUR FRAMES | STILL (`media/B04.png`) | One success, three failures, each named and sourced. |
| B05 | THE FORK | `BinaryBranch` | More data, or tune overlap first? They fix different frames. |
| B06 | THE ORDER | `ClaudeScienceChipGrid` | The seven proposed features, plus the CVAT recommendation. **16:9 only.** |
| B07 | VERDICT | `ClaudeVerdictArtifact` | One page, including the hand-audit caveat in full. |
| B08 | HANDOFF | `ClaudeComposerAsk` | A prompt the viewer can paste: sort errors by cause. |
| B09 | OUTRO | `LogoOutro` | Title restate, `@HumanitariansAI`, signed "Sai." |

---

## ILLUSTRATE LAW check

Claude UI appears at B00, B08 and the verdict/outro only. The body beats run:

```
ChipGrid → STILL → DivergentFates → STILL → BinaryBranch → ChipGrid
```

No two consecutive body beats share a pattern. ✓
Both STILL beats hold rather than pan — see `make_plates.py` for why a contact
sheet cannot take a Ken Burns push or a centre cut.

---

## Evidence and honesty

**What the author supplied.** 106 training images; approximately 26 held out
from the same repository; two YOLO prediction mosaics; three named weaknesses
(duplicate detections, one section of land read as a loon, a training set that
is too small); the note that a dedicated false-positive evaluation has not been
run and that precision/recall/accuracy are not yet available.

**What is quoted verbatim off the plates.** Every per-frame confidence value
(0.3 through 0.9) and both class names — `common loon` and `non loon` — are
printed into the supplied mosaics by the YOLO plotter itself. These are the
model's own output and are quotable as such.

**What is a hand audit, and is labelled as one.** The aggregate figures — 26
populated frames, 28 loons visible, 19 clean, 7 defective, ~26 of 28 found —
come from reading the two sheets cell by cell. They are not model metrics. B07's
fourth artifact line says so on screen, in the reel, unhedged:

> These are hand counts read off the two batch sheets — NOT a validation run.

That line is load-bearing. **Do not cut it for time.**

**A fourth weakness the author did not list.** `web_20260818_0076.jpg` shows two
loons in fog and returned no detection at all. The author reviewed this finding
and approved putting it on screen.

**A claim deliberately not made.** `web_20260818_0107.jpg` appears to show a
Black Guillemot detected as a common loon at 0.7. The identification is not
certain enough to assert, so it is counted nowhere and appears on no plate. It
is logged in `SOURCES.md` as a data-quality item for the author to check.

**No names.** No teammate is named in narration, on screen, or in these notes.
Collaborators appear as "we" and "the team". This is the author's instruction.

**No invented numbers.** No mAP, F1, IoU, epoch count, image size, batch size,
train/val ratio or confidence threshold appears anywhere. None were supplied.

---

## Human review checklist

Work through this before signing. The reel makes claims about a model that other
people will be shown.

- [ ] **106 and 26 are right.** These are the two figures the whole reel rests on.
- [ ] **19 of 26 clean matches your own read** of the two sheets. If your count
      differs, change the number — the count is Claude's, not the model's.
- [ ] **The four failure modes are fairly described**: duplicates, vegetation
      false positive, a duck called a loon at 0.3, two loons missed in fog.
- [ ] **The fog frame is fair to include** as a fourth weakness.
- [ ] **The guillemot frame is correctly left out** — or, if you have identified
      it, decide what it becomes.
- [ ] **B05's claim is right**: that double-counting is an overlap-threshold
      setting rather than a data-volume problem. This is an editorial argument
      the voice makes; it is not something you reported.
- [ ] **B06's ordering is yours** and is framed as a proposal for the meeting,
      not as a settled decision.
- [ ] **The CVAT recommendation** is stated as a recommendation.
- [ ] **No teammate is named** anywhere.
- [ ] **B07's hand-audit caveat is intact.**

---

## What happens after you sign

Audio unlocks. `generate_audio_kokoro.py` measures the real narration durations
and those become the master clock — the estimates in `beat_sheet.json` are
advisory only and are replaced. If a beat then runs long, change the words and
regenerate; never hand-edit a duration.

---

VERDICT: PASS    — reviewer: SAI NIKHIL KUNAPAREDDY  date: 09-11-2026
