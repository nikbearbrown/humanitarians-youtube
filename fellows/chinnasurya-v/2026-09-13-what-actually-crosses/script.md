# WHAT ACTUALLY CROSSES
### Canvas and the hub: what moves between them, and what deliberately does not

Single-topic explainer. This is the "how does sync work" research, done against
the code. Source: `medhavi-hub/lib/lti-utils.ts`, `app/api/lti/*`,
`app/api/quizzes/[id]/submit/route.ts`, `db-migrations/04_quizzes.sql`, and
`medhavy-lti-security-review.md` §2.1.

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

> Hi, I am Surya, and this video is about what actually moves between Canvas and
> our hub — which turns out to be far less than the word integration suggests.

**Shot** — TITLE. "WHAT ACTUALLY CROSSES" flush left; signal rule above; mono
subtitle `CANVAS ↔ HUB`. Hard snap at frame 6.

---

### B01 — THE ASSUMPTION

> It is easy to assume that integrating two systems means synchronising them.
> Two things connected, therefore kept in step. Rosters flowing one way, grades
> flowing back the other. That is not what we built, and the difference is a
> decision, not an omission.

**Shot** — Two blocks, `CANVAS` and `THE HUB`, with a thick two-headed arrow
between them drawn in mute and then struck through in signal. Caption beneath:
`THE ASSUMPTION`.

---

### B02 — ONE THING CROSSES

> Exactly one thing crosses from Canvas to us, and only when a student clicks.
> The launch token. It carries who they are, which course they are in, what role
> they hold, and what they clicked. Nothing arrives on a schedule. Nothing is
> fetched in the background. If nobody clicks, nothing moves.

**Shot** — `CANVAS` and `THE HUB` again, but now one single arrow, left to
right, carrying a labelled block `LAUNCH TOKEN`. Three mono lines beneath, 3
frames apart: `ON CLICK — NOT ON A SCHEDULE` · `NO BACKGROUND FETCH` ·
`NO CLICK, NO DATA`.

---

### B03 — THE DATABASE FILLS LAZILY

> The links are built out of that, as it happens. The first time a person
> launches, we record the correspondence between their Canvas identifier and
> ours. Same for the course. So the database fills up as people arrive. It is
> never a copy of Canvas made in advance.

**Shot** — Three rows appearing one at a time, 3 frames apart, under the heading
`lti_user_links`, each row a pair of abstract identifiers joined by an arrow.
Caption in signal: `WRITTEN ON ARRIVAL — NEVER PRE-COPIED`.

---

### B04 — THE TWO SERVICES WE DID NOT TAKE

> LTI does have services for real synchronisation. Names and Role Provisioning
> reads the class roster. Assignment and Grade Services writes to the gradebook.
> Both are permissions you request when you register the tool. We request
> neither. Not disabled somewhere in the code — never asked for. The tool cannot
> read a class list or write a grade, because it holds no permission to.

**Shot** — Two bordered cards, both struck through in signal: `NAMES AND ROLE
PROVISIONING — reads the roster` and `ASSIGNMENT AND GRADE SERVICES — writes the
gradebook`. Beneath, the live config line in mono: `scopes: []`. Closing line:
`NEVER REQUESTED · NOT MERELY DISABLED`.

---

### B05 — THE ONE PATH BACK

> There is one route that runs the other way, and it is configured. Deep
> linking. An instructor picks a piece of content from inside Canvas, our tool
> hands back a pointer to it, and Canvas stores that pointer in the course. That
> is the only tool-to-platform message we carry.

**Shot** — A single arrow, right to left this time, from `THE HUB` to `CANVAS`,
carrying a block labelled `CONTENT POINTER`. Mono caption:
`LtiDeepLinkingRequest`. Everything else on the frame in mute, so the direction
reads immediately.

---

### B06 — THE HONEST GAP

> Which leaves a gap worth naming out loud. We built quizzes. Grading runs on
> our server — the client never sends a score. But with no grade service, a
> score has nowhere to go. It sits in our database and never reaches the Canvas
> gradebook. The code is honest about it: there is a comment marking the exact
> place where a background job would push it, and that job does not exist yet.

**Shot** — A short pipeline, left to right: `QUIZ SUBMITTED` → `GRADED SERVER
SIDE` → `STORED` → then a hard stop: a filled signal block reading `NO ROUTE TO
THE GRADEBOOK`. The arrow after it is drawn and then absent. Hero frame; holds
longest.

---

### B07 — THE REAL QUESTION

> So the research question was never how synchronisation works. It is whether we
> want it. Turning on grade passback means asking for a permission we removed
> deliberately, and reopening the data conversation we just finished having. It
> is a decision about scope, not a missing function.

**Shot** — Two options as facing cards: `KEEP IT CLOSED — no roster, no grades,
smallest surface` and `OPEN IT — request AGS, reopen the data review`. Neither
is marked as correct. Caption beneath, in signal: `A DECISION — NOT A TODO`.

---

### B08 — OUTRO

> So here is the honest description, as of today. One token, per click, one
> direction. One content pointer going back. Nothing else crosses.

**Shot** — Three mono rows, each snapping at 3 frames: `ONE TOKEN · PER CLICK ·
ONE DIRECTION` · `ONE CONTENT POINTER BACK` · `NOTHING ELSE`. Hard cut to the
title restated, held.

---

## APPENDIX — CLAIMS AND SOURCES

| # | Beat | Claim | Source |
|---|---|---|---|
| 1 | B02 | The launch token is the only Canvas→hub transfer, and it arrives on click | `app/api/lti/callback/route.ts`; no scheduled job or background fetch exists in `app/api/lti/*` |
| 2 | B02 | The token carries user identifier, course context, role and resource link | `medhavy-ferpa-data-flow.md` §2 |
| 3 | B03 | User and course links are written at launch, not pre-populated | `02_lti_multi_tenant_schema.sql`; links are created during callback handling |
| 4 | B04 | NRPS reads the roster; AGS writes the gradebook; both are registration-time scopes | LTI 1.3 specification (IMS Global), scope URNs as used in the codebase |
| 5 | B04 | The live Canvas configuration requests no scopes | `lib/lti-utils.ts` — `scopes: []`, with the data-minimisation comment above it |
| 6 | B04 | AGS/NRPS scopes were removed deliberately | `medhavy-lti-security-review.md` §2.1 |
| 7 | B05 | Deep linking is configured as the tool→platform message | `lib/lti-utils.ts` placements — `message_type: 'LtiDeepLinkingRequest'`; `lib/lti-validation.ts` allows `LtiDeepLinkingRequest` |
| 8 | B06 | Quiz grading is server-side; the client never submits a score | `lib/quiz/grading.ts` header comment and implementation |
| 9 | B06 | No grade reaches the Canvas gradebook; the push is designed but unbuilt | `app/api/quizzes/[id]/submit/route.ts` lines 22–23: a comment describing a future `grade_sync_status = 'pending'` and an AGS background job |

**Open question, stated as open.** Whether to request AGS and re-enable grade
passback is a scope decision that reopens the data review. B07 presents it as a
decision with two options and does not recommend one. Nothing in this reel claims
a sync mechanism exists that does not.

**Two code findings surfaced by this research, deliberately kept off camera**
(they belong in a ticket, not a video):

1. `app/api/lti/self-register/route.ts` contains a second, dormant Canvas-config
   generator that still lists all four AGS/NRPS scopes. The route returns 403
   unless `LTI_SELF_REGISTRATION_ENABLED=true`, so it is unreachable in normal
   operation — but the data-minimisation change was applied to only one of the
   two config generators.
2. The live config advertises `assignment_selection` and `link_selection`
   placements whose `target_link_uri` is `/api/lti/deep-linking`. No such route
   exists under `app/api/lti/`. The `course_navigation` placement points at
   `/api/lti/callback`, which does exist — which is why testing passes.

**Invented values: none.**
