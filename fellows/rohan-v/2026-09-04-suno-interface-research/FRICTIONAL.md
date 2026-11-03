# FRICTIONAL — Suno — interface research and series plan

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-08-29 → 2026-08-31 — Suno interface research (Lyrical Literacy tutorials)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's plan and factcheck, the series' build playbook and my dated session record
> with Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** Finding out how Suno actually looks and behaves, so the tutorials could
rebuild it accurately; the three-part series plan; and a playbook for building it.

**Tried, and expected.**
- Research only at first — I asked for no screenshots, just an exact account of the
  Suno workflow. Expected that to be enough for an accurate recreation.

**Where it resisted, and what I did next.**
- It wasn't: research got the sidebar, the sign-in and a card button wrong. I captured
  the real interface myself — 21 screens (`CAPTURES.md`) — and the spec was rewritten
  from them (`SUNO-UI-SPEC.md`).
- For Part 3, six more captures I was asked for overturned the model of the card menu,
  and one correction reached back into the already-shipped Part 1.
- The plan's runtime estimates went stale as the parts were built — Part 1 was planned
  at about 3:30 and came out at 3:56.

**What Claude contributed — accepted, changed, rejected.**
- Claude researched Suno, wrote the spec from my captures and the series plan, and —
  when I asked it to keep what it had learnt — wrote `SERIES-PIPELINE.md`.
- Changed: from research-only to capture-first.

**Understand now / still don't.**
- Now: for an interface tutorial, the captures are the source and everything else is commentary.
- Still open: the captures are not in this repository, for the reason in `CAPTURES.md`.

**Evidence:** [`SUNO-UI-SPEC.md`](./SUNO-UI-SPEC.md) · [`SERIES-PLAN.md`](./SERIES-PLAN.md) · [`SERIES-PIPELINE.md`](./SERIES-PIPELINE.md) · [`CAPTURES.md`](./CAPTURES.md)

## 2026-09-24 — First commit to the fellows repository

**Working on.** Moving this piece of work into the fellows repository beside the rest,
as the renewal requirements ask, with a frictional log.

**Tried, and expected.** Expected to copy it across as it was. It needed more than that.

**Where it resisted, and what I did next.**
- This folder had never been committed to the fellows repository — the work lived
  only in my Lyrical Literacy workspace. Committed today, three weeks after it was
  built —
  [`fa99475`](https://github.com/nikbearbrown/humanitarians-youtube/commit/fa99475).
- The captures are **not** committed: feeds in them show other creators' names and
  work, and the repository allows no personal data about anyone else. `CAPTURES.md`
  lists every one instead.
- My surname appeared in `SERIES-PIPELINE.md`, `SERIES-PLAN.md`; now first name and
  last initial, or the first name alone where it is the spoken form.
- Added this log.

**What Claude contributed — accepted, changed, rejected.** Claude assembled the folder,
checked every file and capture for personal data, and proposed the changes as their own
commits in the same pull request as the rest of my compliance pass.

**Understand now / still don't.**
- Now: a piece of work that only exists in a private workspace is not on the record.
- Still open: none of this was written while the work happened. From here on the log is
  kept during the build.

**Evidence:** [`fa99475`](https://github.com/nikbearbrown/humanitarians-youtube/commit/fa99475)
