# Frictional Log — how-a-room-changes-music (Week 26 topic video)

**Record provenance:** drafted 2026-10-10 with Claude from this folder's own records
(`TOPIC-DECISION.md`, `ANGLE.md`, `FACTCHECK.md`, `BEATS-DRAFT.md`, `PEDAGOGY.md`, the
`PROOF-REVIEW*.md` files, `experiment/`), after the work was done rather than while it happened.
**Awaiting Tanmay's review.** Every entry points at the record it comes from.

## 2026-10-10 — A topic nobody had taken

- **Work and expectation:** draw this week's topic at random from the `claude-for-<topic>`
  collections, and make sure no fellow has taken it, with git commands that only read.
- **Where it resisted:** 5,163 topic folders across `main` and 60 fellow branches, many of them
  near-duplicates under different names.
- **What was done:**
  - Repeated W25's method on a fresh, read-only bare mirror (`ls-remote`, `ls-tree`, `grep`, `show`,
    `diff --name-only`); nothing in the shared repo was checked out, fetched into or modified.
  - 1,855 singletons, filtered down to a pool of 5; an unseeded shuffle drew
    `claude-for-music/how-music-works-audible`.
- **Decided by:** Tanmay set the rules; the draw decided the topic.
- **Record:** `TOPIC-DECISION.md`, `_selection/`.

## 2026-10-10 — An angle and a structure of its own

- **Work and expectation:** a completely new angle and structure, unlike any earlier film, built on
  the topic's own content plus fresh research.
- **Where it resisted:**
  - The source review had only two ideas and no statistics.
  - The fellow sweep found a neighbour, a fellow's audio-engineering series (MP3s, loudness, mono
    phones). The first draft's ending ("how our mix was adapted for your phone") sat too close to it.
- **What was done:**
  - Research found a direct test of Byrne's idea: one cellist, seven halls, slower at *both* ends.
  - The structure became the voice changing rooms.
  - The phone ending was replaced with a two-room sonic callback.
  - Boundaries were recorded against W22 ("a distribution, not a person") and W17/18 ("right advice,
    wrong reason").
- **Decided by:** Claude proposed; Tanmay approved the angle.
- **Record:** `ANGLE.md` §§3–6.

## 2026-10-10 — 9/12 to 12/12

- **Where it resisted:** the first draft had no reusable rubric (1) and no task (0).
- **What was done:**
  - Added the decide/ask test (B13), applied on screen to three new cases.
  - Added a clap task before the payoff (B18–B20), with holds and strong/weak answers on screen.
  - The task's first wording asked the viewer to clap and speak while the voice kept talking, so it
    was split into three beats with silences.
- **Decided by:** Tanmay asked for 12/12; Claude proposed how.
- **Record:** `BEATS-DRAFT.md` (read-through draft 2), `PROOF-REVIEW.md`.

## 2026-10-10 — The cathedral recording we couldn't use

- **Work and expectation:** a measured cathedral impulse response for the demo.
- **Where it resisted:**
  - OpenAIR's York Minster page was offline (its host was suspended).
  - The replacement dataset on Zenodo was listed as CC BY 4.0, but its own `LICENCE.txt` said
    CC BY-NC-SA 4.0, which is non-commercial and so out for a monetised channel.
- **What was done:** downloaded with Tanmay's permission, checksum and licence file read, then deleted
  as he asked. A simulated echo (`make_ir.py`, measured T30 4.7 s) was built instead, labelled on
  screen as not a measured room. B01 became "a simulated cathedral", which re-opened Gate P for one line.
- **Decided by:** Tanmay chose simulation.
- **Record:** `FACTCHECK.md` §C (A23) and B5; `PEDAGOGY.md`.

## 2026-10-10 — The demo didn't do what the script said

- **Where it resisted:** Whisper heard the slowed cathedral sentence *worse* than the normal one
  (0.2 vs 0.5): stretching words smears them further.
- **What was done:**
  - Five logged runs. Pauses between phrases beat both normal pace and stretching in every room,
    which matches the cellist's own account.
  - A pre-registered final run (whisper small.en) found the normal sentence still mostly
    followable (0.65 vs 0.70), so "Most of that got lost" was not supported.
  - Per the rule written before the run, the line was rewritten rather than the room tuned:
    B02 → "Hear that?… with room between the phrases." What the film claims is what was measured: the
    echo falls 11–14 dB in each gap.
- **Decided by:** the pre-registered rule; Tanmay re-signed B01 and B02 at Gate P.
- **Record:** `experiment/demo_grid.py`, `demo_final.json`; `FACTCHECK.md` B1; `PEDAGOGY.md`.

## 2026-10-10 — A defect found after the stills were approved

- **Where it resisted:** in 9:16, the shared card component clipped its own source lines (6 of 10 cards)
  and ran into the Shorts UI zone. My first QC had only checked the portrait frames of the new components.
- **What was done:**
  - The Short uses only the three portrait-safe components (option a).
  - `portrait_check.py` now reads the pixels, so this fails a build instead of waiting to be noticed.
- **Decided by:** Tanmay chose option (a).
- **Record:** `PROOF-REVIEW-2.md`.

## 2026-10-10 — Compiling the Short

- **Where it resisted:**
  - The first compile was refused by Gate V with 12 BLOCKERs. My sheet said `aspect` where the
    compiler reads `aspect_ratio`, so it built a 16:9 canvas and cropped every portrait beat.
  - The next compile: the tempo arch under-filled the portrait frame (50–52% vs 55%).
- **What was done:** the fields were fixed, with `short_validation` computed from the same checks
  shorts.py runs (never hardcoded). The portrait arch was made taller and checked on stills before
  re-rendering. The third compile was clean.
- **Record:** `BEATS-DRAFT.md` (render and compile).

## 2026-10-10 — The Short from 8/12 to 11/12

- **Work and expectation:** Tanmay asked whether the Short could reach 10 or more.
- **What was done:**
  - Option A: the framework shown before the example (S03), and a clap task answered by the payoff
    (S07–S09).
  - Renumbering beats would have paired new beats with old audio (audio and timings are keyed by beat
    id), so the old files were archived to `short/_superseded/`.
  - The portrait check false-positived on compressed frames; it was fixed and re-tested against the
    known defects.
- **Decided by:** Tanmay chose A (11/12) over B (12/12, at the cost of a stuffed ending).
- **Record:** `PROOF-REVIEW-4.md`.

## Still open

- FACTCHECK A1, A5 and A18 are checked only against reviews and summaries of the book, not the book
  itself. This is the condition for public in `PROOF-REVIEW-3.md` and `PROOF-REVIEW-4.md`.
