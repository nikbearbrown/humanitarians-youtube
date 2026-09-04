# Claude, Gated.

Week 2 build-log: two new gates in `finance-event-signals` — validation-svc
(the GIGO gate, rejecting malformed data with a reason) and a LangGraph
enrichment agent that withholds rather than fabricates, gated by a human
`ClearGate`. Real bug: LangGraph 0.2.45 rejects a node returning `{}`.
Honest finding: the offline deterministic LLM withholds ~88% of events.

| | |
|---|---|
| **Runtime** | 1:52 (112.1s) |
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
| B00 | Cold open | Two real gates: one machine, one human |
| B01 | Framework | validation-svc (GIGO) → LangGraph agent → query-api ClearGate → actionable |
| B02 | Ask | Reject anything malformed, stale, or missing provenance — and say why |
| B03 | Code | The four real reject paths in `validation-svc/main.go` |
| B04 | Output | Four malformed test events in, four dead-lettered with the right reason each |
| B05 | Change | Every LangGraph node must return a non-empty state delta |
| B06 | Code (revision) | The real fixed line, with its own inline comment documenting the bug |
| B07 | Output (fixed) | 97 events, 97 signals — 12 to review, 85 honestly withheld, 0 crashes |
| B08 | Falsifiability | The offline model's ~88% withhold rate, disclosed as a real limit |
| B09 | Summary | Six open gates down to three — still `DRAFT` |
| B10 | Handoff | Your turn: hit your own gate three ways, check the status codes |
| B11 | Outro | "Claude, Gated." |

## Source of every claim

See `FACTCHECK.md` and `SOURCES.md` — every number traces to a real
`RUN_LOG.md` entry or commit in the underlying project.
