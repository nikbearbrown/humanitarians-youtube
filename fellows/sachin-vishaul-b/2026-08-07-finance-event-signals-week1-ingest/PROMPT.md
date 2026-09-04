# PROMPT — "Claude, Ingested." (Week 1)

## The brief

Turn Week 1 of a real 4-week portfolio project (`finance-event-signals`, a
SEC 8-K signal pipeline exercising Go, Kafka, Redis, Postgres, gRPC,
Docker, Kubernetes, OTel, and LangGraph against the Snickerdoodle recipe
lifecycle) into a ≤3-minute build-log video: what got built, what broke,
what got fixed, on camera, with real evidence for every claim.

## Constraints given

| Constraint | Resolution |
|---|---|
| ≤3:00 target | Measured 2:17 |
| Real content only, no invented numbers | Every code line and every count traces to a real git commit or `RUN_LOG.md` entry |
| At least one real revision cycle | Two real bugs shown breaking then fixed (gzip header, CIK URL) |
| A falsifiability/limitation beat | The FTS-lookback-window finding, disclosed honestly |
| Skin choice | `github` (real repo cutaway) for code/diff/pipeline beats; `claude` bookends only |
| Persona | `claude-liam` (Kokoro `am_onyx`), free/local, IN-FOR-BEAR LAW applied |

## Structure

```
B00  cold open       persona + series framing
B01  framework       the 5-hop pipeline chain
B02  ask             build the EDGAR HTTP client
B03  code            the real buggy secclient.go
B04  output          broken — real failure text
B05  change          the fix, as a prompt
B06  code (revision) the real diff
B07  output (fixed)  97 events, idempotency proven
B08  falsifiability  the lookback-window finding
B09  summary         recipe stays DRAFT
B10  handoff         scaffolded viewer task
B11  outro           title restate
```
