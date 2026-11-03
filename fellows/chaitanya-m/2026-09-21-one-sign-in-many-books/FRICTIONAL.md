# FRICTIONAL — One Sign-In, Many Books

The frictional log for this piece of work: short, dated, honest entries about
what was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-28 — Port into the repository, and a failed claim

> **Written 2026-09-28, after the build it describes.** Reconstructed from this
> folder's `BUILD-PROMPT.md`, `PEDAGOGY.md`, `QC-REPORT.md` and beat sheet, plus
> a fresh read of `medhavi-hub` — then drafted with Claude from that record.
> **Sections marked `[NOT RECORDED]` are gaps, not omissions: they are things
> only I can supply, and I would rather leave them visible than have them
> filled in for me.** The reel itself was built 2026-09-21.

**Working on.** Getting the 2026-09-21 reel into `fellows/chaitanya-m/` under
the repository's current rules, and fact-checking its claims against the hub
source — which the build itself had not done.

**Tried, and expected.** Expected this to be a port: copy the text package,
write a README, verify the claims, commit. I expected the claims to pass, as
they had for the two earlier reels where the narration tracked the code closely.

**Where it resisted, and what I did next.**

- Three repository rules had changed since my last merge, all after this reel
  was built: the media rule (2026-09-18), the no-surname rule and the
  frictional-log rule (both 2026-09-22). None of them applied when the reel was
  made. All of them apply now.
- The media rule inverted what I had done. My `.gitignore` excluded `pantry/`
  and filtered by file extension; the rule now excludes by *location* and
  expects build inputs tracked. The portrait overrides are exactly that — the
  9:16 cut is not reproducible without them — so they are now committed.
- `timings.json` could not stay in `mp3/`. `mp3/` is an excluded directory, and
  git does not descend into an excluded directory, so a re-include rule inside
  it is unreachable. Moved to the folder root.
- **The fact-check failed on B04**, the reel's central security claim. The
  narration says "change one character and the signature stops matching."
  `app/api/access/verify/route.ts:113–131` calls `jwt.verify`, catches the
  throw, and decodes the same token as unsigned base64 — then continues. The
  signature is not a gate. I found a second instance of the same shape at
  `generate-token/route.ts:73–83`, which issues an unsigned ticket when
  `JWT_SECRET` is unset.
- That is the second time in three reels that a security property described on
  camera turned out to be conditional on configuration — the Memory API reel
  had the same finding about its shared secret. I have started treating it as a
  codebase pattern rather than two coincidences.
- B06's "six checks in order" is eight. Miscount, not a wrong claim, but it is
  a number said out loud.

**What Claude contributed — accepted, changed, rejected.**

- Claude did the port, wrote the README, SHOTLIST-equivalent tables and
  description, and ran the fact-check against the hub at `3775687`.
- Accepted: recording the B04 failure in `description.txt` as a stated
  correction rather than only in `FACTCHECK.md`, so a viewer who watches without
  reading the repo is not left with the wrong belief.
- Accepted: fixing the hub before re-cutting the reel — the one-line change
  makes the claim true, which is cheaper and more useful than re-recording.
- `[NOT RECORDED]` — what I rejected or changed during the original
  **2026-09-21 build**: the plan, the beat structure, the choice to spend the
  most time on B09. Not logged at the time.

**Understand now / still don't.**

- Now: a caught exception can silently delete a security guarantee. `jwt.verify`
  throwing is the check working; catching that throw and carrying on with
  unverified data turns the check into decoration. It reads as defensive code.
- Now: a folder has to be checked against the live rules, not the rules it was
  built under.
- Still open: whether the hub's base64 fallbacks are deliberate for local
  development or an oversight. Both sites log warnings, which suggests
  deliberate — but the outer `catch` in `verify` is not conditional on
  `JWT_SECRET`, so it degrades even a correctly configured deployment. I have
  not raised it with anyone yet.
- Still open: whether this reel should publish before the hub is fixed. My view
  is no.

**Evidence:** [`FACTCHECK.md`](./FACTCHECK.md) · [`QC-REPORT.md`](./QC-REPORT.md) ·
[`PEDAGOGY.md`](./PEDAGOGY.md) (GATE P, signed 2026-09-21) ·
[`gate-p-contact-sheet.png`](./gate-p-contact-sheet.png) ·
[`beat_sheet.json`](./beat_sheet.json)
