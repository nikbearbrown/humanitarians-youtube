# LTI Hardening for the Security Review

Code work, not a video. The Canvas LTI 1.3 integration was delivered and reported
under the previous agreement, which closed with the launch path complete and
production go-live gated on Northeastern IT issuing a developer key. This folder
covers the work that made the integration reviewable: the defects I found auditing
my own code against the LTI 1.3 specification, and the fixes and tests for each.

| | |
|---|---|
| Period | 3 to 16 August 2026, weeks 1 and 2 of the agreement |
| Hours | 52, recorded in [week 1](../weekly-hours/2026-08-03-weekly-hours.md) and [week 2](../weekly-hours/2026-08-10-weekly-hours.md) |
| Repository | `Medhavy/medhavi-hub`, private to the Medhavy organisation |

## What I found and fixed

| Defect | Why it mattered | Fix |
|---|---|---|
| Role matching was a substring test | A role string whose final segment is not an accepted identifier could still read as instructor, because the accepted word appeared somewhere inside it | Exact matching against an allow list of official IMS role URNs, keyed on the final segment after `[/#:]` |
| Stored credential values sat in plain columns | Storage encryption defends a disk. It cannot defend a secret from a query the database is required to answer | AES-256-GCM envelope encryption, `v1:<iv>:<tag>:<ciphertext>` |
| No row level security on the LTI tables | Any role reaching the database could read every launch record | RLS enabled on all 11 tables and restricted to the backend service role |
| Assignment and Grade Services and Names and Role Provisioning scopes requested but unused | The tool could read the Canvas gradebook and a course roster even though no code path wanted either | Both scope sets removed from the registration payload |
| A legacy launch endpoint decoded tokens without verifying the signature | An unverified payload would have been trusted as a launch | Endpoint deleted rather than patched, since nothing current called it |
| Self-service registration was reachable by default | A tool registration path open to anyone is not reviewable | Put behind an explicit flag, off unless set |

## Tests

18 cases written against the two fixes that carry the most risk: 11 on the
AES-256-GCM envelope format, including a tampered tag and a truncated IV, and 7 on
role parsing, including privilege-escalation inputs built to pass a substring test
and fail an exact one. The hardened build was then re-run from Canvas end to end to
confirm the scope removal and the role change had not broken a real launch.

## Schema provisioning

Three LTI migrations had accumulated and had to be applied in order by hand.
Consolidated into one idempotent transactional file, `medhavy-lti-dev-setup.sql`,
so a dev database provisions in a single run and a partial apply rolls back whole.

## Evidence

- [`1fd8443`](https://github.com/Medhavy/medhavi-hub/commit/1fd8443) encryption, row level security, scope removal
- [`55e47ad`](https://github.com/Medhavy/medhavi-hub/commit/55e47ad) the 18 tests
- [FRICTIONAL.md](FRICTIONAL.md) what resisted and what is still open

Two of these fixes later became reels: [The Role That Lied](../2026-10-28-the-role-that-lied/README.md)
and [Encrypted Twice](../2026-10-28-encrypted-twice/README.md).

## Frictional log

This work subfolder carries its own [FRICTIONAL.md](FRICTIONAL.md) per `fellows/README.md`.
