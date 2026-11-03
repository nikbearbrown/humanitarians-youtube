# FACTCHECK — What Actually Crosses

Every on-screen and spoken claim, with the source it came from. Sources are the
operator's own code and documents. **Invented values: none.**

| # | Beat | Claim | Source | Status |
|---|---|---|---|---|
| 1 | B02 | The launch token is the only Canvas to hub transfer, and it arrives on click | `app/api/lti/callback/route.ts`; no scheduled job or background fetch exists anywhere under `app/api/lti/*` | VERIFIED |
| 2 | B02 | The token carries user identifier, course context, role and resource link | `medhavy-ferpa-data-flow.md` §2 | VERIFIED |
| 3 | B03 | User and course links are written at launch, not pre-populated | `02_lti_multi_tenant_schema.sql`; links are created during callback handling | VERIFIED |
| 4 | B04 | NRPS reads the roster, AGS writes the gradebook, and both are registration-time scopes | LTI 1.3 specification (IMS Global); the scope URNs as used in the codebase | VERIFIED |
| 5 | B04 | The live Canvas configuration requests no scopes | `lib/lti-utils.ts` — `scopes: []`, with the data-minimisation comment above it | VERIFIED |
| 6 | B04 | The AGS and NRPS scopes were removed deliberately | `medhavy-lti-security-review.md` §2.1 | VERIFIED |
| 7 | B05 | Deep linking is configured as the tool to platform message | `lib/lti-utils.ts` placements — `message_type: 'LtiDeepLinkingRequest'`; `lib/lti-validation.ts` admits `LtiDeepLinkingRequest` | VERIFIED |
| 8 | B06 | Quiz grading is server side and the client never submits a score | `lib/quiz/grading.ts` header comment and implementation | VERIFIED |
| 9 | B06 | No grade reaches the Canvas gradebook, and the push is designed but unbuilt | `app/api/quizzes/[id]/submit/route.ts` lines 22-23: a comment describing a future `grade_sync_status = 'pending'` and an AGS background job | VERIFIED |

## The open question, stated as open

Whether to request AGS and enable grade passback is a scope decision that reopens
the data review. B07 presents it as two options and recommends neither. Nothing
in this reel claims a synchronisation mechanism exists that does not.

## Two code findings surfaced by this research, deliberately kept off camera

They belong in a ticket, not in a video.

1. `app/api/lti/self-register/route.ts` holds a second, dormant Canvas-config
   generator that still lists all four AGS and NRPS scopes. The route returns 403
   unless `LTI_SELF_REGISTRATION_ENABLED=true`, so it is unreachable in normal
   operation, but the data-minimisation change was applied to only one of the two
   config generators.
2. The live config advertises `assignment_selection` and `link_selection`
   placements whose `target_link_uri` is `/api/lti/deep-linking`. No such route
   exists under `app/api/lti/`. The `course_navigation` placement points at
   `/api/lti/callback`, which does exist, which is why testing passes.

Both are recorded in the project's research plan as work for the next period.
