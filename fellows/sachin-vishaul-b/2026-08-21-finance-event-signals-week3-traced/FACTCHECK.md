# FACTCHECK — "Claude, Traced." (Week 3)

| Claim (beat) | Verdict | Source |
|---|---|---|
| Kafka doesn't propagate trace context natively; needs a header carrier (B01/B03) | ✓ | `services/common/kafka.go` lines 14, 45-49 (verbatim) |
| One real trace, unbroken parent→child across 3 Kafka hops (B04) | ✓ | `RUN_LOG.md` Week 3a verification table, trace `e9dae472…` row |
| `topic-init` readiness probe never matched in-cluster (B05/B06) | ✓ | `deploy/k8s/infra.yaml` lines 108-112 (verbatim real fix); `RUN_LOG.md` account of the bug |
| Killed `ingest-gateway` pod mid-run → 0 restarts downstream, row count unchanged (B07) | ✓ | `RUN_LOG.md` Week 3b verification table, chaos-test row |
| HPA configured and reporting real metrics but never demonstrated a scale-out (B08) | ✓ | `RUN_LOG.md` "Finding — HPA is configured and functional but not demonstrated scaling" |
| Recipe stays `DRAFT`, `todos_open: 3`, unchanged through Week 3 (B09) | ✓ | Recipe frontmatter, unchanged since Week 2 gap-closing commit |

## Corrections applied

None needed.

## Numbers on screen

None invented — every number is a direct quote from RUN_LOG.md or a real
source file.
