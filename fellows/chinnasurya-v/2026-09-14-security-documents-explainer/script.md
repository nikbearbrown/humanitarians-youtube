# FOUR DOCUMENTS
### What the institution asked for, and what we wrote to answer it

Single-topic explainer. Source: the four review documents produced for the IT /
Canvas admin team — `medhavy-lti-security-review.md`,
`medhavy-ferpa-data-flow.md`, `medhavy-architecture-hosting-summary.md`,
`medhavy-hecvat-lite-answers.md`.

---

## ART DIRECTION

**Script-native brutalism.** Same system as `medhavy-lti-verify`.

| Role | Value |
|---|---|
| ground | `#0A0A0A` |
| paper | `#F2F0EB` |
| signal | `#E8452C` |
| mute | `#6B6B6B` |

Four colours. Never a fifth.

**Type** — two families only. Display: one grotesk, weight 700+, tracking −2%.
Data/labels: one mono, 400/700. Display type is always flush left on the grid.

**Grid** — 12 columns. Margins sit outside the 4K title-safe inset (192 × 108).
Content is placed by fraction of the band between header and footer, so it fills
the frame at any canvas size.

**Hard rules**

- Hard cuts only. No easing, no interpolation, no fades between states.
- `border-radius: 0`. Boxes are drawn as four filled rectangles.
- Arrows are straight segments plus a filled triangle. N sources converging on
  one target means N separate arrowheads, never a merged bus.
- The visible grid is part of the look: mute blended over ground at ~12%.
- No screenshots, no logos, no photography. Drawn frames only.
- Nothing key-shaped, credential-shaped, or hostname-shaped ever appears.
- Table and parameter names appear in mono, exactly as spelled in the code.

**Naming** — "Canvas", "the hub", "the institution". No individual is named, no
real hostname, no institution's internal process identified.

---

## SCENES

### B00 — INTRO · title card

> Hi, I am Surya, and this video is about the four documents we wrote to get a
> Canvas integration through a university's security review.

**Shot** — TITLE. "FOUR DOCUMENTS" flush left, display; signal rule above; mono
subtitle `WHAT THE REVIEW ASKED FOR`. Hard snap at frame 6.

---

### B01 — ONE QUESTION, FOUR DOCUMENTS

> We asked for a developer key. The reply was one question — had this completed
> the required FERPA and security reviews. Answering that question honestly took
> four documents, and each one answers a different kind of doubt.

**Shot** — Four bordered cards in a row, appearing 3 frames apart, each with a
number and a short title in mono: `01 SECURITY REVIEW` · `02 FERPA DATA FLOW` ·
`03 ARCHITECTURE AND HOSTING` · `04 HECVAT LITE`. This is the reel's index and
the layout every later beat returns to.

---

### B02 — DOCUMENT ONE · THE SECURITY REVIEW

> The first answers: is the integration itself sound. It walks the login
> endpoint, the key endpoint and the launch endpoint, and states for each one
> what is verified — the signature against Canvas's published keys, the issuer,
> the audience, the expiry, the algorithm pinned so it cannot be talked out of
> checking. Then it does something most review responses avoid. It lists what we
> found wrong and fixed: a legacy endpoint that decoded tokens without verifying
> them, a role check that could be tricked into promoting a student, an open
> registration endpoint, credentials stored unencrypted.

**Shot** — Card 01 lit in signal, the other three dropping to mute. Left column,
what is verified: `SIGNATURE` · `ISS` · `AUD` · `EXP` · `ALG PINNED`. Right
column in signal, headed `FOUND AND FIXED`: four short rows. The two columns
sit side by side deliberately.

---

### B03 — DOCUMENT TWO · FERPA DATA FLOW

> The second answers a different question: not is it secure, but what happens to
> the student. It names the legal basis — we act as a school official under the
> FERPA exception — then lists every field Canvas sends us and why we need it,
> every store it lands in, how long each piece is kept, and every third party
> that touches it. Six subprocessors, named, with what each one receives.

**Shot** — Card 02 lit. A three-column table: `RECEIVED` · `WHY` · `KEPT FOR`,
five rows filling in 3 frames apart. Beneath, a mono strip listing six
subprocessor slots as abstract blocks, with the AI provider's block marked in
signal and labelled `NO IDENTIFIERS`.

---

### B04 — DOCUMENT THREE · ARCHITECTURE AND HOSTING

> The third answers where it all runs. Cloud provider, region, web server,
> runtime, database. And the part reviewers actually care about: backups. Not a
> promise that backups exist — the archiver's own numbers. Continuous
> write-ahead-log archiving, a segment shipped at least every two minutes, a
> hundred and five segments archived, zero failures. That puts recovery at
> roughly two minutes of lost writes.

**Shot** — Card 03 lit. A vertical stack showing the request path: `CANVAS` →
`TLS TERMINATION` → `THE HUB` → `DATABASE`, each with its own arrowhead. To the
right, three measured values in signal: `RPO ≈ 2 MIN` · `105 SEGMENTS` ·
`0 FAILURES`.

---

### B05 — DOCUMENT FOUR · HECVAT LITE

> The fourth is not ours. HECVAT is the standard questionnaire institutions send
> every vendor, so that answers can be compared across products. Product
> overview, data and privacy, encryption, access control, application security,
> AI use, infrastructure and continuity. The value of a standard form is that
> you cannot choose which questions to answer.

**Shot** — Card 04 lit. Seven section labels as mono rows, snapping in 3 frames
apart: `PRODUCT` · `DATA + PRIVACY` · `ENCRYPTION` · `ACCESS CONTROL` ·
`APP SECURITY` · `AI / LLM` · `INFRASTRUCTURE`. Caption in signal:
`A STANDARD FORM — YOU DO NOT PICK THE QUESTIONS`.

---

### B06 — THE ANSWERS THAT ARE NO

> Which is why the most useful answers in that document are the ones that say
> no. We do not hold a SOC 2 certification. We have had no third-party
> penetration test. Administrative multi-factor enrolment is still being
> confirmed. A questionnaire answered entirely in the affirmative is not a
> reassuring document. It is an unread one.

**Shot** — Three rows, each a bordered box with the answer set large in signal:
`SOC 2 — NO` · `THIRD-PARTY PEN TEST — NONE` · `ADMIN MFA — CONFIRMING`.
Beneath, in paper: `ALL YES IS NOT A GOOD SIGN`. Hero frame; holds longest.

---

### B07 — THE ONE STILL OPEN

> And one item stays open across all four. The backup retention window is a
> platform plan setting rather than a database setting, so it cannot be read
> from inside the database. Every document says so, says why, and commits to
> sending it. An open item that is named is not a hole. An open item that is
> quietly omitted is.

**Shot** — A single wide row in signal: `BACKUP RETENTION — STILL CONFIRMING`,
with the reason in mute beneath: `A PLAN SETTING · NOT VISIBLE FROM THE
DATABASE`. All four document cards drawn small above, each with a signal tick,
showing the item appears in every one.

---

### B08 — OUTRO

> Four documents, and none of them describes anything we built for the review.
> They describe what was already true, or what we fixed once someone finally
> asked. That is the whole value of being asked.

**Shot** — The four cards restated in a row, all in paper. Hard cut to the title,
`FOUR DOCUMENTS`, flush left, held to the end.

---

## APPENDIX — CLAIMS AND SOURCES

| # | Beat | Claim | Source |
|---|---|---|---|
| 1 | B01 | Four documents were produced for the review | The four files named in the header |
| 2 | B02 | Security review covers the login, JWKS and launch endpoints and states what each verifies | `medhavy-lti-security-review.md` §1.1–1.3 |
| 3 | B02 | Signature / `iss` / `aud` / `exp` validated, algorithm pinned to RS256 | security review §1.3 |
| 4 | B02 | Remediations listed: legacy endpoint decoding without verification; substring role matching; unauthenticated registration endpoint; credentials stored in plain text | security review §1.3, §2.2, §2.4; HECVAT "Recent remediations" |
| 5 | B03 | FERPA basis is the school-official exception, 34 CFR §99.31(a)(1) | `medhavy-ferpa-data-flow.md` §1 |
| 6 | B03 | Every received field, its purpose, its store and its retention are listed | FERPA data flow §2, §3, §4 |
| 7 | B03 | Six subprocessors named; the AI provider receives no student identifiers | FERPA data flow §5, §6 |
| 8 | B04 | Hosting, region, web server, runtime and database are stated | architecture summary §2, §3 |
| 9 | B04 | WAL archiving on; `archive_timeout = 120s`; RPO ≈ 2 minutes; 105 segments archived, 0 failures | architecture summary §4 |
| 10 | B05 | HECVAT Lite sections answered: product, data/privacy, encryption, access control, app security, AI, infrastructure | `medhavy-hecvat-lite-answers.md` (section headings) |
| 11 | B06 | No SOC 2 held; subprocessors hold SOC 2 attestations | HECVAT "Documentation" |
| 12 | B06 | No third-party penetration test to date; internal review completed and findings remediated | HECVAT "Application security" |
| 13 | B06 | Administrative MFA enrolment status being confirmed | HECVAT "Authentication and access control" |
| 14 | B07 | Backup retention outstanding because it is a plan-level setting, not visible from the database | architecture summary §4; HECVAT "Infrastructure and continuity" |

**Invented values: none.** Every figure traces to a row above.

**Not claimed on camera.** No individual is named — not the professor, not the
reviewer, not the platform engineer. The institution is "a university". No
hostname, no key material, no subprocessor is named aloud, and nothing about the
production environment is claimed: every verified figure was measured on dev.
