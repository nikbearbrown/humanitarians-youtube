# Chinnasurya V.

**Role:** AI Software Engineer
**Project:** Medhavy Canvas LTI 1.3 integration
**GitHub:** [@surya16122114](https://github.com/surya16122114)

## Executive summary

I build the Canvas LTI 1.3 integration for the Medhavy Hub: the path that takes a
student from a click inside their university's Canvas course to an authenticated
session inside a Medhavy textbook. The launch itself was delivered under the
previous agreement, 15 June to 31 July 2026. Since 1 August the work has been
hardening it for Northeastern's FERPA and security review, which the developer key
depends on: credential encryption, row level security, removing the unused
gradebook and roster scopes, scoping instructor access, and writing the security
and data-handling document that review asked for.

Alongside the integration I produce Brutalist explainer reels on how the thing
actually works. Six are rendered, with the complete film-as-code record in this
folder and the masters on Drive. All six also exist as native 9:16 cuts, rendered
at portrait dimensions rather than centre-cropped; each carries its own
`beat-sheet-short.json` as the build input. Twelve masters in all, thirteen
minutes twenty-four of 4K explainer.

**Series voice:** Kokoro Onyx (`am_onyx`), recorded as `metadata.voice_kokoro` in every
beat sheet and kept across the series. No re-voice decision has been made.

**Status:** all six reels are built, QC'd and fact-checked, and none is published to
YouTube. Publishing is the first item of the next period.

## Quick review

- [Renewal request, 28 October 2026](renewal-requests/2026-10-28-renewal-request.md)
- [Weekly hours](weekly-hours/README.md)
- [Research and project plan for the next period](research-plan.md)
- Video masters: [Drive folder](https://drive.google.com/drive/folders/1jtAWaeQ5k_HyH-P5c_D-A7tUklGo1hZG)

## What is in this folder

| Folder | What is inside |
|---|---|
| [2026-08-10-lti-hardening-for-review/](2026-08-10-lti-hardening-for-review/README.md) | Code work, no video. The six defects found auditing my own code against the LTI 1.3 spec, the fix and tests for each, and the migration consolidation. 52 hours across weeks 1 and 2 |
| [2026-09-13-canvas-launch-explainer/](2026-09-13-canvas-launch-explainer/README.md) | "How a Canvas Launch Works" — 11 beats, 3:15, rendered in 16:9 and 9:16. Beat sheet, script, fact-check, sources, pedagogy note, build log, scene renderer, QC contact sheets |
| [2026-09-13-what-actually-crosses/](2026-09-13-what-actually-crosses/README.md) | "What Actually Crosses" — 9 beats, 2:09, rendered in 16:9 and 9:16. Full film-as-code record. Research done against the code, which turned up two defects the documents did not describe |
| [2026-09-13-ten-prefixes-eleven-tables/](2026-09-13-ten-prefixes-eleven-tables/README.md) | "Ten Prefixes, Eleven Tables" — 8 beats, 1:54, rendered in 16:9 and 9:16. Resolves the 10-vs-11 table count; one claim shipped with a documented contradiction |
| [2026-09-14-security-documents-explainer/](2026-09-14-security-documents-explainer/README.md) | "Four Documents" — 9 beats, 2:37, rendered in 16:9 and 9:16. Full film-as-code record |
| [2026-10-12-security-data-handling-document/](2026-10-12-security-data-handling-document/README.md) | Written work, no video. The document Northeastern IT asked for, the instructor-scoping fix that writing it surfaced, and the two claims I withdrew as unverifiable. 58 hours across weeks 11 and 12 |
| [2026-10-28-the-role-that-lied/](2026-10-28-the-role-that-lied/README.md) | "The Role That Lied" — 8 beats, 1:40, rendered in 16:9 and 9:16. Why a substring match is the wrong way to read an LTI role |
| [2026-10-28-encrypted-twice/](2026-10-28-encrypted-twice/README.md) | "Encrypted Twice" — 8 beats, 1:47, rendered in 16:9 and 9:16. Why a stored credential gets a second layer above the database's own |
| [weekly-hours/](weekly-hours/README.md) | One dated time record per week for the 1 Aug – 31 Oct agreement, thirteen weeks, with an index |
| [renewal-requests/](renewal-requests/README.md) | Dated renewal requests, most recent first |
| [research-plan.md](research-plan.md) | What the next period covers: the remaining code fixes, the developer key handoff, and the first live course launch |

Rendered narration, beat clips and masters live on Drive per the repo rule. What
is here is what the pipeline consumed plus the checks it produced.

## Masters on Drive

[Drive folder](https://drive.google.com/drive/folders/1jtAWaeQ5k_HyH-P5c_D-A7tUklGo1hZG).

| Work folder | 16:9 master | 9:16 cut |
|---|---|---|
| `2026-09-13-canvas-launch-explainer/` | `canvas-launch-explainer.mp4` | `canvas-launch-explainer-short.mp4` |
| `2026-09-13-what-actually-crosses/` | `what-actually-crosses.mp4` | `what-actually-crosses-short.mp4` |
| `2026-09-13-ten-prefixes-eleven-tables/` | `ten-prefixes-eleven-tables.mp4` | `ten-prefixes-eleven-tables-short.mp4` |
| `2026-09-14-security-documents-explainer/` | `security-documents-explainer.mp4` | `security-documents-explainer-short.mp4` |
| `2026-10-28-the-role-that-lied/` | `the-role-that-lied.mp4` | `the-role-that-lied-short.mp4` |
| `2026-10-28-encrypted-twice/` | `encrypted-twice.mp4` | `encrypted-twice-short.mp4` |

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
