# Carry the Couch, Week Six — Beat Sheet

**Slug:** `claude-liam-couch-week-six` · **Voice:** Kokoro `am_onyx`

Generated from [`beat_sheet.json`](beat_sheet.json), which is the source of truth: edit the JSON, not this table. Start times add up each beat's rendered duration.

## 12 beats, 1:54 (114.7s)

| # | Act | Start | Dur | Pattern | Motion | Narration |
|---|---|---|---|---|---|---|
| B00 | COLD_OPEN | 0:00 | 6.6s | ClaudeComposerAsk | type-on | Hello! This is Liam, in for Kriti, sharing the week six update on the Carry the Couch project. |
| B01 | OVERVIEW_(BLUF) | 0:06 | 5.2s | BrutalistHesitantWriter | hesitant-type | Week six marks the completion of Milestone One. |
| B02 | BODY_RESEARCH_SCOPE | 0:11 | 11.4s | UpdConceptGrid | motion-in | The research: identical agents, trained with multi-agent reinforcement learning in VMAS and PyTorch, learn to carry a couch-shaped load together, across different environments. |
| B03 | BODY_RESEARCH_QUESTION | 0:23 | 9.3s | UpdFlow | motion-in | The question: can a policy trained with two to four agents carry the couch with eight to twelve, in layouts it has never seen, without retraining? |
| B04 | BODY_STEP_1_SIMULATION | 0:32 | 13.6s | UpdChecklist | motion-in | Step one, the simulation: a custom 2D multi-body world in VMAS, with couch inertia, viscous floor friction, and boundary walls. Each agent sees the couch relative to itself, as eight local coordinates. |
| B05 | BODY_STEP_2_DEEP_SETS | 0:46 | 9.5s | TypesetMath | motion-in | Step two, coordination. Teammates are pooled with Deep Sets: the same network, phi, on each one, then a sum, so order and team size don't matter. |
| B06 | BODY_STEP_2_WHISPERS | 0:55 | 8.8s | UpdCompare | motion-in | Identical agents can deadlock, pushing in perfect symmetry. So each one gets a private whisper of Gaussian noise to break the tie. |
| B07 | BODY_STEP_3_VERIFICATION | 1:04 | 9.6s | UpdScorecard | motion-in | Step three, verification: all six unit tests pass. Test six shows that uneven pushing moves the couch forward and turns it, at the same time. |
| B08 | BODY_STEP_4_DIAGNOSTICS | 1:14 | 15.2s | UpdHub | motion-in | Step four, diagnostics: an action tracker sorts behavior into six categories: translation, arc steering, opposed couple, anchoring or pivoting, repositioning, and back off. Bout counts and average bout length show how long agents hold a role. |
| B09 | VERDICT | 1:29 | 8.2s | PiVerdict | motion-in | Milestone One: the world, the coordination, the tests, and the diagnostics are in place. Next comes training. |
| B10 | YOUR_TURN_HANDOFF | 1:37 | 12.8s | ClaudeComposerAsk | type-on | Your turn: 'My identical agents sometimes freeze in symmetric standoffs. What are the ways to break that symmetry, and what does each one cost?' Breaking symmetry is a design choice, not just a bug fix. |
| B11 | OUTRO | 1:50 | 4.3s | ClaudeTitleOutro | outro-card | Carry the Couch, Week Six. At Nik Bear Brown. |
