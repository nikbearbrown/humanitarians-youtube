# Frictional log: 2026-07-27

**Data visualization: building the AI Buzz Tracker dashboard**

This log records where the week's work pushed back and what I did about it. The details trace to
`docs/worklog.md`, `docs/dashboard_design.md`, `docs/relevance_fix_design.md` and the n8n node
code in the project repo.

---

## What I was working on

Until this week the tracker's output only existed as rows in a Postgres table and an email that
went out on breakouts. Every run produced a score per company, but nobody could look at it
without writing a query. The goal was a dashboard: a ranked leaderboard, a trend line per company,
and a breakdown of which kinds of news were driving attention, served from the n8n instance I
already run rather than from a new app I would have to host.

In the same week I was also building the Community Opinion branch, which reads the actual comment
threads on each company's top stories and asks a model to summarise what people think. The video
covers both, because the dashboard is where the opinions were meant to show up.

## What I tried, and what I expected

The plan was a single static HTML page using Chart.js and the Supabase JavaScript client, reading
`hn_buzz_runs` directly from the browser with the read-only anon key. n8n would serve it with three
nodes: a Webhook on `GET /dashboard`, a node to read the file, and Respond to Webhook.

Because I had no live Supabase credentials configured in the development environment at first, I
added a `?mock=1` mode that renders the page against `fixture_runs.json`, which is the real week 5
backfill output (13 weekly rows) in the same shape as the live table. That let me check the charts
before touching the live system.

I expected the n8n side to be the easy part. It is three nodes. I expected it to take an evening.

## Where it resisted, and what I did next

**The n8n wiring broke six separate times against the live instance.** None of these showed up in
the design, and each one only appeared when I ran it for real:

- `Respond to Webhook` had its body typed as `= {{ $json.html }}` with a space after the `=`. n8n
  expressions do not tolerate that space. Small, but it returned nothing useful until I found it.
- `Read/Write Files from Disk` refused to read the file (`Access to the file is not allowed`).
  n8n only allows reads under `/home/node/.n8n-files` by default, and the design had mounted the
  dashboard at `/data/dashboard`. I remounted it in `docker-compose.yml` and updated the node.
- The Code node that injects the Supabase URL and key could not read environment variables,
  because n8n blocks `$env` in Code nodes by default. I set `N8N_BLOCK_ENV_ACCESS_IN_NODE=false`
  and added `env_file: [.env]` so the keys reach the container without being hardcoded into the
  workflow JSON.
- The browser threw `Failed to construct 'URL': Invalid URL`. The page referenced each
  `%%TOKEN%%` placeholder twice, and JavaScript's `.replace()` only replaces the first match, so
  the second copy was handed to `createClient` as a literal string. I changed the page to
  reference each token once, detect an uninjected page with `.includes('%%')`, and switched the
  node to `.replaceAll()`.
- **The key I had wired in was the wrong one.** It was the `service_role` key, not `anon`. I
  confirmed it by decoding the JWT payload and reading its `role` claim. That key has full read,
  write and delete access to the whole project, and this page puts its key in the browser where
  anyone can view source. I rotated it in Supabase before shipping and replaced it with the real
  anon key. The lesson I wrote into the design doc is to check the `role` claim, not the key's
  length or shape, before using any Supabase key client side.
- `supabase-js` failed with a `navigator.locks` `SecurityError`, because its auth client takes a
  Web Locks lock at startup even when no session is stored. The dashboard has no logged-in user,
  so I passed a no-op `auth.lock` override.

There was also a seventh mismatch: the live table predated the `community_opinions` column, so
selecting it failed. I dropped it from the query and noted that the column and the select have to
come back together once the opinions branch is live.

After those fixes, `GET http://localhost:5678/webhook/dashboard` returned the live page with the
keys injected, and I confirmed it rendering real `hn_buzz_runs` data in a browser on 2026-07-21.
I kept the dashboard as its own workflow (`Hacker News Dashboard.json`) instead of merging it into
the daily pipeline, so a dashboard problem can never stop a scoring run.

**Getting the opinions branch into the live pipeline was a separate job.** The analyser existed
as a Python reference and a written wiring spec, and both live steps were still open. I ran the
`alter table` migration to add the `community_opinions` column to the live Supabase table, then
built the branch in the running n8n workflow: 17 nodes, from Explode For Story Fetch through the
story and comment fetches, Clean & Group Comments, the Groq call and Attach Opinions, to the
sector clustering. With the column live, I put `community_opinions` back into the dashboard's
query so its Community Opinion panel shows real data instead of a placeholder.

The sector step pushed back first. Early on, with every entity degraded, the clustering call still
wrote a confident sector narrative out of nothing. I put a Has Usable Opinions check in front of
it, so when nothing usable exists the run routes to Skip Sector Clustering and no model call is
made.

**The Community Opinion branch failed for every company.** The design asked the model for
verbatim quotes from commenters, and the request used Groq's strict JSON mode. Comment text is
full of quotation marks, and `llama-3.3-70b` mis-escaped them under constrained decoding, so Groq
returned `json_validate_failed` and every entity failed. Because the branch was designed to
degrade instead of crash, the run completed normally. Nothing looked broken except that every
opinion was empty. I removed strict mode, added a lenient parser in `Attach Opinions` that pulls
the JSON object out of whatever text comes back, and changed the prompt to ask for paraphrased
highlights instead of verbatim quotes. That took the branch from 0 of 12 working to 9 of 12.

**The output was confident and wrong.** Once opinions were coming back, I read them, and OpenAI's
and Anthropic's both praised presentation software. The top story for both was a Show HN post for
Bento, a slide tool, with 1,018 points. It mentioned Claude and ChatGPT in its body. Top stories
were picked purely by points, and the search matches a term anywhere in a story, so the most
popular post that mentioned them won. The low-confidence guard did not catch it, because it only
flags opinions built on fewer than 3 comments and this post had 15. The analyser had worked
correctly on the wrong input. I put this in the video as an open finding rather than cutting it,
and scheduled the fix for the next week: a story only counts for a company if the company is
named in the title.

## What Claude contributed, and what I did with it

Claude wrote the first draft of `dashboard/index.html`, the mock mode and fixture, and
`docs/dashboard_design.md`, and it wrote most of `community_opinion.py` and its 12 fixture tests.
It drafted the n8n wiring for both as written specs, and the design doc itself says that wiring
had not been verified against a running instance.

Everything after the drafts was mine, and that is where most of my week went. I built both
workflows in my live n8n, ran the Supabase migration, set up the container configuration and
credentials, debugged the wiring and the Groq failure, connected the dashboard panel to the new
column, and checked the result in a browser against real data. The six wiring failures above were
all found by running the workflow against my own n8n and Supabase and reading the errors. Code review would not have found
the file sandbox, the `$env` block or the Web Locks error, because they come from how my instance
is configured, not from the code. The wrong key was a mistake in my own setup, and catching it
came from checking what the key actually was rather than trusting that it worked.

The Community Opinion design Claude drafted asked for verbatim quotes under strict JSON mode, and
that combination is exactly what broke. Choosing paraphrase over verbatim was a tradeoff I made:
it loses the exact wording but keeps the output valid.

The Bento finding is the one I am most sure no tool would have caught. Every check passed. The
output was well formed, the confidence flag was correct for the rule it implements, and the
summary was faithful to the comments it was given. It was only wrong if you read it and knew that
OpenAI does not make slide software.

## What I understand now, and what I still do not

**Understood.** n8n's defaults (file sandbox, blocked environment access, strict expression
syntax) are security features, and working with them is better than switching them all off. A
Supabase anon key is only safe in a browser if row-level security restricts it, and the
`service_role` key is never safe there. Graceful degradation can hide a total failure: a pipeline
that never crashes can still be returning nothing. And a correct analyser on misattributed input
produces a confident wrong answer, which is worse than a missing one.

**Not yet understood or verified.**

- I have not explicitly tested that the anon key's row-level security policy rejects writes. I
  only know reads work. That check is still open in the worklog.
- The trend chart draws a marker where the watchlist version changes. Both the fixture and the
  live data are all version v1, so that code has only ever run in the "no boundary" case.
- I know 9 of 12 companies returned an opinion after the fix, but the record does not say why the
  other three did not.
- The dashboard displays an attention score whose link to share price my own backtest in week 6
  could not show (0 of 7 tests survived correction). It measures attention, and I should not let
  a clean leaderboard suggest it measures more.
