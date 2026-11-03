# FRICTIONAL — Who Can Open What

The frictional log for this piece of work: short, dated, honest entries about
what was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-28 — Port into the repository, and a clean fact-check

> **Written 2026-09-28, after the build it describes.** Reconstructed from this
> folder's `PEDAGOGY.md`, `SOURCE-SCRIPT.md` and beat sheet, plus a fresh read
> of `medhavi-hub` — then drafted with Claude from that record.
> **Sections marked `[NOT RECORDED]` are gaps, not omissions: they are things
> only I can supply.** The reel itself was built 2026-09-17.

**Working on.** Porting the 2026-09-17 reel into `fellows/chaitanya-m/` under
the repository's current rules, and verifying its claims against the hub.

**Tried, and expected.** The cold open states the brief I actually gave: "the
whole rule in plain language: every path a person can take to end up with
permission, and where that decision actually gets made." I expected the answer
to be spread across several files and to be hard to state cleanly.

**Where it resisted, and what I did next.**

- It resisted less than expected, and that turned out to be the story. The
  entire rule lives in one function — `lib/textbook-manager.ts:80`
  `getUserAccess(userId)` — about fifty lines. The reel's structure follows the
  function's own branches rather than an invented narrative.
- The interesting beat (B04) is not a fact about the rule but about *where* it
  lives: the same question is asked when a student opens a book and again when
  the textbook calls back, and both call the same function. That is only
  interesting if you have seen systems where the two checks drifted apart, so I
  had to justify the beat rather than assume it landed.
- The sharp edge took finding: `.eq('classes.archived', false)` at line 112.
  Archive a class and its books silently stop opening, with nothing explaining
  why to the student. That became the "where it bites" half of the verdict page.
- At port time the fact-check came back fifteen claims, fifteen pass — the
  cleanest of the four reels. One nuance did not fit on camera: the two callers
  reach the same answer for `hidden` books by different reasoning, so the
  guarantee holds in behaviour but is not enforced by one shared branch.
- Same three rule changes as the sibling reel: media rule, no-surname,
  frictional logs — all postdating the build. `pantry/` now committed,
  `timings.json` moved out of the excluded `mp3/` location.

**What Claude contributed — accepted, changed, rejected.**

- Claude did the port, wrote the README, description and fact-check, and read
  `getUserAccess` line by line against each on-camera claim.
- Accepted: recording the `hidden`-book asymmetry even though nothing on camera
  is false, because it is the detail that would matter if someone changed one
  branch and not the other.
- `[NOT RECORDED]` — what I rejected or changed during the original
  **2026-09-17 build**: how many drafts the three-roles scene took, whether the
  archived-class edge was in the plan or found late, what the handoff prompt
  went through. Not logged at the time.

**Understand now / still don't.**

- Now: "one question, one place" is a property worth a whole beat, and the way
  to show it is two call sites pointing at one function — not a diagram.
- Now: a clean fact-check is evidence the narration was written from the code
  rather than from memory of the code. The reels where I paraphrased from
  understanding are the ones with findings against them.
- Still open: the reel says a student gets no explanation when class-granted
  access disappears. That is true, and it is a real usability defect in the
  hub — but I only stated it, I did not file it or fix it.
- Still open: whether these two access reels should have been one longer video.
  They share a subject and were built four days apart.

**Evidence:** [`FACTCHECK.md`](./FACTCHECK.md) ·
[`PEDAGOGY.md`](./PEDAGOGY.md) (GATE P, signed 2026-09-17) ·
[`qc-sheet-16x9.png`](./qc-sheet-16x9.png) ·
[`qc-sheet-9x16.png`](./qc-sheet-9x16.png) ·
[`SOURCE-SCRIPT.md`](./SOURCE-SCRIPT.md)
