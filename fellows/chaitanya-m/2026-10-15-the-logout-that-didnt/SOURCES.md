# SOURCES — The Logout That Didn't

**Reel:** `claude-hai-the-logout-that-didnt` · ai-explainer (war story / postmortem)
**Channel:** claude-hai (@HumanitariansAI) · Bella (`af_bella`) · Pragmatist
**Verified:** 2026-10-15, live against `Medhavy/medhavi-hub` via `gh`

## Primary sources

| # | Source | How checked |
|---|---|---|
| S1 | Author's script — `the-logout-that-didnt-script.md` | the 5 body scenes |
| S2 | `components/LogoutButton.tsx` **on `main`** | fetched via `gh api …?ref=main`, 140 lines |
| S3 | `components/LogoutButton.tsx` **on `development`** | fetched via `gh api …?ref=development`, 128 lines |
| S4 | PR #14 (merged) | `gh pr view 14 --json …` + body |
| S5 | PR #13 (open) | `gh pr view 13 --json …` + body |

## The author's "verified facts" — confirmed, stated without hedging

**`signOut({ redirectUrl })` is live on `main`, raced against a 5s timeout with a
fallback redirect.** Confirmed in S2, lines 108–118:

```ts
await Promise.race([
  signOut({ redirectUrl }),
  new Promise((_, reject) => setTimeout(() => reject(new Error('signOut timed out')), 5000)),
])
…
} catch (signOutError: unknown) {
  console.warn('⚠️ Clerk signOut failed, redirecting anyway:', errorMessage)
  window.location.replace(redirectUrl)
}
```

**Merged via PR #14 on 2026-10-13.** Confirmed: `"state":"MERGED"`,
`"mergedAt":"2026-10-13T17:14:11Z"`, `baseRefName: main`,
`headRefName: hotfix/clerk-logout`, merge commit `a976e07`.

**The old "no Clerk signOut call" comment is gone from `main`.** Confirmed: zero
matches for `No Clerk` in S2. (It is still present on `development` — see below.)

These three are narrated as settled fact, with no hedging language.

## The open item — re-checked at build time, not taken from the prompt

```
$ gh pr view 13 --repo Medhavy/medhavi-hub --json state,mergedAt,mergeStateStatus,baseRefName
{"baseRefName":"development","mergeStateStatus":"CLEAN","mergedAt":null,"state":"OPEN", …}
```

**PR #13 is OPEN as of 2026-10-15.** `development` therefore does not have the fix, and
the code confirms it independently of the PR state — S3 line 9 destructures `signOut`
but never calls it, and line 106 still carries the stale comment:

```ts
// No Clerk signOut call - we handle everything manually to avoid POST conflicts
```

So the caveat is **required** in this cut. It is carried twice: as an on-screen branch
status on B09 and as a spoken line in both B09 and the verdict (B11).

> **Re-check before publish.** If #13 merges, the caveat becomes false. Re-run the
> `gh pr view 13` command above; if `state` is `MERGED`, re-record B09 and B11 and
> re-render those two beats. Nothing else in the reel depends on #13.

## Body scene ledger

| Claim | Verdict | Evidence |
|---|---|---|
| Logout redirects but leaves you signed in, every time, in production only | ✓ | S5 PR #13 body: "Clicking **Logout** on hub.medhavy.com does not sign the user out — after the redirect they are still logged in." |
| It called the server to record the logout | ✓ | S2 step 1 posts `/api/auth/logout`; S4/S5 bodies: it "records `lastLogoutAt`, which textbook token checks use" |
| It deleted every cookie it could see — plain domain, parent domain, localhost | ✓ | S2 lines ~48–72: for each cookie it clears at root path, `domain=${hostname}`, `domain=.${domain}` (parent), and `domain=localhost` |
| Cleared local storage and session storage | ✓ | S2: `localStorage.clear(); sessionStorage.clear()` |
| It never asked the provider to end the session | ✓ | The whole point of the fix; still literally true on `development` (S3) |
| The project moved from the provider's development setup to its production one | ✓ | S5 body: "Since the 2026-10-06 cutover, hub.medhavy.com uses the Clerk **production** instance" |
| Dev: session cookie on the app's own domain, reachable by page JavaScript | ✓ | S5 body: "That worked on the old Clerk **development** instance, where the session cookie lived on the app's own domain." |
| Prod: session on a different domain, HttpOnly, unreachable | ✓ | S5 body: "the session is kept in an HttpOnly `__client` cookie on `clerk.medhavy.com`. Page JavaScript can't clear it". Also S2's own code comment: "the session lives in an HttpOnly cookie on the Clerk frontend API domain, which the cookie cleanup above cannot reach" |
| Reload and the provider signs you back in | ✓ | S5: "so Clerk re-establishes the session on reload" |
| The fix is raced against a 5s timer with fallback redirect | ✓ | S2 lines 108–118 (quoted above) |
| The cookie-clearing loop stayed | ✓ | S2 still contains the full loop; 5 `document.cookie` writes, same as `development` |
| Hotfix was cherry-picked to `main` to avoid shipping unreleased LTI work | ✓ | S4 body: "cherry-picked onto `main` so prod can be fixed without also shipping the unreleased LTI integration that `development` carries" |

## Reconciliation with "One Sign-In, Many Books"

That reel closes on logout: *"Logging out writes one timestamp; every ticket older than
it stops counting."* **That claim was and is correct**, and this reel must not
contradict it.

The evidence that they are two different halves comes from the PRs themselves. PR #13:
the `/api/auth/logout` call "still records `lastLogoutAt` for textbook token
invalidation". PR #14: it "records `lastLogoutAt`, which textbook token checks use".

So:

- **Textbook token revocation** — the One Sign-In reel's subject — worked throughout.
  The timestamp was always written; outstanding textbook tickets were always retired.
- **The hub's own session** — this reel's subject — was the half that survived logout.

B11 states this distinction explicitly so neither video overclaims. Nothing in this
reel says logout is "fully solved": it says one half is fixed on `main`, and that
`development` is still waiting.

## Naming

The script narrates "the identity provider" rather than naming Clerk, and this build
keeps that choice. It is the author's, it keeps the lesson portable, and it avoids
dating the video on a vendor's product naming. The PRs and the code name Clerk, and
this file records it; the narration does not need to.
