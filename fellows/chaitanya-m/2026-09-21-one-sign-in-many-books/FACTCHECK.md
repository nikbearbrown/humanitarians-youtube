# FACTCHECK — One Sign-In, Many Books

Every claim spoken on camera, checked against its source.

**Checked against:** `medhavi-hub`, branch `chaitanya` @ `3775687`.
**Checked on:** 2026-09-28, at port-in time.
**Method:** the token route, the verify route and the shared entitlement
function read line by line; the signature path traced through both its
fallbacks.

## Verdicts

| # | Claim on camera | Source | Verdict |
|---|---|---|---|
| 1 | Each textbook is its own site, at its own address; none has your password | `app/api/access/verify/route.ts` (per-textbook `url`, CORS allow-list built from registered textbook origins, `:20–52`) | **PASS** — textbooks are external origins that call the hub; no credential ever reaches them |
| 2 | The hub checks access *before* writing a ticket | `generate-token/route.ts:37–49` | **PASS** — `public` short-circuits to allow; otherwise `getUserAccess(user.id)` must include the id, else 403 |
| 3 | The ticket carries who you are, which one book, and when it expires | `generate-token/route.ts:54–59, 66–70` | **PASS** — `{userId, email, textbookId, iat}`, plus `exp` via `expiresIn`, and `audience: textbookId` binds it to that one book |
| 4 | Twenty-four hours | `generate-token/route.ts:67, 71` | **PASS** — `expiresIn: '24h'` |
| 5 | Signed with a secret only the hub knows | `generate-token/route.ts:66` | **PASS as written** — `jwt.sign(tokenData, JWT_SECRET)`. But see both findings below |
| 6 | The textbook can't check the signature itself — it doesn't know the secret | design of the flow | **PASS** — the secret is hub-side only; the textbook has no verification path of its own |
| 7 | So it asks the hub: is this ticket real, and is this person allowed in my book | `verify/route.ts:97` (`POST /api/access/verify`) | **PASS** — that is exactly the route's job |
| 8 | Logging out writes one timestamp; any ticket issued before it is dead | `verify/route.ts:166–177`, `lib/textbook-session-auth.ts:105–110` | **PASS** — `lastLogoutAt` in user metadata; `tokenIssuedAt < lastLogoutAt` → `Token invalidated by logout`. No revocation list exists, exactly as the reel says |
| 9 | Not cancelled — just older than your logout | same | **PASS** — the comparison is `<`; nothing is stored per-ticket |

## FAIL — "change one character and the signature stops matching"

**Beat B04.** This is the reel's central security claim, and the code does not
implement it.

`app/api/access/verify/route.ts:113–131`:

```js
try {
  if (JWT_SECRET) {
    decoded = jwt.verify(token, JWT_SECRET)      // signature enforced
  } else {
    decoded = JSON.parse(Buffer.from(token, 'base64').toString())
  }
} catch (tokenError) {
  try {
    decoded = JSON.parse(Buffer.from(token, 'base64').toString())
    console.log('🔄 JWT failed, base64 fallback successful')   // ← and continues
  } catch (base64Error) { /* only now rejected */ }
}
```

`jwt.verify` throws on a bad signature. That throw is **caught**, and the same
token is then decoded as unsigned base64 and execution continues. So changing a
character does not stop the ticket being accepted: it stops the *signature* path
and silently takes the *unsigned* path instead.

The consequence is that the signature is not a gate. A hand-written base64
payload naming any `userId` and `textbookId` reaches the remaining checks.

**What still holds the door.** This is not a full bypass — the forged payload
must still survive checks 3–8: unexpired, the named user exists in Clerk and is
not banned, `iat` is not before that user's `lastLogoutAt`, the textbook exists,
the request origin matches its registered URL, and for a `private` book
`getUserAccess()` must include it. An attacker needs a real user id and a real
entitlement. What they do *not* need is the hub's secret.

**Severity: high for the code, factual error for the video.** The narration's
B05 framing — "holding a ticket and checking one are different powers" — is
sound design reasoning. The reel just credits the implementation with enforcing
it, and it doesn't.

**Fix:** delete the outer `catch`'s base64 fallback, or gate it on
`!JWT_SECRET`. One-line change; not this reel's to make.

## Also not mentioned — the unsigned issuance fallback

`generate-token/route.ts:73–83`: when `JWT_SECRET` is unset the hub issues
`Buffer.from(JSON.stringify(...)).toString('base64')` — a ticket with no
signature at all. The route logs `🔓 Generated base64 token`, and `verify`
warns `⚠️ Using base64 fallback - configure JWT_SECRET for better security`.

So "signed with a secret only the hub knows" is conditional on deployment
configuration. Same shape as the Memory API reel's finding that shared-secret
auth is skipped when the secret is unset — worth treating as a pattern in this
codebase rather than two coincidences.

## PARTIAL — "the hub runs six checks in order"

**Beat B06.** The ordered sequence in `verify/route.ts` is **eight** gates, each
returning `hasAccess: false` on failure:

| # | Gate | Line |
|---|---|---|
| 1 | token present | 105 |
| 2 | decode / verify | 113–131 |
| 3 | not expired | 135–152 |
| 4 | user exists and is not banned | 156–164 |
| 5 | issued after last logout | 166–177 |
| 6 | textbook exists | 186–192 |
| 7 | request URL matches the registered origin | 196–228 |
| 8 | status rule — `hidden` admin-only, `private` via `getUserAccess`, `public` open | 231–257 |

"Six" undercounts. Nothing false is asserted about what the checks *do*, and the
"in order" part is exactly right, so this is a miscount rather than a wrong
claim. If a number is stated on camera it should be eight.

## Note — check 7 fails open on a malformed URL

`verify/route.ts:224–227`: if either URL fails to parse, the mismatch branch is
never reached — it logs `⚠️ URL validation failed` and falls through to the
status check. Not claimed on camera; recorded because it is adjacent to a claim
that is.

## Scope of this check

Verified against the repository at one commit. Not covered: whether a live
deployment sets `JWT_SECRET`, whether the textbook sites implement their side
correctly, pacing, or anything about the audio. The base64 findings are
read from source, not exploited — no request was made against any deployment.
