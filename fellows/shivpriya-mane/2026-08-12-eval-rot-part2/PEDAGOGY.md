# PEDAGOGY — Why AI Evaluation Benchmarks Stop Working, Part 2 (hai claude explainer)

Explains a real production case study (continuous benchmark generation from
developer intent documents at Microsoft), the LLM-as-judge drift problem
(Goodhart's Law operating one layer down inside the scoring harness), and
the criteria for retiring a benchmark rather than just patching it. Second
of a two-part series; Part 1 covered benchmark saturation (Goodhart's Law,
MMLU) and the Benchmark Self-Evolving multi-agent test-generation system.

## Act structure

- B00 cold open with RESULT lines (ASK\u2192RESULT at B00) \u2713
- B01 executive summary beat, explicitly recapping Part 1's scope \u2713
- ILLUSTRATE LAW: Claude UI at B00/B14/B15 only. B02\u2013B13 illustrate the
  concept via original diagrams, statement cards, and one original
  fellow-made STILL image (B12) \u2014 no reproductions of any source paper's
  figures anywhere \u2713
- Verdict card at B13 restates the episode's human-in-the-loop conclusion
  \u2713 \u00b7 Handoff at B14 (composer, viewer audits their own judge setup) \u2713 \u00b7
  Title-restate outro at B15, marked "Part 2 of 2" \u2713

## Copyright / REBUILD LAW note

No figures, charts, or diagrams from any source paper are reproduced or
screenshotted anywhere in this reel. B12 uses an original diagram the fellow
built herself (Production signals \u2192 Generator \u2192 Verifier \u2192 CI/CD gate \u2192
Human calibration, with a recalibrate loop) \u2014 this is the fellow's own
synthesis visualization, not a reproduction of any published figure. All
other visual beats are native toolkit diagrams built from underlying facts
and numbers only.

## Evidence discipline (source: fellow-compiled research synthesis on AI evaluation pipeline evolution \u2014 same source as Part 1, covering the Microsoft continuous-benchmark-generation case study, LLM-as-judge drift, and benchmark retirement criteria)

| Claim | Source | Verdict |
|---|---|---|
| Microsoft case study: enterprise agent migrating services between deployment platforms; task spans build/compilation scripts, deployment files, and source code | Research synthesis, "Case study: continuous benchmark generation at Microsoft" | OK |
| Fixed benchmarks fall short for enterprise-scale agents where services/requirements evolve continuously and ground-truth examples are sparse | Research synthesis, same section | OK |
| Fix: developer-authored semi-structured Knowledge Bases repurposed to describe eval task specifics; new benchmark cases generated from a small number of these documents | Research synthesis, same section | OK |
| Authors' explicit caveat: generalization beyond service-migration agents (e.g. to troubleshooting agents) is flagged as future work, not a proven result | Research synthesis, same section | OK \u2014 stated as an honest limitation, not overclaimed |
| LLM-as-judge drift: tuning against a biased judge (verbosity bias, self-preference bias) lets gradient pressure discover and exploit those biases \u2014 Goodhart's Law one layer down | Research synthesis, "The failure mode nobody fully solved yet" | OK |
| Same-family judges (e.g. GPT-4 judging GPT-4) systematically over-reward their own family's outputs; fix is a judge from a different model lineage | Research synthesis, "How teams keep the judge itself from drifting" | OK |
| Calibration set of 100\u2013500 human-labeled examples; monthly re-run tracking judge-human agreement; recalibration triggered below a 75% agreement threshold; drift typically occurs within 60\u201390 days without this cadence | Research synthesis, same section | OK |
| Benchmark saturation formally defined as loss of reliable discriminative power \u2014 top models statistically indistinguishable \u2014 not simply a high average score; benchmark age/scale are strong predictors, private test sets show limited protective effect | Research synthesis, "When to retire a metric or benchmark" | OK |
| Named retire-and-replace examples: MMLU\u2192MMLU-Pro, HumanEval\u2192HumanEval+, SWE-bench\u2192SWE-bench Pro | Research synthesis, "Retire-and-replace isn't automatically the right move" | OK |
| Retire-and-replace critiqued as sometimes inadequate: saturation on one dimension doesn't mean nothing is left to measure; alternative is adding orthogonal metrics rather than a harder version of the same test | Research synthesis, same section | OK |
| MT-Bench finding: GPT-4 agrees with human experts at roughly 80%, comparable to human-human inter-rater agreement | Research synthesis, "Building the first gold/calibration set" | OK \u2014 cited for context on what "good enough" judge agreement looks like |

## Friction protected

- Kept: the real named benchmark-pair examples (MMLU\u2192MMLU-Pro, etc.) as
  concrete, checkable evidence rather than a generic claim about
  "retire-and-replace"
- Kept: the authors' own caveat about their case study's limited scope
  (B06) \u2014 stated honestly rather than smoothed over to make the finding
  sound more general than it is
- Excluded: SEAGym / self-evolving-agent-harness evaluation (a fifth
  paradigm in the source research) \u2014 deferred as out of scope for this
  two-part series to keep each video to one focused thesis

VERDICT: PASS
