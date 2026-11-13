# TEN PREFIXES, ELEVEN TABLES
### The schema behind a Canvas integration, and why the count disagreed

Single-topic explainer. Source: `medhavi-hub/db-migrations/02_lti_multi_tenant_schema.sql`,
`03_lti_v1_credentials.sql`, `05_lti_multi_tenant_rls.sql`, and
`medhavy-lti-security-review.md`.

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

> Hi, I am Surya, and this video is about the database behind a Canvas
> integration — eleven tables, what each one is for, and a count that looked
> like a mistake and was not.

**Shot** — TITLE. "TEN PREFIXES" / "ELEVEN TABLES" flush left; signal rule above;
mono subtitle `THE LTI SCHEMA`. Hard snap at frame 6.

---

### B01 — THREE JOBS

> The schema does three jobs, and nothing else. It remembers who is allowed to
> launch. It maps Canvas's idea of a person onto ours. And it forgets things, on
> a timer, on purpose.

**Shot** — Three full-width bands snapping in at 3 frames: `01 WHO MAY LAUNCH` ·
`02 MAP IDENTITY` · `03 FORGET, ON A TIMER`. The third band in signal.

---

### B02 — WHO MAY LAUNCH

> Two tables answer the first. Platform registrations holds every Canvas
> instance we trust — its client identifier, its issuer, where it publishes its
> keys. Deployments holds the specific installation inside that instance.
> Together they are the guest list. A launch from something not in these tables
> is not a launch. It is a stranger.

**Shot** — Two mono table cards side by side, each a bordered box with the table
name in paper and its purpose in mute: `lti_platform_registrations` / `which
Canvas instances we trust`, `lti_deployments` / `which installation inside it`.
Beneath, in signal: `NOT IN HERE = NOT A LAUNCH`.

---

### B03 — MAPPING IDENTITY

> Three tables answer the second. User links maps a Canvas subject identifier to
> a user in our system. Course links maps a Canvas course to ours. Resource
> links maps the specific thing that was clicked. Which means we do not store a
> Canvas person at all. We store a correspondence between two identifiers.

**Shot** — Three rows, each drawn as `CANVAS SIDE` → arrow → `OUR SIDE`, with
the table name in mono between them: `lti_user_links` · `lti_course_links` ·
`lti_resource_links`. Three separate arrowheads, never merged. Closing line in
signal: `A CORRESPONDENCE — NOT A COPY`.

---

### B04 — TABLES THAT FORGET

> Two tables exist in order to forget. The nonce store holds the one-time values
> from a login, for ten minutes. Launch sessions holds the audit record of a
> launch, for one hour. Then both are purged. A table whose job is to expire is
> doing security work, not bookkeeping.

**Shot** — Two cards with a countdown treatment: `lti_nonce_store` / `10 MIN` and
`lti_launch_sessions` / `1 HR`, the durations large in signal. Beneath, in mute:
`THEN PURGED`. Hero frame; holds longest.

---

### B05 — THE LEGACY THREE

> Three more carry the older protocol — credentials, nonces and launches for
> LTI one point one. The same three shapes, an older handshake, kept for
> platforms that have not moved yet.

**Shot** — Three mono rows in mute, visually set back from the others:
`lti_v1_credentials` · `lti_v1_nonces` · `lti_v1_launches`. A label to the side
in mute: `OLDER HANDSHAKE · SAME SHAPES`.

---

### B06 — TEN AND ELEVEN

> Which brings us to a number that looked like an error. Our working notes said
> ten tables. The security review said eleven. Both were correct. Ten tables
> carry the LTI prefix. Eleven have row level security switched on — those ten,
> plus the institutions table, which belongs to the same schema but is not
> prefixed. The count depended on whether you were counting names, or counting
> protections.

**Shot** — Two large numerals side by side in display type: `10` and `11`, with
mono captions beneath: `TABLES NAMED lti_*` and `TABLES WITH RLS ENABLED`.
Between them, in signal: `+ institutions`. Closing line: `COUNTING NAMES vs
COUNTING PROTECTIONS`.

---

### B07 — OUTRO

> Row level security is on all eleven, restricted to the backend service role,
> and a non-service role is denied both reads and writes. The schema is small
> deliberately. Every table it does not have is a table that cannot leak.

**Shot** — `RLS — 11/11 · SERVICE ROLE ONLY` in signal, full width. Beneath:
`NON-SERVICE ROLE — DENIED READ, DENIED WRITE`. Hard cut to the title restated,
held to the end.

---

## APPENDIX — CLAIMS AND SOURCES

| # | Beat | Claim | Source |
|---|---|---|---|
| 1 | B02 | `lti_platform_registrations` and `lti_deployments` hold trusted platforms and their installations | `02_lti_multi_tenant_schema.sql` lines 19, 42 |
| 2 | B03 | `lti_user_links`, `lti_course_links`, `lti_resource_links` map Canvas identifiers onto the hub's | `02_lti_multi_tenant_schema.sql` lines 55, 73, 91 |
| 3 | B04 | `lti_nonce_store` and `lti_launch_sessions` exist and are purged | `02_lti_multi_tenant_schema.sql` lines 111, 135 |
| 4 | B04 | Nonce retention 10 minutes; launch audit 1 hour | `medhavy-ferpa-data-flow.md` §4 |
| 5 | B05 | `lti_v1_credentials`, `lti_v1_nonces`, `lti_v1_launches` carry LTI 1.1 | `03_lti_v1_credentials.sql` lines 3, 18, 30 |
| 6 | B06 | 10 tables carry the `lti_` prefix | Count of the 7 in `02_…` plus the 3 in `03_…` |
| 7 | B06 | 11 tables have RLS enabled — the 10 plus `institutions` | `05_lti_multi_tenant_rls.sql` lines 16–23 (8 tables incl. `institutions`) + `03_lti_v1_credentials.sql` lines 46–48 (3 tables) |
| 8 | B07 | RLS restricted to the backend service role; non-service roles denied reads and writes | `medhavy-lti-security-review.md` §2.4 |

**Count resolution.** The "10 vs 11" discrepancy flagged in the first video is
resolved here and the resolution is itself on camera: both numbers were right,
counting different things. Row 7 shows the arithmetic — 8 + 3 = 11 with RLS, of
which 10 carry the prefix.

**Invented values: none.** Every table name on screen is copied from a migration
file. No column contents, no sample rows, no identifiers appear.
