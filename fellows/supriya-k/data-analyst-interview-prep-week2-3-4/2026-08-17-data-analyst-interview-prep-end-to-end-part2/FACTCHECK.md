# Sources & Fact-Check — "The SQL Interview Bug Even a Correct-Looking Query Can Hide"

## Claim-by-claim trace

| # | Claim in the video | Source | Verdict |
|---|---|---|---|
| 1 | "A window function computes a value for each row using a set of rows, without collapsing them — unlike GROUP BY, which collapses each group to one row." | Ch.4, verbatim (cites Wikipedia, "Window function (SQL)") | Inherited — already CONFIRMED in the book's own GATE-4 fact-check (definitional, anchored to Wikipedia). |
| 2 | `PARTITION BY` sets the groups, `ORDER BY` sets order within each group; omitting `PARTITION BY` makes the whole result one partition. | Ch.4, verbatim | Inherited, same anchor. |
| 3 | `RANK()` = "position with gaps for ties"; `ROW_NUMBER()` = "sequential number per partition" (never repeats). | Ch.4 function table, verbatim | Inherited, same anchor. |
| 4 | "Top-N per group → ROW_NUMBER() partitioned by the group, filtered to rn <= N." | Ch.4 recurring-patterns table, verbatim | Inherited. |
| 5 | Exercise 3 bug scenario: "A candidate's 'top track per user' query uses RANK() and returns two rows for users with a tie. Find the bug and fix it so exactly one row returns per user." | Ch.4, Exercise 3, verbatim | This is the video's premise, quoted directly from the book. |
| 6 | MySQL 8.0+ assumed; CTEs since 8.0.1, window functions since 8.0.2. | Ch.4 footnote, CONFIRMED against dev.mysql.com in the book's GATE-4 fact-check (`factchecks/MASTER_REPORT.md`, row 4). | Inherited, already independently verified — not re-checked here, cited as-is. |
| 7 | "Lean on it for boilerplate, syntax recall, and first drafts. Read it line by line when correctness matters — AI output can pass a surface smell test and still be subtly wrong." | Ch.7, verbatim | Inherited, editorial/process claim per the book's own sourcing notes (labeled process description, not a technical fact needing independent verification). |
| 8 | Loopr is an invented streaming service; `plays(user_id, track_id, played_at)` is its schema. | Ch.4, worked example | Inherited — the book's own invented company/schema, used here for a different (but related) query than the book's worked example. |

## What is new here (not in the book, and why it's not a fabricated fact)

- **The full buggy and fixed SQL text** (both queries in `beat_sheet.json`
  B04/B07). The book states the bug and its fix in prose (Exercise 3); the
  actual SQL implementing "RANK() causes 2 rows on a tie" and "ROW_NUMBER()
  + tiebreaker fixes it" is standard MySQL window-function syntax built to
  match the book's own described behavior — not a claim about the world,
  and directly checkable against MySQL's documented semantics for `RANK()`
  vs `ROW_NUMBER()` (Ch.4's own function table already states the relevant
  behavior difference).
- **The sample `plays` aggregate rows** (three users, one genuine tie).
  Loopr is already the book's invented company; this is illustrative
  sample data for it, not a new real-world fact, statistic, or claim.
  The exact rows are recorded in `VISUAL-PLAN.md` along with the full
  hand-worked derivation of both query outputs, so a human reviewer can
  independently re-run the SQL against the stated rows and confirm:
  - Buggy query → 4 rows for 3 users (user 101 duplicated).
  - Fixed query → exactly 3 rows for 3 users (user 101 resolved to
    `T-ECHO`, the alphabetically-first track under the `track_id ASC`
    tiebreaker).

## Original-questions rule

This video does not introduce a new interview question — it dramatizes
Chapter 4's own Exercise 3 (a bug-and-fix exercise already inside the
book's original-questions inventory, audited clean in
`factchecks/MASTER_REPORT.md`). No content here is drawn from any external
question bank, coding-interview site, or company-specific source.

## No paid services

No external APIs, stock imagery, or paid generation used or required
anywhere in this package's plan — all visuals are planned as Manim or
Remotion, per the toolkit's no-paid-services rule.

---

## v2 corrections (2026-10-16)

**The receipt is now real.** `sql/plays.sql` is a 33-row Loopr fixture (three users; user 101
ties T-ECHO and T-NOVA at 5 plays). The B04/B07 queries are saved verbatim as
`sql/top_track_buggy.sql` / `sql/top_track_fixed.sql` and run in SQLite 3.51, which handles CTEs
and window functions the same way as MySQL 8 (the book's assumed engine). Outputs are saved as
`sql/*.out`, and the Manim scenes read their rows from those files.

| Beat | v1 | Real run / Ch.4 | v2 |
|---|---|---|---|
| B02 (screen) | GROUP BY panel: "user 101: 3 plays" | `group_by_collapse.out`: user 101 = **12** plays | shows the real 12 |
| B05 | (hand-typed rows; drawn INK on INK, so invisible) | `top_track_buggy.out`: 4 rows for 3 users; 101 twice at 5 | rows parsed from the .out and drawn visibly |
| B08 | (hand-typed) | `top_track_fixed.out`: 3 rows; 101 → T-ECHO | parsed from the .out |
| B07 | "One line changes … one column added, one function swapped" | the diff changes the function, adds an ORDER BY key, and renames the alias and its filter | "Two changes … the alias follows" |
| B05/B08 | users named Jon / Priya / Maya (not in the book; not on screen) | screen shows user ids 101/102/103 | ids only (Supriya, 2026-10-16) |
| B10 | prompt paraphrased in narration | HANDOFF LAW: read verbatim | read verbatim |

Still true from v1: the premise is Ch.4 Exercise 3; RANK = "position with gaps for ties",
ROW_NUMBER = "sequential number per partition" (Ch.4 table); "surface smell test" (Ch.7). The
`track_id ASC` tiebreaker goes one step beyond the book's own worked example (which uses
ROW_NUMBER with no tiebreaker, so its winner on a tie is arbitrary).
