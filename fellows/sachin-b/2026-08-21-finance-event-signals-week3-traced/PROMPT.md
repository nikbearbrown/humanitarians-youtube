# PROMPT — "Claude, Traced." (Week 3)

## The brief

Turn Week 3 of `finance-event-signals` into a ≤3-minute build-log video:
distributed tracing across Kafka, then the same stack on Kubernetes with a
chaos test — including the HPA limitation, disclosed honestly.

## Constraints given

| Constraint | Resolution |
|---|---|
| ≤3:00 target | Measured 2:10 |
| Real content only | Every trace, every chaos-test number, traces to `RUN_LOG.md` |
| At least one real revision cycle | The `topic-init` readiness-probe bug and its fix |
| A falsifiability beat | The HPA-never-scaled finding |
| Skin choice | `github` for code/diff/pipeline beats; `claude` bookends only |
| Persona | `claude-liam` (Kokoro `am_onyx`) |

## Structure

```
B00  cold open        both halves of the week named
B01  framework        why Kafka needs manual header work
B02  ask              inject/extract trace context
B03  code             the real kafka.go
B04  output           a real Jaeger trace, 3 hops
B05  change           readiness probe loops forever
B06  code (revision)  the real fix
B07  output (chaos)   kill a pod, zero data loss
B08  falsifiability   the HPA finding
B09  summary          two wins, one gap
B10  handoff          run your own chaos test
B11  outro            title restate
```
