# Weekly Learning Report / /hai
**Week of September 15–19, 2026**

---

## VOLUNTEER & PROJECT
- **Name:** Amos Jaimes
- **Project:** RamanSPy reproducibility and variance characterization
- **Hours this week:** 23.5 / 20 required
- **Tool compliance:** Gru (satisfied via Claude Code plan-mode SDD), CRITIQ (N/A), Zelda (N/A), Walker (N/A)

---

## ACTIVITIES & HOURS BREAKDOWN

| Day | Activity | Hours | Notes |
|---|---|---|---|
| Mon 14 | Reading: RESEARCH_REFERENCE.md, README, RamanSPy paper, repo structure mapping | 4.0 | Mapped 5 architectures, 2-phase training, 18 historical logs |
| Tue 15 | Environment verification; scoping deliverable; reviewing historical logs | 4.0 | Verified torch 2.11.0+cu128 CUDA available (contradicted reference doc CPU-only claim); ramanspy 0.2.10 version retrieval method |
| Wed 16 | Team intro meeting (0.7h) + teammate codebase walkthrough (0.5h) | 1.2 | Status sync; publishing strategy discussion with PM (unresolved: two-model comparison vs best-performing model) |
| Wed 16 | Stage 0 design review; backups; installing 9 files | 2.8 | — |
| Thu 17 | Debugging `ds_kwargs` NameError; acceptance tests | 1.5 | Diagnosed from traceback; moved assignment above reference dataset load |
| Thu 17 | Noise-floor runs (3 × LegacyCNN 100/20 epochs), attended GPU runtime | 1.5 | Reading streaming output, checking for divergence |
| Thu 17 | Variance attribution script + interpretation | 1.0 | — |
| Thu 17 | Ablation patch; 6-run ASPLS comparison (attended, ~2h GPU) | 2.0 | — |
| Thu 17 | Extended ablation, 5 arms × 3 seeds (attended, ~4h GPU) | 3.0 | — |
| Fri 18 | Architecture grid launch + monitoring (overnight to 23:36 Thu, reviewed Fri) | 1.5 | 12 runs (4 models × 3 seeds) |
| Fri 18 | Results analysis; `DEFAULT_PIPELINE` change; tool-output debugging | 2.0 | — |
| Fri 18 | Phase 2 patch application + verification runs | 3.0 | 2 short runs; 4.3-point regression vs baseline (unresolved) |
| **TOTAL** | | **23.5** | 8h attended GPU runtime (not idle waiting) |

---

## TIER JUSTIFICATION

### Activity A: Stage 0 Reproducibility Infrastructure (Tier 1 + Tier 4)

**Tier 1 (AI Fluency):** Claude drafted five new modules (`repro.py`, `runmeta.py`, `cache.py`, `metrics.py`) and integration patches. Applied them directly.

**Tier 4 (Judgment and Supervision):** Two catches:
1. `ds_kwargs` block placement: Claude generated the code block *after* its first use in the dataset load, causing `NameError` at line 106. Diagnosed from the traceback and moved the assignment above the reference dataset load.
2. Unseen-label guard structural failure: Claude's acceptance test 4 asserted the guard would raise `ValueError` on clinical files. It didn't, because both label sets use integers 0–29 and a value-level check cannot detect a semantic collision (clinical files carry antibiotic-level labels; reference/finetune/test carry isolate-level labels). Supplied the correct model (label spaces, not label values) afterward.

The first is debugging competence. The second is catching a validated-looking safeguard that validates nothing—evidence of Tier 4 reasoning.

### Activity B: Preprocessing Ablation (Tier 4 + Tier 5)

Claude predicted 2–5 accuracy points from removing ASPLS, derived from a validation-to-test pass-through ratio measured on seed variance. Actual result: +7.61 points (pooled McNemar p = 2.5e-57).

**Tier 5 (Causal Reasoning):** The prediction was wrong in number and reasoning pattern. Identified that the reasoning pattern was invalid: a variance-derived ratio measured on fixed test-set accuracy does not transfer to a change in input representation. The gap between "number wrong" and "reasoning pattern doesn't apply" is the learning. This is evidence of understanding why, not just what happened.

### Activity C: Architecture Grid Re-evaluation (Tier 4)

Claude argued twice that the repo's "smaller models win" finding was an ASPLS artefact. Ran 12 runs at the corrected pipeline (4 models × 3 seeds). LegacyCNN still won (83.89 ± 0.33 vs ResNet 79.56 ± 1.78). The hypothesis was wrong. On evidence, rejected a confidently-argued position. The original finding is now better supported.

### Activity D: Reading Tool Output Critically (Tier 4)

`check_variance_source.py` reported "stdev 6.60, noise band 19.83 points" across 15 runs pooled over 5 architectures. Per-class stability table showed "per-seed" values that were actually 5 models × 3 seeds in run order. Both outputs were meaningless. Surfaced by reading them against known per-model numbers. Evidence of critical evaluation of AI-generated analysis, not blind acceptance.

---

## STRUGGLE SECTION

**Unresolved, live issues:**

1. **Phase 2 verification regression (4.3 points worse):** Same seed, bit-identical pre-trained checkpoint, but 66.90% vs 71.20%. Two candidate explanations: validation split removes 10% of small training set (2700 vs 3000), and augmentation slows early convergence so 3 epochs measures cost with no payback. Both plausible, neither confirmed. Do not yet know whether phase 2 instrumentation helps or hurts.

2. **Transformer1D seed bimodality:** Stdev 5.65 across three seeds (66.23, 76.10, 75.93) vs LegacyCNN 0.33. Either genuine bimodality from unscaled `torch.randn` initialisation at d_model 64, or early stopping firing at very different epochs. *Deprioritized, not overlooked.* Transformer1D is fourth of five at 72.76% and isn't the deployed model. Diagnosing why one seed lands 10 points low buys a footnote, not a decision. Judgment call: reasonable, but should have surfaced the reasoning instead of "diagnosable in minutes, not done."

3. **Clinical-file label guard patch unapplied:** Clinical files carry antibiotic-level labels while reference/finetune/test carry isolate-level labels. Both use integers starting at 0, so mismatch is invisible to value-based checks. A patch exists; not applied yet. False expectation: ran the guard check expecting `ValueError`, it loaded 10,000 samples cleanly because the collision is semantic, not syntactic.

4. **Variance check float-accumulation sensitivity:** Six rows reported `DIFF` between freshly computed and recorded accuracies. Cause: batch size 256 vs 128 changing float accumulation order and flipping single samples on decision boundaries. Benign, but the earlier "all checks passed" claim was luckier than rigorous.

---

## DECISION DOCUMENTATION

**Phase 2 12-run grid:** Deprioritized by volunteer, not blocked on hours. Kept adding verification steps before launch; 4.3-point regression in check run created a speculation spiral (wanting to explain it first). Retrospectively correct to deprioritize: the grid itself explains better than pre-run speculation.

**Publishing decision (two-model comparison vs best-performing model):** Volunteer is an engineer, not the project manager. First week on project. Cannot finalize a publishing decision without PM approval at this stage. Position: proceed with compare-two-models until new data acquired for retraining, then publish best-performing model. Final decision deferred to PM authority.

**Transformer1D diagnosis (seed bimodality):** Deprioritized by judgment, not oversight. Fourth-place model, diagnosing a seed outlier buys a footnote not a decision. Reasoning surfaced here, should have been surfaced when deprioritization occurred.

---

## EXPLORATION TIME
None this week. All 23.5 hours tied to pipeline deliverables. Closest to capability-building: paired McNemar testing (why it beats t-test on three accuracy numbers with fixed test set), but in service of ablation, not separate.

---

## COMPLIANCE STATUS

| Item | Status | Notes |
|---|---|---|
| Weekly hours | ✓ PASS | 23.5 / 20 required |
| Tool usage (Gru) | ✓ PASS | Claude Code plan-mode SDD (4 MD files), linked from project site. Provenance: tool-authored, volunteer-reviewed/applied. |
| Tier justifications | ✓ PASS | Four activities, Tier 1/4/5 evidence documented |
| Struggle documentation | ✓ PASS | Four unresolved items with honest reasoning |
| Claude artifact | ✓ PASS | Stage 0, Ablation, Phase 2 patch documentation (linked) |
| Substack article | ✓ PASS | Published in website on the topic Why Variance-Derived Ratios Don't Transfer to Representation Changes |
| Hours credibility | ✓ PASS | Breakdown by activity, GPU runtime separated and counted |

---

## SESSION METADATA
- **Session duration:** ~45 min interactive (intake, probes, tier justification argument building)
- **Report compiled:** /hai default mode

---


