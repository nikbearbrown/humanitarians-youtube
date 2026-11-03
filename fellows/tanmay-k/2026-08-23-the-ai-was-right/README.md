# The AI Was Right. That Was the Problem.

Tanmay Kulkarni, in for Humanitarians AI · Week 19 · 2026-08-23

Sync licensing — getting your song into film and TV — and what happens when you let an AI do
the research before you pitch a music supervisor.

## The two cuts

| File | Aspect | Resolution | Runtime |
|---|---|---|---|
| `2026-08-23-the-ai-was-right.mp4` | 16:9 | 3840 × 2160 | 2:56.8 |
| `2026-08-23-the-ai-was-right-short.mp4` | 9:16 | 2160 × 3840 | 2:57.9 |

Both are clean masters — no slate, no review burn-ins. The vertical cut is the 16:9 master's
derivative: same ten beats, same audio, no beats dropped, plus a 3.0s silent endcard. Both
carry a hold before every cut so a viewer can absorb the frame (0.60s on the long cut, 0.35s
on the Short, which cannot afford more without breaking YouTube's 180s cap). Narration is
171.12s in both.

**This is the first 9:16 deliverable in this repo.** Four of the components it uses were
written portrait-portable from the first line, so each `916` variant is a ~10-line alias
rather than a re-layout. Details in `QC-REPORT.md`.

## What it teaches

Every claim an AI hands you has layers. Three of them you can check — did this person work
on this show, is the song really in it, is the detail right. There is a fourth underneath
that no check catches: **whose decision was it.**

The film tests this rather than asserting it. Ten supervisor/show/song claims were generated
cold, frozen to a file, then verified one by one. Eight held up — better than expected — and
the two failures were the two the model was least confident about. The finding is in the
eight that were *right*: Breaking Bad's finale song passes all three checkable layers, and
the supervisor still did not choose it. The creator did. An email praising his song choice
would be built entirely on true facts and still land wrong.

Tunefind's own April 2025 scam warning is the independent witness: the fraudulent emails
worked because they carried *references to real shows*. True facts, doing the work of a lie.

## Files here

| File | What it is |
|---|---|
| `*.mp4` × 2 | the two masters |
| `beat_sheet.json` | source of truth for the 16:9 cut |
| `beat_sheet-short.json` | source of truth for the 9:16 cut |
| `FACTCHECK.md` | every spoken **and on-screen** claim, verdict, source |
| `QC-REPORT.md` | resolution chain, defects found and fixed, frame QC |
| `PEDAGOGY.md` | append-only build log and Gate P sign-off |

Two beat sheets because there are two cuts; each is the compiled record of its own.

The extended build record — topic selection, research, the frozen experiment, the three
PROOF review passes, the script with tone notes, and the analysis of the source folder this
was rebuilt from — lives in the working folder outside this repo. References to those
documents inside `FACTCHECK.md`, `QC-REPORT.md` and `PEDAGOGY.md` point there, not to this
directory.

## Rebuilt from

`claude-for-music/indie-on-the-pitch` — a Musinique episode (6/7) that had been mechanically
rebranded. What survived is the subject. The thesis, the structure, every line of narration
and every asset are new; the source's own evidence file (`RECEIPTS.md`) does not exist
anywhere in this repo, so every claim was re-sourced from primaries. Diagnosis is in the
working folder's `SOURCE-ANALYSIS.md`.

## Status

Teaching 12/12 (ship bar 8). Production gate PASS in both aspects, re-run on rendered frames.
Gate P signed in `PEDAGOGY.md`.

**Not published.** Publication is a separate human decision, and no human has yet watched
either cut end to end at speed — the one gate a review of frames and transcript cannot close.

## Built with

Brutalist toolkit — Kokoro `af_bella` for narration, Remotion for every beat, `compile.py`
at `--height 2160` / `3840`, `shorts.py` for the derivative cut, and a post-compile pacing
pass for the holds.
