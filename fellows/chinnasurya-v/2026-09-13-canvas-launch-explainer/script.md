# HOW A CANVAS LAUNCH WORKS
### LTI 1.3, end to end — what actually happens when a student clicks your tool

Single-topic explainer. Mechanism only. Source: the Medhavy Canvas LTI 1.3
security & compliance review, the FERPA data-flow doc, the architecture and
hosting summary, and `LTI_1_3_IMPLEMENTATION_GUIDE.md`.

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
- Parameter names appear in mono, exactly as they are spelled in the spec.

**Naming** — "Canvas" and "the tool". No individual is named, no real hostname,
no institution's internal process.

---

## SCENES

### B00 — INTRO · title card

> Hi, I am Surya, and this video is about LTI one point three — what actually
> happens in the seconds between a student clicking a tool inside Canvas and
> that tool knowing who they are.

**Shot** — TITLE. Display "HOW A CANVAS LAUNCH WORKS" flush left, two lines;
signal rule above; mono subtitle `LTI 1.3 · END TO END` below. Hard snap in at
frame 6. Nothing moves after that.

---

### B01 — THE PROBLEM

> A student is inside Canvas, already logged in. They click your tool, which is
> a completely separate application on a different server. It needs to know who
> they are, which course they came from, and whether they are a student or an
> instructor — without asking them to log in a second time, and without simply
> believing whatever the browser tells it.

**Shot** — Two blocks with a gap between them: `CANVAS` left, `YOUR TOOL` right,
both in paper on ground. Three mono questions snap in beneath the gap, 3 frames
apart: `WHO?` · `WHICH COURSE?` · `WHAT ROLE?` The gap itself is the subject.

---

### B02 — REGISTRATION COMES FIRST

> None of this works on the day. Before a single launch, the two sides exchange
> registration details. Canvas issues a client ID and a deployment ID that
> identify your tool. You record Canvas's authorization endpoint and the address
> where it publishes its keys. Canvas records your login endpoint, your redirect
> endpoint, and where you publish yours. Trust is established here, in advance —
> not during the launch.

**Shot** — Two columns, `CANVAS ISSUES` and `THE TOOL REGISTERS`, each with mono
rows snapping in at 3 frames: left `client_id` · `deployment_id` · `auth
endpoint` · `jwks_url`; right `login endpoint` · `redirect_uri` · `jwks
endpoint`. A signal rule spans both at the settle: `TRUST IS SET UP BEFORE THE
FIRST LAUNCH`.

---

### B03 — TWO KEYPAIRS, NO SHARED SECRET

> Each side holds a private key and publishes the matching public key at a JWKS
> endpoint — a JSON Web Key Set. Canvas signs with its private key, and you
> verify with the public key you fetch from Canvas. You sign with yours, and
> Canvas verifies with the one you publish. Neither side ever ships the other a
> password. That is the whole basis of the trust.

**Shot** — Mirrored diagram. Left `CANVAS`: `PRIVATE KEY` (signal) over
`PUBLIC — /jwks` (mute). Right `THE TOOL`: same pair. Two separate straight
arrows cross the middle, each with its own arrowhead — signs one way, verifies
the other. Mono footer: `RS256 · NO SHARED SECRET`.

---

### B04 — MOVE ONE · THE LOGIN CALL

> The launch has four moves. Move one. Canvas calls your login endpoint and
> tells you which platform is calling and which user is arriving. You do not
> trust that yet. You generate a random state and a random nonce, store them on
> your own server, and redirect the browser back to Canvas's authorization
> endpoint, asking for an identity token.

**Shot** — Station `01 LOGIN` in signal, top left, with the other three stations
drawn in mute to its right so the shape of the whole handshake is visible.
Mono rows under station 01: `iss` · `login_hint` · `target_link_uri`, then
below a rule: `state + nonce → STORED SERVER-SIDE` in signal.

---

### B05 — MOVE TWO · THE TOKEN COMES BACK

> Move two. Canvas authenticates the user itself, then posts an identity token
> back to your redirect endpoint. It arrives as a form post, not as a redirect
> with the token in the address bar, so it never lands in a browser history or
> a server log. The token is a JWT — a signed, self-contained statement about
> who this person is.

**Shot** — Station `02` lit in signal, `01` dropping to mute. A single wide
arrow from Canvas to the tool carrying a labelled block `id_token (JWT)`.
Mono line, right: `response_mode = form_post`. Second mono line beneath, in
mute: `NOT IN THE URL · NOT IN THE LOG`.

---

### B06 — WHAT THE TOKEN SAYS

> Inside that token are the claims. A stable user identifier. Name and email.
> The role claim, saying student or instructor. The course context — its ID and
> title. The resource link and custom parameters, which say which piece of
> content they were trying to open. And the protocol fields — deployment ID,
> message type, version — that let you confirm the launch is the shape you were
> expecting.

**Shot** — The token drawn as a tall stack of mono rows, each a filled
rectangle, snapping in at 3 frames: `sub` · `name` · `email` · `roles` ·
`context` · `resource_link` · `custom` · `deployment_id` · `message_type` ·
`version`. A right-hand column gives the plain-English purpose of each. This is
the reel's densest frame and it holds longest.

---

### B07 — MOVE THREE · VERIFY

> Move three, and this is the one that matters. Verification is four separate
> checks, not one. Validate the signature against the public keys Canvas
> publishes. Check the issuer — that it came from the platform you registered.
> Check the audience — that it was meant for you. Check the expiry. And pin the
> algorithm to RS256, so nobody can hand you a token that asks to be trusted
> without a signature at all.

**Shot** — Station `03` lit. Four mono rows, each with a filled signal square
snapping in at 3 frames: `SIGNATURE — RS256 vs CANVAS JWKS` · `ISS` · `AUD` ·
`EXP`. A fifth row drops below a rule, in signal: `ALG PINNED — RS256`.

---

### B08 — MOVE FOUR · AND ONLY ONCE

> Move four. The state and nonce you stored back at move one are checked against
> what came back, and consumed on read. A captured launch cannot be replayed,
> because the second attempt finds nothing left to match. Nonces live ten
> minutes. Launch records are kept for one hour, then purged.

**Shot** — The same launch drawn twice, stacked. Top: `LAUNCH 01 → MATCH → OK`
in paper. Bottom: `LAUNCH 01 REPLAYED → NO MATCH → REJECTED`, rejection in
signal. Two mono data rows, right-aligned: `NONCE — 10 MIN` · `LAUNCH AUDIT —
1 HR`.

---

### B09 — WHAT YOU DO WITH IT

> Only now do you act on it. The role is matched against a list of official role
> identifiers, so a student is a student. Access is evaluated on your server on
> every request, never asserted by the browser. And the tool asks for no grade
> or roster permissions at all — so it cannot read a gradebook or a class list,
> because it never requested the right to.

**Shot** — Three stacked bands, each snapping at 3 frames: `ROLE → OFFICIAL
IDENTIFIER LIST` · `ACCESS → EVALUATED SERVER-SIDE` · `SCOPES → NONE FOR GRADES
OR ROSTER`. Third band's label sits in signal.

---

### B10 — OUTRO

> So that is LTI one point three. Not a password shared between two systems, but
> two keypairs registered in advance, a signed statement passed once, verified
> four ways, and spent. The launch is not where the trust comes from. The
> registration is. The launch is just where it gets used.

**Shot** — Four mono rows snapping in at 3 frames: `REGISTER` · `SIGN` ·
`VERIFY` · `SPEND`. Hard cut to the title restated, `HOW A CANVAS LAUNCH
WORKS`, flush left, held to the end.

---

## APPENDIX — CLAIMS AND SOURCES

Every figure spoken or shown, and where it comes from.

| # | Beat | Claim | Source |
|---|---|---|---|
| 1 | B02 | Platform registration precedes launch: `client_id`, deployment id, Canvas auth endpoint, `jwks_url`, tool login/redirect/JWKS endpoints | security review §1.1, §1.2; architecture §6 |
| 2 | B03 | Tool publishes its public RSA key set in JWKS format at its own endpoint; Canvas's keys resolved from the registered `jwks_url` | security review §1.2, §1.3 |
| 3 | B04 | Login endpoint generates a cryptographically random `state` and `nonce`, stored server-side before redirect | security review §1.1 |
| 4 | B04 | Redirect carries `client_id`, `redirect_uri`, `state`, `nonce`, `scope=openid`, `response_type=id_token`, `login_hint`, `response_mode=form_post` | security review §1.1 |
| 5 | B05 | The `id_token` arrives as a POST to the launch endpoint | security review §1.3 |
| 6 | B06 | Claims consumed: user identifier (`sub`), name, email, role claim, course context (id, title), resource link + custom parameters, deployment id, message type, LTI version | FERPA data-flow §2 |
| 7 | B07 | RS256 signature validated against Canvas's published JWKS; `iss`, `aud`, `exp` all validated; algorithm pinned to RS256 | security review §1.3; architecture §6 |
| 8 | B08 | `state` and `nonce` validated and consumed delete-on-read, so a launch cannot be replayed | security review §1.3; architecture §6 |
| 9 | B08 | Nonce/state retention 10 minutes; launch audit records 1 hour, then purged | FERPA data-flow §4 |
| 10 | B09 | Roles matched against an allow-list of official IMS role URNs, exact identifier match | security review §1.3; architecture §6 |
| 11 | B09 | Authorization evaluated server-side on every request; the client cannot assert its own access | architecture §6; FERPA data-flow §7 |
| 12 | B09 | No AGS (`lineitem`, `result.readonly`, `score`) and no NRPS (`contextmembership.readonly`) scopes requested; cannot read gradebook or roster | security review §2.1; architecture §8 |

**Deliberately not in this cut.** The two security findings from the review —
the legacy endpoint that decoded rather than verified, and the substring role
match that would have escalated a student — are held back for a possible second
video. The earlier draft covering them is kept at `script-findings-v1.md`.

**Not claimed on camera.** No hostname, no key material, no individual's name,
no institution's internal review process, nothing about production. Every
verified figure traces to a measurement made on the dev environment.

**Invented values: none.** Every number and parameter name on screen traces to a
row above. The B05 claim that a form post keeps the token out of browser history
and server logs is the standard rationale for `response_mode=form_post`, stated
as mechanism rather than as a measured finding.
