SQL, Read Fewer Rows.

Two queries. The same 4,459 rows of output, byte for byte identical. One reads
11,369 rows to get there. The other reads 400,000. Nothing in the SQL tells you
which is which — the query plan does.

The one takeaway: an index works on the column, not on a function of the column.
Wrap an indexed column in strftime, CAST or UPPER and the index stops being
usable, so the engine reads every row. Unwrap it into a bare range and the same
query reads 35× fewer rows for a byte-identical answer.

One caveat before you copy the UPPER version: dropping UPPER() is only equivalent
when the column is genuinely stored normalised under a case-sensitive collation.
With mixed-case data, or under COLLATE NOCASE or MySQL's default collation, the
two queries return different rows and removing the UPPER() is a correctness bug —
normalise on write, or index the expression, instead.

Run EXPLAIN. Look for the word SCAN.

CHAPTERS
0:00  The two queries
0:23  What an analytics query actually does
0:45  Ask the database, not your intuition
0:59  The two plans, side by side
1:20  35× fewer rows, on a log scale
1:40  Your turn — predict it
1:53  The function is the problem
2:18  The takeaway
2:46  A prompt to run on your own query
3:23  Read the plan first

(Chapter times are estimates from the beat sheet. Regenerate them from the
measured mp3 durations after audio lock — they will move.)

EVIDENCE
Every number in this video was produced by running real code on a real database,
not by estimation. A local SQLite table of 400,000 postings, an index on the date
column, and the actual EXPLAIN QUERY PLAN output for both queries:

  A  WHERE strftime('%Y-%m', posted_at) = '2026-01'
     |--SCAN postings

  B  WHERE posted_at >= '2026-01-01' AND posted_at < '2026-02-01'
     |--SEARCH postings USING INDEX idx_postings_posted_at (posted_at>? AND posted_at<?)

The same fixture also demonstrates the other two function wrappers named in the
video, so nothing in the spoken takeaway rests on analogy:

  CAST   WHERE CAST(branch_id AS TEXT) = '42'      -> SCAN postings        (400,000 rows)
         WHERE branch_id = 42                      -> SEARCH via index     (1,625 rows)

  UPPER  WHERE UPPER(account_ref) = 'AC-04242'     -> SCAN postings        (400,000 rows)
         WHERE account_ref = 'AC-04242'            -> SEARCH via index     (76 rows)

In every pair both queries return identical results — the build script compares
them and fails if they ever diverge. The UPPER case is the sharpest one: that
column is already stored uppercase, so the UPPER() changes no rows at all and
costs the entire index.

(That UPPER() equivalence is collation-dependent — see the caveat above. The
build script asserts the column really is uniformly uppercase before claiming the
two queries match.)

The fixture is deterministic (seed 20260916) and rebuilds in seconds with SQLite,
which ships with macOS and most Linux distros. No API key, no paid service, no
cloud warehouse needed to reproduce any of it.

A function the video deliberately does NOT name: date_trunc. It behaves exactly
the same way — wrap an indexed timestamp in it and the index goes unused — but
it's a PostgreSQL function with no SQLite equivalent, so it couldn't be measured
on this fixture. Rather than assert it on screen, it lives here: same mechanism,
documented rather than demonstrated. Everything the narration names was actually
run.

A note on engines: this demo is SQLite, which names the steps SCAN and SEARCH.
PostgreSQL calls them Seq Scan and Index Scan. Different words, same mechanism —
which is why the takeaway says "run EXPLAIN and look for a full scan" rather than
naming one engine's keyword.

And one thing this video deliberately does NOT claim: 35× fewer rows read is not
35× faster. On the machine used here it was about 4× faster. Rows read is a
structural property of the plan; milliseconds belong to your hardware.

Made with the Brutalist toolkit — audio-first, free and local end to end: Kokoro
TTS (Bella), Remotion, Manim, ffmpeg. No paid voices, no paid APIs.

Supriya Kushwaha · AI+1 Humanitarians AI fellow · weekly report, 2026-09-16

#sql #queryoptimization #explain #sqlite #postgres #dataengineering #analytics
#dataanalyst #indexing #humanitariansai

youtube.com/@HumanitariansAI
