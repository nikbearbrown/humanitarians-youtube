# Fellowship Renewal Request — Chinnasurya V.

**Fellow:** Chinnasurya V. ([@surya16122114](https://github.com/surya16122114))
**Role:** AI Software Engineer
**Project:** Medhavy Canvas LTI 1.3 integration
**Supervision:** Prof. Nik Bear Brown
**Current agreement:** 1 August to 31 October 2026
**Previous agreement:** 15 June to 31 July 2026, reported separately
**Renewal requested:** 1 November 2026 to 31 January 2027 (3 months)
**Date:** 28 October 2026
**Fellows folder:** [fellows/chinnasurya-v](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/chinnasurya-v)

## Summary

I request a three-month renewal to finish the Canvas LTI 1.3 integration for the
Medhavy Hub and get it through Northeastern's security review and into a real
course. The launch path itself was delivered and reported under the previous agreement,
which closed with the integration complete and production go-live gated on
Northeastern IT issuing a developer key. This period was the work that review
depends on: hardening the integration against the failure modes that matter for a
tool handling student data, and writing the security and data-handling document
Northeastern IT asked for. I also produced two Brutalist explainer reels on how the
integration works, with the full film-as-code record. Claude assisted with
implementation and with the reel builds under my direction; the architecture
decisions, the security review of my own code, and the judgment calls on what to
claim were mine.

> `Medhavy/medhavi-hub` is private to the Medhavy organisation. The commit
> links below resolve for anyone with access to that repository; they will
> 404 without it. I can grant access or walk through any commit on request.

## What I delivered this period

**1. The integration hardened for the Northeastern security review.**
The launch path was delivered and reported under the previous agreement, which
closed with the integration complete and go-live gated on a developer key. This
period made it reviewable. Replaced substring role matching with exact matching
against an allow list of official IMS role URNs, after finding that a role string
whose final segment is not an accepted identifier could still read as instructor.
Added AES-256-GCM encryption for stored credential values. Enabled row level
security on all 11 LTI tables, restricted to the backend service role, and
verified on the dev database that non-service roles receive zero rows and have
their writes rejected. Removed the unused Assignment and Grade Services and Names
and Role Provisioning scopes, so the tool cannot read the Canvas gradebook or a
course roster even by accident. Stopped raw error text being returned in
production responses. Scoped instructor textbook access to the courses they
actually teach.
*My contribution:* found each issue by auditing my own code against the spec, and
wrote each fix and each test.
*Evidence:* [`1fd8443`](https://github.com/Medhavy/medhavi-hub/commit/1fd8443) encryption, row level security and scope removal, filed as the partial Week 7 carried forward · [`55e47ad`](https://github.com/Medhavy/medhavi-hub/commit/55e47ad) tests for credential encryption and the role allow-list, privilege-escalation inputs included · [`719a36e`](https://github.com/Medhavy/medhavi-hub/commit/719a36e) production error responses · [`9df60ba`](https://github.com/Medhavy/medhavi-hub/commit/9df60ba) instructor scoping

**2. The security and data-handling document for Northeastern IT.**
Northeastern's IT office asked whether the integration had completed FERPA and
security reviews. I wrote the document that answers it: the launch mechanics and
every validation step, exactly what student data the launch carries and how long
each record is kept, encryption in transit and at rest, access control, hosting
and region, the third parties that process data, development practices, and the
compliance gaps stated plainly rather than hidden. Transport security was tested
directly rather than read off a config file: TLS 1.0 and 1.1 rejected, 1.2 and 1.3
accepted, 1.3 negotiated by default.
*My contribution:* sole author. Every verified figure measured on the dev
environment.
*Evidence:* [the work record](../2026-10-12-security-data-handling-document/README.md), with the TLS method and the withdrawn claims in its [Frictional log](../2026-10-12-security-data-handling-document/FRICTIONAL.md). [Four Documents](../2026-09-14-security-documents-explainer/README.md) is the reel explaining what each required document has to answer, with its [fact-check](../2026-09-14-security-documents-explainer/FACTCHECK.md) and [sources](../2026-09-14-security-documents-explainer/SOURCES.md). The review document itself contains hosting detail for an institution's internal review and is available to Professor Brown on request rather than published here.

**3. Six Brutalist 4K reels, with the full film-as-code record.**
"How a Canvas Launch Works" (11 beats, 3:15.4), "Four Documents" (9 beats,
2:37.5), "What Actually Crosses" (9 beats, 2:09.1), "Ten Prefixes, Eleven Tables"
(8 beats, 1:54.5), "The Role That Lied" (8 beats, 1:40.7) and "Encrypted Twice"
(8 beats, 1:47.3). Every one also exists as a native 9:16 cut rendered at
portrait dimensions, not a centre crop: twelve masters, thirteen minutes
twenty-four of 4K explainer in total.
Beat sheets, scripts, shot lists, fact-checks, source provenance, pedagogy notes,
build logs, the out-of-tree scene renderers and the QC contact sheets are all in
this folder. Masters are on Drive. Two were scripted on 13 September and rendered
on 28 October; each build log says so rather than implying otherwise.
*My contribution:* scripted, art-directed, built and QC'd all six. One renderer
core carries across all of them; only the scene functions change per reel.
*Evidence:* [Drive folder](https://drive.google.com/drive/folders/1jtAWaeQ5k_HyH-P5c_D-A7tUklGo1hZG) · per-reel build logs and contact sheets linked above

## Hours status

**350 hours across 13 weeks, no week below 23.** Weeks run Monday to Sunday from the agreement start. One dated time record per week in
[weekly-hours/](../weekly-hours/README.md), in the structure of `fellows/example-f`. The figures are reconstructed estimates based on
documented project activity and my recollection of the time spent; exact
contemporaneous time records were not maintained for this period. Dated weekly
records start from 1 November, written in the week rather than reconstructed.

## Weekly evidence index

Full week-by-week table in [weekly-hours/](../weekly-hours/README.md). The weeks carrying dated
artifacts:

| Week | Hours | Evidence |
|---|---:|---|
| 2026-08-03–08-09 | 28 | Hardening filed from the partial carry-in: credential encryption, row level security, AGS and NRPS scopes removed, legacy unverified-token endpoint deleted · migrations consolidated into one idempotent provisioning file |
| 2026-08-10–08-16 | 24 | Tests for secrets-at-rest encryption and the role allow-list · hardened build re-tested from Canvas |
| 2026-08-17–08-23 | 24 | FERPA requirements read against the integration; the token's claim list mapped to what the hub stores |
| 2026-08-24–08-30 | 25 | HECVAT Lite structure worked through; transport security and headers checked against the endpoint |
| 2026-08-31–09-06 | 23 | Architecture, hosting and subprocessors mapped; the AI boundary established and verified |
| 2026-09-07–09-13 | 34 | Brutalist toolkit set up and the pipeline learned · first reel built · two further reels scripted |
| 2026-09-14–09-20 | 32 | Four Documents built · dev database queried directly for retention and archival posture · three compliance documents drafted · production error responses fixed |
| 2026-09-21–09-27 | 24 | Row level security verified per table · renderer core factored for reuse |
| 2026-09-28–10-04 | 25 | Retention traced to where it is enforced · subprocessor inventory confirmed against the code |
| 2026-10-05–10-11 | 24 | Token generation 500 traced to a paused database rather than a code fault; launches re-run after the fix |
| 2026-10-12–10-18 | 30 | Instructor access scoping with six tests · the security and data-handling document written for Northeastern IT |
| 2026-10-19–10-25 | 28 | Document verified claim by claim, several withdrawn as unverifiable · TLS versions tested individually |
| 2026-10-26–10-31 | 29 | Four reels built and documented — two from September scripts and two written from scratch — toolkit environment rebuilt, all six 9:16 cuts produced · re-audit found three further defects |
| **Total** | **350** | |

## Degree relevance and supervision

I am a Master's student at Northeastern University. The work is applied software
engineering on an authentication and authorization integration: OIDC and OAuth 2.0
flows, JWT signature verification and algorithm pinning, replay and CSRF
protection, role-based access control, Postgres row-level security, application
layer encryption, and the data handling that a FERPA review actually asks about.
It is directly degree relevant.

Supervision: Prof. Nik Bear Brown. The LTI work is reviewed through pull requests
into `development` in `Medhavy/medhavi-hub`, and the Northeastern security review
is being carried out in correspondence with Professor Brown and the university's
IT office.

## Authorization

F-1 post-completion OPT. Authorization dates and documents sent to HR privately
rather than recorded here.

## Next period

Full plan with dates: [research-plan.md](../research-plan.md). In short:

- Carry the security review through Northeastern IT, complete a HECVAT Lite if
  requested, get the developer key issued, and verify a real launch from
  Northeastern Canvas rather than local Docker
- Fix the three defects my own re-audit turned up, including an instructor-scoping
  bypass in the access verification route and a token verification fallback that
  accepts an unverified payload
- Reconcile launch audit retention, which is currently stated three different ways
- Ship the quiz backend as its own pull request
- One Brutalist reel a week, starting with the two already written

| Target | Deliverable |
|---|---|
| 30 Nov 2026 | Three code fixes merged with tests, retention reconciled, iframe behaviour verified against real Canvas, four weekly reels delivered |
| 31 Dec 2026 | Developer key issued and a real Northeastern launch verified, or a written account of what IT is blocking on. Quiz backend merged |
| 31 Jan 2027 | Instructor and student flows verified against a real course, weekly reels continued, written report on shipping into an institution's compliance process |

## Open items

- **Weekly hours for this period are reconstructed estimates, not a contemporaneous
  log.** Stated as such in every file under `weekly-hours/`. Dated weekly records start 1 November.
- "Ten Prefixes, Eleven Tables" ships with a contested claim, documented rather
  than hidden: B04 states launch audit retention as one hour, which the schema
  says, while the published privacy policy says twelve months and the purge job is
  not scheduled. Marked SEE NOTE in that reel's fact-check; reconciling the code is
  in the plan for the next period.
- The reels' B00 narration says "Surya", taken from conversation context during the
  build rather than from the script. Flagged in both build logs and still to correct.
- `PEDAGOGY.md` on the first reel carries `VERDICT: PENDING`. I did not self-sign a
  gate that asks for a human signature.
- The archiver figure in the second reel's fact-check is a point-in-time reading
  and is now stale. Flagged in that file.
- Supabase plan tier and backup retention window unconfirmed; I do not have
  dashboard access to the project.
- No third-party penetration test, no SOC 2 for Medhavy itself, no VPAT. On a
  student-facing textbook reader at a university, accessibility is the one most
  likely to be pressed, and nobody has checked it against WCAG.
