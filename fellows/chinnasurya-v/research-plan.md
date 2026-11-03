# Research and Project Plan — November 2026 to January 2027

## Where the project stands

The Canvas LTI 1.3 integration for the Medhavy Hub works end to end against a
local Canvas instance: OIDC login, JWKS, and a callback that verifies the
`id_token` signature against Canvas's published keys, checks issuer, audience and
expiry, pins the algorithm, and consumes `state` and `nonce` so a launch cannot be
replayed. Roles are matched against an allow list of official IMS role URNs. The
tool requests no gradebook and no roster scopes.

What it is waiting on is not code. Northeastern IT needs to approve the developer
key, which means passing a FERPA and security review. I produced the security and
data-handling document for that review on 15 October.

## Next period

**1. Finish the security review loop with Northeastern IT.**
Carry the review document through IT's questions, complete a HECVAT Lite if they
send one, and get the dev developer key issued. Then register the Northeastern
platform in the dev database using the Client ID and Deployment ID IT returns, and
verify a real launch from Northeastern Canvas rather than from local Docker.

**2. Close the gaps my own audit found.**
Re-auditing the integration against the review document turned up defects the
document did not reflect. Three are mine to fix:

- The access verification endpoint short-circuits on an instructor role and
  bypasses the per-course scoping, so an instructor still reaches private
  textbooks outside their own courses. The scoping itself is correct in
  `lib/textbook-manager.ts`; the bypass is in the verify route.
- Token verification falls back to decoding an unverified base64 payload when
  signature verification fails. That fallback exists for tokens minted before
  `JWT_SECRET` was configured and needs removing.
- Launch audit retention is stated three different ways: one hour in the schema,
  twelve months in the published privacy policy, and the cleanup job is not
  actually scheduled. One number, enforced, and the privacy policy corrected to
  match.

**3. Close the two defects the reel research turned up.**
Researching "What Actually Crosses" against the code rather than against the
documents surfaced two things the documents do not describe:

- `app/api/lti/self-register/route.ts` holds a second, dormant Canvas-config
  generator that still lists all four AGS and NRPS scopes. The route returns 403
  unless `LTI_SELF_REGISTRATION_ENABLED=true`, so it is unreachable in normal
  operation, but the data-minimisation change was applied to only one of the two
  config generators. Both should say the same thing.
- The live config advertises `assignment_selection` and `link_selection`
  placements whose `target_link_uri` is `/api/lti/deep-linking`. No such route
  exists. `course_navigation` points at `/api/lti/callback`, which does exist,
  which is why testing passes and this went unnoticed. Either build the route or
  drop the placements.

**4. Verify the launch survives Canvas's iframe.**
The course navigation placement sets no window target, and Canvas defaults that
placement to a cross-origin iframe, while the Hub sends
`X-Frame-Options: SAMEORIGIN` on the page the callback redirects to. This needs
testing against real Canvas, and if it fails, replacing the header with a
Content-Security-Policy `frame-ancestors` directive naming the Canvas domain.

**5. Ship the quiz backend.**
The quiz schema and APIs are built on a branch off `development` and are type
clean. They need their own pull request, access scoping tied to the same identity
path as the textbook routes, and tests.

**6. Keep producing weekly Brutalist reels.**
Four are now rendered. The project has more topics that deserve reels than I have
produced, and the next ones should be built in the week they are scripted rather
than six weeks later. One reel a week, film-as-code record in this folder, render
on Drive. The first candidates are the instructor-scoping fix and the launch
audit retention reconciliation, both of which are worth explaining once they are
real.

## Deliverables and dates

| Target | Deliverable |
|---|---|
| 2026-11-30 | The three code fixes merged, with tests, plus the two defects the reel research found. Retention reconciled to one enforced number and the privacy policy corrected to match. Iframe behaviour verified against real Canvas |
| 2026-12-31 | Developer key issued and a real Northeastern Canvas launch verified end to end, or a written account of what IT is still blocking on. Quiz backend pull request merged |
| 2027-01-31 | Instructor and student flows verified against a real course. Weekly reels continued. Written report on what the LTI integration taught about shipping into an institution's compliance process |

## Reporting changes I am making

Dated weekly time records from 1 November, one dated file per week in `weekly-hours/`, written
in the week rather than reconstructed. `FRICTIONAL.md` appended as the work
happens. Every renewal claim will have a clickable artifact behind it.

## Open issues

- Supabase plan tier and backup retention window are unconfirmed. The account
  owner has them; I do not have dashboard access to the project.
- No third-party penetration test, no SOC 2 for Medhavy itself, and no VPAT.
  Accessibility is the one a university is most likely to press on, and nobody has
  checked the textbook reader against WCAG.
