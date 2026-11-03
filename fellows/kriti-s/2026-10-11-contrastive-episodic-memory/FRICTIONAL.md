# Frictional Log — contrastive-episodic-memory


## 2026-10-09 — Build Explainer Video on Contrastive Episodic Memory in 16:9 and 9:16 format

Drafted by Optimus(AI) from videos folders and reviewed by me.

- **Work and expectation:** In the scenario, I review and verify the contrastive episodic memory explainer and expect its core thesis that paired contrastive trajectories prevent unconstrained context pollution and embedding similarity traps to be intuitive and verifiable in ~60 seconds.
- **What I try:** Formalize the breakdown of naive episodic storage (cosine similarity misses logical runtime failure), demonstrate prefix alignment to locate the exact decision fork, specify the compact delta schema, and show dual-sided retrieval ("do this" + "avoid that") with background dreaming consolidation.
- **Where it resists:** 
  - *Visual Balance:* Balancing complex Remotion animations (`CwcSplitMechanism`, `CwcDreamingService`) to ensure split trajectories and clustering cycles remain legible on small screens.
  - *Audio Pacing:* Compacting narration lines so that each beat stays within the tight word budget without losing technical precision.
- **What I do next:** Implement the SQLite WAL delta schema for contrastive storage and benchmark Pass@1 improvement on realistic SWE-rebench agent trajectories.
- **AI and other contributions:** Claude Code compiled the beat sheet, constructed custom Remotion scenes (`CwcMemoryTimeline`, `CwcMemorySchema`, `CwcDreamingService`), verified factual grounding against literature sources, and ran the Brutalist video build pipeline. Audio voiced via Kokoro `am_onyx` (Liam in for Kriti). Human fellow selected the research foundations, specified the causal delta tuple, and approved the review cut.
- **What I understand:**  Vector databases and raw log accumulators are passive storage equipment and without contrastive causal alignment, they hoard noise and repeat mistakes with false confidence.
- **Evidence:** [beat_sheet.json](beat_sheet.json)
