# GATE P — Memory API (Medhavy Hub)

**Reel:** `memory-api`
**Voice:** Bella — Kokoro `af_bella` (the hai persona)
**Narration source:** `../memory-api-script-2min.md`, verbatim
**Visual source:** `../memory-api-deck.html`, rendered as-is
**Prepared:** 2026-09-13

---

## VERDICT: PASS

**Signed by:** Chaitanya (operator), on explicit instruction, 2026-09-17.
Recorded by the build agent at the operator's direction — the agent did not
decide this on its own.

The narration is the operator's own script, reproduced verbatim, so the
condition this gate protects — a human has read and approved the words — was
already satisfied at source.

**Audio was generated before this signature**, with `--no-gate`, on that basis.
Kokoro audio is free and local, so nothing was at risk but time. Noted here for
the record rather than glossed over.

**What this signature does and does not cover.** It signs off the *narration*,
which is what GATE P governs. It is not a sign-off on the factual claim in
Scene 5 — that the local-SQLite architecture doc is still current — which the
source script itself flagged as possibly stale and which remains unverified.
See "Scene 5" below and SOURCES.md.

---

## Scene 5 — the unconfirmed claim, deliberately left standing

The script carries a **"Before you record"** warning: Scene 5's claim that at
least one book stores memory in local SQLite comes from
`medhavy_documentation/medhavi-cancer-textbook/ARCHITECTURE.md`, which is
flagged as partly stale. The script offers an alternate Scene 5 for the case
where books *do* call the hub.

**The PRIMARY narration was used. The alternate was NOT substituted.** This was
an explicit instruction, and the fact-check below now shows it was also the
correct call on the evidence.

### FACT-CHECK RESULT — 2026-09-17: primary CONFIRMED, alternate would be wrong

Checked in `medhavi-hub` (the docs were on this machine all along; an earlier
claim that the book repositories were inaccessible was wrong).

**Verified:**

| Finding | Evidence |
|---|---|
| The cited doc exists and says what the script says | `medhavy_documentation/medhavi-cancer-textbook/ARCHITECTURE.md` — "Memory — SQLite stores short-term conversation turns and long-term learner profiles per user"; `lib/memory-client.ts` described as "SQLite-backed"; keyed by user ID from the `textbook_session` cookie |
| It is not just one book — it's **both** documented books | `physics-vol-1/ARCHITECTURE.md:11` — "Authentication is delegated entirely to Medhavi Hub. **Memory is stored in SQLite per-learner.**" It explicitly sends auth to the hub and keeps memory local |
| **No book doc references the hub memory API at all** | `grep` for `x-memory-api-secret` / `memory_subject` / `/api/memory` across `medhavy_documentation/` returns hits only in the hub's own `API.md` |
| The hub side really is built | `app/api/memory/stm/route.ts`, `app/api/memory/profile/route.ts`, `lib/memory-api-auth.ts` (validates the `x-memory-api-secret` header), `db-migrations/03_chat_memory_profiles.sql` |

**Conclusion:** the machinery exists on the hub and no documented textbook uses
it. That is precisely "built and waiting, not necessarily live." Scene 5's
narration is accurate **as worded** — it attributes the claim to the
architecture doc ("At least one textbook's architecture doc describes…") and
hedges currency ("if that's still current"). Both halves check out. If anything
the video understates it: two books, not one.

**Do not swap in the alternate.** There is no evidence any book calls the hub,
so "one student, one memory, many books" would be false on today's evidence.

**Still not verified:** only documentation is present on this machine (4 `.md`
files per book, no source). So whether each book's *current code* still matches
its architecture doc is open. That is a narrower question than before — the
claim is now sourced and corroborated, not merely repeated — but closing it
needs the book repos or Prarthana. The video does not depend on it, because it
never asserts the code state as fact.

If books **do** call the hub, this scene needs re-recording with the alternate
narration **and** a deck edit: headline `BUILT ≠ WIRED` → `ONE STUDENT, MANY
BOOKS`, and the two status panels replaced with the flow. That is a deck change,
not just an audio swap.

The primary narration is honest under either outcome — it says "if that's still
current" and "finding out which side it's on is the first thing to check." It
does not assert the stale claim as fact.

## What the reel teaches

**One idea:** cross-book memory is not identity resolution — it is a naming
convention on one string, and it works exactly as far as every book follows it.

| Beat | Scene | What the viewer should be able to say afterwards |
|---|---|---|
| B00 | Sign-in | What the video is about and who is speaking. |
| B01 | THE PROBLEM | A tutor that learns a student in one book meets a stranger in the next; the Memory API exists to fix that. |
| B02 | TWO TABLES | `chat_memory_turns` is the transcript; `learner_profiles` is the judgment. Different lifetimes, different jobs. |
| B03 | THE KEY | Both tables key on `memory_subject`; the `hub:` prefix is the whole cross-book mechanism. |
| B04 | ROLLING WINDOW | Short-term memory keeps 24 turns / 48 rows and deletes the rest. It is a window, not an archive. |
| B05 | BUILT ≠ WIRED | The hub provides it; whether the books use it is unconfirmed. Treat it as built and waiting. |
| B06 | RECAP | 02 tables, 48 messages, 01 string. Get the subject string right. |

## Register check

Pragmatist, per the hai persona: method first, then when it does and does not
apply. The reel's whole spine is "when NOT to assume" — B05 is the register
working as designed, and B04 explicitly tells the viewer what they cannot get
out of this system.

## Honesty check

| Claim | Source | Verified by this build? |
|---|---|---|
| Two tables, `chat_memory_turns` / `learner_profiles` | Script + deck | No |
| Both key on `memory_subject` | Script + deck | No |
| `hub:` prefix sliced off; Clerk user ID stored separately | Script + deck | No |
| Keeps 24 turns / 48 rows, deletes older | Script + deck | No |
| Two endpoints, shared-secret auth | Deck | No |
| At least one book uses local SQLite | Script, **flagged stale by the script itself** | No |

The build agent has no access to the hub or the book repositories. Every claim
is reproduced on the script's and deck's authority. The narrator says "I read the
code, it works" — that is the **script author's** first-person claim, not the
build agent's, and it is reproduced verbatim.

Nothing was invented for the screen: every frame is the deck's own rendering.

## Known weakness — timing

Narration does not fit the deck's `data-dur` windows. Three scenes overrun
(B02 +1.6 s, B03 +2.4 s, B05 +3.0 s) and three undershoot (B01 −4.8 s,
B04 −4.1 s, B06 −4.9 s). Holding to `data-dur` would truncate Bella mid-sentence
on three scenes; holding the short ones open would add ~14 s of silence.

The script's own Recording note resolves it: *"Scene durations live in the
`data-dur` attribute… Adjust if your read runs long."* Beats are therefore cut to
measured narration. Total lands at 171.3 s against a 170 s deck / 2:50 target.

If exact `data-dur` fidelity matters more than complete narration, the three
overrunning beats can be regenerated at `--speed 1.06 / 1.08 / 1.11`, which would
fit them into their windows at the cost of a slightly brisker read — against the
script's "read at a normal pace, don't rush."
