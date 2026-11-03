# Lookup, Not Training

How the Medhavi AI tutor actually knows the textbook. Almost everyone assumes
the book was fed to a model and the model learned it. Nothing is trained: the
system searches the book at question time, hands the relevant passages to an
off-the-shelf model along with the question, and the model answers from what
it was given. An open-book exam, not a study session.

| | |
|---|---|
| **Runtime** | 3:27.18 (207.18 s) |
| **Format** | 30 fps · 16:9 and 9:16 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 14 (B00–B13) · `ai-explainer` spine intact |
| **Brand** | `claude` · `@HumanitariansAI` |
| **Presenter** | Chaitanya M. |
| **Series** | Medhavi Hub — subsystem research reels |
| **GATE P** | `VERDICT: PASS`, 2026-10-01 |
| **Status** | Built · QC'd · fact-checked · **not published** |
| **Renders** | [Google Drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) |

## Through-line

It stays correct as the book changes, it can show you where it got something,
and it costs cents instead of hundreds. That's the trade.

## Beats

| Beat | Act | | Measured |
|---|---|---|---:|
| B00 | ASK | Lookup, not training — and the guess changes how you judge the system | 14.23 s |
| B01 | THE ASSUMPTION | Nothing is trained; no training run, no model of our own | 15.02 s |
| B02 | OFF THE SHELF | OpenAI's model, rented, never knows our books | 13.50 s |
| B03 | THE SEARCH | The real sequence — search before the model sees the question | 13.33 s |
| B04 | OPEN BOOK | Question and passages sent together | 15.81 s |
| B05 | YOU CAN FIX IT | Reason one — fix the chapter, fix the tutor | 14.21 s |
| B06 | IT CAN CITE | Reason two — it can point at the section | 11.86 s |
| B07 | THE COST | Reason three — a cent per question, not hundreds a month | 13.14 s |
| B08 | THE CATCH | The index has to exist, and be current | 12.42 s |
| B09 | THE SILENT FAILURE | Stale index, confident wrong answers, no error | 15.89 s |
| B10 | CLOSE | The trade, and why it's the right one | 17.94 s |
| B11 | VERDICT | Recap on the Claude artifact page | 15.19 s |
| B12 | HANDOFF | Take the lookup-vs-training question into Claude | 30.59 s |
| B13 | OUTRO | — | 4.05 s |

## Fact-check — twelve claims, twelve pass

Verified against `medhavi-hub` @ `3775687`. The cleanest of the five reels, and
the reason is visible in the sourcing: the narration was written *from*
`docs/how-the-tutor-uses-the-textbook.md` rather than from recollection of it,
and in places it is close to verbatim.

The cost figures hold exactly — `docs/ai-models.md:46` gives "on the order of
one cent" per answer and "$300–800+/month" for a self-hosted GPU instance. The
silent-drift beat (B09) is almost word for word from `:87`.

The reel also hedges where the evidence stops: B08 says the index is rebuilt
"**by default**", and `description.txt` records why — the trigger could not be
confirmed against the book repositories' own build config, which isn't in this
repo. That is the right way to state a claim you can't close.

**Two items in [`FACTCHECK.md`](FACTCHECK.md), neither a false statement:**

1. **The primary source isn't committed.** `SOURCES.md` cites S2 as
   `docs/how-the-tutor-uses-the-textbook.md`, which carries eight of the twelve
   claims — and it is **untracked** in `medhavi-hub`. The other four citations
   resolve. So those eight claims are verified but not auditable by anyone else,
   which is the wrong gap for a reel arguing that citability is the point.
2. **"One catch" is three.** B08 covers index drift. The same document records
   two more silent failures: hybrid mode needs the OpenAI key at *build* time
   (`:91`), and changing `OPENAI_EMBEDDINGS_MODEL` breaks retrieval silently
   (`:93`). Drift is the right one to film; "one catch" just claims a
   completeness the source doesn't support.

## Process changes that landed in this build

Two things I recommended after the previous round were applied *during* this
build rather than caught at review, which is the whole point:

- **Chapters generated and validated before the description was written.**
  `description.txt` carries the provenance in its build-notes footer: the
  `chapters.py` run on 2026-10-01 after audio lock, against measured
  `actual_duration_s`, with all six rules passing — 13 chapters, shortest
  11.86 s. B13's 4.05 s outro was merged forward into B12, because one sub-10 s
  chapter silently disables the entire list.
- **Frame QC sampled at t=0.** [`qc-sheet-t0.png`](qc-sheet-t0.png) exists
  because the previous reel's QC missed a 7.5 s empty opening by sampling only
  at 55% and 92% of each beat.

One gotcha the build notes record for next time: `chapters.py` splits `--names`
on commas, so a label containing one silently becomes two names and the script
exits with a count mismatch.

## What is in this folder

**Committed** — source, checks and build inputs:

```
beat_sheet.json              every beat: narration, shot, measured duration
short/beat_sheet.json        the 9:16 cut
timings.json / words.json    measured clock + per-word timings
short/timings.json / words.json   same, for the short
claude-hai-lookup-not-training.srt       subtitles, 16:9
short/…-short.srt            subtitles, 9:16
make_srt.py                  subtitles from measured word timings
short/make_srt.py            same, for the short
chapters.py                  generates + VALIDATES the chapter list
BUILD-PROMPT.md              the brief this was built from
README.md                    this file
FACTCHECK.md                 every claim, its source, its verdict
SOURCES.md                   provenance and toolchain
PEDAGOGY.md                  GATE P — signed, VERDICT: PASS
short/PEDAGOGY.md            GATE P for the short, and its cut plan
QC-REPORT.md                 frame-level visual QC
qc-sheet-t0.png              t=0 contact sheet
FRICTIONAL.md                the process log for this piece of work
description.txt              YouTube description, chapters, and build notes
.gitignore                   renders out, build inputs in
```

**In Drive, not here** — the renders: masters, narration `mp3/`, beat `clips/`,
`media/`.

`timings.json` and `words.json` sit at the folder root rather than in `mp3/`,
because `mp3/` is an excluded *location* under the 2026-09-18 media rule and
git will not descend into an excluded directory.

Note `description.txt` is **not** paste-ready as-is: everything below the `---`
is a labelled build-notes section recording the chapter provenance. Paste only
what's above it.

## Open before publication

1. **Commit the primary source, or re-cite.** See fact-check item 1. This is
   the one worth doing before the reel goes out.
2. **"One catch" understates it.** Not a correction that needs a re-cut; worth
   a line in the description if the video publishes as-is.
3. **Channel** — `@HumanitariansAI` is in the beat sheet and description;
   confirm before upload.
4. **Audio not listened to.** Verified as text and as measured duration only.
   Pacing and whether B09 lands are human judgments.
