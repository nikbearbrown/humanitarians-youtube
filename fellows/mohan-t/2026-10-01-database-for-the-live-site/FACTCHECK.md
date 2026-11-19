# FACTCHECK.md — Project Ledger – Week 3: Extending the Database

Checked on 2026-10-29 against `hai-ledger-demo` (no git history) and Mohan's weekly notes. `.env.local` was not opened and no database was contacted.

| Claim | Evidence | Status |
|---|---|---|
| Only additions (ADD COLUMN IF NOT EXISTS / CREATE TABLE IF NOT EXISTS) | sql/real-site-migration.sql | VERIFIED IN CODE |
| fellows.github_username | sql/real-site-migration.sql | VERIFIED IN CODE |
| projects.phase, next_step, weekly_hours_target, strands | sql/real-site-migration.sql | VERIFIED IN CODE |
| ledger_entries columns incl. entered_by, created_at, updated_at | sql/real-site-migration.sql | VERIFIED IN CODE |
| ledger_updates table | sql/real-site-migration.sql | VERIFIED IN CODE |
| Existing fellows, projects, fellow_projects with roles | Mohan's notes; migration references fellows and projects | FROM MOHAN'S NOTES |
| Tested in a separate schema; run on production by Professor Nik on October 9 | Mohan's week 3 notes | FROM MOHAN'S NOTES |

FROM MOHAN'S NOTES = Mohan's own first-person report; the evidence is outside this folder (the live website repo, the production database, or a design not yet built). The video states these as his account and adds no numbers beyond his notes.
