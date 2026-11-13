# Week 27 — Topic Selection

**Selected:** `claude-for-video-production/birthday-paradox` (working name; folder is created at build time)
**Subject:** the birthday paradox — why a group of 23 has better-than-even odds of a shared birthday
**Decided:** 2026-10-16
**Angle:** not chosen yet. This file settles the subject only. An angle audit comes before any beat is written.

---

## How the topic was chosen

A seeded draw in three stages, with every step recorded in `DRAW.md`. All access to `humanitarians-youtube` was
read-only (`git for-each-ref`, `git ls-tree`, `git grep`, `git cat-file`). Nothing was fetched, checked out or pushed.

### Stage 1: category

The pool was the 22 `claude-for-<topic>` categories in the repo. Flat `claude-for-legal--*` entries and
lecture-chapter entries were excluded.

- Seed 20261016 gave `claude-for-cancer`. Rejected on request and redrawn with a different seed.
- Seed 27 gave **`claude-for-video-production`**. Kept.

### Stage 2: subject

The category already holds about 40 distinct topics, mostly `vox-*` explainers. Ten counterintuitive-statistics
subjects were checked against it:

| Subject | Result |
|---|---|
| Simpson's paradox | taken |
| Survivorship bias | taken |
| Braess's paradox | taken |
| Berkson's paradox | taken |
| Goodhart's law | free |
| Regression to the mean | free |
| Monty Hall | free |
| Birthday paradox | free |
| Benford's law | free |
| p-hacking | free |

Seed 2701 drawn over the six free subjects gave **birthday paradox**.

### Stage 3: uniqueness sweep

- One pass over every unique text blob reachable from all 65 refs: 56,521 files of type md, json, txt, py, srt,
  vtt, ts, tsx, js, csv and html. The match was case-insensitive: birthday paradox, problem, attack or
  collision, "shared birthday" and "same birthday". **0 hits.**
- A control search for `braess` on the same pass returned 41 hits, so the sweep works.
- Filenames across all refs containing "birthday": **0.**
- Our own Weeks 18–26: **0.**

## Caveats

- Refs are as last fetched locally. A fellow's very recent push would not appear. Re-run the blob sweep after a
  fetch if you want certainty on the day of building.
- The sweep matches text. A fellow could cover the idea without those phrases (for example "23 people, 50%").
  The angle audit should grep for the underlying ideas, not just the name.
- Adjacent ground already held, to differentiate from at angle time: `vox-base-rate`, `vox-99-percent-test`,
  `vox-prosecutors-fallacy`, `vox-turkey-problem` and the Simpson and survivorship videos. All are
  probability-intuition failures.

## Files in this folder

- `DRAW.md`: seeds and method
- `CANDIDATES.md`: subject-level sweep table
- The raw lists: the raw lists (the category pool, the used topic names and the 2,456-line list of existing topic pairs) stay in the working folder
