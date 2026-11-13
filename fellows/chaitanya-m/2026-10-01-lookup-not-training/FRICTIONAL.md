# FRICTIONAL — Lookup, Not Training

The frictional log for this piece of work: short, dated, honest entries about
what was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-05 — Port into the repository, and the cleanest fact-check yet

> **Written 2026-10-05, after the 2026-10-01 build.** Reconstructed from this
> folder's `BUILD-PROMPT.md`, `PEDAGOGY.md`, `QC-REPORT.md`, the build-notes
> footer in `description.txt` and the beat sheet, plus a fresh read of
> `medhavi-hub` — then drafted with Claude from that record. **Sections marked
> `[NOT RECORDED]` are gaps only I can fill.**

**Working on.** An explainer on how the tutor knows the textbook — lookup at
question time, not training — ported into `fellows/chaitanya-m/` and
fact-checked against the hub docs.

**Tried, and expected.** After the previous round I had a list of process
changes to apply at build time rather than discover at review. Two of them were
load-bearing here: generate and validate the chapter list *before* writing the
description, and sample QC frames at t=0 rather than only mid-beat. I expected
both to be bookkeeping. One of them caught something.

**Where it resisted, and what I did next.**

- Wrote the narration *from* `docs/how-the-tutor-uses-the-textbook.md` with the
  document open, instead of from my understanding of it. That is the change
  that mattered: twelve claims, twelve pass, several close to verbatim. The
  earlier reels where I paraphrased from memory are the ones carrying findings.
- Where the evidence stopped, I stopped. The index-rebuild trigger is described
  as automatic in the docs but could not be confirmed against the book
  repositories' own build config, which isn't in this repo — so B08 says "by
  default" rather than asserting it, and `description.txt` records why.
- `chapters.py` splits `--names` on commas. A label I wrote as "The model is
  rented, not built" silently became two names and the script exited with "got
  14 names for 13 chapters". Renamed to "The model is rented off the shelf".
  The validator catching this rather than emitting a broken list is the whole
  reason it exists.
- B13's outro measures 4.05 s and cannot stand as its own chapter, so it merged
  forward into B12. Same rule that bit the Memory API reel, handled at build
  time this round instead of at review.
- **At port time the fact-check found a provenance problem, not a factual one.**
  `SOURCES.md` cites `docs/how-the-tutor-uses-the-textbook.md` as S2, and that
  file carries eight of the twelve claims — but it is untracked in
  `medhavi-hub`. Verified with `git ls-files`; the other four citations resolve.
  So the claims are verified and nobody else can audit them.
- Also understated: B08 says "one catch," and the same document records three
  silent failure modes (`:87`, `:91`, `:93`). I filmed the most consequential
  one, which was the right pick, but the wording claims a completeness the
  source doesn't support.

**What Claude contributed — accepted, changed, rejected.**

- Claude did the port, wrote the README and fact-check, matched every on-camera
  claim to a line, and tested each cited path with `git ls-files` — which is how
  the untracked-source problem surfaced.
- Accepted: recording the untracked source as a provenance finding rather than
  quietly fixing the citation, because which way to resolve it is my call.
- `[NOT RECORDED]` — what I rejected or changed during the **2026-10-01 build**
  itself: how the three-reasons structure was arrived at, whether the
  open-book-exam framing was first or third, what the handoff prompt went
  through.

**Understand now / still don't.**

- Now: writing narration with the source document open is not a slower way to
  work, it is the difference between a clean fact-check and a correction in the
  description. Five reels in, the correlation is exact.
- Now: a validator that refuses bad output earns its keep on the day it rejects
  your own input for a reason you did not anticipate — a comma in a label.
- Still open: the untracked source. Committing it makes the citation resolve and
  changes nothing else; it is held back deliberately for reasons outside this
  reel, so I have not touched it.
- Still open: five reels built, **none published.** Every status line says "not
  published," and renewal is at the end of this month. The repository evidence
  is in better shape than the thing it is evidence of.

**Evidence:** [`FACTCHECK.md`](./FACTCHECK.md) · [`QC-REPORT.md`](./QC-REPORT.md) ·
[`qc-sheet-t0.png`](./qc-sheet-t0.png) ·
[`PEDAGOGY.md`](./PEDAGOGY.md) (GATE P, signed 2026-10-01) ·
[`description.txt`](./description.txt) (chapter provenance in the build-notes footer) ·
[`chapters.py`](./chapters.py)
