# CHECKS-REPORT — written before the first slate

11 SHOW / 1 justified-HOLD (B09 verdict) / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ (B03 robot, B04 sim-to-real) | WORKED EXAMPLE ✓ (one duck through the pipeline: B05 sim → B06 export → B08 stage)
              FALSIFIABILITY ✓ (B08 live failure; B07 numbers recomputed by evidence/sim_to_real_toy.py) | SCAFFOLDED TASK ✓ (B10) | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓ (SOURCES.md)
GATE L: `./art scenes` had no biped/robot scene ("biped robot walking falling" = PUNT, logged to TEMPLATE-MISSES.md); DtlChipGrid / JevParallel / Illu-SourceFlow were leads, not fits → new runtime/remotion/src/MicroduckSim.tsx (7 scenes × 16:9 + 916, reusable <Duck>), registered in Root.tsx. Reused ClaudeComposerAsk, BrutalistHesitantWriter, ClaudeVerdictArtifact, HaiOutro (+916).
