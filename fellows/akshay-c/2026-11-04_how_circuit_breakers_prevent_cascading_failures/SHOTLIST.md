# SHOTLIST - How Circuit Breakers Prevent Cascading Failures in Distributed Systems

| Beat | Act | Visual Subject | Motion Type | Primary Source |
|---|---|---|---|---|
| B00 | PROBLEM | Cascading failure: Downstream latency saturating upstream thread pool and crashing services | annotate | manim |
| B01 | SOLUTION | Circuit breaker architecture: Call proxy intercepting traffic between calling service and downstream | annotate | manim |
| B02 | CLOSED_STATE | Closed state: Requests passing through freely while monitoring rolling error window | annotate | manim |
| B03 | TRIP_TRIGGER | Error threshold exceeded: Metric counter triggers instant switch trip to Open | annotate | manim |
| B04 | OPEN_STATE | Open state: 0ms fail fast, returning instant fallback response and relieving downstream load | annotate | manim |
| B05 | HALF_OPEN | Half-Open state: Sleep timer elapsed, sending controlled canary probe requests | annotate | manim |
| B06 | RECOVERY | Dual resolution: Successful probes reset to Closed; failures immediately retrip to Open | annotate | manim |
| B07 | PAYOFF | Production resilience architecture: Circuit breakers, bulkheads, timeouts, and fallback caches | hold | manim |
| B08 | OUTRO | Branded Humanitarians AI closing title card | hold | remotion |
