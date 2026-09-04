# Claude, Traced.

Week 3 build-log: distributed tracing through Kafka record headers (one
accession = one trace across 4 services), then the same stack deployed to
Kubernetes with a passing chaos test. Real bug: the `topic-init` readiness
probe never matched in-cluster. Honest finding: the HPA is wired and
reporting real metrics but was never demonstrated scaling — disclosed, not
hidden.

| | |
|---|---|
| **Runtime** | 2:10 (129.5s) |
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
| B00 | Cold open | Trace one request across services, then move it all to Kubernetes |
| B01 | Framework | Kafka doesn't carry trace context for free — inject/extract by hand |
| B02 | Ask | Inject context into Kafka record headers on produce, extract on consume |
| B03 | Code | The real `kafka.go` — `recordCarrier`, `ProduceSpan` |
| B04 | Output | A real trace: one accession number, unbroken parent→child across 3 hops |
| B05 | Change | The `topic-init` readiness probe loops forever in-cluster |
| B06 | Code (revision) | The real fix — wait on `rpk topic list`, not a health-check string |
| B07 | Output (chaos test) | Kill a pod on purpose: 0 restarts downstream, 0 rows lost |
| B08 | Falsifiability | The HPA never demonstrated scaling — disclosed honestly |
| B09 | Summary | Two wins, one honest gap — the recipe doesn't move on vibes |
| B10 | Handoff | Your turn: kill a pod in your own cluster, check three things |
| B11 | Outro | "Claude, Traced." |

## Source of every claim

See `FACTCHECK.md` and `SOURCES.md` — every number traces to a real
`RUN_LOG.md` entry or commit in the underlying project.
