# Chapter 3 — SQL I: Querying, Filtering, and Joins

SQL is the skill nearly every technical screen assumes. This chapter builds the core: a correct query, the right join, and the ability to *explain what you wrote.* All examples use **MySQL**.

> **What's tested here**
> Correct SQL **and** clear reasoning. A query that runs but that you can't explain is a weak answer — screens grade logic and communication, not just execution.[^trends3]

## What SQL is

SQL is a domain-specific language for managing data in a relational database.[^sql] Its statements group into families — querying (`SELECT`), definition (`CREATE`), manipulation (`INSERT`/`UPDATE`/`DELETE`), and control. Interviews live almost entirely in `SELECT`.

**Dialects differ.** Date syntax, string handling, `NULL` behavior, and identifier casing vary by vendor, so SQL rarely ports unchanged between engines.[^sql] This book standardizes on MySQL.

## The query skeleton

```sql
SELECT   column(s)
FROM     table
WHERE    row filter
GROUP BY grouping column(s)
HAVING   group filter
ORDER BY column(s)
LIMIT    n;
```

Two traps interviewers watch for:
- **`WHERE` filters rows; `HAVING` filters groups.** You can't filter an aggregate in `WHERE`.
- Logical evaluation runs roughly `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`, which is why a column alias from `SELECT` isn't always usable in `WHERE`.

## Joins — pick by the relationship

| Join | Returns |
|---|---|
| `INNER JOIN` | Only rows with a match in **both** tables.[^join] |
| `LEFT JOIN` | **All** left rows + matches; unmatched right columns are `NULL`.[^join] |
| `RIGHT JOIN` | All right rows + matches; unmatched left columns are `NULL`.[^join] |
| Self-join | A table joined to itself, using aliases.[^join] |

**Rule of thumb:** "everyone, plus their data if any" → `LEFT JOIN`. "Only matched pairs" → `INNER JOIN`.

![Which rows each join returns: INNER (matches only), LEFT (all of A), RIGHT (all of B).](images/03-sql-i-fig-01.png)

## Worked example — FreshCrate

Schema for an invented meal-kit company:
`customers(id, name, city)` · `orders(id, customer_id, ordered_at)` · `order_items(order_id, product, price)`

**Q: For each city, how many customers placed at least one order in 2025?**

```sql
SELECT   c.city,
         COUNT(DISTINCT c.id) AS active_customers
FROM     customers c
JOIN     orders o ON o.customer_id = c.id
WHERE    o.ordered_at >= '2025-01-01'
     AND o.ordered_at <  '2026-01-01'
GROUP BY c.city;
```

*Say it aloud:* "Inner-join customers to orders so I only keep customers who ordered, restrict to 2025 dates, group by city, and count distinct customers so multiple orders don't double-count." The query is half the answer; saying it out loud like that is the other half.

## Exercises (FreshCrate schema)

1. **(Warm-up.)** List all customers who have **never** placed an order. *(Hint: `LEFT JOIN` + `WHERE ... IS NULL`.)*
2. **(Representative.)** Given a one-to-many relationship (one customer, many orders), if you `JOIN` customers to orders, do the customer rows inflate? Explain what happens and why `COUNT(DISTINCT ...)` fixes it.
3. **(Stretch.)** Return the **top 3 cities by total 2025 revenue**, where revenue is the sum of `order_items.price`.

---

*Next:* the SQL that separates candidates — window functions and the recurring problem patterns.

[^trends3]: `blueprint-trends-notes.md`.
[^sql]: Wikipedia, "SQL," https://en.wikipedia.org/wiki/SQL (accessed 2026-07-15).
[^join]: Wikipedia, "Join (SQL)," https://en.wikipedia.org/wiki/Join_(SQL) (accessed 2026-07-15).
