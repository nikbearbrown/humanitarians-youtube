# FACTCHECK.md — Timesheet Redesign – Week 3: Security Fixes and the Release Checklist

Checked against `nikbearbrown/humanitarians_html PR #16` and Mohan's notes. Only public GitHub data was read; no database or secret was accessed.

| Claim | Evidence | Status |
|---|---|---|
| Self-change bypass via alternate ID spellings, fixed; 8 spellings tested | commit 76b6f21; PR #16 'Second review' table | VERIFIED (GitHub) |
| Email change → reset takeover: owner-only for PMs and admins, confirmation for others | commit 406398e; PR #16 table | VERIFIED (GitHub) |
| Save / Discard / Keep editing on leaving | commit 106680f; PR #16 table | VERIFIED (GitHub) |
| Shared reset limit, 3 per 15 minutes across instances | commit e23ef74; PR #16 table | VERIFIED (GitHub) |
| One release checklist; limited database role for the website | commit d093582; PR #16 table | VERIFIED (GitHub) |
| 84/84 and 25/25 tests; both checks green | PR #16 'Testing'; CI run 44384744932: success | VERIFIED (GitHub) |
| Findings came from the second review (17 Nov) | PR #16 description | VERIFIED (GitHub) |
| Not merged; nothing live; staging needs Professor Nik's setup | PR #16 state and description | VERIFIED (GitHub) |
| Reached out to the Agents team PM | Mohan's notes | FROM MOHAN'S NOTES |

FROM MOHAN'S NOTES = Mohan's own report with no public record to check it against. The video states these as his account and adds no numbers beyond his notes.
