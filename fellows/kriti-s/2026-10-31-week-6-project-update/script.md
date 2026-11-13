# Carry the Couch, Week Six — script (narration as rendered)

Voice: Kokoro `am_onyx`

Narration copied word for word from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

### B00 · COLD_OPEN
> Hello! This is Liam, in for Kriti, sharing the week six update on the Carry the Couch project.

### B01 · OVERVIEW_(BLUF)
> Week six marks the completion of Milestone One.

### B02 · BODY_RESEARCH_SCOPE
> The research: identical agents, trained with multi-agent reinforcement learning in VMAS and PyTorch, learn to carry a couch-shaped load together, across different environments.

### B03 · BODY_RESEARCH_QUESTION
> The question: can a policy trained with two to four agents carry the couch with eight to twelve, in layouts it has never seen, without retraining?

### B04 · BODY_STEP_1_SIMULATION
> Step one, the simulation: a custom 2D multi-body world in VMAS, with couch inertia, viscous floor friction, and boundary walls. Each agent sees the couch relative to itself, as eight local coordinates.

### B05 · BODY_STEP_2_DEEP_SETS
> Step two, coordination. Teammates are pooled with Deep Sets: the same network, phi, on each one, then a sum, so order and team size don't matter.

### B06 · BODY_STEP_2_WHISPERS
> Identical agents can deadlock, pushing in perfect symmetry. So each one gets a private whisper of Gaussian noise to break the tie.

### B07 · BODY_STEP_3_VERIFICATION
> Step three, verification: all six unit tests pass. Test six shows that uneven pushing moves the couch forward and turns it, at the same time.

### B08 · BODY_STEP_4_DIAGNOSTICS
> Step four, diagnostics: an action tracker sorts behavior into six categories: translation, arc steering, opposed couple, anchoring or pivoting, repositioning, and back off. Bout counts and average bout length show how long agents hold a role.

### B09 · VERDICT
> Milestone One: the world, the coordination, the tests, and the diagnostics are in place. Next comes training.

### B10 · YOUR_TURN_HANDOFF
> Your turn: 'My identical agents sometimes freeze in symmetric standoffs. What are the ways to break that symmetry, and what does each one cost?' Breaking symmetry is a design choice, not just a bug fix.

### B11 · OUTRO
> Carry the Couch, Week Six. At Nik Bear Brown.

