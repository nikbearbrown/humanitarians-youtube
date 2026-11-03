# SOURCES — AI Effort Estimation

Per the DOUBLE-CHECK LAW: no fabrication, no undated claims, every on-screen
number produced by the reel's own runnable code.

## On-screen numbers — all derived, all reproducible
Every figure shown comes from one seed-locked dataset in `scenes.py`, which is
identical to the `HISTORY` / `VELOCITY` shown in the `estimate.py v2` CODE beat (B07):

```
CLASSES = {"integration": [4,6,7,9,14], "ui_form": [1,2,2,3], "crud": [2,3,3,4,6]}
VELOCITY = 1.15
```

Computed with `numpy.percentile(actuals, [50, 80]) * VELOCITY`:

| Task | Class | Gut (v1) | P50 | P80 |
|---|---|---|---|---|
| OAuth login | integration | 5 | 8.0 | 11.5 |
| Settings page | ui_form | 2 | 2.3 | 2.8 |
| Export endpoint | crud | 3 | 3.4 | 5.1 |

- Gut sprint total = 5 + 2 + 3 = **10 days**.
- Honest P80 total = 11.5 + 2.8 + 5.1 = **~19 days**.
- Each gut number lands at or below its class's P50 — i.e. on the optimistic edge.
  This is the reel's central, self-verifying claim.

The dataset is an illustrative sample project's history (clearly framed as "your
team's finished work"). It is not a citation of any external project — it is the
worked example, and every number shown is computed from it, so the video passes
its own "no source, no verdict" rule.

## Concept — reference-class forecasting
Reference-class forecasting is an established estimation method (taking the "outside
view": estimate a new case from the distribution of outcomes of similar past cases,
rather than from a bottom-up "inside view" guess). The "planning fallacy" — the
tendency to underestimate task time even when we know similar tasks ran long — is a
well-documented cognitive bias. No specific author, study figure, or model version
number is shown on screen, so nothing here dates the video.

## Honesty notes
- No model version numbers, benchmark scores, or drifting counts on screen.
- The v1→v2 effect is large and shown as an explicit number (10 → ~19), addressing
  the prior film's noted weakness (a subtle effect). Not exaggerated: it is the
  literal sum of the computed P80s.
- The falsifiability case (DB migration, no reference class → spike it) is the honest
  boundary of the method and is shown, not just voiced.
