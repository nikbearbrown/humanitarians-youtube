# CHECKS-REPORT — AI in Your Project Management Tools

Reel: `ai-project-management-tools` · ai-explainer (claude-explainer) · @HumanitariansAI

## Beat classification (nopunt: SHOW / HOLD / CARD / PUNT)

| Beat | Role | Class | On-screen artifact |
|---|---|---|---|
| T00 | Cold open (ClaudeComposerAsk) | SHOW | composer types the ask; result lines land |
| T01 | BLUF (BrutalistHesitantWriter) | SHOW | the overview written + corrected on screen |
| T02 | Problem (Manim) | SHOW | tool chips; hope=AUTOPILOT vs reality=FAST INTERN |
| T03 | Framework (Manim) | SHOW | THE TICKET TEST — 3 question rows, green/red sides |
| T04 | Ask (ClaudeComposerAsk) | SHOW | composer types the drafting ask |
| T05 | Worked example (Manim) | SHOW | note → 4 tickets; 3-green scorecard → AI DRAFTS |
| T06 | Falsifiability (Manim) | SHOW | same test, 3 reds → HUMAN DECIDES; stale-board flip |
| T07 | Summary/verdict (Manim) | SHOW | DRAFT & SURFACE vs DECIDE & COMMIT router |
| T08 | Handoff (ClaudeComposerAsk) | SHOW | composer types the viewer's prompt; read aloud |
| T09 | Outro (ClaudeTitleOutro) | SHOW | title restate + @HumanitariansAI |

**10 SHOW / 0 justified-HOLD / 0 PUNT-flagged.**

## Teaching arc

- FRAMEWORK ✓ — T03 (The Ticket Test) lands BEFORE the first worked example (T05).
- WORKED EXAMPLE ✓ — T05 walks the stand-up-note → tickets case through all three axes.
- FALSIFIABILITY ✓ — T06: same tool/AI scores three reds; plus the stale-board green→red flip.
  Proves the framework isn't reverse-engineered (a case that fits the OTHER verdict).
- SCAFFOLDED TASK ✓ — T08 hands a copyable prompt with an explicit "stop at judgment +
  ask me the question you'd need" clause; names good-vs-bad answers. Not "ask Claude".
- BOOKENDS ✓ — cold open (T00) · hesitant-writer BLUF (T01) · handoff (T08) · title outro (T09).
- NO-SOURCE-NO-VERDICT ✓ — every routing verdict is shown with its 3-axis scorecard visible
  and legible at the moment of assertion; no external unsourced statistics anywhere.

## Legibility contract (each SHOW claim beat)

- Names its on-screen artifact in `visual_intent` / `role_note`. ✓
- ~15–35% negative space (Claude cream ground, restrained). ✓ (verify in _qc)
- Un-highlighted elements not below ~40% opacity. ✓ (muted = #B7AE9E, ~solid)
- Comparisons side-by-side, held ≥2s: T02 hope|reality, T06 gut-red rows, T07 two columns. ✓

## Audio-first / pacing

Per-beat af_bella durations are the master clock (mp3/). Manim scenes paced to keep
conform slow-factor ≤ ~1.3× on every beat (T02 1.28 / T03 1.15 / T05 ~1.17 / T06 1.30 /
T07 ~1.14 after re-pace) — no sluggish slow-mo.
