# Weekly Hours — 2026-09-28 to 2026-10-04

| Activity | Illustrative hours | Record / artifact |
|---|---|---|
| Establish Phase 0 isolated environment and permanent logging sandbox under `pi_test/iacon_pi/` | 4 | [Phase 0 Sandbox](../2026-10-04-week2-project-update/report.md#1-executive-summary--engineering-scope) · [Module Manifest](../2026-10-04-week2-project-update/report.md#3-codebase-architecture--file-manifest) |
| Formalize 6-paradigm cognitive memory taxonomy and comparative dimensions against Pi baseline | 4 | [Comparative Architecture](../2026-10-04-week2-project-update/report.md#41-pi-baseline-vs-proposed-memory-architectures) · [Master Document](../2026-10-04-week2-project-update/Episodic%20and%20Causal%20Memory%20Architectures.docx) |
| Scope 3 Episodic Memory designs: Contrastive Pairs ($\tau^+/\tau^-$), Subtask Milestone DAGs, and Closed-Loop Retrieval | 4 | [Episodic Architecture](../2026-10-04-week2-project-update/report.md#41-pi-baseline-vs-proposed-memory-architectures) · [Episodic Spec](../2026-10-04-week2-project-update/Episodic%20and%20Causal%20Memory%20Architectures.docx) |
| Scope 3 Causal Memory designs: SCM Dependency Graphs, Interventional Pruning ($P(Y \mid do(X))$), and Failure-Repair Graphs | 4 | [Causal Architecture](../2026-10-04-week2-project-update/report.md#41-pi-baseline-vs-proposed-memory-architectures) · [Causal Spec](../2026-10-04-week2-project-update/Episodic%20and%20Causal%20Memory%20Architectures.docx) |
| Weekly progress reports and explainer adaptation | 2 | [Progress report & beat sheet](../2026-10-04-week2-project-update/beat_sheet.json)  |
| Organize links, evidence indexing, and documentation | 2 | [Evidence index](../2026-10-04-week2-project-update/README.md) · [Deliverables](../2026-10-04-week2-project-update/report.md#6-generated-deliverables--output-artifacts) |
| **Total** | **20** | **16 engineering + 4 reporting hours** |

### Task Details & Artifact Linkage

1. **Phase 0 Environment Setup (4 hrs):** Migrated Pi evaluation harness from ephemeral `/tmp/` paths to an isolated, permanent virtual environment under `pi_test/iacon_pi/` with pinned Python dependencies and persistent logging to guarantee run auditability ([report.md §1](../2026-10-04-week2-project-update/report.md#1-executive-summary--engineering-scope), [report.md §3](../2026-10-04-week2-project-update/report.md#3-codebase-architecture--file-manifest)).
2. **Cognitive Taxonomy & Baseline Comparison (4 hrs):** Mapped six cognitive memory systems (Procedural, Semantic, Episodic, Causal, Prospective, Metacognitive) and evaluated Pi's unindexed sliding-window history against proposed structured stores across storage primitives, retrieval mechanics, token costs ($O(N)$ vs. fixed 1,000 budget), and failure recovery ([report.md §4.1](../2026-10-04-week2-project-update/report.md#41-pi-baseline-vs-proposed-memory-architectures)).
3. **Episodic Memory Architectures (4 hrs):** Scoped three distinct episodic architectures derived from *Reflexion* (Shinn et al.) and *MemR³*:
   - *Architecture 1 (Contrastive Episodic Memory):* Structured `ContrastiveEpisode` schema isolating the Causal Pivot Delta ($\Delta_{\text{pivot}}$) between failing ($\tau^-$) and successful ($\tau^+$) trajectories for pre-flight tool interception.
   - *Architecture 2 (Hierarchical Subtask Milestone DAG):* Formalized $\text{MDAG} = (S, E_{\text{dep}})$ over five lifecycle phases ($s_{\text{repro}} \to s_{\text{local}} \to s_{\text{hypo}} \to s_{\text{synth}} \to s_{\text{valid}}$) integrated via `compaction.ts` and phase-matched composite retrieval ($<120$ tokens).
   - *Architecture 3 (Closed-Loop Episodic Retrieval):* Multi-turn query refinement loop ($\text{Retrieve} \to \text{Assess} \to \text{Reason} \to \text{Verify} \to \text{Refine}$).
   *(Documented in detail in [Episodic and Causal Memory Architectures.docx](../2026-10-04-week2-project-update/Episodic%20and%20Causal%20Memory%20Architectures.docx) and synthesized in [report.md §4.1](../2026-10-04-week2-project-update/report.md#41-pi-baseline-vs-proposed-memory-architectures)).*
4. **Causal Memory Architectures (4 hrs):** Scoped three causal architectures rooted in Pearlian causal inference:
   - *Architecture 1 (Causal Dependency Graph Memory):* Structural Causal Model DAG $\mathcal{G} = \langle \mathcal{V}, \mathcal{E} \rangle$ capturing dependencies between environment mutations, tool executions, and test outcomes.
   - *Architecture 2 (Intervention-Based Counterfactual Memory):* Interventional reasoning $P(Y \mid do(X))$ with dynamic edge invalidation upon state divergence.
   - *Architecture 3 (Failure–Repair Graph):* 5-slot causal tuple (condition, action, outcome, mechanism, mitigation) embedded into Pi's `beforeToolCall` hook as an active prevention layer.
   *(Documented in detail in [Episodic and Causal Memory Architectures.docx](../2026-10-04-week2-project-update/Episodic%20and%20Causal%20Memory%20Architectures.docx) and synthesized in [report.md §4.1](../2026-10-04-week2-project-update/report.md#41-pi-baseline-vs-proposed-memory-architectures)).*
5. **Progress & Explainer Adaptation (2 hrs):** Condensed week-2 technical milestones into an 11-beat review cut (`claude-liam-pi-memory-week-two`), excised duplicate beat B08, and aligned narration in [beat_sheet.json](../2026-10-04-week2-project-update/beat_sheet.json) and [SCRIPT.md](../2026-10-04-week2-project-update/SCRIPT.md).
6. **Documentation & Evidence Index (2 hrs):** Structured [README.md](../2026-10-04-week2-project-update/README.md), verified audit trails, and aligned deliverables in [report.md §6](../2026-10-04-week2-project-update/report.md#6-generated-deliverables--output-artifacts).


