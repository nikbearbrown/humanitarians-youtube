# Claude, Ingested.

Week 1 build-log: the data spine of `finance-event-signals`, a SEC 8-K
signal pipeline built against the Snickerdoodle recipe lifecycle.
ingest-gateway polls two independent EDGAR sources, dedupes through Redis,
and persistence-svc idempotently upserts into Postgres — with two real bugs
(gzip double-decompression, a wrong-CIK archive URL) found and fixed on
camera, and one honestly disclosed edge case (a wide lookback window
silently swallowing a whole source).

| | |
|---|---|
| **Runtime** | 2:17 (136.7s) |
| **Format** | 16:9, 3840×2160 (4K), 24 fps, h264/aac |
| **9:16 cut** | Not yet built (flagged — see BUILD-LOG.md) |
| **Voice** | Kokoro `am_onyx` — local, free, no API |
| **Beats** | 12 · Claude-skin bookends + GitHub-dark skin for code/diff/pipeline beats |
| **Presenter** | Sachin Vishaul B |
| **Channel** | @HumanitariansAI (Mycroft) |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art) |
| **Status** | Built and QC'd (GATE V: 0 BLOCKER) · solo build, no independent reviewer · not published |

## What this video covers

| Beat | | |
|---|---|---|
| B00 | Cold open | "Namaste — this is Liam, in for Bear." The 4-week series intro + Week 1's ask |
| B01 | Framework | The 5-hop chain: poll → dedupe → passthrough enrich → persist → store |
| B02 | Ask | Build an EDGAR HTTP client with gzip support |
| B03 | Code | The real (buggy) `secclient.go` — a manual `Accept-Encoding` header |
| B04 | Output (broken) | First run: every fetch fails — `invalid character '\x1f'` |
| B05 | Change | Drop the manual header; resolve the archive URL from the subject company's CIK |
| B06 | Code (revision) | The real diff — `secclient.go` + `edgar_fts.go` |
| B07 | Output (fixed) | 97 events stored; offset-rewind idempotency test: `inserted 0, skipped_dupe 97` |
| B08 | Falsifiability | A 3-day lookback silently absorbed the whole Atom feed — disclosed, not hidden |
| B09 | Summary | The recipe still says `DRAFT` — proving the spine and clearing gates are different jobs |
| B10 | Handoff | Your turn: kill your own consumer mid-batch, rewind, replay, check three things |
| B11 | Outro | "Claude, Ingested." |

## Source of every claim

Every number and every line of code shown traces to a real commit or a real
`RUN_LOG.md` entry in the underlying project. See `FACTCHECK.md` and
`SOURCES.md` in this folder.
