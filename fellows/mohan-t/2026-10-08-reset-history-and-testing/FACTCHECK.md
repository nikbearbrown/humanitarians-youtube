# FACTCHECK.md — Project Ledger – Week 4: Sign-in, History and Testing

Checked on 2026-10-29 against `hai-ledger-demo` (no git history) and Mohan's weekly notes. `.env.local` was not opened and no database was contacted.

| Claim | Evidence | Status |
|---|---|---|
| Forgot password with a one-time link expiring after 60 minutes | lib/reset.ts (RESET_MINUTES = 60; used_at, expires_at checks) | VERIFIED IN CODE |
| History with year, month, week, project and PM filters | public/scripts/ledger.js; README 'Weekly details and History' | VERIFIED IN CODE |
| All records, five weeks per page | ledger.js RECORDS_PER_PAGE = 5 | VERIFIED IN CODE |
| PM guide with screenshots | docs/Project-Ledger-PM-Guide.pptx | VERIFIED (file exists) |
| Google sign-in built, then replaced | Mohan's week 4 notes | FROM MOHAN'S NOTES |
| End-to-end testing on sample data | Mohan's week 4 notes | FROM MOHAN'S NOTES |

FROM MOHAN'S NOTES = Mohan's own first-person report; the evidence is outside this folder (the live website repo, the production database, or a design not yet built). The video states these as his account and adds no numbers beyond his notes.
