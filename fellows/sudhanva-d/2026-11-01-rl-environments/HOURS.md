# Weekly Hours: Week 2 — Foraging Worlds, Six Learners and HyperLogLog Explainer

**Project:** RL Environments (ant foraging, multi-agent RL)  
**Report & Friction Log:** [FRICTIONAL.md](FRICTIONAL.md)  
**Report Week:** Oct 26 to Nov 1, 2026  
**Total Hours:** 20.0 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Evidence | Hours |
|---|---|---|---:|
| **Foraging Worlds** | Grid world and free (continuous) world with four jobs: find food, bring it home, cut big food into pieces, carry pieces together; on the grid two holders must pull the same way, in the free world pulls add as forces | [`600355b`](https://github.com/Nenyax-AI/team-work/commit/600355bde928daeec9e0078cec27a23f911ade9e) | 4.0 |
| **Six MARL Learners and Training CLI** | IQL, IQL-team, VDN, QMIX, IPPO and MAPPO; training presets, held-out evaluation (team food, per-ant share, Gini, pulls), CSV logs, checkpoints and tests | [`600355b`](https://github.com/Nenyax-AI/team-work/commit/600355bde928daeec9e0078cec27a23f911ade9e) | 6.0 |
| **First Training Results** | First single-seed runs: every learner collected crumbs, none carried a piece | [`db2195c`](https://github.com/Nenyax-AI/team-work/commit/db2195c59ef4dca3126a5f2ddfb30ae70393c346) | 1.0 |
| **Debugging Piece Transport** | Fixed four problems (grab/release reward loophole, path ties, exploration breaking a hold, PPO timeouts); added role assignment and a scripted next-step cue (later withdrawn) | [`bfe4eb3`](https://github.com/Nenyax-AI/team-work/commit/bfe4eb35889b5cf928147487cb76a673548e8c1b) | 1.0 |
| **Checking the 12/12 Result** | Re-ran the saved models (3 seeds, 20 held-out episodes) against a no-learning cue follower and with the cue blanked: the cue did the cooperating | [Check table](FRICTIONAL.md) | 2.0 |
| **Project Update Video** | "Did the Ants Learn to Cooperate?", 16:9 and 9:16 | [16:9](https://drive.google.com/file/d/1_BwCwNFtzX5jRuZSyHROQPy2qHG3VDA-/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1Mf0X9HVxuMVSgomlgt2qJYwSV1YUOyke/view?usp=sharing) · [Beat sheets](ant-head-rl-research/) | 2.0 |
| **STEM Explainer Video** | "How HyperLogLog Counts", built on a real HyperLogLog (1,000,000 visitors in 768 bytes) | [16:9](https://drive.google.com/file/d/1IrxJ0-tlCrfOpzgItNBg5AqLwJSw5tjU/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1dXlN1YILCDm2PSX1D9XoXueLtfp_fZRk/view?usp=sharing) · [Beat sheets](hyperloglog/) | 2.0 |
| **Research, Engineering & Video Subtotal** | | | **18.0** |
| **Documentation** | Project README and RESULTS.md; weekly report and Frictional log | [`600355b`](https://github.com/Nenyax-AI/team-work/commit/600355bde928daeec9e0078cec27a23f911ade9e) · [`db2195c`](https://github.com/Nenyax-AI/team-work/commit/db2195c59ef4dca3126a5f2ddfb30ae70393c346) · [FRICTIONAL.md](FRICTIONAL.md) | 1.5 |
| **Meetings** | Weekly meeting | — | 0.5 |
| **Total** | | | **20.0** |
