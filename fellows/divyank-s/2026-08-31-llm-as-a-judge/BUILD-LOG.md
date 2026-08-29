# BUILD-LOG — Claude, Judged.

## Decisions

- **No single source document.** Unlike the three prior builds this
  session, this topic (LLM-as-a-judge evaluation systems) isn't explained
  from one book/chapter — it's a software engineering pattern. Content is
  general, well-established practice plus one specific citation (Zheng et
  al. 2023) for the bias taxonomy. See `FACTCHECK.md`'s method note for the
  General/Cited discipline used to avoid inventing statistics or
  tool-specific claims.
- **8 required points → 4 acts of 2 points each.** Test Case Structure +
  Judge Prompts (Act I, the input side), Output Parsing + Bias Mitigation
  (Act II, the judgment side), Metric Abstraction + Batch Evaluation Runner
  (Act III, the system side), Aggregation + CI/CD Integration (Act IV, the
  pipeline side) — a coherent Define → Judge → Scale → Ship arc.
- **No Manim** (same `pangocairo` gap as the prior two builds) — the
  documented MANIM lane share is absorbed into REMOTION.
- **VOX quota met with metaphor imagery, not literal depictions.** The
  topic has no historical photographic referent, so all 6 archival stills
  illustrate a CONCEPT (a structured record, the judge role, transcribing
  a signal, fairness, an assembly line, continuous production) rather than
  the subject itself — captioned as such everywhere, per the DOUBLE-CHECK
  LAW's honesty requirement extended to imagery, not just narration.
- **Two new Remotion compositions added:** `DivergentFates916` and
  `BinaryBranch916` in `runtime/remotion/src/Root.tsx`. Both underlying
  components (`deckPatterns.tsx`) already read `useVideoConfig()` for their
  own width/height rather than hardcoding 1280×720, so registering them a
  second time at 1080×1920 required zero new component logic — just two
  `<Composition>` entries. **Known limitation:** neither component was
  actually re-laid-out for a narrow portrait canvas, so expect a tighter
  horizontal spread than a purpose-built portrait design would choose;
  this reel's other content-lane components (`ClaudeScienceChipGrid`,
  `ClaudeScienceLayerStack`, `FluencySegmentCard`) have no portrait
  variant at all and were NOT given one — see the Short's own build notes
  for how surviving beats were chosen with this in mind.
- **Two-deliverable plan:** one 16:9 master (this folder, the full 8-point,
  ~8-minute deep-explainer) and one 9:16 Short (`short/`, derived via
  `runtime/scripts/shorts.py` — a hard-capped 3:00 derivative that AUTO-CUTS
  the longest unprotected middle beats rather than being separately
  authored). Both compiled at 4K (16:9 → 3840×2160; 9:16 → 2160×3840).
