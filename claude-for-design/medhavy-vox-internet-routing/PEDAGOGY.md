# PEDAGOGY — medhavy-vox-internet-routing

## What the learner already knows
Shortest path, what a router does, the concept of a graph

## What this reel teaches
Bellman-Ford distributed shortest-path: each router stores one distance estimate per destination. Update rule: d_v = min over neighbors w of (c_vw + d_w). Distances ripple outward from destination in synchronous rounds, converging to true shortest distances in n-1 rounds. No router needs the full graph.

## Key facts
- Each router: one distance estimate per destination ✓
- Update rule: d_v = min(c_vw + d_w) ✓
- 5-node chain: correct distances in 4 rounds ✓
- Converges in n-1 rounds ✓
- Bellman-Ford 1958 → RIP → modern internet ✓

## Exclusions honored
- No convergence proof
- No negative-cost loop pathology
- No BGP/OSPF engineering details

## Medhavy register compliance
- FIRST beat: MedhavyOpen (B00) ✓
- LAST beat: MedhavyOutro (B11) ✓
- narration_text phonetics: "med davy A-I" / "med davy dot com" ✓
- No exercise beat ✓
- Wonder register: genuine curiosity about how a network routes itself; builds from update rule to convergence to fixed point ✓
- Palette: medhavy (Okabe-Ito) — TEAL #009E73, CRIMSON #D55E00 ✓

VERDICT: PASS
