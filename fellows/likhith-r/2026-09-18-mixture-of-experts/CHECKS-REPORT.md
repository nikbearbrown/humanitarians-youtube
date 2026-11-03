# CHECKS-REPORT — written before the first slate

11 SHOW / 1 justified-HOLD (B09 verdict) / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ (B03 dense baseline) | WORKED EXAMPLE ✓ (B05–B06, one sentence routed token by token; B07 real Mixtral figures) | FALSIFIABILITY ✓ (B08 memory cost — where MoE does not win)
              SCAFFOLDED TASK ✓ (B10) | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓ (SOURCES.md)
GATE L: reused ClaudeComposerAsk, BrutalistHesitantWriter, ClaudeVerdictArtifact, HaiOutro (+916). `./art scenes` searches (router / sparse activation / dense / total-vs-active / memory-vs-compute) returned no MoE fit — misses logged. New dual-aspect: runtime/remotion/src/MoeExplainer.tsx (7 scenes).
