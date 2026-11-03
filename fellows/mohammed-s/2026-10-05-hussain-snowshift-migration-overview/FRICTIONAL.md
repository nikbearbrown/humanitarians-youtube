# FRICTIONAL — Compiling Is Not Migrating.

- **Folder:** `2026-10-05-hussain-snowshift-migration-overview` · reporting week **2026-10-05 → 2026-10-11**
- **Dates inside this folder's artifacts:** build, QC and gate run 2026-10-07
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-10-05 · written later, on 2026-10-28

> Reconstructed after the fact from the files in this folder, not written at the time.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- A 3:14 overview of my SQL Server → Snowflake migration project, `snowshift`
  (commits `eb342d4` restructure + lint/deploy/parity tooling, `7ba5900` duplicate-key fixes).

**2. What I tried, and what I expected**
- Turn the project into a reel whose every claim traces to the repo: a 1,244-line `Main.sql`
  split into 29 files / 8 stages, a 27-rule linter, ordered deploy, aggregate parity checks.

**3. Where it resisted, and what I did next**
- The real migration gap: Snowflake declares but does not enforce `PRIMARY KEY` / `UNIQUE`,
  so running the budget import twice would double the budget. The fix in `7ba5900` makes the
  import check for itself; three smoke tests assert it.
- Did **not** present "duplicate journals on re-run" as a migration regression — SQL Server
  would have accepted that too.
- Frame-reading found: B01's second correction running past the beat (cut to two lines),
  strike lines spanning the whole column, empty pillar cards in B05, and elements below the 40% opacity floor.
- **A re-render was stopped for low system memory.** A B02 contrast fix and some 9:16 footnote
  fixes are in source but not re-rendered; assembled with the current beats.
- Like the Cortex reel, Gate V fails on B01's typing beat, so the masters were assembled from
  the compiler's clips and have **not** passed the house gate.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude built the reel and the QC. Reused `CortexWhereItBites` and `CortexTitleOutro` from the
  previous week's reel.
- At build time (2026-10-07) GATE P was pending and I had not reviewed the reel. I have since
  signed GATE P and watched the finished cut (confirmed 2026-10-28); `PEDAGOGY.md` was not updated.

**5. What I understand now, and what I still do not**
- Understood: a migration is done when you can prove it behaves the same, not when it compiles.
  The dangerous differences are the ones that raise no error.
- Open: **nothing has run against a live Snowflake account** — 103 tests pass and none touch a
  database (deploy was blocked on missing credentials). Concurrent imports can still both pass
  the existence check, and two procedures are still placeholders. B09 must be re-recorded after the first live deploy.

**Evidence in this folder**
- [`QC-STATUS.md` — gate results and known issues, 2026-10-07](QC-STATUS.md) · [`build-state.json`](build-state.json)
- [`FACTCHECK.md` — 21 claims traced to snowshift commits](FACTCHECK.md) · [`SOURCES.md`](SOURCES.md) · [`CHECKS-REPORT.md`](CHECKS-REPORT.md)
- [`PEDAGOGY.md` — GATE P pending](PEDAGOGY.md) · [`README.md`](README.md)
