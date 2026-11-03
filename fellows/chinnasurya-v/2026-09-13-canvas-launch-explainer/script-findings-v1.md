# VERIFY, NOT DECODE
### What it takes to trust a Canvas launch — and three places ours didn't

Single-topic explainer. Source: the Medhavy Canvas LTI 1.3 security & compliance
review, the FERPA data-flow doc, and the architecture/hosting summary.

---

## ART DIRECTION

**Script-native brutalism.** Not the ai-explainer chassis. No Claude branding.

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
Content fills the frame; empty ground is not minimalism here, it is a defect.

**Hard rules**

- Hard cuts only. No easing, no interpolation, no fades between states.
- `border-radius: 0`. Boxes are drawn as filled rectangles.
- Arrows are straight segments plus a filled triangle. N sources converging on
  one target means N separate arrowheads, never a merged bus.
- The visible grid is part of the look: mute blended over ground at ~12%.
- No screenshots, no logos, no photography. Drawn frames only.
- Nothing key-shaped, credential-shaped, or hostname-shaped ever appears.

**Naming** — the institution is "Canvas" / "the university". No individual is
named. No real hostname on screen.

---

## SCENES

### B00 — INTRO · title card

> Hi, I am Surya, and this video is about verifying a Canvas launch — how an
> LTI one point three integration proves that a token is real, and three places
> where ours did not.

**Shot** — TITLE. Display "VERIFY, NOT DECODE" flush left; signal rule above it;
mono subtitle below. One hard snap in at frame 6. Nothing moves after that.

---

### B01 — THE STAKE

> When a student clicks your tool inside Canvas, Canvas hands your application a
> signed token that says who they are and what course they are in. Everything
> after that — what they can open, what role they hold — rests on a single
> question. Is this token real? Answering that badly is how a student becomes
> an instructor.

**Shot** — Two blocks: CANVAS on the left, YOUR TOOL on the right, one straight
arrow between them carrying a labelled token. The question "IS THIS TOKEN REAL?"
snaps on in signal beneath the arrow, 6-frame snap, held.

---

### B02 — THE HANDSHAKE

> The handshake has four moves. Canvas calls your login endpoint. You generate a
> random state and nonce, store them on the server, and redirect to Canvas's
> authorization endpoint. Canvas posts back an identity token. You verify it.
> Only then do you know who is standing in front of you.

**Shot** — Four numbered stations, left to right, revealed one at a time with
3-frame snaps: `01 LOGIN` · `02 STATE + NONCE STORED` · `03 ID_TOKEN POSTED` ·
`04 VERIFIED`. Each station gets its own arrowhead. Settled state holds longest.

---

### B03 — WHAT VERIFICATION MEANS

> Verification is four separate checks, not one. Validate the RS256 signature
> against the public keys Canvas publishes at its JWKS endpoint. Check the
> issuer. Check the audience. Check the expiry. And pin the algorithm to RS256,
> so that nobody can hand you a token asking to be verified with no algorithm
> at all.

**Shot** — Checklist, four rows, mono, each with a filled signal square snapping
in at 3 frames: `SIGNATURE / RS256 vs JWKS` · `ISS` · `AUD` · `EXP`. A fifth row
in signal drops below the rule: `ALG PINNED — RS256`.

---

### B04 — REPLAY

> Then there is replay. The state and nonce you stored at login are validated
> and consumed delete-on-read. A captured launch cannot be replayed, because the
> second attempt finds nothing left to match against. Nonces live ten minutes.
> Launch records live one hour.

**Shot** — Same launch drawn twice, stacked. Top: `LAUNCH 01 → MATCH → OK`.
Bottom: `LAUNCH 01 REPLAYED → NO MATCH → REJECTED`, the rejection in signal.
Two mono data rows right-aligned: `NONCE 10 MIN` · `LAUNCH AUDIT 1 HR`.

---

### B05 — FINDING 01

> Finding one. A legacy launch endpoint decoded the token instead of verifying
> it. Decode reads the claims. Verify checks the signature. That endpoint did
> the first and never did the second. It also generated its state and nonce with
> Math dot random, and never stored them. It has been deleted, and every
> reference repointed.

**Shot** — Hard-cut card: `FINDING 01` in signal, top left. Two facing columns,
mono: `decode()` → `reads the claims` / `verify()` → `checks the signature`.
The word `DELETED` strikes across the left column in signal at the settle.

---

### B06 — FINDING 02

> Finding two. Role matching was substring based. Canvas sends a role string,
> and the code asked whether that string contained the word Instructor. A
> crafted role reading Not An Instructor Really contains it. That escalates a
> student. Roles are now matched against an allow-list of official role
> identifiers, compared exactly, with tests that assert escalation attempts
> fail closed.

**Shot** — `FINDING 02`. The string `NotAnInstructorReally` set large in mono,
with the substring `Instructor` highlighted in signal inside it. Below, two
rows: `SUBSTRING MATCH → INSTRUCTOR` (signal) and `EXACT MATCH, ALLOW-LIST →
DENIED` (paper). The hero frame of the reel — it holds longest.

---

### B07 — ASK FOR LESS

> The third fix was asking for less. The tool no longer requests grade services
> or roster services. It cannot read the gradebook and it cannot read the class
> list, because it never asks for the scopes that would let it. A permission you
> do not hold cannot leak.

**Shot** — Four scope chips in mute, struck through one at a time with 3-frame
snaps: `lineitem` · `result.readonly` · `score` · `contextmembership.readonly`.
Closing line flush left in paper: `NOT REQUESTED. NOT READABLE.`

---

### B08 — WHAT IS LEFT

> What is left is deliberately small. A user link, a course link, an access
> grant, a launch audit record. Row level security is enabled on all eleven LTI
> tables and restricted to the backend service role — non-service roles are
> denied reads and writes. Tokens issued to a textbook are signed, scoped to
> that one textbook, and expire in twenty-four hours.

**Shot** — Four stacked table rows in mono, then a full-width rule, then the
data line `RLS: 11/11 TABLES · SERVICE ROLE ONLY` in signal. Right column holds
`TOKEN — SIGNED · ONE TEXTBOOK · 24 H`.

---

### B09 — OUTRO

> An integration is not finished when the launch works. A launch that works only
> proves the happy path. It is finished when a forged token fails, a replayed
> launch fails, and a crafted role fails. That is the difference between
> something that runs, and something you can put in front of students.

**Shot** — Three rows snapping in at 3 frames each, all in signal:
`FORGED → FAILS` · `REPLAYED → FAILS` · `CRAFTED ROLE → FAILS`. Then a hard cut
to the title restated, `VERIFY, NOT DECODE`, flush left, held to the end.

---

## APPENDIX — CLAIMS AND SOURCES

Every figure that appears on screen or is spoken, and where it comes from.

| # | Beat | Claim | Source |
|---|---|---|---|
| 1 | B02 | OIDC login generates and server-stores a random `state` + `nonce` before redirect | security review §1.1 |
| 2 | B03 | RS256 signature validated against Canvas's published JWKS; `iss`/`aud`/`exp` checked; algorithm pinned to RS256 | security review §1.3 |
| 3 | B04 | `state`/`nonce` validated and consumed delete-on-read, so a launch cannot be replayed | security review §1.3 |
| 4 | B04 | Nonce retention 10 minutes; launch audit records 1 hour | FERPA data-flow §4 |
| 5 | B05 | Legacy `/api/lti/launch` used `decode()` not `verify()` — no signature verification; `Math.random()` for `state`/`nonce`, never stored; endpoint deleted and references repointed | security review §1.3 |
| 6 | B06 | Role matching was substring-based; a value such as `NotAnInstructorReally` would have escalated a student | security review §1.3 |
| 7 | B06 | Now matched against an allow-list of official IMS role URNs, exact identifier match, with unit tests asserting escalation fails closed | security review §1.3 |
| 8 | B07 | AGS (`lineitem`, `result.readonly`, `score`) and NRPS (`contextmembership.readonly`) scopes removed; tool cannot read gradebook or roster | security review §2.1 |
| 9 | B08 | RLS enabled on all 11 LTI tables, restricted to the backend service role; non-service roles denied reads and writes | security review §2.4 |
| 10 | B08 | Textbook access tokens are signed, scoped to a single textbook, 24-hour expiry | security review §2.4 |

**Discrepancy, stated on the record.** Working notes during the build referred to
"10 `lti_*` tables"; the verified review says RLS was confirmed on **11** LTI
tables. The script uses eleven and cites the verified review. If ten is correct,
change it in B08 narration and re-generate that beat's audio.

**Not claimed on camera.** No hostname, no key material, no individual's name,
no institution's security posture beyond what this project itself implements.
Nothing about the production environment — every verified figure above was
measured on the dev environment.

**Invented values: none.** Every number on screen traces to a row above.
