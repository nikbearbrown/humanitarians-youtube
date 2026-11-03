# CHECKS-REPORT — written before the first slate

11 SHOW / 1 justified-HOLD (B09 verdict) / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ (B03 RAG, B04 OKF) | WORKED EXAMPLE ✓ (one question, "How is revenue calculated?", through both: B03 top-3, B06 walk)
              FALSIFIABILITY ✓ (B03/B06 recomputed by evidence/rag_vs_okf_toy.py; B06 git output by evidence/okf_git_demo.sh) | SCAFFOLDED TASK ✓ (B10) | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓ (SOURCES.md)
GATE L: `./art scenes` hit RagPipeline.tsx (one RAG step per scene) and GitHubCodeDiff; neither covers a one-beat RAG loop or an OKF bundle, so new dual-aspect scenes: runtime/remotion/src/RagOkf.tsx (7 scenes). Reused ClaudeComposerAsk, BrutalistHesitantWriter, ClaudeVerdictArtifact, HaiOutro (+916).
