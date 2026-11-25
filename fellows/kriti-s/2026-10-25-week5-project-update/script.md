# Week 5: Pi Memory Ablations (E1–E7), Leakage Audits, and Carry the Couch Modules — script (narration as rendered)

Voice: Kokoro `am_onyx` · Persona: Kriti (voiced by Kokoro am_onyx)

Narration copied word for word from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

### B00 · cold open
> Hello, this is Kriti, sharing the weekly update on evaluating memory architectures for Pi.

### B01 · overview (BLUF)
> Week five focused upon the ablations.

### B02 · body — E1 + E2 (established)
> Experiments one and two are results established earlier: the baseline memory under the corrected evaluation harness, at six and a half percent, and better episode quality with a code-diff format guard, at thirty.

### B03 · body — E3 multi-phase
> Experiment three designs multi-phase contrastive memory: applicability filtering across five execution phases: planning, code editing, test execution, recovery, and verification.

### B04 · body — E3 novelty dampening
> It adds novelty dampening, an access-count penalty, so Pi stops over-relying on the templates it retrieves most. Experiment three: thirty-two and a half percent.

### B05 · body — E4 + E5
> Experiment four, phase-aware retrieval with fixed token budgets, scores twenty-nine. Experiment five, selective interception, splitting hard constraints from soft recommendations, scores thirty-three and a half.

### B06 · body — E6 → E7
> Experiment six combines them into CEM-v2: thirty-four and a half. Experiment seven adds upstream fault localization, scoped Best-of-N patches, and contrastive verification: sixty-three percent.

### B07 · body — all results
> Side by side, Pass at 1 on two hundred tasks climbs from six and a half to sixty-three, and McNemar's paired test is in place to check which gaps are real.

### B08 · body — Carry the Couch
> Next, Carry the Couch: the environment setup, a body design module, and a budget module capping memory injection at a thousand tokens. More on that in the next video.

### B09 · verdict
> Week five: seven experiments, and the biggest jump came from E7's changes upstream of memory.

### B10 · your turn handoff
> Your turn: 'I'm comparing two versions of my agent on the same tasks. Show me how to run McNemar's test on the results, and what it does and doesn't tell me.' When two arms run the same tasks, a paired test is the honest comparison.

### B11 · outro
> Pi Memory, Week Five. At Nik Bear Brown.
