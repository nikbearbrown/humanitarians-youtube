# FRICTIONAL — Midjourney — interface research and series plan

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-06 → 2026-09-09 — Midjourney interface research (Lyrical Literacy tutorials)

> **Written 2026-09-24, after the week it describes.** Reconstructed from this
> folder's plan and factcheck, the series' build playbook and my dated session record
> with Claude, then drafted with Claude from that record. The decisions and
> corrections below are mine. Where something was not recorded at the time, the
> entry says so rather than filling it in.

**Working on.** A week spent almost entirely on Midjourney: using it myself, researching
prompting techniques, capturing the interface, and planning the series.

**Tried, and expected.**
- Plan everything first, set up the folders, use the exact framework from the Suno
  series, and research how many parts the tool actually needs.

**Where it resisted, and what I did next.**
- My captures overturned five assumptions in the plan and exposed two surfaces it had
  missed (`MIDJOURNEY-SERIES-PLAN.md`, "What the captures changed").
- The series grew from four parts to five on the evidence, then to six when I asked for
  a part on writing prompts.
- The plan's header says 23 captures; its body and the folder say 29.

**What Claude contributed — accepted, changed, rejected.**
- Claude wrote the 863-line interface spec from my captures, promoted the Suno playbook
  into the tool-agnostic `VIDEO-PIPELINE.md` so the two series could not drift apart,
  and wrote `make_paperwork.py` and `verify_all.py`.
- Accepted: a longer series on the evidence; changed: the order, for the prompt part.

**Understand now / still don't.**
- Now: the captures changed the plan more than the plan shaped the captures.
- Still open: `verify_all.py` reports "no master" for every part, because the masters
  were renamed for the Drive upload after it was written. The captures are not in this
  repository, for the reason in `CAPTURES.md`.

**Evidence:** [`MIDJOURNEY-UI-SPEC.md`](./MIDJOURNEY-UI-SPEC.md) · [`MIDJOURNEY-SERIES-PLAN.md`](./MIDJOURNEY-SERIES-PLAN.md) · [`VIDEO-PIPELINE.md`](./VIDEO-PIPELINE.md) · [`CAPTURES.md`](./CAPTURES.md)

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
- My surname appeared in `VIDEO-PIPELINE.md`, `make_paperwork.py`, `verify_all.py`;
  now first name and last initial, or the first name alone where it is the spoken
  form.
- `verify_all.py` checked for my full name in each sign-off and `make_paperwork.py`
  wrote it into every SHOTLIST; both now use the redacted sign-off.
- Added this log.

**What Claude contributed — accepted, changed, rejected.** Claude assembled the folder,
checked every file and capture for personal data, and proposed the changes as their own
commits in the same pull request as the rest of my compliance pass.

**Understand now / still don't.**
- Now: a piece of work that only exists in a private workspace is not on the record.
- Still open: none of this was written while the work happened. From here on the log is
  kept during the build.

**Evidence:** [`fa99475`](https://github.com/nikbearbrown/humanitarians-youtube/commit/fa99475)
