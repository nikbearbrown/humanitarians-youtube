# FACTCHECK.md — claude-liam-medhavy-hub-walkthrough

Every spoken number or mechanism, with where it was checked. Source = the hub repo at `efcc3f5` unless noted; Screen = visible in `capture/run-05.mp4` on 2026-09-17.

| Beat | Claim | Basis | Status |
|---|---|---|---|
| B00 | Live admin, scripted browser, names masked | `capture/run-05-actions.jsonl`, `capture/redaction.jsonl` (0 raw emails at every step) | PASS |
| B01 | One sign-in; per-textbook 24h token verified back against the hub | `DEVELOPER.md` §4.1–4.2; README "Single sign-on" | PASS |
| B01 | Three roles: student, instructor, admin | `DEVELOPER.md` §3 | PASS |
| B02 | 79 users, 11 admins, 0 pending | Screen: overview tiles (68 learners = 54 students + 14 instructors) | PASS |
| B02 | Status is public / private / hidden | Screen: badges; `DEVELOPER.md` §5.1 | PASS |
| B03 | Open mints the token and redirects | `DEVELOPER.md` §4.1, `StudentDashboard`/`AdminDashboard` open flow | PASS (source fact, said as such) |
| B03 | Registering a URL whitelists its origin for CORS | README "Textbook registry"; `DEVELOPER.md` §5.1 | PASS (source fact, said as such) |
| B04 | First hundred Clerk accounts | `DEVELOPER.md` §9: `/admin` fetches first 100 Clerk users | PASS |
| B04 | Admin rows locked; API refuses to demote | Screen: "Admin role locked"; `DEVELOPER.md` §3 "Admin is irreversible" (403) | PASS |
| B05 | Two live classes, 8 and 13 students, Archive | Screen: Classes tab buttons "8 Students", "13 Students", "Archive" | PASS |
| B05 | Invite code join; enrollment confers access | README "Classes & invites"; `DEVELOPER.md` §5.2 access oracle | PASS |
| B06 | Import by timestamp, review every node, export verified map; Grant Access | Screen: placeholder `e.g. 20260411_120000`, buttons Import / Grant Access, 4 rows; `docs/concept-map-editor.md` | PASS |
| B07 | Requests empty; approve/deny updates library | Screen: empty queue; `DEVELOPER.md` §5.3, §8.3 | PASS (action described from source) |
| B08 | PostHog; 80 unique users / 429 page views / 36 textbook opens / 51 AI interactions (30 days) | Screen: analytics tiles ("Powered by PostHog · Last 30 days") | PASS |
| B08 | Breakdown: hub, then cancer textbook, then dev instances | Screen: platform breakdown order hub.medhavy.com, cancer.medhavy.com, dev-hub.medhavy.com | PASS |
| B08 | First-party session counter is a separate system; summary writes not atomic | `DEVELOPER.md` §11.1 | PASS |
| B09 | Settings = Clerk profile; role lives in metadata | `DEVELOPER.md` §9 `/settings`; §3 role metadata | PASS |
| B10 | Textbook sites bounce to hub with localhost blocked_url | curl 2026-09-17: three 307s to `hub.medhavy.com/dashboard?blocked_url=https://localhost:300x/` | PASS (observed; cause not diagnosed) |
| B10 | Student library, request flow, invite join not shown | Single-account run; admin `/dashboard` redirects to `/admin` (observed) | PASS |
| B11 | `docs/creating-a-new-textbook.md` exists | Repo listing | PASS |

Stripped before recording: nothing. Numbers that changed between run-01 and run-05 (page views etc.) were re-read from the run-05 frames.
