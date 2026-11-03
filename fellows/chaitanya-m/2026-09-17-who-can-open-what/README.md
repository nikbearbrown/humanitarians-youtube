# Who Can Open What

How the Medhavi hub decides who may open which textbook: the three kinds of
people, the two ways a student gets permission, and the design idea that the
same question is asked in one place no matter who is asking.

| | |
|---|---|
| **Runtime** | 3:48.44 (228.44 s) |
| **Format** | 3840×2160 and 2160×3840, 24 fps |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 9 (B00–B08) · `ai-explainer` spine intact |
| **Brand** | `claude` · Claude fidelity palette |
| **Presenter** | Chaitanya M. |
| **Series** | Medhavi Hub — subsystem research reels |
| **GATE P** | `VERDICT: PASS`, 2026-09-17 |
| **Status** | Built · QC'd · fact-checked · **not published** |
| **Renders** | [Google Drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) |

## Through-line

One question, asked in one place, answered the same way every time.

## Beats

| Beat | Act | | Measured |
|---|---|---|---:|
| B00 | COLD OPEN | The ask: every path to permission, and where the decision is made | 15.15 s |
| B01 | SCENE 1 | The question — several different ways to end up with permission | 22.55 s |
| B02 | SCENE 2 | Three kinds of people — admin, instructor, student; and `hidden` | 36.58 s |
| B03 | SCENE 3 | Two ways in — direct grant, or through a class; and archiving | 39.76 s |
| B04 | SCENE 4 | The idea — the same question asked at two different moments | 40.04 s |
| B05 | SCENE 5 | Close — the shape of the whole rule | 22.98 s |
| B06 | VERDICT | What it gets right, and where it bites | 20.57 s |
| B07 | HANDOFF | Map every permission path; find the two that could disagree | 26.07 s |
| B08 | OUTRO | — | 4.74 s |

This is an `ai-explainer` with the spine intact — cold open → body → verdict
page → handoff → outro — unlike the two Brutalist reels that opened this series.

## Fact-check

All **fifteen** on-camera claims verified against `medhavi-hub` @ `3775687`.
**Fifteen pass.** The cleanest of the four reels so far.

The whole reel rests on one function, `lib/textbook-manager.ts:80`
`getUserAccess(userId)`, and the narration describes it accurately:

- admin → every textbook, unfiltered (`:85–89`)
- instructor → every textbook except `status === 'hidden'` (`:91–95`)
- student → `textbook_access` rows **plus** textbooks from non-archived enrolled
  classes, unioned and deduped (`:98–131`)
- archived class → filtered out by `.eq('classes.archived', false)` (`:112`), so
  its books silently stop opening, with nothing explaining why

And the central claim — same question, two moments, one answer — holds:
`generate-token/route.ts:42` and `verify/route.ts:243` both call it.

One nuance recorded in [`FACTCHECK.md`](FACTCHECK.md): the two callers reach the
same *outcome* for `hidden` books by different reasoning — `generate-token`
relies on `getUserAccess` having filtered it, `verify` uses an explicit
admin-only role test (`:231–239`). Behaviour is identical today; the guarantee
just isn't enforced by a single shared branch the way the framing implies.

## What is in this folder

**Committed** — source, checks and build inputs:

```
beat_sheet.json            every beat: narration, shot, measured duration
short/beat_sheet.json      the 9:16 cut
timings.json               the measured clock the beats were conformed to
short/timings.json         same, for the short
SOURCE-SCRIPT.md           the script this was built from
who-can-open-what.srt      subtitles, 16:9
short/…-short.srt          subtitles, 9:16
scenes/render_body.py      the body-scene renderer
scenes/make_srt.py         subtitle generation from measured word timings
pantry/B01,B04,B05-916.mp4 native portrait overrides — build inputs
qc-sheet-16x9.png          frame QC contact sheet
qc-sheet-9x16.png          portrait QC pair
README.md                  this file
FACTCHECK.md               every claim, its source, its verdict
PEDAGOGY.md                GATE P — signed, VERDICT: PASS
FRICTIONAL.md              the process log for this piece of work
description.txt            YouTube description + chapter markers
.gitignore                 renders out, build inputs in
```

**In Drive, not here** — the renders: masters, narration `mp3/`, beat `clips/`,
`media/`.

`pantry/` **is** committed, deliberately. `shorts.py`'s default centre-cut keeps
roughly a third of the frame width and destroys any two-column layout; these
portrait frames are the fix, and without them the 9:16 cut can't be reproduced
from this repo.

`timings.json` sits at the folder root rather than in `mp3/`, because `mp3/` is
an excluded *location* under the 2026-09-18 media rule and git will not descend
into an excluded directory.

## Open before publication

1. **Channel handle not confirmed.** The reel is `claude`-branded; the channel
   line needs settling before upload.
2. **Audio not listened to.** Narration was verified as text and as measured
   duration. Pacing and whether the verdict page lands are human judgments.
3. **The archived-class edge is stated but not demonstrated.** B03 and B06 both
   say a student gets no explanation when class-granted access disappears. That
   is true in the code; the reel doesn't show the failure as a viewer would
   experience it. Worth a follow-up if this becomes a series on access.
