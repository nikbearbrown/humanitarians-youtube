# FACTCHECK — Who Can Open What

Every claim spoken on camera, checked against its source.

**Checked against:** `medhavi-hub`, branch `chaitanya` @ `3775687`.
**Checked on:** 2026-09-28, at port-in time.
**Method:** `getUserAccess()` read line by line, its callers enumerated by
grep, and the archived-class query traced to the schema.

The whole reel rests on one function: `lib/textbook-manager.ts:80`
`getUserAccess(userId)`. Every structural claim maps onto it.

## Verdicts

| # | Claim on camera | Source | Verdict |
|---|---|---|---|
| 1 | Three kinds of people: admin, instructor, student | `lib/authz.ts:5` `AppRole = 'admin' \| 'instructor' \| 'student'` | **PASS** — and `lib/authz.ts:21–26` normalizes anything unrecognised to `student`, so there is no fourth state |
| 2 | Admins get every textbook, no exceptions, nothing to set up | `textbook-manager.ts:85–89` | **PASS** — `role === 'admin'` returns every textbook id unfiltered |
| 3 | Instructors get every textbook too, except anything marked hidden | `textbook-manager.ts:91–95` | **PASS** — `filter(t => t.status !== 'hidden')` |
| 4 | Nobody has to grant an instructor anything — it comes with the role | same | **PASS** — the role branch returns before any grant table is read |
| 5 | Students get nothing by default | `textbook-manager.ts:97–131` | **PASS** — a student with no rows in `textbook_access` and no enrollments gets `[]` |
| 6 | Exactly two ways a student gets permission | same | **PASS** — precisely two sources are unioned, and no third is consulted |
| 7 | First way: an admin grants a specific book directly | `textbook-manager.ts:98–103` (`textbook_access` by `user_id`); granted via `grantAccess()` `:134` | **PASS** |
| 8 | Usually because the student asked and the request was approved | `createAccessRequest()` `:161`, `approveRequest()` `:238` | **PASS** — request/approve flow exists and writes through to the same table |
| 9 | Second way: an instructor assigns textbooks to a class; enrolled students get them automatically | `textbook-manager.ts:105–125` — `class_enrollments` → `class_textbooks` | **PASS** — no per-student approval step anywhere in that path |
| 10 | Those two lists get added together, duplicates removed | `textbook-manager.ts:131` | **PASS** — `Array.from(new Set([...explicitAccess, ...classTextbookAccess]))` |
| 11 | If a class is archived, the books that came with it stop working | `textbook-manager.ts:112` `.eq('classes.archived', false)` | **PASS** — archived classes are filtered out of the enrollment join, so their textbooks never enter the union |
| 12 | Nothing tells the student why the book stopped opening | the same line, plus the verify route's error strings | **PASS** — access simply ceases; the failure surfaces as generic denial, with no archived-class explanation anywhere |
| 13 | The question is asked at two different moments — on opening, and when the textbook checks back | `generate-token/route.ts:42` and `verify/route.ts:243` | **PASS** — both call the same `getUserAccess` |
| 14 | Two different pieces of the system, same question, same place, same answer | same two call sites | **PASS** — one implementation, two callers. This is the reel's main claim and it is correct |
| 15 | Add a new way in, and every door already knows | structural consequence of 13–14 | **PASS** — a new source added inside `getUserAccess` is picked up by both callers with no other change |

Fifteen claims, fifteen pass. This is the cleanest of the four reels — the
narration describes the function accurately, including its sharp edge.

## Worth knowing — the two callers are not quite symmetric

Claim 14 is true of `getUserAccess`, but the two call sites wrap it slightly
differently, and a reader taking "the same answer every time" literally should
know where the wrapping differs:

| | `generate-token` | `verify` |
|---|---|---|
| `public` book | allowed without calling `getUserAccess` (`:37–38`) | allowed without calling it (`:255–256`) |
| `private` book | `getUserAccess` must include the id (`:42–43`) | `admin \|\| instructor \|\| getUserAccess` includes it (`:247`) |
| `hidden` book | falls to `getUserAccess`, which already excludes `hidden` for instructors | **admin only** — instructors rejected outright (`:231–239`) |

For `hidden` books the two paths reach the same outcome by different routes:
`generate-token` excludes an instructor because `getUserAccess` filtered the
book out; `verify` excludes them with an explicit role test. Same answer,
different reasoning — so the guarantee holds in behaviour but is not enforced
by sharing a single code path in the way the reel's framing implies.

This does not falsify anything said on camera. It is the detail that would
matter if someone changed one branch and not the other.

## Scope of this check

Verified against the repository at one commit on 2026-09-28. Not covered:
whether the Supabase schema matches the queries at runtime, pacing, the deck's
legibility, or anything about the audio. Those are human judgments and open.
