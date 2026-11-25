# Week 2: Pinned Baseline, Persistent Logging, and Scoping Six Memory Designs (Pi Memory) — script (narration as rendered)

Voice: Kokoro `am_onyx` · Persona: Kriti (voiced by Kokoro am_onyx)

Narration copied word for word from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

### B00 · cold open
> Hello, this is Kriti, sharing the weekly update on evaluating memory architectures for Pi.

### B01 · overview (BLUF)
> Week two built a solid baseline: Pi pinned, every run logged, and six memory designs scoped for testing.

### B02 · body — pinned baseline
> First, the baseline. I pinned Pi to one specific version from its GitHub repository, so every run uses exactly the same harness.

### B03 · body — Optimus code
> Then I read through the model config and arm0_runner files that Optimus generated, to understand how a run is wired together.

### B04 · body — runner change
> The runner used to write to temporary folders. I changed it to save to permanent directories, so every log is kept and every run can be audited.

### B05 · body — check-in
> I met with the team and the lead to review progress and agree on next steps.

### B06 · body — episodic scoped
> Then I scoped three episodic designs: contrastive memory that keeps failures next to successes, a milestone graph that recalls only the current phase, and closed-loop retrieval that drops memories that don't help.

### B07 · body — causal scoped
> And three causal designs: a dependency graph that traces an error to its root cause, intervention memory that suggests a better action instead of just blocking one, and a failure-repair graph that turns a failed run into a repair plan.

### B09 · verdict
> Week two: pinned, logged, and scoped.

### B10 · your turn handoff
> Your turn: 'Review my agent experiment runner. What should every run log so the results can be audited and reproduced later?' A result you can't trace is a result you can't trust, so that's the question worth asking early.

### B11 · outro
> Pi Memory, Week Two. At Nik Bear Brown.
