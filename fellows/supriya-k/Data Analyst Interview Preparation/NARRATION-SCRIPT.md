# Narration Script — "The SQL Interview Bug Even a Correct-Looking Query Can Hide"

CLI-explainer · HAI persona (Kokoro `af_bella`) · Pragmatist register · ~4:12 estimated
Source: Chapter 4 (SQL II — Window Functions), Exercise 3 · Chapter 7 tie-in

---

**B00 — INTRO (cold open, ask answered)**
> Supriya, for Humanitarians AI. Here's the ask: from a streaming service's play log, find each user's single top track. Watch what comes back — the query runs, it returns rows, and at first glance it looks right. That's exactly the trap this video is about: a query that executes without error is not the same as a query that's correct on every case.

**B01 — PROBLEM**
> Top-N per group is one of the most common SQL interview patterns — top track per user, top product per city, top order per customer. Almost everyone reaches for a window function to solve it. Fewer people check what happens when two rows tie for first place. Loopr, an invented streaming service, keeps one simple table: plays, with a user, a track, and a timestamp for every play. The interview question sounds easy. The tie is where it stops being easy.

**B02 — MECHANISM (window functions vs. GROUP BY)**
> Why a window function at all? GROUP BY collapses every user's rows into one — you lose the ability to point at "the top one" because there's no per-row context left. A window function computes a value for each row using a set of related rows, without collapsing them. PARTITION BY sets the groups — here, each user. ORDER BY sets the order inside each group. That's what makes "rank within user" possible in the first place.

**B03 — CLI (cycle 1: the ask)**
> The plan: count plays per user and track, rank them within each user, and keep only the top one. In an interview you'd narrate this as you type it — group by user and track, order by play count descending, take rank one. It sounds complete. Here's the query as written.

**B04 — CODE (cycle 1: the buggy query)**
> Two steps. First, counts: how many times each user played each track. Second, ranked: RANK, ordered by play count descending, partitioned by user. The final SELECT keeps only rnk equals one. Nothing here throws an error. It compiles, it runs — and RANK gives every tied row the same rank.

**B05 — OUTPUT (cycle 1: the bug appears)**
> Run it against three users. Jon's clear top track appears — one row. Priya's clear top track appears — one row. Then user 101, Maya: track Echo and track Nova, tied at five plays each. RANK gives both of them rank one. The query that was supposed to return one top track per user just returned two for her.

**B06 — CLI (cycle 2: the revision)**
> Check the output before you trust it: does exactly one row come back per user? For Maya, it doesn't — two rows, same rank. The fix isn't a different WHERE clause. It's a different window function: swap RANK for ROW_NUMBER, and give it a tiebreaker so a tie can never produce two winners.

**B07 — CODE (cycle 2: the fixed query)**
> One line changes. ROW_NUMBER instead of RANK — it never repeats a value, even on a tie. And the ORDER BY inside OVER now sorts by play count descending, then track ID ascending, so ties resolve to a single, deterministic winner instead of splitting the rank. Same shape, one column added, one function swapped.

**B08 — OUTPUT (cycle 2: the better output)**
> Run it again. Jon: one row. Priya: one row. And Maya: exactly one row now too — track Echo, her top track by the tiebreaker. Three users in, three rows out. That's what "top track per user" actually promised.

**B09 — SUMMARY**
> The lesson isn't RANK versus ROW_NUMBER — it's that a query returning rows is not proof it's correct. Ties are the classic case that breaks a top-N query quietly, and they're exactly the kind of edge case the book's chapter on AI tools warns about too: code can pass a surface smell test and still be subtly wrong. Read the output. Count the rows. Check the case the happy path skips.

**B10 — NEXT STEPS (handoff, "Your turn.")**
> Your turn. Take any top-N-per-group query you've written and ask: what happens on a tie? Run this prompt: "Here's my top-N-per-group SQL query — check whether ties in the ranking column can produce more than one row per group, and if so, add a deterministic tiebreaker to ORDER BY." Read what comes back, then verify it yourself against a case with a real tie.

**B11 — OUTRO**
> The SQL Interview Bug Even a Correct-Looking Query Can Hide. Supriya, for Humanitarians AI.

---

Total words ≈ 681 · at ~2.7 words/sec ≈ 252s ≈ 4:12 — inside the requested 4–6 minute band. Duration is an output of this script, not a padded target (per `duration-planner` doctrine); nothing here was stretched to hit a number.
