# SOURCES — How a Canvas Launch Works

## Narration provenance

All narration is the operator's own approved script text (`script.md`),
reviewed line by line before the build. Kokoro synthesised it verbatim; no
sentence was rewritten, paraphrased, or generated during the build.

## On-camera claims

Every claim and its source is enumerated in `FACTCHECK.md` (15 rows). Sources
are the operator's own documents:

| Document | Used for |
|---|---|
| `medhavy-lti-security-review.md` | OIDC login parameters, JWKS, signature/iss/aud/exp validation, algorithm pinning, state/nonce replay protection, role allow-list, scope removal |
| `medhavy-ferpa-data-flow.md` | The claim list in the `id_token`; nonce and launch-audit retention windows |
| `medhavy-architecture-hosting-summary.md` | Registration model, server-side authorization, data minimisation |
| `medhavi-hub/LTI_1_3_IMPLEMENTATION_GUIDE.md` | Cross-check on endpoint structure |

## Invented values

**None.** Every parameter name and number on screen traces to a FACTCHECK row.

One claim is mechanism rather than measurement and is labelled as such in
`FACTCHECK.md` row 7: that `response_mode=form_post` keeps the token out of
browser history and server logs. The operator's documents confirm the parameter
is used; the consequence is the standard rationale for that parameter, not a
measurement of this system.

## Deliberately excluded

No hostname, no key material, no individual's name, no institution's internal
review process, and no claims about the production environment. Every verified
figure was measured on the dev environment.
