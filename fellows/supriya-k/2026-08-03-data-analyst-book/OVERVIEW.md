# Data Analyst Interview Prep — 3-Video Package (HAI / Bella persona)

**Source book (read once, reused across all three videos):**
`/Users/supriyakushwaha/Documents/ai1-cli/books/data-analyst-interview-prep/`
(`book.md`, `outline.md`, `chapters/01`–`10`, `factchecks/MASTER_REPORT.md`)

> Note: the `project-source/` folder inside this `brutalist.art/` toolkit
> contains a *different* book (the "AI1 CLI" meta-book, about writing books
> with the AI1 system) — not the Data Analyst Interview Prep book. This
> package was built from the real book at the path above instead. Flagging
> this in case `project-source/` was meant to be replaced/symlinked.

All three scripts use **only** facts, code, and examples already in the
signed, fact-checked manuscript (all 7 gates passed 2026-07-15,
`STATUS.md`; `factchecks/MASTER_REPORT.md` found zero errors). No new
facts, stats, or code were invented — the one exception is illustrative
*sample data rows* for the CLI-explainer's invented `Loopr` schema, which
the book itself already presents as an invented company (its own
original-questions rule permits this).

Persona: **HAI / Bella** (Kokoro `af_bella`, Pragmatist register,
humanitarians palette, `@HumanitariansAI`). Narrator introduces herself in
every video's cold open as **"Supriya for Humanitarians AI."**

---

## The three videos

### 1. `hai-star-method-behavioral/` — EXPLAINER (~3 min)
**Title:** *"The STAR Method: How to Actually Answer a Behavioral Interview Question"*
**Source:** Chapter 9 (The Behavioral Round).
**Why this one:** it is the single most self-contained, practical technique
in the book — one structure (Situation, Task, Action, Result), one common
failure mode ("all situation, no result"), one worked example. It lands
cleanly in 3 minutes without cutting anything load-bearing, and it's the
stage candidates most under-prepare for relative to its weight ("when two
candidates are technically even, the behavioral round often decides the
offer" — Ch.9).

### 2. `hai-interview-end-to-end/` — DEEP EXPLAINER (5–7 min)
**Title:** *"The Data Analyst Interview, End to End: What Every Stage Actually Tests in 2026"*
**Source:** Chapter 1 (primary spine), with the "what's tested where" matrix
threaded through and pointers to Ch.2–10 as the stage map.
**Why this one:** it's the book's own broadest research claim — the
end-to-end process map plus the three 2026 shifts (AI-tool fluency
assessment, messy-data take-homes, heavier communication weighting), each
sourced to `blueprint-trends-notes.md`'s career-guide research. It's
multi-act by construction (6 stages + 3 trends + a worked prep-plan), which
is exactly what the deep-explainer format is for, and it's the natural
"main weekly research video" — everything else in the book hangs off this map.

### 3. `hai-sql-window-functions-tie-bug/` — CLI EXPLAINER (4–6 min)
**Title:** *"The SQL Interview Bug Even a Correct-Looking Query Can Hide"*
**Source:** Chapter 4 (SQL II — Window Functions), Loopr schema, Exercise 3.
**Why this one:** it's a real, complete interview problem in the book — find
each user's top-played track — solved with a window function, then broken
by a genuine, book-specified bug (`RANK()` returns two rows on a tie) and
fixed (switch to `ROW_NUMBER()` with a tiebreaker). It's real, runnable
MySQL, has a natural verification step (does exactly one row come back per
user?), and gives a one-beat tie-in to Ch.7's "read AI-generated code before
you trust it" theme — appropriate for a CLI-explainer's build-with-Claude
loop.

---

## Status

Research summaries, beat sheets, complete narration scripts, visual plans,
and source/fact-check files are complete in each subfolder. **No audio
generated, nothing rendered.** Each folder's `PEDAGOGY.md` carries
`VERDICT: PENDING` — awaiting your GATE P sign-off before
`generate_audio_kokoro.py` runs.

Render note for later: default `compile.py` height is 720; use
`--height 2160` for the required 3840×2160 (4K) final output, and check each
beat's rendered frame resolution before compiling the master.
