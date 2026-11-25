# FACTCHECK.md — Project Ledger – Week 2: Sign-in and Weekly History

Checked on 2026-10-29 against `hai-ledger-demo` (no git history) and Mohan's weekly notes. `.env.local` was not opened and no database was contacted.

| Claim | Evidence | Status |
|---|---|---|
| Register and sign in with email and password | app/register, app/login, lib/auth.ts | VERIFIED IN CODE |
| Passwords hashed (scrypt + per-user salt) | lib/auth.ts | VERIFIED IN CODE |
| Signed session cookie checked on ledger pages and APIs | lib/session.ts, middleware.ts, lib/guard.ts | VERIFIED IN CODE |
| Volunteer added date; one row per volunteer with weekly details | ledger.js ('Added ...'); README 'Weekly details and History' | VERIFIED IN CODE |
| PM section at the top; week picker for the current month | README 'Weekly details and History' | VERIFIED (README) |
| Changes based on feedback from the PM and Professor Nina | Mohan's week 2 notes | FROM MOHAN'S NOTES |
| No password reset and open registration after week two | README at that stage; reset added week 4 | FROM MOHAN'S NOTES |

FROM MOHAN'S NOTES = Mohan's own first-person report; the evidence is outside this folder (the live website repo, the production database, or a design not yet built). The video states these as his account and adds no numbers beyond his notes.
