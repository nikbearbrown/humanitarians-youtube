# GATE P — The Logout That Didn't

**Reel:** `claude-hai-the-logout-that-didnt` · ai-explainer · claude palette (fidelity)
**Channel:** claude-hai · @HumanitariansAI · Bella (`af_bella`) · Pragmatist
**Beats:** 14 (B00–B13) · estimated ~3:48
**Reviewer:** Chaitanya (author)
**Date:** 2026-10-15

> Nothing downstream runs until this reads `VERDICT: PASS`.

---

## 1. The one idea

**The logout button deleted every trace of your session it could reach, and never asked
the provider to end it — which was the same thing, right up until the session moved
somewhere the page couldn't reach.**

## 2. War-story shape, deliberately not flattened

The author's instruction: keep the narrative shape — report, investigation, root cause,
fix, lesson — rather than flattening it into a walkthrough. So the body is built as five
acts, and each act is allowed to behave like its act:

| Act | Beats | What the act does that a feature tour wouldn't |
|---|---|---|
| **Report** | B01, B02 | B01 shows the failure happening, not a description of it. **B02 ends on a question, not an answer** — "whatever's wrong here probably isn't the code" — and the visual greys the code out and accents the *environments*. The investigation turns on screen. |
| **Investigation** | B03, B04 | B03 is staged to *look like a success* — a checklist going all green. B04 then lands a seventh, unticked row underneath it. The omission is felt because the beat before it was allowed to feel complete. |
| **Root cause** | B05, B06, B07 | B05 moves the ground while the code stays stamped UNCHANGED. B06 is the two-diagram reveal, and re-labels the blocked reach from *failure* to *defence*. B07 is the payoff: SUCCESS stamped on a job that didn't do the thing. |
| **Fix** | B08, B09 | B08 shows the race as a race — both lanes converging on the same outcome. B09 is the honest ending: what's fixed, and what isn't. |
| **Lesson** | B10 | Draws the moral, and ends on the reel's own image: the search happening on the side where the bug isn't. |

B11's verdict recaps **the investigation**, not a feature list.

## 3. Facts stated as settled (author instruction: do not hedge)

Verified live against the repo on 2026-10-15 — full ledger in `SOURCES.md`:

- `signOut({ redirectUrl })` is live on `main`, raced against a 5-second timeout with a
  fallback redirect. Read out of `LogoutButton.tsx` on `main`, lines 108–118.
- Merged via **PR #14 on 2026-10-13** (`mergedAt: 2026-10-13T17:14:11Z`, merge commit
  `a976e07`).
- The old `// No Clerk signOut call` comment **is gone from `main`** (zero matches).

Checked mechanically: zero hedging constructions ("appears to", "seems to", "may have
been merged", "believed to") anywhere in the narration.

## 4. The open item — carried, not resolved

**Re-checked live at build time rather than taken from the brief:**

```
$ gh pr view 13 --repo Medhavy/medhavi-hub --json state,mergedAt,mergeStateStatus
{"mergeStateStatus":"CLEAN","mergedAt":null,"state":"OPEN"}
```

PR #13 is **OPEN**. Independently confirmed in the code: `LogoutButton.tsx` on
`development` destructures `signOut` (line 9) and never calls it, and still carries the
stale comment at line 106.

So the caveat is required, and it is carried **three** ways:

1. **On screen at B09** — a two-row branch status board: `main — fixed` /
   `development — not yet`, the second in terracotta, plus a persistent "status checked
   2026-10-15" footnote.
2. **Spoken at B09** — "The fix is on main. The development branch does not have it yet,
   so the next release cut from development would bring the bug straight back."
3. **Spoken and on the verdict card at B11** — "development is still waiting."

> **If PR #13 merges before publish:** re-run the `gh pr view 13` check. If it reports
> `MERGED`, the caveat becomes false — re-record B09 and B11 and re-render those two
> beats. Nothing else in the reel depends on #13.

**Re-checked once more immediately before delivery**, per the author's instruction that
this not come from the brief's date.

## 5. No overclaim — the reconciliation with "One Sign-In, Many Books"

That reel ends on logout: *"Logging out writes one timestamp; every ticket older than it
stops counting."* **That is true and this reel does not touch it.** The PRs are explicit
that `/api/auth/logout` "records `lastLogoutAt`, which textbook token checks use".

Logout has two halves. **Textbook token revocation always worked** — the sign-in reel's
subject. **The hub's own session** is the half that survived, and is this reel's subject.

B11 says this in as many words. Checked mechanically: the phrase "fully solved" appears
nowhere, and no sentence pairs `development` with a fixed state.

## 6. Flagged for the reviewer

1. **Runtime ~3:48.** Longer than the two prior reels in the series (both 3:27). The
   cause is structural: five acts plus the mandatory caveat and the reconciliation line.
   Say so if you want it tighter — the order of sacrifice is B06's defence aside, then
   B10's second lesson, then the handoff's discussion. **B09 and B11 are not on that
   list** — they carry the open item and the no-overclaim line.
2. **Ten new Remotion components** are specified and do not exist yet
   (`LogoutNoOp`, `WorksOnMyMachine`, `CleanupSweep`, `TheOmission`, `TheMove`,
   `WhereSessionLives`, `TheSurvivor`, `RacedFix`, `BranchStatus`, `TheLesson`), each
   with a 9:16 sibling, all at 1920×1080 / 1080×1920 so `--scale=2` gives true 4K.
   Bookends reuse the existing `haiKit` wrappers, including the preroll that keeps a
   beat from opening on blank frames.
3. **No vendor name is spoken.** The script says "the identity provider"; the code and
   PRs say Clerk. Keeping the author's choice — it keeps the lesson portable and avoids
   dating the video. Say if you'd rather name it.

## 7. Full narration, in order

**B00 · ASK** (39) — Hi — this is Bella, for Chaitanya. A bug report: the Logout button logs nobody out. Every user, every time, and only in production. This is the postmortem — what broke, and why it was invisible where you'd look.

**B01 · THE REPORT** (40) — Someone clicks Logout. The page redirects. And they're still signed in. Not a rare edge case, not a flaky one — every time, for everyone, on the live site. The button does something; it just doesn't do what it says.

**B02 · THE TWIST** (44) — And here's what makes it interesting. The same code, on a developer's laptop, logged out perfectly. It had worked for months, and nothing in the logout code had changed. So before you read a line of it: whatever's wrong here probably isn't the code.

**B03 · WHAT IT WAS DOING** (45) — On paper the button did a thorough job. It called the server to record that you'd logged out. Then it walked every cookie it could see and deleted it — plain domain, parent domain, localhost. Cleared local storage, cleared session storage, and redirected you home.

**B04 · THE OMISSION** (39) — What it never did was ask the identity provider to actually end the session. It cleaned up every piece of evidence that you were logged in, by hand, and assumed that was the same thing. For months, it was.

**B05 · THE MOVE** (34) — Then the project moved from the provider's development setup to its production one. Different infrastructure — and a different place to keep the session. Nobody touched the logout code. The ground moved under it.

**B06 · ROOT CAUSE** (69) — On the development setup the session cookie lived on the app's own domain. Page JavaScript could see it, so deleting it by hand worked. On production the session lives on a different domain — the provider's own — and it's marked HttpOnly. Page JavaScript cannot read it or delete it. That's not a bug; that's the point of the flag. It's what stops a malicious script stealing your session.

**B07 · THE SURVIVOR** (42) — So the loop ran, deleted everything it could reach, reported success — and the one cookie that mattered sat there untouched. Reload, and the provider helpfully signs you back in. The code wasn't wrong. Its assumption about where the session lived was.

**B08 · THE FIX** (65) — The fix is one line in spirit: actually call the provider's sign-out. But look at how it's written. The call is raced against a five-second timer, and if it loses, the code redirects you anyway. Signing out is a network call to someone else's service — if that service is slow, you don't want a user stranded on a page that won't let them leave.

**B09 · WHAT STAYED, WHAT HASN'T LANDED** (57) **[the open item]** — The cookie loop stayed, by the way — it isn't what fixes this, but it's harmless and it covers the local case. And one thing is still live as I record. The fix is on main. The development branch does not have it yet, so the next release cut from development would bring the bug straight back.

**B10 · THE LESSON** (58) — Two things to take away. Don't reimplement what a library already does, especially security. The manual cleanup looked more thorough than one function call; it wasn't, it was more code doing less. And this bug could not be found in development — the environments differed in exactly the way the broken assumption depended on. That's the dangerous kind.

**B11 · VERDICT** (69) **[no-overclaim reconciliation]** — Let's recap with Claude. The button deleted every trace of the session it could reach, and never asked the provider to end it. That worked until the session moved to a domain the page can't touch. And be precise about what's fixed: logging out always revoked textbook access correctly. It was the hub's own session that survived, and that half is fixed on main — development is still waiting.

**B12 · HANDOFF** (72) — Your turn. Take this into Claude: My logout clears cookies and local storage by hand instead of calling my auth provider's sign-out. Tell me what that breaks once the session cookie is HttpOnly and on the provider's own domain, and what else in my app might be assuming state lives somewhere it no longer does. That last clause is the one to push on. This was never really a bug about logout.

**B13 · OUTRO** (9) — The Logout That Didn't. For Chaitanya and Humanitarians AI.

**Total:** 682 words · estimated ~229s (~3:48) at Bella's measured rate. Real durations replace this at audio lock.

---

## VERDICT

Reviewed by the author on 2026-10-15 against the narration in §7 and the flags in §6.
Signed as written — the ~3:48 runtime stands; a postmortem earns its length.

Short-cut policy set at the same time: **protect B09** (the PR #13 branch-status
caveat) in the 9:16 derivative; B10, B11 and B12 are the drops. The short therefore
never claims a full fix, and its rewritten outro points at the long for the lesson.

VERDICT: PASS
