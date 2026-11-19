# FACTCHECK.md — Project Ledger – Week 1: Building the Project Ledger

Checked on 2026-10-29 against `hai-ledger-demo` (no git history) and Mohan's weekly notes. `.env.local` was not opened and no database was contacted.

| Claim | Evidence | Status |
|---|---|---|
| Project cards with five phases | public/scripts/ledger.js (Idea, Active, Blocked, Paused, Done) | VERIFIED IN CODE |
| Needs-attention box: not filed, blocked, short of hours, no PM | public/scripts/ledger.js needsAttention() | VERIFIED IN CODE |
| Filters: all, needs attention, I am PM | components/LedgerWidget.tsx filter buttons | VERIFIED IN CODE |
| File my week, Meeting view, Export week (CSV) | components/LedgerWidget.tsx buttons; ledger.js | VERIFIED IN CODE |
| Data in Neon Postgres | lib/db.ts, package.json | VERIFIED IN CODE |
| Built from the shared ledger template | Mohan's week 1 notes | FROM MOHAN'S NOTES |
| No sign-in and a weekly-reset volunteer list in week one | Mohan's week 2 notes (what changed) | FROM MOHAN'S NOTES |

FROM MOHAN'S NOTES = Mohan's own first-person report; the evidence is outside this folder (the live website repo, the production database, or a design not yet built). The video states these as his account and adds no numbers beyond his notes.
