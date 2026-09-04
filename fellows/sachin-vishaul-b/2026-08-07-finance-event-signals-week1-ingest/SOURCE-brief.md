# SOURCE-brief — "Claude, Ingested." (Week 1)

## The original ask

Design and build, from scratch, a portfolio/learning project exercising a
specific tech stack (Go, Python, Kafka, Redis, PostgreSQL, gRPC, Docker,
Kubernetes, Linux, OpenTelemetry, LangGraph) that also makes decent use of
the Snickerdoodle framework's governance discipline (recipe lifecycle,
phase gates, pre-registration, no-fabrication). The plan was split into 4
weeks of incremental work, each week built and logged for real (not
scripted), then turned into a weekly build-log video for the Humanitarians
AI YouTube submission.

## Why Week 1 specifically

Week 1 is the data spine: get real SEC EDGAR filings flowing end to end
through a Go ingest service into Postgres, with idempotency proven, before
any of the later weeks' gates (validation, the LangGraph agent, the human
review gate, OTel, Kubernetes, or grading) exist.
