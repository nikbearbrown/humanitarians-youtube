# One Sign-In, Many Books

How a student signs in once and opens every textbook they're entitled to, when
every textbook is a separate site that has never seen them and doesn't have
their password. The signed ticket, the call back to the hub, and the one logout
timestamp that retires every outstanding ticket without keeping a list.

| | |
|---|---|
| **Runtime** | 3:28.15 (208.15 s) |
| **Format** | 30 fps · 16:9 and 9:16 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 14 (B00–B13) · `ai-explainer` spine intact |
| **Brand** | `claude` · Claude fidelity palette · `@HumanitariansAI` |
| **Presenter** | Chaitanya M. |
| **Series** | Medhavi Hub — subsystem research reels |
| **GATE P** | `VERDICT: PASS`, 2026-09-21 |
| **Status** | Built · QC'd · fact-checked · **not published — see finding below** |
| **Renders** | [Google Drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) |

## Through-line

One timestamp instead of a list. The trick doesn't remove the call home — it
removes the list.

## Beats

| Beat | Act | | Measured |
|---|---|---|---:|
| B00 | ASK | Sign in once, open every entitled book; every book a separate site | 12.37 s |
| B01 | PROBLEM | No one big website — each textbook its own site, own address | 11.73 s |
| B02 | QUESTION | How does a site that's never seen you know you're allowed in? | 12.59 s |
| B03 | THE TICKET | Who you are, which one book, when it expires — 24 hours | 11.99 s |
| B04 | THE SEAL | Signed with a secret only the hub knows | 11.24 s |
| B05 | THE ASYMMETRY | Holding a ticket and checking one are different powers | 13.72 s |
| B06 | THE CALL BACK | The textbook asks the hub; checks run in order | 14.59 s |
| B07 | THE HARD PROBLEM | Logging out changes nothing — tickets are already out there | 17.88 s |
| B08 | THE OBVIOUS FIX | A cancellation list works, and becomes permanent cost | 18.26 s |
| B09 | THE PAYOFF | One logout timestamp; older tickets simply stop counting | 20.84 s |
| B10 | CLOSE | Separate websites, one front door | 17.77 s |
| B11 | VERDICT | Recap on the Claude artifact page | 16.26 s |
| B12 | HANDOFF | Take the ticket approach into Claude — then ask where it breaks | 24.43 s |
| B13 | OUTRO | — | 4.48 s |

B09 is the payoff and gets the most time of any beat, which is the right call —
the logout timestamp is the one genuinely non-obvious idea in the system.

## Fact-check — one FAIL, and it is the central security claim

Nine structural claims verified against `medhavi-hub` @ `3775687`. The ticket
shape, the 24-hour expiry, the access check before issuance, the call back to
the hub, and the logout-timestamp mechanism **all pass** — including the absence
of any revocation list, exactly as B08 and B09 describe.

**But B04's claim fails.** "Change one character and the signature stops
matching" is not what the code does:

`app/api/access/verify/route.ts:113–131` calls `jwt.verify(token, JWT_SECRET)`,
and when that **throws on a bad signature the error is caught** and the same
token is decoded as unsigned base64, after which execution continues. The
signature is therefore not a gate. Tampering doesn't reject the ticket; it just
routes it down the unsigned path.

What still holds the door: a forged payload must survive the remaining checks —
unexpired, named user exists in Clerk and isn't banned, `iat` not before that
user's `lastLogoutAt`, textbook exists, request origin matches the registered
URL, and for a `private` book `getUserAccess()` includes it. So an attacker
needs a real user id and a real entitlement — but **not** the hub's secret.

Related, and not mentioned on camera: `generate-token/route.ts:73–83` issues an
**unsigned** base64 ticket when `JWT_SECRET` is unset. So "signed with a secret
only the hub knows" is conditional on deployment config. This is the same shape
as the Memory API reel's finding that shared-secret auth is skipped when the
secret is unset — two instances now, worth treating as a codebase pattern.

Also **PARTIAL:** B06 says "six checks in order." The ordered sequence is
**eight** gates. Nothing false is claimed about what they do, and "in order" is
right — it's a miscount. Full table in [`FACTCHECK.md`](FACTCHECK.md).

**This is the reason the reel should not publish as-is.** B04 is 11 seconds of
a 3:28 video and it tells viewers a security property the system doesn't have.
The fix is a one-line change in the hub (drop the fallback, or gate it on
`!JWT_SECRET`) — after which the claim becomes true and the reel is correct
without re-cutting. That ordering is worth preferring to re-recording.

## What is in this folder

**Committed** — source, checks and build inputs:

```
beat_sheet.json            every beat: narration, shot, measured duration
short/beat_sheet.json      the 9:16 cut (B10, B11, B12 dropped)
timings.json               the measured clock the beats were conformed to
words.json                 per-word timings, the subtitle source
short/timings.json         + short/words.json — same, for the short
claude-hai-…-many-books.srt   subtitles, 16:9
short/…-short.srt          subtitles, 9:16
make_srt.py                subtitle generation from measured word timings
short/make_srt.py          same, for the short
BUILD-PROMPT.md            the brief this was built from
README.md                  this file
FACTCHECK.md               every claim, its source, its verdict — one FAIL
SOURCES.md                 provenance: narration, visuals, toolchain
PEDAGOGY.md                GATE P — signed, VERDICT: PASS
short/PEDAGOGY.md          GATE P for the short, and its cut plan
QC-REPORT.md               frame-level visual QC
FRICTIONAL.md              the process log for this piece of work
gate-p-contact-sheet.png   the contact sheet GATE P was signed against
qc-sheet-16x9-part{1,2,3}.png   frame QC, landscape
qc-sheet-9x16.png          frame QC, portrait
description.txt            YouTube description + chapter markers
.gitignore                 renders out, build inputs in
```

**In Drive, not here** — the renders: masters, narration `mp3/`, beat `clips/`,
`media/`.

This reel ships subtitles and per-word timings, which the two Brutalist reels
didn't. `words.json` is what `make_srt.py` reads, so the `.srt` can be
regenerated exactly rather than re-timed by hand.

`timings.json` and `words.json` sit at the folder root rather than in `mp3/`,
because `mp3/` is an excluded *location* under the 2026-09-18 media rule and git
will not descend into an excluded directory.

## Open before publication

1. **B04 states a security property the hub doesn't enforce.** See above. Fix
   the hub first, then this reel is correct as built.
2. **B06 says six checks; there are eight.** Cosmetic, but it's a number stated
   on camera.
3. **Channel handle** — `@HumanitariansAI` is in the beat sheet metadata but
   should be confirmed before upload.
4. **Audio not listened to.** Verified as text and as measured duration only.
