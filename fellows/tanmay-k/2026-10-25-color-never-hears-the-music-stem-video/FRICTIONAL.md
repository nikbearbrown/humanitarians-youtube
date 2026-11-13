# Frictional Log — color-never-hears-the-music (Week 28 topic video)

**Record provenance:** drafted 2026-10-25 with Claude from this folder's own records (`TOPIC-DECISION.md`, `ANGLE.md`,
`FACTCHECK.md`, the proof reviews, `GATE-P-LINT.md`, the video gates), after the work was done rather than while it
happened. **Awaiting Tanmay's review.** Every entry points at the record it comes from.

## 2026-10-25 — A topic nobody had taken

- **Work and expectation:** draw the week's topic at random from the `claude-for-<topic>` collections and make sure no
  one else has it, with git commands that only read.
- **Where it resisted:** about 3,100 topic folders across 98 remote branches, many of them variants of one another.
  Three draws were rejected: `variational-bound` (about 16 variants of the same idea), `nine-weights-convolution` (in our
  own Weeks 18/19/20/26 notes) and `classifying-supernovae` (a fellow's video on the same subject).
- **What was done:** a plain `git fetch` refreshed the local remote refs (the one non-read-only command, flagged to
  Tanmay at the time); the rest was `ls-tree`/`show`/`grep`. `claude-for-design` was our Week 24 collection; Tanmay
  decided to keep the pick because the topic itself is unused.
- **Decided by:** Tanmay set the rules; the draw decided the topic.
- **Record:** `TOPIC-DECISION.md`.

## 2026-10-25 — A paper that would not open

- **Work and expectation:** read Palmer et al. 2013 in full before any number went on screen.
- **Where it resisted:** PNAS, PubMed Central and Europe PMC all answered automated requests with a bot check. The
  abstract was readable; the methods were not.
- **What was done:** the checks were not worked around. The authors' own lab site (`palmerlab.berkeley.edu`) hosts the
  paper; it was downloaded into an isolated folder, read, and deleted afterwards at Tanmay's request.
- **What it changed:** draft 1's "calm–agitated" scale was not the paper's (its dimensions are happy–sad and
  strong–weak), and the fast-minor case draft 1 called "not in the data" is in it (the design crossed tempo and mode).
  Both were fixed before any audio existed.
- **Record:** `FACTCHECK.md` ("Corrections the paper forced"), `PROOF-REVIEW.md`.

## 2026-10-25 — A Short that read as rushed

- **Work and expectation:** a Short that is complete and does not feel hurried.
- **Where it resisted:** the first Short passed its rubric at 12/12 and still read as one new idea every few seconds.
  Later the measured voice ran at 3.1–3.8 words per second, not the 2.4 the script had planned (the plan divided words
  by line budgets that include the gaps).
- **What was done:** the script was rewritten (8 lines, about 92 s planned, with a concrete example and the limit
  added back); the measured rate was reported, and Tanmay's listen cleared the pace.
- **Record:** `PROOF-REVIEW-SHORT.md`, `PROOF-REVIEW-SHORT-RENDERED.md`, `PROOF-REVIEW-SHORT-VIDEO.md`.

## 2026-10-25 — Defects the checks found

- **Work and expectation:** each check catches what the one before cannot see.
- **Where it resisted, and what caught it:**
  - A missing tone tag on B13's header meant its audio was never generated; the beat count (12 of 13) showed it.
  - "Guadalajara" came out of Kokoro's tokenizer with a "j" and a doubled r, so it was dropped from the spoken line
    (the on-screen source line still names the university).
  - Five source lines sat 6–10 px from the bottom edge on the stills; the measured check flagged it.
  - On the first video gate: labels up to 2.5 s late, a one-frame hard cut, a loudness overshoot (−1.4 dBTP against a
    −1.5 limit), and old and new text cross-fading at half strength. Viewing frames caught the last one; the gate
    could not.
- **What was done:** each was fixed and the gate re-run; the Short passes 11/11 and the long film's measured gate passes.
- **Record:** `GATE-P-LINT.md`, `PROOF-REVIEW-RENDERED.md`, `VIDEO-GATE-LONG.md`, `VIDEO-GATE-SHORT.md`.

## 2026-10-25 — Time spent re-rendering

- **Work and expectation:** two 4K renders, in parallel.
- **Where it resisted:** the machine has 6 cores; two renders with 8 workers each pushed the load average to about 170, and
  the Short was rendered more than once because each defect surfaced after a full 4K pass.
- **What was done:** every later fix was checked before the next render; the cheap checks (label timing against the
  word clock, frame-to-frame change at low resolution) should have run first.
- **Record:** this entry.
