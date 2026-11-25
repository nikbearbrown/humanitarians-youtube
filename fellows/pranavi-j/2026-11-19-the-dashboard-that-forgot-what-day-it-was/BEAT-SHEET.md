# Beat Sheet (APPROVED — Gate P, 2026-11-19): "The Dashboard That Forgot What Day It Was"

**Creator:** Sai Pranavi J. | Weekly work video
**Format:** `work-report`, same register as this fellow's prior Project 29 reports
**Phase:** 2 — approved for narration lock / audio generation.

---

## Premise

**What this covers:** a real bug found and fixed this week (F1) in Project 29's regulatory
intelligence backend (`mycroft`), `Regulatory_QA/backend/app/crud.py`'s `FeedCRUD.get_stats()`.
D1 (2026-11-03) fixed *which column* the dashboard's severity breakdown reads (`impact_level`
instead of stale re-derived `urgency_score` cutoffs) and, in the process, flagged — but did not
close — a second, separate defect in the same query: the `urgency_distribution` query was
filtered to `WHERE created_at >= NOW() - INTERVAL '7 days'`. The live `mycroft_intelligence` DB's
fixture data has `created_at` between 2026-07-14 and 2026-07-24 — today is 2026-11-19, four months
later — so that filter unconditionally returns zero rows, on every single page load, forever,
since nothing re-ingests the fixture. Meanwhile `total_feeds` (same endpoint) is an unwindowed
`COUNT(*)`, and `list_feeds()` — which backs the always-visible `FeedList.jsx` panel, including
the "Select All" button fixed last week in E1 — applies no date filter at all. Result: the
dashboard's stats cards read "Total Feeds: 411, Critical: 0, High Priority: 0" while the feed list
directly below shows 24 real Critical- and 8 real High-tagged items a user can click and select
right now. Zero clicks to reach — it's the default page load, not an edge case.

**The fix:** drop the 7-day filter from the severity-count query only, so it reads the same
unwindowed population as `total_feeds` and `list_feeds`. `source_distribution`'s 30-day window and
`recent_activity`'s 14-day window were deliberately left alone — `recent_activity` is an
intentional time series (a windowed trend is the point), and `source_distribution` isn't directly
contradicted by an adjacent always-visible panel the way severity is.

**What this deliberately avoids:** no claim that `source_distribution`'s own 30-day window is
fixed — it has the same structural staleness risk and is called out at full weight as an open
follow-up, per `RUN_LOG.md`'s own "Open issues" line. No claim of a live running
backend/frontend browser session — this session verified by running the real pre-fix and
real post-fix query text directly against the live Postgres DB, not by loading the dashboard in a
browser.

**Source status:** real Project 29 (`mycroft`) engineering fix, closed 2026-11-19
(`Regulatory_QA/backend/app/crud.py`; commit `a7e1628` on `feature/regulatory-intelligence-
hardening`; see `RUN_LOG.md`'s 2026-11-19 entry and `F1-VERIFICATION.md`). Independently
re-verified this session via a live Python/psycopg2 harness
(`verification/verify_stale_stats_window.py`) that extracts the real, current severity SQL from
`crud.py` on disk, confirms it matches verbatim, reconstructs the pre-fix query by re-adding
exactly the removed clause, and runs BOTH — unmodified — directly against the real, live
`mycroft_intelligence` Postgres DB (411 rows, `localhost:5431`), plus a separate replication of
`list_feeds()`'s actual default ordering/limit. See `SOURCES.md` and `FACTCHECK.md`.

---

## Legibility Contract (what's on screen at each claim)

| Beat | On-screen artifact | Legibility note |
|---|---|---|
| B00 Title | Title card, silent | No narration |
| B01 Exec summary | Fellow name + one-line plain-language summary | Narrated, matches program's fixed format |
| B02 Hook | Fixture date range vs. today's date, vs. the 7-day window — the arithmetic that guarantees zero rows | Verbatim real dates/window from `F1-VERIFICATION.md`/live DB |
| B03 Setup | The real pre-fix `WHERE` clause, the real `Stats.jsx` card labels, and the real unwindowed `list_feeds`/frontend `limit: 100` | Verbatim from `crud.py` (pre-fix), `Stats.jsx`, `App.jsx` |
| B04 Discovery/fix | The real one-line diff removing the `WHERE` clause, matches `F1-VERIFICATION.md`'s "The fix" exactly | Real diff, not illustrative |
| B05 Verification | The real before/after numbers from this session's own live Postgres query run | Real measured results against the live DB, not illustrative |
| B06 Honest limits | What was NOT fixed (`source_distribution`'s own 30-day window) and what was NOT done (no live browser/frontend session) | Full weight, no softening |
| B08 Sign-off | Brand card | @HumanitariansAI, in for Sai Pranavi J. |

---

## Beats

**B00. Title (silent, ~0:00–0:04)**
Visual: title card — "The Dashboard That Forgot What Day It Was" + @HumanitariansAI. No narration.

**B01. Exec summary (~0:04–0:21)**
VO: "Hi, I'm Sai Pranavi J. This video is about a dashboard whose severity counts went blind the
moment its fixture data got old enough — a seven-day filter that quietly zeroed out Critical and
High, forever, while the list right below it kept showing the real thing."
Visual: name card, one-line summary text on screen as it's spoken.

**B02. Hook (~0:21–0:44)**
VO: "The data this dashboard reads from was loaded back in July. Today is November nineteenth —
four months later. And the severity query behind the stats cards only ever looked back seven
days. Seven days, against data four months stale, is zero, every single time."
Visual: fixture date range (July 14 to July 24, 2026) next to today's date (November 19, 2026) and
the seven-day window, with the arithmetic flagged as impossible.

**B03. Setup (~0:44–1:14)**
VO: "Here's the real query. It counted Critical, High, Medium, and Low, but only from rows created
in the last seven days. Total Feeds, right next to it on the same dashboard, had no such filter.
And the feed list underneath — the one with Select All — loads the hundred most recent items, no
date filter either. So the cards said Critical: zero, High Priority: zero. The list below them was
full of both."
Visual: the real pre-fix `WHERE created_at >= NOW() - INTERVAL '7 days'` clause, the real
`Stats.jsx` labels ("Total Feeds", "Critical", "High Priority"), and the real unwindowed
`list_feeds` ordering with the frontend's real `limit: 100`, shown verbatim.

**B04. Discovery and fix (~1:14–1:36)**
VO: "The fix is one line: drop the seven-day filter from the severity query, so it reads the same
unwindowed population as Total Feeds and the feed list already do. Source breakdown's thirty-day
window, and recent activity's fourteen-day window, stay untouched — recent activity is supposed to
be a time series, and source breakdown isn't contradicted by an always-visible panel the way
severity was."
Visual: the real one-line diff removing the `WHERE` clause, plus a note on what was deliberately
left alone.

**B05. Verification (~1:36–2:05)**
VO: "I ran both versions of the query directly against the live database. The old query, with the
seven-day window: zero, zero, zero, zero. The new query, unwindowed: thirty-three Critical, ninety-
eight High, two hundred eighty Medium — matching last week's independently verified counts
exactly. And the feed list's actual top hundred items, same database, no date filter: twenty-four
Critical, eight High, right there to click."
Visual: the real before/after table from this session's own live Postgres run — 0/0/0/0 versus
33/98/280/0, plus the 24/8 top-100 slice.

**B06. Honest limits (~2:05–2:33)**
VO: "Two honest limits. First: source breakdown still has its own thirty-day window, with the same
staleness risk as the one just fixed — not touched this round, a reasonable follow-up, not
required to close this bug. Second: this was verified by running the real query text straight
against the live database, not by loading the dashboard in a running browser session — no frontend
or backend server was up this session."
Visual: 2 honest-limit cards, side by side, full weight, no softening language.

**B07. Takeaway (~2:33–2:44)**
VO: "A dashboard's summary is only as honest as the window it looks through — and a window that
quietly stops matching the data underneath it is worse than no window at all."
Visual: statement card.

**B08. Sign-off (~2:44–2:46)**
VO: "Explained with Claude Code."
Visual: brand card — @HumanitariansAI, in for Sai Pranavi J..

---

## Production Gate Self-Check (pre-review)

- [ ] B02/B03's quoted dates, window, SQL clause, and `Stats.jsx` labels shown verbatim, match the
      real pre-fix `crud.py` and the real `Stats.jsx`/`App.jsx` on disk
- [ ] B04's diff matches the real committed fix exactly (per `F1-VERIFICATION.md`)
- [ ] B05's numbers are real measured results from this session's own live Postgres run, not
      illustrative; matches `F1-VERIFICATION.md`'s own verification table exactly (0/0/0/0 ->
      33/98/280/0; 24 Critical / 8 High in the top-100 slice)
- [ ] B06's honest limits kept at full weight, not softened: `source_distribution`'s own
      unaddressed 30-day window, no live browser/frontend session
- [ ] Silent title card present; brand/fellow sign-off card present
- [ ] No claim that this was observed to break a real user's session in production — this closes a
      confirmed, reproducible defect, verified via live-DB query replication, not an observed
      incident

**Estimated runtime:** ~2:46 (draft estimate; real timing measured after Kokoro audio generation,
per the toolkit's audio-first rule — see `SHOTLIST.md` for the measured total).

---

## Gate P — approved

Fellow reviewed and approved this beat-by-beat outline 2026-11-19. See `FACTCHECK.md`. Cleared to
generate Kokoro audio and proceed to previz.
