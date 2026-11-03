# FRICTIONAL — The Logout That Didn't

The frictional log for this piece of work: short, dated, honest entries about
what was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-25 — Port into the repository, and a warning that hasn't expired

> **Written 2026-10-25, ten days after the 2026-10-15 build.** Reconstructed
> from this folder's `BUILD-PROMPT.md`, `PEDAGOGY.md`, `QC-REPORT.md` and beat
> sheet, plus a fresh read of `medhavi-hub` on both `main` and `development` —
> then drafted with Claude from that record. **Sections marked `[NOT RECORDED]`
> are gaps only I can fill.**

**Working on.** A postmortem reel on the production logout bug, ported into
`fellows/chaitanya-m/` and fact-checked against both branches.

**Tried, and expected.** This is the first reel where the subject is a bug I
investigated rather than a subsystem I documented. I expected the fact-check to
be easy — I had read the code to write the narration. I did not expect the
re-check to matter as much as it did.

**Where it resisted, and what I did next.**

- Eleven claims, eleven pass. The mechanism beats are unusually tight because
  the fix's own comment on `main` (`LogoutButton.tsx:103–106`) states the
  HttpOnly / provider-domain reasoning in almost the same words as B06. When the
  code already explains itself, the narration's job is to not get in the way.
- B11 makes a precision claim I nearly got wrong: textbook access was *always*
  revoked correctly; only the hub's own session survived. Those are two separate
  mechanisms — the server-side `lastLogoutAt` check I had already verified for
  the One Sign-In reel, and the client-side cleanup. Easy to conflate into "the
  logout was broken," which would have been false.
- **The branch claim needed re-testing, not restating.** B09 says the fix is on
  `main` and `development` doesn't have it — true when recorded on 2026-10-15,
  but that is exactly the kind of claim that rots. Re-tested at port time:
  `4777b36` is still not an ancestor of `origin/development`, whose HEAD is from
  2026-10-22, three days *after* I recorded. Still true, and now more urgent.
- The re-check also found something sharper than what I put on camera.
  `development:106` carries a comment: "No Clerk signOut call - we handle
  everything manually to avoid POST conflicts." The omission wasn't an
  oversight. It was a documented decision, made for a reason that the production
  move invalidated. I described the bug as an assumption that stopped being
  true; the comment proves it.

**What Claude contributed — accepted, changed, rejected.**

- Claude did the port, wrote the README, fact-check and description, read
  `LogoutButton.tsx` in full on both branches, and located the fix commit.
- Accepted: re-testing the branch claim rather than carrying it forward from the
  build. That is the step that turned a possibly-stale line into a verified
  live warning.
- Accepted: flagging in "open before publication" that publishing this reel
  while `development` still carries the bug is a choice to make deliberately —
  either merge the fix first and the beat becomes historical, or publish knowing
  the reel describes something still shipping.
- `[NOT RECORDED]` — the investigation itself on **2026-10-15**: how long it
  took to stop reading the logout code and start looking at the environment,
  what I tried first, whether anyone pointed me at the HttpOnly flag.

**Understand now / still don't.**

- Now: "it works on my machine" is not a joke when the environments differ in
  exactly the way a broken assumption depends on. This bug was unreachable in
  development by construction.
- Now: a claim about a branch is a claim about a moment. Anything of the form
  "X hasn't landed yet" has to be re-tested at publication, not just at
  recording. That is a new item for my checklist.
- Still open: the fix is still not on `development` as I write this. I made a
  video about it and the thing the video warns about is still true. Writing the
  warning up is not the same as closing it.
- Still open: the reel says "every user, every time" but never says for how
  long, or what an un-ended session could still reach. A viewer will ask.

**Evidence:** [`FACTCHECK.md`](./FACTCHECK.md) · [`QC-REPORT.md`](./QC-REPORT.md) ·
[`qc-sheet-t0.png`](./qc-sheet-t0.png) · [`qc-sheet-mid.png`](./qc-sheet-mid.png) ·
[`PEDAGOGY.md`](./PEDAGOGY.md) (GATE P, signed 2026-10-15) ·
`medhavi-hub` fix commit `4777b36` (2026-10-09)
