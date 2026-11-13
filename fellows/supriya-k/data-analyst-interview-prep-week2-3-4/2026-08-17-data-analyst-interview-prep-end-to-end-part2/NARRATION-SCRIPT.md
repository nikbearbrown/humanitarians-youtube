# Narration Script — "The SQL Interview Bug Even a Correct-Looking Query Can Hide"

cli-explainer · v2 (2026-10-16) · 12 beats · 440 words · ~157s estimated at v1's per-beat pace · Voice: Kokoro `af_bella` ("Bella") · Register: Pragmatist · Narrator identity: **Supriya**

v1 (676 words, 234.9s measured) is in git history. Same 12 beat ids and cli-explainer spine. Every number on screen now comes from a real SQLite run of `sql/` (see `FACTCHECK.md`, "v2 corrections").

---

**B00** (INTRO). Hi, I am Supriya and this video is about a SQL interview bug that even a correct-looking query can hide. The ask: from a streaming service's play log, find each user's single top track. That's the trap: running without an error isn't the same as being correct.

**B01** (PROBLEM). Top-N per group is one of the most common SQL interview patterns: top track per user, top order per customer. Most people reach for a window function. Fewer check what happens when two rows tie for first. Loopr, the book's invented streaming service, logs every play: a user, a track, and a timestamp.) Top-N per group, like top track per user, is one of the most common SQL interview patterns. Most people reach for a window function. Fewer check what happens when two rows tie for first. Loopr, the book's invented streaming service, logs every play: a user, a track, and a timestamp.

**B02** (PROBLEM (why a window function)). Why a window function? GROUP BY collapses each user to one row: user 101 becomes twelve plays. A window function computes a value for each row without collapsing them. PARTITION BY sets the groups, here each user. ORDER BY sets the order inside each one.

**B03** (CLI — cycle 1). The ask: count plays per user and track, rank them within each user, and keep rank one. In an interview you'd narrate that plan as you type. It sounds complete. Here's the query.) The ask: count plays per user and track, rank them within each user, and keep rank one. It sounds complete. Here's the query.

**B04** (CODE). Two steps. First, counts: plays per user, per track. Second, RANK, ordered by plays descending and partitioned by user. Keep rank one. It compiles, it runs. But RANK gives tied rows the same rank.

**B05** (OUTPUT). Run it. Users 102 and 103 get one row each. Then user 101: Echo and Nova, tied at five plays. RANK gives both of them rank one. Three users, four rows.

**B06** (CLI — cycle 2 (revision)). So check the output before you trust it: exactly one row per user? Not for 101. The fix isn't a different WHERE clause. It's a different window function: ROW_NUMBER, with a tiebreaker, so a tie can never produce two winners.

**B07** (CODE (revised)). Two changes. ROW_NUMBER replaces RANK: it never repeats a number, even on a tie. And ORDER BY gains a second key, track ID ascending, so the tie resolves to one deterministic winner instead of an arbitrary one. The alias follows: rn equals one.

**B08** (OUTPUT (revised)). Run it again. 102: one row. 103: one row. And 101: exactly one row, Echo, by the tiebreaker. Three users in, three rows out.

**B09** (SUMMARY). The lesson isn't RANK versus ROW_NUMBER. It's that returning rows isn't proof of correctness. Ties break top-N queries quietly, and the book's chapter on AI tools warns the same way: output can pass a surface smell test and still be subtly wrong. Read the output. Count the rows.

**B10** (NEXT STEPS / HANDOFF). Your turn. Try this: Here's my top-N-per-group SQL query. Can ties in the ranking column return more than one row per group? If so, add a deterministic tiebreaker to ORDER BY. Paste your query under it, then test the fix yourself on a real tie.

**B11** (OUTRO). The SQL Interview Bug Even a Correct-Looking Query Can Hide.

---


Word count 440. Sources: Ch.4 (`04-sql-ii.md`, Exercise 3 is the premise) and Ch.7 (`07-python-pandas-ai-tools.md`).
