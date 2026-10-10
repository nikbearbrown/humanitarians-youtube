# Design From Real Data — script (final, as shot)

Channel claude-hai · Persona Rishabh · Register Plain · Voice Kokoro `af_sarah`
16:9 long cut: 5:37 (336.7s) · 9:16 Short: 1:23 (83.0s)

Timestamps are measured from the locked audio. This is exactly what is spoken in the final render; on-screen props live in `beat_sheet.json`.

## 16:9 — long cut

### B00 · OPEN (0:00–0:14)
> Greetings — this is Rishabh for Humanitarians AI. Part four of building a research assistant. Stage one ended with everything running, and a database holding one sample paper. This week, real papers go in.

### B01 · OPEN (0:14–0:30)
> Here's the whole video in one line. Don't design from guesses. Design from data. I fetched real responses from arXiv first, and they shaped the parser before I'd written any of it. Everything after that had to respect arXiv's limits.

### B02 · I — The Goal (0:30–0:47)
> The goal for stage two: fill that database automatically. Every day, ask arXiv for the new AI papers, save their details, and later, download and parse the PDFs. This week was the first part. Metadata only: titles, authors and abstracts, into Postgres.

### B03 · I — The Goal (0:47–1:08)
> Coming back after a break, I found two bugs stage one had left me. First, my tests had never been committed. One line in git ignore was silently hiding every file starting with test. And my model redeclared timestamp columns it should have inherited, so they had no defaults. The rule, again: check what git and the database actually have.

### B04 · II — Four Rules (1:08–1:27)
> So before writing any new code, I set four rules. Respect the service: arXiv allows one request every three seconds. Design from real data, not assumptions. Isolate failures at the right level. And make every run safe to repeat. The rest of this video is those four rules turning into code.

### B05 · III — The Build (1:27–1:44)
> Rule one went into the settings first. Every arXiv option lives in its own small section, and the delay between requests has a floor. Set it to one second, and the settings refuse to load. A limit that only lives in a comment is a limit someone will break.

### B06 · III — The Build (1:44–2:10)
> Rule two. Before writing the parser, I sent three requests to the real API: a normal search, a bad one, and an old paper. Each answer changed a decision. Paper IDs carry a version, so I store them without it. Otherwise a revised paper becomes a second row. Old IDs have a slash inside them, so I keep everything after abs. And a bad query explains itself inside the feed, so the parser raises with arXiv's own reason.

### B07 · III — The Build (2:10–2:28)
> Rule three lives in the same file. One malformed paper is logged and skipped, and the rest of the feed still loads. But a broken feed, or an error entry, raises. And because parsing is pure, text in and papers out, the tests just feed it a saved real response. No network, no mocks.

### B08 · III — The Build (2:28–2:49)
> Back to rule one, in the client. Every request goes through one rate limiter first: searches, retries, and later, PDF downloads. It waits only for whatever is left of the three seconds. It uses the monotonic clock, because wall-clock time can jump. And the clock and the sleep are passed in, so the tests can run instantly.

### B09 · III — The Build (2:49–3:10)
> What to retry is a decision, not a default. Timeouts, rate limits and server errors get retried, with a wait that doubles each time, plus a little randomness, so clients that failed together don't all come back together. But a four hundred means my request is wrong. Retrying just wastes arXiv's time, so it fails at once, with arXiv's own message.

### B10 · III — The Build (3:10–3:31)
> Then I ran it against one real day. September first: two hundred forty-three papers, in three pages of a hundred, in six and a half seconds. One gap in the log said two point seven nine seconds, which looked like a violation. It wasn't. The log records when a response arrives. The limiter spaces out when requests are sent.

### B11 · III — The Build (3:31–3:55)
> Rule four starts with the schema. Creating tables at startup never changes a table that already exists, so every schema change would mean wiping the database. Once papers take minutes each to parse, a wipe costs hours. So I adopted Alembic now, and gave migrations their own one-off container. It runs once and exits, and the API and Airflow start only after it succeeds.

### B12 · III — The Build (3:55–4:16)
> Then the save itself. Instead of checking each paper and then inserting it, one statement upserts the whole day: insert, and on conflict, update. It's atomic, so a failed run saves nothing and can simply run again. And it's safe to repeat. I ran September first twice: still two hundred forty-three rows, all refreshed, no duplicates.

### B13 · III — The Build (4:16–4:35)
> Last, the scheduler. A manual Airflow DAG runs the same ingestion code, for any date I give it. It ran in about nine seconds, and saved two hundred eighty-three papers from October eighth. With September first and the sample paper, the database went from one row to five hundred twenty-seven.

### B14 · IV — When Not To (4:35–4:51)
> When is this too much? If you need ten papers once, for a demo, a loop and a sleep is fine. No migrations, no upsert, no scheduler. This structure earns its keep when the job runs every day, on data that's expensive to rebuild.

### B15 · V — Verdict (4:51–5:05)
> So, stage two, part one. Real arXiv papers are in the database, by hand for now. Every decision came from real data, or from respecting arXiv's limits. Next: downloading the PDFs, and parsing them.

### B16 · V — Verdict (5:05–5:31)
> Your turn. Before you write code against any API, paste this into Claude, with one real response underneath. Here is a real response from an API I'm about to use, below. Don't write the code yet. List what in it would break a parser written from the docs alone, and what I should decide before I write one. Then ask me what the rate limit is, and how I'll respect it. Notice what it's not asking for: code. You're asking it to read the data with you, before you guess.

### B17 · OUTRO (5:31–5:36)
> Look at the data before you write the code. Rishabh, for Humanitarians AI.

## 9:16 — Short

### S00 (0:00–0:12)
> Greetings — this is Rishabh for Humanitarians AI. My research assistant had one sample paper. Here's how real arXiv papers got in, and the rule behind each step.

### S01 (0:12–0:20)
> Four rules first. Respect the service. Design from real data. Isolate failures. And make every run safe to repeat.

### S02 (0:20–0:27)
> The limit lives in config, with a floor. Set the delay under three seconds, and the settings refuse to load.

### S03 (0:27–0:40)
> Before the parser, I asked the real API. Paper IDs carry a version, so I strip it, or a revision becomes a second row. Old IDs hide a slash, so I keep everything after abs.

### S04 (0:40–0:48)
> Every request goes through one rate limiter: searches, retries, and later, PDF downloads. One clock, one rule.

### S05 (0:48–0:57)
> Saving is one statement per day: insert, and on conflict, update. I ran the same day twice. Still two hundred forty-three rows.

### S06 (0:57–1:05)
> Schema changes go through migrations, in their own container. It runs once, and nothing else starts until it succeeds.

### S07 (1:05–1:13)
> Then a manual Airflow DAG ran the same code. One sample paper became five hundred twenty-seven.

### S08 (1:13–1:23)
> The full version has the parser, the retry rules, and a prompt to use before your next API. Watch it next. Rishabh, for Humanitarians AI.
