# SOURCES — One Sign-In, Many Books

**Reel:** `claude-hai-one-sign-in-many-books`
**Channel:** claude-hai (@HumanitariansAI) · Bella (`af_bella`) · Pragmatist
**Verified:** 2026-09-21

## Primary sources

| # | Source | Used for |
|---|---|---|
| S1 | Author's script — `one-sign-in-many-books-script.md` (5 scenes, ~440 words) | The reel's body: scene order, visuals, the ticket metaphor, the "payoff" designation on Scene 4 |
| S2 | `medhavi-hub/app/api/access/generate-token/route.ts` | Scene 2 — what the hub checks, what it writes into the ticket, the 24-hour expiry, the signing secret |
| S3 | `medhavi-hub/app/api/access/verify/route.ts` | Scene 3 — the call back and its checks; Scene 4 — the `lastLogoutAt` comparison |
| S4 | `medhavi-hub/DEVELOPER.md` §4.1–§4.4 | The six-step verification pipeline in order; logout semantics; the textbook-side session |

## DOUBLE-CHECK LAW — claim ledger

| Claim in narration | Verdict | Evidence |
|---|---|---|
| Each textbook is a separate site at its own address | ✓ | S4 §4.1: the dashboard opens `{textbook.url}?access_token=…` on another origin; S3 builds its CORS allow-list from each registered textbook's own URL |
| The hub checks access **before** it writes the ticket | ✓ | S2 lines 35–49: `hasAccess` is resolved and a 403 returned before any ticket is created |
| The ticket carries who you are, which one book, and when it expires | ✓ | S2 lines 54–70: payload `{ userId, email, textbookId, iat }`, options `{ expiresIn: '24h', audience: textbookId }`. "Who you are" covers two fields (id + email) — a simplification, not a distortion |
| Twenty-four hours | ✓ | S2 `expiresIn: '24h'`; S4 §4.1 |
| Signed with a secret only the hub knows; altering it breaks the signature | ✓ | S2 line 66 signs with `JWT_SECRET`; S3 line 115 verifies with the same secret. Standard signature semantics |
| The textbook cannot verify the signature itself | ✓ | The secret is server-side only on the hub (S2/S3 read it from the hub's env); the textbook's middleware is the *caller* of `/api/access/verify` (S4 §4.2), never a verifier |
| The hub runs **six** checks, in order | ✓ | S4 §4.2 enumerates exactly six: signature → expiry → user exists/not banned → logout invalidation → textbook exists + URL match → status-based access. Narration and the on-screen list follow that order |
| The textbook remembers the student so later pages skip the round trip | ✓ | S4 §4.3: a `textbook_session` token is resolved from header/bearer/cookie on subsequent requests |
| Logging out writes one timestamp | ✓ | S4 §4.4: `POST /api/auth/logout` sets `publicMetadata.lastLogoutAt = now` |
| Any ticket issued before that moment stops counting | ✓ | S3 lines 168–177: `if (lastLogoutAt && tokenIssuedAt < lastLogoutAt) → reject`. Not a revocation list — a comparison |
| "The trick doesn't remove the call home — it removes the list" (B10) | ✓ | The `lastLogoutAt` comparison happens *inside* `verify` (S3), so it depends on the call back existing. Honest statement of the trade the design makes |
| "The two machines have to agree what time it is" (B12) | ✓ | Expiry and the logout comparison are both unix-second comparisons across two hosts (S2 `iat`, S3 `now`/`lastLogoutAt`) |
| "A copied ticket keeps working until it expires or you log out" (B12) | ✓ | Nothing in S3 binds a ticket to a device or session; the URL/origin check (§4.2 step 5) constrains *where* it is presented, not *who* presents it |

## Simplifications, declared

1. **The unsigned fallback is not mentioned.** S2 lines 73–83 and S4 §4.1: with no secret configured, the hub emits unsigned base64 instead. DEVELOPER.md calls this "dev convenience, not security". Out of scope for a general-audience explainer about the configured path; narration says "it's signed" without qualifying, which is true of the deployed configuration. Logged here rather than on screen.
2. **"Six checks" is the documented pipeline, not a count of `if` statements.** S3 contains additional guards (CORS origin resolution, base64 decode fallback, error handling). Six is §4.2's own enumeration and is what the on-screen list shows.
3. **Four textbook titles on screen are illustrative** ("Cancer Biology", "Organic Chemistry", "Statistics", "Immunology") — chosen to show plurality, not lifted from the live catalogue, and no count of the real catalogue is claimed.

## Wording rule (author's, enforced)

- The word **"JWT" appears nowhere** in narration, on-screen copy, card text, or the outro. "Ticket" carries the whole reel.
- **One metaphor only.** No keys, passports, or wristbands. The script's own "secret" and the visual "seal" both stay inside the ticket metaphor — a stamped, signed stub.

## Security constraints (hard, author-set)

- **No real token string is shown anywhere in the reel.** The only beat that displays a ticket identifier is B04, and it uses the invented placeholders `TCKT-0000-EXAMPLE-0000` / `TCKT-0000-EXAMPLX-0000`, carrying an on-screen caption "example — not a real ticket". No token was captured, pasted, or screen-recorded at any point in this build.
- **`auth-debug.txt` is never opened, displayed, or referenced.** The file was not read during this build. S4 §4.2 documents that the verify route appends real emails, textbook IDs, and access decisions to it; the reel's B06 check list is written from DEVELOPER.md's documented pipeline, not from that log.
