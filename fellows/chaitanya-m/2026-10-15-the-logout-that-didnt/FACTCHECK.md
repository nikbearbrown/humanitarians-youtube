# FACTCHECK — The Logout That Didn't

Every claim spoken on camera, checked against its source.

**Checked against:** `medhavi-hub` — `origin/main` and `origin/development`.
**Checked on:** 2026-10-25, ten days after the reel was recorded.
**Method:** `components/LogoutButton.tsx` read in full on both branches, the fix
commit located, and the branch claim re-tested rather than assumed.

## Verdicts

| # | Claim on camera | Source | Verdict |
|---|---|---|---|
| 1 | It called the server to record that you'd logged out | `LogoutButton.tsx:20` — `fetch('/api/auth/logout', {method:'POST'})` | **PASS** |
| 2 | It walked every cookie and deleted it — plain, parent domain, localhost | `:52–73` | **PASS** — exactly four passes: root path `:58`, current domain `:61`, parent domain `:65`, localhost `:70` |
| 3 | Cleared local storage and session storage | `:76–79` | **PASS** |
| 4 | And redirected you home | `:88–98`, `:100` | **PASS** |
| 5 | It never asked the identity provider to end the session | `development:106` — "No Clerk signOut call - we handle everything manually to avoid POST conflicts" | **PASS** — and the pre-fix code says so in its own comment |
| 6 | The session cookie is on the provider's own domain and marked HttpOnly, so page JavaScript cannot touch it | `main:103–106` — the fix's own comment states this verbatim as the reason | **PASS** |
| 7 | The fix is to actually call the provider's sign-out | `main:109` — `signOut({ redirectUrl })` | **PASS** |
| 8 | It's raced against a five-second timer, and redirects anyway if it loses | `main:108–118` — `Promise.race` against a 5000 ms rejection, `catch` → `window.location.replace(redirectUrl)` | **PASS** — precisely as described |
| 9 | The cookie loop stayed | `main:52–73` still present after the fix | **PASS** |
| 10 | Logging out always revoked textbook access correctly; it was the hub's own session that survived | `app/api/access/verify/route.ts:166–177` — the `lastLogoutAt` check, independently verified for the 2026-09-21 reel | **PASS** — the two mechanisms are separate, and only the client-side one was broken |
| 11 | The fix is on main; development does not have it | re-tested below | **PASS — still true on 2026-10-25** |

Eleven claims, eleven pass. The mechanism claims are unusually tight because the
fix's own source comment (`main:103–106`) states the HttpOnly / provider-domain
reasoning in almost the same words as beat B06.

## Claim 11 re-tested — the bug is still live on `development`

B09 and B11 are time-sensitive: "The fix is on main. The development branch does
not have it yet… the next release cut from development would bring the bug
straight back." Spoken 2026-10-15. Re-checked 2026-10-25:

| | |
|---|---|
| Fix commit | `4777b36` — "fix: single redirect and timeout for logout signOut", 2026-10-09, on `main` |
| On `development`? | **No.** `git merge-base --is-ancestor 4777b36 origin/development` → false |
| `development` HEAD | `a8308c0`, 2026-10-22 — three days *after* the reel, still without the fix |
| `signOut` on `development` | imported `:5`, destructured `:9`, **never called** |

The giveaway is `development:106`, immediately after the redirect:

```js
// No Clerk signOut call - we handle everything manually to avoid POST conflicts
```

So the omission was deliberate and documented, for a reason ("POST conflicts")
that the production move invalidated. That is a sharper version of the reel's
own point than the reel makes: this was not a line someone forgot, it was a
decision that stopped being correct when the ground moved.

**The warning has not expired — it has aged into something more urgent.** Ten
days on, with `development` committed to as recently as 2026-10-22, any release
cut from that branch still reintroduces the bug.

## Note — B08's "one line in spirit"

Accurate as stated, and the reel immediately qualifies it ("but look at how it's
written"). For the record the fix is 11 lines (`main:107–118`): the `signOut`
call, the 5 s race, the catch, and the forced `replace` fallback. The reel's
framing — one line of intent, more than one line of care — matches the code.

## Scope of this check

Both branches read at the commits above. Not covered: whether the production
Clerk instance is configured as described (not inspectable from the repo),
whether a release has since been cut from `development`, pacing, or the audio.
