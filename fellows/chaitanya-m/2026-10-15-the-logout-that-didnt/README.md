# The Logout That Didn't

A postmortem. The Logout button logged nobody out — every user, every time, and
only in production. The code hadn't changed in months and worked perfectly on a
laptop. What moved was where the session lived.

| | |
|---|---|
| **Runtime** | 3:52.80 (232.80 s) |
| **Format** | 30 fps · 16:9 and 9:16 |
| **Voice** | Kokoro `af_bella` — the series voice |
| **Beats** | 14 (B00–B13) · `ai-explainer` spine intact |
| **Brand** | `claude` · `@HumanitariansAI` |
| **Presenter** | Chaitanya M. |
| **Series** | Medhavi Hub — subsystem research reels |
| **GATE P** | `VERDICT: PASS`, 2026-10-15 |
| **Status** | Built · QC'd · fact-checked · **not published** |
| **Renders** | [Google Drive](https://drive.google.com/drive/folders/17fbvQu3dP4PzBrAFZpMxKRLyIzHInZ_v) |

## Through-line

The code wasn't wrong. Its assumption about where the session lived was.

## Beats

| Beat | Act | | Measured |
|---|---|---|---:|
| B00 | ASK | A bug report: the Logout button logs nobody out | 14.08 s |
| B01 | THE REPORT | Every time, for everyone, on the live site | 13.35 s |
| B02 | THE TWIST | Same code logs out fine on a laptop — so it probably isn't the code | 14.85 s |
| B03 | WHAT IT WAS DOING | Server call, every cookie, local and session storage, redirect | 16.58 s |
| B04 | THE OMISSION | It never asked the provider to end the session | 12.48 s |
| B05 | THE MOVE | Provider dev setup → production. Nobody touched the logout code | 12.35 s |
| B06 | ROOT CAUSE | The session moved to the provider's domain, marked HttpOnly | 23.72 s |
| B07 | THE SURVIVOR | The loop reported success; the one cookie that mattered survived | 15.25 s |
| B08 | THE FIX | Call sign-out — raced against 5 s, redirect anyway if it loses | 21.01 s |
| B09 | WHAT STAYED, WHAT HASN'T | Cookie loop kept; development still doesn't have the fix | 16.87 s |
| B10 | THE LESSON | Don't reimplement security, and this couldn't be found in dev | 21.55 s |
| B11 | VERDICT | Be precise about what was fixed | 22.78 s |
| B12 | HANDOFF | What else assumes state lives where it no longer does? | 23.94 s |
| B13 | OUTRO | — | 3.99 s |

## Fact-check — eleven claims, eleven pass

Verified against `medhavi-hub` on both `origin/main` and `origin/development`.
See [`FACTCHECK.md`](FACTCHECK.md).

The mechanism claims are unusually tight, because the fix's own source comment
(`LogoutButton.tsx:103–106` on `main`) gives the HttpOnly / provider-domain
reasoning in almost the same words as beat B06. The 5-second race in B08 is
exactly `Promise.race` against a 5000 ms rejection with a forced
`window.location.replace` in the catch (`:108–118`).

B11's precision also holds: textbook access was **always** revoked correctly via
the `lastLogoutAt` check in `app/api/access/verify/route.ts:166–177` — the same
mechanism the [One Sign-In reel](../2026-09-21-one-sign-in-many-books/)
documented. Only the hub's own client-side session was broken. The reel is
careful about that split and the code backs it up.

### The time-sensitive claim is still true

B09 and B11 say the fix is on `main` and `development` doesn't have it. Spoken
2026-10-15, **re-tested 2026-10-25 and still accurate**:

- fix commit `4777b36` (2026-10-09) is **not** an ancestor of `origin/development`
- `development` HEAD is `a8308c0`, committed 2026-10-22 — three days *after* this
  reel — still without it
- on `development`, `signOut` is imported and destructured but **never called**

And `development:106` carries the reason in a comment:

```js
// No Clerk signOut call - we handle everything manually to avoid POST conflicts
```

That is a sharper version of the reel's own point than the reel makes: this
wasn't a forgotten line, it was a documented decision that stopped being correct
when the ground moved. **Any release cut from `development` still reintroduces
the bug.**

## What is in this folder

**Committed** — source, checks and build inputs:

```
beat_sheet.json              every beat: narration, shot, measured duration
short/beat_sheet.json        the 9:16 cut
timings.json / words.json    measured clock + per-word timings
short/timings.json / words.json   same, for the short
claude-hai-the-logout-that-didnt.srt     subtitles, 16:9
short/…-short.srt            subtitles, 9:16
make_srt.py                  subtitles from measured word timings
short/make_srt.py            same, for the short
chapters.py                  generates + VALIDATES the chapter list
BUILD-PROMPT.md              the brief this was built from
README.md                    this file
FACTCHECK.md                 every claim, its source, its verdict
SOURCES.md                   provenance and toolchain
PEDAGOGY.md                  GATE P — signed, VERDICT: PASS
short/PEDAGOGY.md            GATE P for the short, and its cut plan
QC-REPORT.md                 frame-level visual QC
qc-sheet-t0.png              t=0 contact sheet
qc-sheet-mid.png             mid-beat contact sheet
FRICTIONAL.md                the process log for this piece of work
description.txt              YouTube description + validated chapters
.gitignore                   renders out, build inputs in
```

**In Drive, not here** — the renders: masters, narration `mp3/`, beat `clips/`,
`media/`.

`timings.json` and `words.json` sit at the folder root rather than in `mp3/`,
because `mp3/` is an excluded *location* under the 2026-09-18 media rule.

QC sampled at **both** t=0 and mid-beat this time — two contact sheets rather
than one.

## Open before publication

1. **B09's warning is live.** The reel tells viewers `development` would
   reintroduce the bug, and as of 2026-10-25 that is still true. Either merge
   the fix into `development` before publishing — which makes the beat
   historical — or publish as-is and accept that the reel is describing a bug
   that is still shipping. Worth a deliberate choice, not a default.
2. **Channel** — `@HumanitariansAI`; confirm before upload.
3. **Audio not listened to.** Verified as text and as measured duration only.
4. **Blast radius not stated.** The reel says "every user, every time" on the
   live site but doesn't say for how long, or what a stranded session could
   reach. Not a correction — a question a viewer will ask.
