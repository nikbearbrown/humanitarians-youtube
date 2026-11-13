# FACTCHECK — Four Documents

Status: every on-camera claim traced to one of the four review documents.
All measured figures were taken on the dev environment; nothing about
production is claimed.

| # | Beat | Claim (as spoken / shown) | Verdict | Source | Fix if needed |
|---|---|---|---|---|---|
| 1 | B01 | Four documents were produced in response to the review | ✅ PASS | The four files: security review, FERPA data flow, architecture & hosting summary, HECVAT Lite answers | — |
| 2 | B01 | The reply to the key request asked whether FERPA and security reviews were complete | ✅ PASS | Build-session correspondence; quoted as narration, not shown on screen | — |
| 3 | B02 | The security review walks the login, JWKS and launch endpoints | ✅ PASS | security review §1.1, §1.2, §1.3 | — |
| 4 | B02 | Signature verified against Canvas's JWKS; `iss`, `aud`, `exp` checked; algorithm pinned to RS256 | ✅ PASS | security review §1.3 | — |
| 5 | B02 | Remediations listed: a legacy endpoint decoded tokens without verifying signatures; role matching allowed privilege escalation; an unauthenticated registration endpoint was disabled; stored credentials were unencrypted and now are not | ✅ PASS | security review §1.3, §2.2, §2.4; HECVAT "Recent remediations" | — |
| 6 | B03 | FERPA basis is the school-official exception at 34 CFR §99.31(a)(1) | ✅ PASS | FERPA data flow §1 | — |
| 7 | B03 | Every field received, its purpose, its store, and its retention are enumerated | ✅ PASS | FERPA data flow §2, §3, §4 | — |
| 8 | B03 | Six subprocessors named in the document; the AI provider receives no student identifiers | ✅ PASS | FERPA data flow §5, §6 (AWS, Supabase, Clerk, OpenAI, PostHog, Resend = 6) | Not named aloud or on screen |
| 9 | B04 | The architecture document states cloud provider, region, web server, runtime and database | ✅ PASS | architecture summary §2, §3 | — |
| 10 | B04 | Continuous WAL archiving on; `archive_timeout = 120s`; RPO ≈ 2 minutes | ✅ PASS | architecture summary §4 | — |
| 11 | B04 | 105 segments archived, 0 failures | ✅ PASS | architecture summary §4 (read from the dev database) | Figure is a point-in-time reading; re-measure before reuse |
| 12 | B05 | HECVAT Lite covers product, data & privacy, encryption, access control, application security, AI/LLM, infrastructure & continuity | ✅ PASS | HECVAT Lite section headings | — |
| 13 | B06 | No SOC 2 held; subprocessors maintain SOC 2 attestations | ✅ PASS | HECVAT "Documentation" | — |
| 14 | B06 | No third-party penetration test to date; internal review completed and findings remediated | ✅ PASS | HECVAT "Application security" | — |
| 15 | B06 | Administrative MFA enrolment status still being confirmed | ✅ PASS | HECVAT "Authentication and access control" | — |
| 16 | B07 | Backup retention window outstanding because it is a plan-level setting not visible from the database | ✅ PASS | architecture summary §4; HECVAT "Infrastructure and continuity" | — |

**Invented values: none.** Every figure on screen traces to a row above.

**Deliberately absent from camera.** No individual's name. No subprocessor named
aloud or on screen. No hostname, no key material, no credential. Nothing about
the production environment. The institution is "a university" throughout.

**Time-sensitive figure.** Row 11 (105 segments, 0 failures) was true when
measured. If this reel is rebuilt later, re-read the archiver rather than
reusing the number.
