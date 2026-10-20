# Chapter 4 — SQL II: Aggregation, Window Functions, and Problem Patterns

Basic joins get you into the room; **window functions and pattern recognition** get you the offer. This chapter covers the harder SQL and the handful of problem shapes that recur. MySQL 8.0+ assumed — CTEs arrived in 8.0.1 and window functions in 8.0.2.[^mysqlver]

> **What's tested here**
> Can you reach past `GROUP BY` when the question needs per-row context — and can you *name the pattern* fast, then write it correctly and efficiently.

## CTEs: readable multi-step logic

A common table expression (`WITH`) names an intermediate result so a query reads top-to-bottom instead of nesting inside-out. Prefer them for anything with two or more steps.

## Window functions vs. GROUP BY

A **window function computes a value for each row using a set of rows, without collapsing them** — unlike aggregation with `GROUP BY`, which collapses each group to one row.[^win] They use an `OVER` clause with optional `PARTITION BY` (the groups) and `ORDER BY` (the order within each). Omit `PARTITION BY` and the whole result is one partition.[^win]

The ones to know:[^win]

| Function | Does |
|---|---|
| `ROW_NUMBER()` | Sequential number per partition |
| `RANK()` | Position with **gaps** for ties |
| `DENSE_RANK()` | Position with **no gaps** for ties |
| `LAG()` / `LEAD()` | Previous / next row's value |
| `SUM() OVER (...)` | Running / windowed total |

## The recurring patterns

Most SQL questions are one of a few shapes. Learn to name them on sight:

- **Top-N per group** → `ROW_NUMBER()` partitioned by the group, filtered to `rn <= N`.
- **Running total** → `SUM() OVER (ORDER BY ...)`.
- **Month-over-month / change** → `LAG()`.
- **Gaps & islands** → row-number differencing.
- **Deduplication** → `ROW_NUMBER()` keep `= 1`.

![Each recurring SQL pattern, its cue phrase, and the window function it calls for.](images/04-sql-ii-fig-01.png)

## Worked example — Loopr

Invented streaming service. `plays(user_id, track_id, played_at)`.

**Q: For each user, find their 2nd-most-played track.**

```sql
WITH counts AS (
  SELECT user_id, track_id, COUNT(*) AS plays
  FROM   plays
  GROUP  BY user_id, track_id
),
ranked AS (
  SELECT user_id, track_id, plays,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY plays DESC) AS rn
  FROM   counts
)
SELECT user_id, track_id, plays
FROM   ranked
WHERE  rn = 2;
```

**Why a naive `GROUP BY` fails:** grouping collapses each user to one row, so there's no way to point at "the 2nd" — you need per-row ranking *within* the user, which is exactly what the window function preserves.[^win]

## Exercises (Loopr schema)

1. **(Warm-up.)** Compute a **7-day running total** of plays per day using `SUM() OVER`.
2. **(Representative.)** Given the prompt *"the play with the largest gap since a user's previous play,"* name the pattern and the window function you'd use.
3. **(Stretch.)** A candidate's "top track per user" query uses `RANK()` and returns two rows for users with a tie. Find the bug and fix it so exactly one row returns per user.

---

*Next:* numbers without code — statistics, probability, and experimentation.

[^win]: Wikipedia, "Window function (SQL)," https://en.wikipedia.org/wiki/Window_function_(SQL) (accessed 2026-07-15).
[^mysqlver]: MySQL 8.0 Reference Manual, "What Is New in MySQL 8.0" (https://dev.mysql.com/doc/refman/8.0/en/mysql-nutshell.html); CTEs introduced in 8.0.1, window functions in 8.0.2. Accessed 2026-07-15.
