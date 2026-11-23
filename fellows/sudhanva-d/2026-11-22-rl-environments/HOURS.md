# Weekly Hours: Week 5 — QMIX Diagnosis, Sampled Scores and Target Networks Explainer

**Project:** RL Environments (ant foraging, multi-agent RL)  
**Report & Friction Log:** [FRICTIONAL.md](FRICTIONAL.md)  
**Work Record:** [WORK_PROGRESS.md](https://github.com/Nenyax-AI/team-work/blob/ant-head-research/projects/learning-environments/ant-foraging/WORK_PROGRESS.md)  
**Report Week:** Nov 16 to Nov 22, 2026  
**Total Hours:** 25.5 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Evidence | Hours |
|---|---|---|---:|
| **Long Training and Credit Seeds** | Free-world IPPO and MAPPO to 10M steps (3 seeds each); seeds 3–4 for both MAPPO credit variants in both worlds | [`8d85f5f`](https://github.com/Nenyax-AI/team-work/commit/8d85f5f50061f6b7fe388de7688a3772da38dce6) | 12.0 |
| **Agreement During Training and Sampled Evaluation** | `--coord` records holder behaviour at every evaluation; sampled evaluation with the random state restored; 12 IPPO/MAPPO reruns that reproduce last week's runs exactly | [`8d85f5f`](https://github.com/Nenyax-AI/team-work/commit/8d85f5f50061f6b7fe388de7688a3772da38dce6) | 2.0 |
| **QMIX Diagnosis and Value-Based Retuning** | Logged TD prediction and target, gradient norm and mixer weights, and reran QMIX in both worlds: the 500-update target sync made the team value overshoot. Screened five settings (18 runs) and confirmed the best on seeds 0–2 in both worlds (24 runs): grid QMIX 0.08 → 8.44, VDN 5.51 → 8.23 | [`8d85f5f`](https://github.com/Nenyax-AI/team-work/commit/8d85f5f50061f6b7fe388de7688a3772da38dce6) | 4.0 |
| **Sampled Scores as the Headline** | Re-scored final models with each ant sampling as in training; `scripts/compare.py --sample` with a test; 39 tests pass | [`c9369a8`](https://github.com/Nenyax-AI/team-work/commit/c9369a8c450baecbd8efb3d657ac5395402f2a92) | 1.0 |
| **Project Update Video** | "Why QMIX Collapsed, and Why Sample over Greedy?", 16:9 and 9:16 | [16:9](https://drive.google.com/file/d/1WKsM7oCrWpoegIH3LdKKdMeDZOLAUqDJ/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1dBu1S78Uozv7ub8eK0RsoymXgjoWtI20/view?usp=sharing) · [Beat sheets](ant-head-rl-research/) | 2.0 |
| **STEM Explainer Video** | "Chasing Its Own Guess." (target networks), built on the QMIX prediction and target logs | [16:9](https://drive.google.com/file/d/1tswge_MZtiulv8O_554tqwXmMlLE5OH8/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1ePoxFQde7ZXdspUD4OLm4s9Xm_Sp7WXE/view?usp=sharing) · [Beat sheets](target-networks/) | 2.0 |
| **Research, Engineering & Video Subtotal** | | | **23.0** |
| **Documentation** | Moved the project into `Nenyax-AI/team-work` with its full history and committed the evaluation files; README project brief, problem statement and end goal; WORK_PROGRESS.md with the commit ID map; RESULTS.md rewritten around sampled scores; weekly report and Frictional log | [`384d0c9`](https://github.com/Nenyax-AI/team-work/commit/384d0c9a6e53ba57c6d9362a00f84dbc19ece6de) · [`f46147a`](https://github.com/Nenyax-AI/team-work/commit/f46147a76ac552c08b002d05c5b2187dc399874f) · [`c9369a8`](https://github.com/Nenyax-AI/team-work/commit/c9369a8c450baecbd8efb3d657ac5395402f2a92) · [FRICTIONAL.md](FRICTIONAL.md) | 2.0 |
| **Meetings** | Weekly meeting | — | 0.5 |
| **Total** | | | **25.5** |
