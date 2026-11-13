# SOURCES — The Gate Is Closed

## Primary source

| Field | Value |
|---|---|
| Title | Week 8: API Security & JWT Authentication |
| Series | Provenance Gatekeeper Development Log |
| Supplied | 2026-10-22 |
| Author / narrator | Onkar Bhujbal (Humanitarians AI) |

## Beat ↔ scene map

| Scene | Beats |
|---|---|
| 1 — HOOK | B00 (+ B01, the mandatory BLUF the script does not carry) |
| 2 — THE BCRYPT PIVOT | B02 |
| 3 — THE TOKEN EXCHANGE | B03 |
| 4 — ADVERSARIAL AUTHENTICATION | BASK (ask) → B04 |
| 5 — SCAFFOLDED TASK & CLOSE | B05 · BHTF · BOUT |

## Claims taken from the source, verbatim or near-verbatim

| On screen / in narration | Source |
|---|---|
| "Hi, I am Onkar Bhujbal." | Scene 1 VO, verbatim |
| `401 UNAUTHORIZED` blocking anonymous requests to `/verify` | Scene 1 visual |
| "Anyone with the URL could bombard our endpoint, poison our logs, and exhaust our vector database." | Scene 1 VO |
| `passlib` importing `bcrypt`; `ValueError: password cannot be longer than 72 bytes` | Scene 2 visual, verbatim |
| Python 3.13 environment; deprecated library removed; custom raw-`bcrypt` wrapper | Scene 2 VO |
| `/token` endpoint; credentials exchanged for a time-limited JWT | Scene 3 VO |
| stress test fails with `401`, authenticates, then proceeds | Scene 4 visual + VO |
| "The test script must now actively negotiate a Bearer token." | Scene 4 VO |
| `TASK: Implement stateless authentication.` | Scene 5 visual |

## ONE CORRECTION — the 72-byte limit is bcrypt's, not passlib's

The script frames the error as "`passlib` triggered a fatal 72-byte truncation bug."
Half of that is right and the half that is wrong matters.

**bcrypt itself only ever hashes the first 72 bytes.** That is the algorithm, not any
library. Every correct implementation has to decide what happens past that boundary —
truncate explicitly, reject, or pre-hash. What `passlib` contributed was failing hard on
a modern runtime rather than handling the case.

Why the distinction is worth the airtime: told only that the library was buggy, a viewer
concludes the constraint disappeared along with the dependency. It did not. The reel
says both — the library broke, and the limit is still there in the wrapper that replaced
it, now explicit and visible.

The wrapper shown is **illustrative of the pattern**, not a copy of the project's file,
which was not supplied.

## Illustrative — NOT measured

- **B04** — the two request-log rows (`no token → 401`, `Bearer → 200 · EVALUATED`) are
  constructed and **captioned as such on screen**. No real `stress_test.py` output was
  provided.
- **B00** — no attack or abuse is claimed to have happened; the beat states the exposure
  an open endpoint allowed.

## Additions under DOUBLE-CHECK LAW

1. **The suite now tests the parser AND the lock (B04).** Once auth is mandatory, a
   broken token flow fails every adversarial case for the wrong reason — the suite goes
   red and the parser looks guilty. Worth knowing before it happens.
2. **Assert the negative case (B05).** A FastAPI dependency that is wired but not
   enforced looks identical to one that is, until a test asserts the `401`. Same logic as
   the Week 7 reel's required-check point.
3. **The handoff targets the forgotten endpoints** — `/docs`, `/openapi.json`, `/health`,
   `/metrics`. Closing `/verify` while the OpenAPI schema stays public is the common
   half-finished version of this week's work.
4. **B01 (the BLUF) is authored** — `internal` → `unlocked` is the reel's actual
   misconception: "internal" is a deployment detail, not a security control.

## Narrator

First person, Onkar Bhujbal. Kokoro `am_onyx` is a **synthetic read of the author's own
script**, not a voice clone. The script's sign-off still reads "Liam, …"; this reel signs
off **"Onkar Bhujbal, for Humanitarians AI."**

## Build mode

Built **straight to `./art final`** — no review cut. No beat chip and no timecode is ever
drawn, and GATE V runs on both aspects.

## Components — zero new

| Scene | Component |
|---|---|
| 1 · 4-ask · handoff | `ClaudeComposerAsk` (+ `916`) |
| BLUF | `BrutalistHesitantWriter` (+ `916`) — fontSize 88 |
| 2 | `GuardrailCompare` — passing stamp |
| 3 | `ThreeStageBand`, three stages |
| 4 | `AlertSplit` |
| 5 | `ClaudeCodeBeat` · outro `HaiTitleOutro` |
