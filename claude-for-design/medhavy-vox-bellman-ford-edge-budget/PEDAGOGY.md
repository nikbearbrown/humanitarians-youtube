# PEDAGOGY — medhavy-vox-bellman-ford-edge-budget

## Learner Profile
Learner knows: what dynamic programming is, what a shortest-path problem is

## Teaching Goals
Teaches:
- A[i,V] subproblem with edge budget as ordering parameter
- Two-case recurrence: inherit A[i-1,V] or last hop from W
- n-1 rounds suffice for any shortest path without a cycle
- Edge count as ordering resource that creates unambiguous "smaller"
- Generalizable trick: look for consumed resource when ordering seems absent

## Gate Numbers
- A[i,V] = min(A[i-1,V], min_W{A[i-1,W]+cost(W→V)}) ✓
- n-1 rounds suffice ✓
- A[0,source]=0, A[0,others]=∞ initialization ✓

## Exclusions Honored
- No pseudocode
- No negative cycle detection
- No APSP extension

## Color Semantics Check
- TEAL (edge budget / A[i,V] / unambiguous ordering): correctly applied ✓
- CRIMSON (circular dependency / no natural order / naive approach fails): correctly applied ✓

## Beat Structure Check
- B00: MedhavyOpen with exact narration_text ✓
- B01–B10: 10 content beats with t_start and estimated_duration_s ✓
- B11: MedhavyOutro with exact narration_text ✓
- B03: CARD kind:question ✓
- B10: CARD kind:endcard ✓
- Graphic beats use ["#009E73"] or ["#009E73","#D55E00"] ✓

VERDICT: PASS
