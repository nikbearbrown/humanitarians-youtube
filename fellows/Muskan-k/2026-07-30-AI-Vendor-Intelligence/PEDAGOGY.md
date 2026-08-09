# PEDAGOGY — Fifty Vendors, One Brief. (claude-hai · ai-explainer, mechanism)

**The ONE insight:** scattered public signal about AI vendors becomes one
scored, auditable, cheap-to-run brief per company — and its honesty is the
whole point.

**Audience (claude-hai):** learners deciding which AI tools to trust — the
channel's spine is *when to lean on a tool and when not to*. So the reel
teaches the mechanism AND names where it can mislead you.

## Act structure (ai-explainer spine)
- B00 COLD OPEN on `ClaudeComposerAsk`, ask answered (RESULT output lines) ✓
- Body B01–B05 illustrate the pipeline; UI does NOT reappear until the verdict
  (ILLUSTRATE LAW) ✓
- Visual-scheme rotation, no two consecutive alike:
  SourceFlow → ChipGrid → LayerStack → ChipGrid → LayerStack ✓
- B06 VERDICT one-page artifact · B07 HANDOFF ("Your turn.", prompt read + discussed) ·
  B08 title-restate OUTRO ✓
- SHOW-DON'T-TELL: every body beat carries a `show` block; body narration 45–70 words ✓

## Evidence discipline (DOUBLE-CHECK LAW — every on-screen claim traces to the platform)
| Claim on screen | Source in the platform | Verdict |
|---|---|---|
| 50 AI vendors, seeded | `collector/seed_companies.json` | OK |
| 5 sources: SEC EDGAR, GitHub, ArXiv, Google News RSS, Neo4j | collector architecture (user brief) | OK |
| Signal taxonomy + importance 0–100, one row per signal | `ai_company_signals` schema | OK |
| Same-day caching; per-brief token/cost logging | `brief_cache`, `brief_costs` tables | OK |
| Competitor/investor graph is hand-seeded | Neo4j "manually seeded" note | OK — stated as a limit, not hidden |

## Friction protected (Pragmatist register: the limits ARE the lesson)
- Kept: public data lags, scores are heuristics, the graph is only as fresh as
  its last hand-edit — said plainly in B04 and the verdict. Removing these would
  make the reel oversell the tool, which is exactly what the hai channel warns against.
- Kept: the cost line (B05) — the reason it's usable daily, not a footnote.

## Narration review (GATE P)
Review this on the ANIMATED slate previz (run `ART_FACTS=0 ./art run <reel>`),
not as text. Listen for: does each body beat's voice REACT to what's on screen
(not recite it)? Does B07's prompt get read aloud AND discussed?

VERDICT: PASS — sign "VERDICT: PASS" here after you review the narration.
