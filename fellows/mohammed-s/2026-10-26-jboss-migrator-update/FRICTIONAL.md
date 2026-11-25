# FRICTIONAL — Today, Batch Mode Lands.

- **Folder:** `2026-10-26-jboss-migrator-update` · reporting week **2026-10-26 → 2026-11-01**
- **Dates inside this folder's artifacts:** code, fact-check and build 2026-11-03 · master
  promoted 2026-11-04 UTC (2026-11-03 evening, US Eastern)
  (after the reporting week — see the README evidence index)
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-10-26 · written later, on 2026-11-03

> Reconstructed from the files in this folder on the day the reel was built.
> Drafted with Claude Code from those files.

**1. Date and what I was working on**
- A 2:12 progress update on the JBoss migrator: the design from the previous video
  ([`2026-10-19-jboss-migrator-overview`](../2026-10-19-jboss-migrator-overview/FRICTIONAL.md))
  is now working code in a public repository, and it gained batch mode.

**2. What I tried, and what I expected**
- Code: [`jboss-migrator`](https://github.com/mdhussainshariff/jboss-migrator) — initial commit
  `74d01c9` (49 files, 3,143 lines, 18 unit tests), then
  [`41d62af`](https://github.com/mdhussainshariff/jboss-migrator/commit/41d62aff2c06b62e384a2aacea969d15d3487bdd)
  "Add batch mode for migrating a portfolio of apps". The same work is in PR #75 into
  `nikbearbrown/mycroft` (open).
- Batch mode: one `portfolio.yaml` deep-merged over shared defaults; every entry validated
  before anything runs; apps run in their own workdirs so one failure doesn't stop the rest;
  one `batch-summary.md/json` at the end. UI checks are serialized behind a lock.
- Every number in the video was re-checked against git, GitHub and pytest on the build date.

**3. Where it resisted, and what I did next**
- **The first draft overclaimed.** It said every stage has unit tests; `baseline.py` has none.
  Corrected to "five of the six" during fact-check.
- The outro underfilled the safe area (48%); a title and repo subline brought it to 68%.
- 9:16: terminal lines overflowed the card in B05, and the B09 subline wrapped mid-URL. Both
  fixed in the portrait beats, but the 9:16 master was **not compiled** — not needed for now.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude built the reel and ran the checks; batch mode was committed the same day.
- 16:9 master: GATE V 0 BLOCKER / 0 MAJOR, promoted through the full final path.
- I reviewed the 16:9 master and approved it on 2026-11-03 (23:34 ET); the approval is recorded
  in `QC-STATUS.md` with the file's sha256. `FACTCHECK.md` was written before that review and
  still says it was pending.

**5. What I understand now, and what I still do not**
- Understood: a migrator for a portfolio has to treat failure as normal — validate everything
  up front, isolate each app, and report per app rather than stop on the first error.
- Open: **not yet run end to end on a real JBoss app**; only unit tests (23 of 23 passing)
  and a batch smoke run against a missing repo. That end-to-end run is the next step.

**Evidence in this folder**
- [`QC-STATUS.md` — GATE V 0/0, presenter approval](QC-STATUS.md) · [`build-state.json`](build-state.json)
- [`FACTCHECK.md` — every number checked against git and pytest](FACTCHECK.md) · [`PROMPTS.md`](PROMPTS.md) · [`SHOTLIST.md`](SHOTLIST.md)
- Master: [16:9](https://drive.google.com/file/d/1i0hmrU8h4Kf1W9MCT9Yj-9YoiupJpfFO/view) (no 9:16 compiled)
- Code: [`41d62af` batch mode](https://github.com/mdhussainshariff/jboss-migrator/commit/41d62aff2c06b62e384a2aacea969d15d3487bdd) · [repository](https://github.com/mdhussainshariff/jboss-migrator) · [PR #75](https://github.com/nikbearbrown/mycroft/pull/75)
