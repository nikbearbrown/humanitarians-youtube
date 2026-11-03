# FACTCHECK — How a Canvas Launch Works

Status: **every on-camera claim traced to a source document.** Sources are the
operator's own Canvas LTI 1.3 security & compliance review, FERPA data-flow doc,
and architecture & hosting summary. All verified figures were measured on the
dev environment; nothing about production is claimed.

| # | Beat | Claim (as spoken / shown) | Verdict | Source | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02 | Registration precedes launch: Canvas issues `client_id` and deployment id; tool records Canvas's authorization endpoint and `jwks_url`; Canvas records the tool's login, redirect and JWKS endpoints | ✅ PASS | security review §1.1, §1.2; architecture §6 | — |
| 2 | B03 | Each side holds a private key and publishes the public key at a JWKS endpoint; tool publishes a valid RS256 key set; Canvas's keys resolved from the registered `jwks_url` | ✅ PASS | security review §1.2 ("live and serving a valid RS256 key"), §1.3 | — |
| 3 | B03 | No shared secret between the two sides | ✅ PASS | Follows from asymmetric RS256 signing per §1.3; no shared-secret mechanism appears anywhere in the implementation | — |
| 4 | B04 | Login endpoint generates a cryptographically random `state` and `nonce` and stores them server-side before redirecting | ✅ PASS | security review §1.1 ("both cryptographically random, stored server-side before the redirect") | — |
| 5 | B04 | Canvas's login call carries `iss`, `login_hint`, `target_link_uri` | ✅ PASS | security review §1.1 | — |
| 6 | B05 | The `id_token` is POSTed back to the launch endpoint; `response_mode=form_post` | ✅ PASS | security review §1.1 (parameter), §1.3 ("accepts the POST carrying the `id_token` JWT") | — |
| 7 | B05 | A form post keeps the token out of browser history and server logs | ⚠️ MECHANISM | This is the standard rationale for `response_mode=form_post` — a property of the parameter, not a measurement of this system. Spoken as mechanism | If challenged, soften to "so it is not carried in the address bar" |
| 8 | B06 | Claims consumed: `sub`, name, email, roles, course context (id + title), resource link + custom parameters, deployment id, message type, LTI version | ✅ PASS | FERPA data-flow §2 (table, verbatim list) | — |
| 9 | B07 | RS256 signature validated against Canvas's published JWKS; `iss`, `aud`, `exp` all validated | ✅ PASS | security review §1.3; architecture §6 | — |
| 10 | B07 | Algorithm pinned to RS256, removing algorithm-confusion exposure | ✅ PASS | security review §1.3 ("the algorithm pinned to RS256 so there is no algorithm-confusion exposure") | — |
| 11 | B08 | `state` and `nonce` are validated and consumed delete-on-read, so a launch cannot be replayed | ✅ PASS | security review §1.3; architecture §6 | — |
| 12 | B08 | Nonce/state retention 10 minutes; launch audit records 1 hour, then purged | ✅ PASS | FERPA data-flow §4 (retention table) | — |
| 13 | B09 | Roles matched against an allow-list of official IMS role URNs, exact identifier match | ✅ PASS | security review §1.3; architecture §6 | — |
| 14 | B09 | Authorization evaluated server-side on every request; the client cannot assert its own access | ✅ PASS | architecture §6; FERPA data-flow §7 | — |
| 15 | B09 | No AGS (`lineitem`, `result.readonly`, `score`) and no NRPS (`contextmembership.readonly`) scopes requested, so the tool cannot read the gradebook or roster | ✅ PASS | security review §2.1; architecture §8 | — |

**Invented values: none.** Every parameter name and number on screen traces to a
row above. Row 7 is the single claim that is mechanism rather than measurement,
and it is labelled as such rather than sourced to a document that does not say it.

**Deliberately absent from camera.** No hostname, no key material, no individual's
name, no institution's internal review process, no production claims. The two
security findings from the review (the endpoint that decoded rather than verified,
and the substring role match) are held back for a possible second video.
