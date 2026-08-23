# PEDAGOGY — Why AI Evaluation Benchmarks Stop Working, Part 1 (hai claude explainer)

Explains why AI evaluation benchmarks lose their discriminative power over time
(Goodhart's Law, benchmark saturation) and walks through one real, fully
automated system — Benchmark Self-Evolving — built to generate harder test
cases from existing ones. First of a two-part series; Part 2 covers the
Microsoft continuous-benchmark-generation case study, judge-drift, and
metric retirement.

## Act structure

- B00 cold open with RESULT lines (ASK\u2192RESULT at B00) \u2713
- B01 executive summary beat (required for submission review) \u2713
- ILLUSTRATE LAW: Claude UI at B00/B12/B13 only. B02\u2013B10 illustrate the
  concept via original, native diagrams and statement cards — no screenshots
  or reproductions of any paper's figures (see Copyright note below) \u2713
- Verdict card at B11 restates the episode's four-line conclusion \u2713 \u00b7
  Handoff at B12 (composer, viewer applies the lesson to their own eval) \u2713 \u00b7
  Title-restate outro at B13, marked "Part 1 of 2" \u2713

## Copyright / REBUILD LAW note

No figures, charts, or diagrams from any source paper are reproduced or
screenshotted anywhere in this reel. All visual beats (B03 MMLU comparison,
B06 pipeline mechanics, B07 reframing operations, B10 generator-verifier
pattern) are original diagrams built natively in the toolkit from the
underlying facts and numbers only — chosen deliberately since this reel may
publish to the org's YouTube channel, where reproducing paper figures would
be a real copyright risk regardless of citation.

## Evidence discipline (source: fellow-compiled research synthesis on AI evaluation pipeline evolution, covering Goodhart's Law / benchmark saturation, the "Benchmark Self-Evolving" multi-agent framework, and related literature)

| Claim | Source | Verdict |
|---|---|---|
| Goodhart's Law: a metric optimized against stops measuring what it was designed to measure | Research synthesis, "Why eval pipelines rot in the first place" | OK |
| MMLU: GPT-3 ~43% vs. ~90% human expert baseline; GPT-4 reached 86.4% by 2023; benchmark stopped discriminating within ~3 years | Research synthesis, same section | OK — figures cited as reported in synthesis |
| LLMs "drift" rather than "break" — gradual behavior change over time, distinct from benchmark contamination | Research synthesis, same section | OK |
| Benchmark Self-Evolving: four GPT-4-powered agent roles; Instance Pre-filter restricts to instances the base model already answers correctly | Research synthesis, "Mechanics: how Benchmark Self-Evolving actually works" | OK |
| Six reframing operations guide instance evolution; only two named explicitly in source ("complex question," "adding noise") | Research synthesis, same section | OK — video states only the two named operations verbatim; describes the remaining four generically ("+ four more") rather than inventing names |
| Separate verifier agent checks new instances before entering the suite; most LLMs showed a performance decline against original scores under the evolved version | Research synthesis, same section | OK |
| Limitation: this and similar approaches (e.g. AutoEvoEval) operate through surface-level structural/semantic transformations, testing robustness rather than evolving underlying task complexity | Research synthesis, same section | OK |
| Generator + verifier is described as the common architectural core across multiple automated eval-evolution approaches discussed in the synthesis | Research synthesis, "How this cashes out into a design pattern" | OK |

## Friction protected

- Kept: the real MMLU numbers (43% \u2192 86.4%) as the sole concrete evidence
  beat — strong, specific, and independently verifiable
- Excluded from this video (deferred to Part 2): the Microsoft case study,
  LLM-as-judge drift, cross-family judging, recalibration cadence, and
  metric retirement — kept for a focused, single-thesis first video rather
  than covering all four paradigms in the source research at once
- Did not invent the four unnamed reframing operations — the source names
  only two explicitly ("complex question," "adding noise"); the video states
  this honestly rather than filling in plausible-sounding but unverified names

VERDICT: PASS
