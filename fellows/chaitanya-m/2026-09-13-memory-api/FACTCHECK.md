# FACTCHECK — Memory API (Medhavy Hub)

Every claim spoken or set on camera, checked against its source.

**Checked against:** `medhavi-hub`, branch `chaitanya` @ `3775687`.
**Checked on:** 2026-09-17, at port-in time.
**Method:** schema and route files read directly; the `hub:` slice, the prune
arithmetic, and the auth path traced line by line.

This supersedes the "**None independently verified**" row in
[`SOURCES.md`](SOURCES.md). Verification has now been performed. Note the
long-form script was researched against `main` @ `efcc3f5`; this check is
against a later commit, so it also confirms nothing has drifted since.

## Verdicts

| # | Claim on camera | Source | Verdict |
|---|---|---|---|
| 1 | Two tables: `chat_memory_turns`, `learner_profiles` | `db-migrations/03_chat_memory_profiles.sql:3,15` | **PASS** — both created, nothing else in the migration |
| 2 | Both key on the same field, `memory_subject` | same, `:5` and `:16` | **PASS** — `TEXT NOT NULL` on turns, `TEXT PRIMARY KEY` on profiles |
| 3 | `chat_memory_turns` is the transcript — one row per message, tagged user or assistant | same, `:6` | **PASS** — `role TEXT NOT NULL CHECK (role IN ('user','assistant'))` |
| 4 | `learner_profiles` is one row per student holding untyped JSON | same, `:16,19` | **PASS** — `memory_subject` is the primary key, so one row per subject; `profile JSONB NOT NULL DEFAULT '{}'` is schemaless |
| 5 | If the subject starts with `hub:`, the profile route slices it off and stores the Clerk user ID separately | `app/api/memory/profile/route.ts:41,48` | **PASS** — `subject.startsWith("hub:") ? subject.slice(4) : null`, written to the `clerk_user_id` column (migration `:17`, indexed `:23`) |
| 6 | Every exchange gets posted as a pair | `app/api/memory/stm/route.ts:63–66` | **PASS** — one insert of two rows; the assistant row is timestamped +1 ms (`:61`) to preserve ordering |
| 7 | No identity resolution — it's a naming convention | routes as a whole | **PASS** — the `hub:` slice is the only subject-aware logic anywhere; nothing joins or reconciles identities. Two subjects that differ by one character are unrelated rows |
| 8 | Two endpoints | `app/api/memory/{stm,profile}/route.ts` | **PASS** — two routes. (Five methods across them: STM has GET/POST/DELETE, profile has GET/PUT. "Two endpoints" is accurate as routes) |

## PARTIAL — "twenty-four turns, forty-eight rows" is a default, not a rule

**Beat B04.** Narration: *"It keeps the most recent twenty-four turns,
forty-eight rows, and deletes everything older for that subject."*

| | |
|---|---|
| **On camera** | 24 turns / 48 rows, stated as the behaviour |
| **In the code** | `maxTurns` is a **caller-supplied request-body field**, clamped to `[2, 100]`, defaulting to 24 — `app/api/memory/stm/route.ts:53` |
| **Prune** | keeps `maxTurns * 2` rows (`:70`), so 48 is the default ceiling, not a fixed one |

A textbook backend that posts `maxTurns: 100` gets a 200-row window. The
rolling-window *shape* of the claim is right and the deletion is real
(`:81–86`), but the numbers are a default the caller can override. Confirmed
against `DEVELOPER.md:378`, which documents `maxTurns? (2..100, default 24)`.

Severity: minor. The point the beat makes — short-term memory is a rolling
window, not an archive — holds either way.

## Not mentioned on camera — auth is skipped in non-production

**Beat B05** says "two endpoints, shared-secret auth." True, and the secret is
real: `x-memory-api-secret` must equal `MEMORY_API_SECRET`
(`lib/memory-api-auth.ts:7,14`).

But `lib/memory-api-auth.ts:9–12`: if `MEMORY_API_SECRET` is unset, a
non-production environment returns `{ ok: true }` and **auth is skipped
entirely**. In production a missing secret is a 500 instead.
`DEVELOPER.md:378` documents this in bold.

Nothing said on camera is false — this is an omission, not an error, and
arguably out of scope for a 2:50 overview. Flagged because a viewer wiring up a
book could reasonably come away thinking the endpoints are always authenticated.

## Scene 5's flagged claim — CONFIRMED at doc level

The script carries a "Before you record" warning: Scene 5 claims at least one
textbook stores memory in local SQLite scoped to that book, sourced from
`medhavy_documentation/medhavi-cancer-textbook/ARCHITECTURE.md` and flagged as
possibly stale. The build deliberately kept the PRIMARY narration and left it
unresolved. **It is now resolved, and the claim holds.**

That doc set lives inside the hub repo. It says, consistently across four files:

| Evidence | Source |
|---|---|
| "**Memory** — SQLite stores short-term conversation turns and long-term learner profiles per user." | `ARCHITECTURE.md:12` |
| Memory row of the stack table reads `SQLite` | `ARCHITECTURE.md:47` |
| "SQLite-backed memory store… short-term memory (last 10 conversation turns per session) and long-term memory (persistent learner profile per user). Both are keyed by user ID derived from the session cookie." | `ARCHITECTURE.md:111` |
| "No database installation is required. SQLite is used for learner memory and is managed by the application at runtime." | `README.md:28` |
| STM "loaded from SQLite"; profile "updated in SQLite" | `API.md:73,74` |

**Supporting check — nothing calls the hub.** `grep -rn "x-memory-api-secret"`
across `medhavi-hub` returns exactly three hits: the auth helper that reads the
header, `DEVELOPER.md:378`, and `docs/creating-a-new-textbook.md:87` telling
future authors to send it. **No caller.** Same shape as the concept-map finding
in the previous reel: the machinery exists and nothing consumes it.

**Two details that make the point sharper than the narration does.** The cancer
book's scheme isn't merely separate — it is incompatible on two axes. It keys
memory off a **session cookie**, not `hub:{clerkUserId}`, and it keeps **10
turns**, not 24. So it isn't one subject-string away from joining; it is a
different identity model.

**Limit of this check.** The book *repositories* are not present — only their
doc sets, which `DEVELOPER.md:82` itself labels "Older per-project doc sets
(partially stale)." So this confirms what the cancer book's architecture
documents say, not what its running code does today. The script's own remedy —
grep a book repo for `x-memory-api-secret`, or ask Prarthana — remains the
definitive test, and is cheap.

On the strength of this, the alternate Scene 5 ("ONE STUDENT, MANY BOOKS")
should **not** be substituted. The evidence runs the other way.

## "I read the code, it works"

**Beat B05**, spoken in the first person by the script's author. Not a claim
this check can verify — no test suite was run and no live hub was called. What
*is* verified is that the routes exist, compile-level logic matches the
description, and the schema backs them. Whether they work against a live
Supabase instance is untested here.

## Scope of this check

Verified against the repository at one commit on 2026-09-17. If `medhavi-hub`
moves, the video still states these numbers — re-check before re-publication.

Not covered: pacing, whether the deck reads well, or anything about the audio.
Those are human judgments and still open — see the README's
"Open before publication" list.
