# Security and Data Handling Document

Written work, not a video. Northeastern's IT office asked whether the integration
had completed FERPA and security reviews. This folder covers the document that
answers it, the instructor-scoping fix found while writing it, and the verification
pass that corrected and withdrew claims I could not substantiate.

| | |
|---|---|
| Period | 12 to 25 October 2026, weeks 11 and 12 of the agreement |
| Hours | 58, recorded in [week 11](../weekly-hours/2026-10-12-weekly-hours.md) and [week 12](../weekly-hours/2026-10-19-weekly-hours.md) |
| Delivered to | Northeastern IT, sent privately. The document is not in this repository |
| Repository | `Medhavy/medhavi-hub`, private to the Medhavy organisation |

## What the document covers

Launch mechanics and every validation step. Exactly what student data the launch
carries and how long each record is kept. Encryption in transit and at rest. Access
control. Hosting and region. The third parties that process data and what each one
receives. Development practices. The compliance gaps, stated plainly in their own
section rather than left out.

It is not committed here. It describes the security posture of a system holding
student data, so it went to IT directly. What is in this folder is the record of
writing it.

## The fix it produced

Instructor textbook access was not scoped to the courses an instructor teaches.
Writing the access-control section is what surfaced it, because the section would
not have been true as written. Six tests cover the three paths that can grant
access: class enrolment, class taught, and an explicit grant.

[`9df60ba`](https://github.com/Medhavy/medhavi-hub/commit/9df60ba)

## Verification, and what I withdrew

Every claim was checked against the code and the live dev environment rather than
against a plan page. Several were corrected. Two were withdrawn as unverifiable: a
backup posture I could not substantiate, and a multi-factor authentication claim
that had never been checked. Both are now in the gaps section instead of the
assurances section.

Transport security was tested rather than read off a configuration file. Each TLS
version was negotiated individually against the dev endpoint: 1.0 and 1.1 rejected,
1.2 and 1.3 accepted, 1.3 negotiated by default. The method and the result are
recorded in [FRICTIONAL.md](FRICTIONAL.md). [Four Documents](../2026-09-14-security-documents-explainer/README.md)
is the reel that explains this document to a non-specialist audience.

## Evidence

- [`9df60ba`](https://github.com/Medhavy/medhavi-hub/commit/9df60ba) instructor scoping and its six tests
- [`719a36e`](https://github.com/Medhavy/medhavi-hub/commit/719a36e) raw error text stopped leaking in production responses
- [Four Documents](../2026-09-14-security-documents-explainer/README.md) the reel built from this work
- [FRICTIONAL.md](FRICTIONAL.md) what resisted and what is still open

## Frictional log

This work subfolder carries its own [FRICTIONAL.md](FRICTIONAL.md) per `fellows/README.md`.
