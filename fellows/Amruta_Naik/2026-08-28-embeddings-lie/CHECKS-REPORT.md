# CHECKS-REPORT — embeddings-lie

Reel: `Why Your Embeddings Lie About Similarity`
Skill: `ai-explainer` · brand `claude-liam` · channel `@HumanitariansAI`
Voice: Kokoro `am_onyx` (free, local) · aspect 16:9
Written BEFORE the first slate compile, per PROOF GATE.

## Beat classification

    5 SHOW / 3 justified-HOLD / 0 PUNT-flagged

| Beat | Act | Pattern | Class | Note |
|---|---|---|---|---|
| B00 | ask (cold open) | ClaudeComposerAsk | SHOW | Command types itself; output lines stagger in. UI is the subject (COLD OPEN LAW). |
| B01 | bluf | ClaudeComposerAsk | HOLD | Executive summary (EXECUTIVE-SUMMARY LAW). Four output lines reveal in narration order. UI-anchored rather than concept-illustrated — see ILLUSTRATE LAW note below. |
| B02 | illustrate | ClaudeComposerAsk | HOLD | Worked example (cat/mat). The contrast is carried by the output lines, not by a divergence illustration. See note below. |
| B03 | mechanism | ClaudeCodeBeat | SHOW | Real code-comment block; lines reveal on a stride. Names its artifact: the cosine-similarity definition. Spark line `Words, not logic.` |
| B04 | consequence | ClaudeComposerAsk | HOLD | RAG failure chain. Same note as B01/B02. |
| BVDT | verdict | ClaudeVerdictArtifact | SHOW | Fixed verdict template. Artifact card scales in, four numbered lines stagger. |
| BHTF | your turn | ClaudeComposerAsk | SHOW | HANDOFF LAW: prompt typed into composer, greeting `Your turn.`, read aloud and discussed in narration. |
| BOUT | outro | ClaudeTitleOutro | SHOW | Fixed outro template. Title restate + terracotta period + handle + subline (OUTRO LAW). |

## Teaching arc

    FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✗
    SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓

- **FRAMEWORK ✓** — B01 states the whole mechanism in one breath (text → point →
  nearest → surface similarity) before B02's example. Framework precedes examples.
- **WORKED EXAMPLE ✓** — B02, "The cat sat on the mat" vs "The mat sat on the cat";
  B03 generalises it to "X approves Y" / "X rejects Y".
- **FALSIFIABILITY ✗** — VIOLATION. No beat stress-tests the thesis. Nothing asks
  "when is similarity actually enough?" or "does a bigger embedding model fix this?"
  Justified in BUILD-LOG.md; flagged to the author for a decision.
- **SCAFFOLDED TASK ✓** — BHTF gives a four-step procedure on the viewer's own
  search system, not a vague "go explore".
- **BOOKENDS ✓** — cold open (B00) → BLUF (B01) → body → verdict (BVDT) →
  handoff (BHTF) → title-restate outro (BOUT). Spine intact.
- **NO-SOURCE-NO-VERDICT ✓** — BVDT rests on definitional claims (cosine similarity
  measures the angle between vectors; surface-overlap embeddings under-weight
  negation and word order). No empirical figures, percentages, or study results
  appear on screen, so no citation is owed and none is invented.

## Legibility contract

- Every SHOW/HOLD beat names its on-screen artifact in `shot.remotion.props`.
- All four patterns are the shipped, gate-passed templates — no new scene source
  was written for this reel, so `SAFE`-inset compliance is inherited.
- Un-highlighted elements: no opacity below ~40% in any template used.
- Verdict card holds four lines for the full beat (~21s) — well past the 2s floor.

## Open violations carried into the build

1. **FALSIFIABILITY beat missing** (arc). See BUILD-LOG.md.
2. **ILLUSTRATE LAW smell** — five of eight beats are `ClaudeComposerAsk`, and
   B01→B02 are consecutive beats sharing one visual scheme. The law reserves the
   Claude UI for beats where the UI is the subject. See BUILD-LOG.md.

Neither was silently passed.
