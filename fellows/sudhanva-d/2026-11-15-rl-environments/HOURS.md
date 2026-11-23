# Weekly Hours: Week 4 — Six Learners Compared, Paired Carries and Value Decomposition Explainer

**Project:** RL Environments (ant foraging, multi-agent RL)  
**Report & Friction Log:** [FRICTIONAL.md](FRICTIONAL.md)  
**Report Week:** Nov 9 to Nov 15, 2026  
**Total Hours:** 23.0 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Evidence | Hours |
|---|---|---|---:|
| **Learner and Evaluation Changes** | Value-based learners treat a timeout as terminal; new `pieces_paired` and carry-length metrics; opt-in MAPPO credit options (`credit=team`, `critic_per_ant`); `scripts/evaluate.py` and `scripts/coordination.py` | [`3c4e2f3`](https://github.com/Nenyax-AI/team-work/commit/3c4e2f311ab335e1894b7c0bf7be3069ba704eaf) | 2.0 |
| **Training Runs** | All six learners at 1M steps in both worlds (IPPO and MAPPO with 5 seeds), free-world IPPO and MAPPO to 3M steps, both credit options with 3 seeds | [`3c4e2f3`](https://github.com/Nenyax-AI/team-work/commit/3c4e2f311ab335e1894b7c0bf7be3069ba704eaf) | 12.0 |
| **Coordination Analysis** | What the two holders of a piece do at each step: 93–94% agreement for IPPO and MAPPO on the grid; most stalled pulls are a lone holder waiting | [Results](FRICTIONAL.md) | 2.0 |
| **Verification** | Re-scored all 62 saved models; every score matched its log | [Results](FRICTIONAL.md) | 1.0 |
| **Project Update Video** | "Which Ants Carry Together?", 16:9 and 9:16 | [16:9](https://drive.google.com/file/d/1J9dj7HdDP6suvWiFXkZs_uL8dK1Nd6GV/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1vC2mkYfr6dm9lsm8iUy52Ev045bQgo9k/view?usp=sharing) · [Beat sheets](ant-head-rl-research/) | 2.0 |
| **STEM Explainer Video** | "One Value, Four Ants" (VDN and QMIX); checked the each-ant's-best-is-the-team's-best property on all 1,296 joint moves over nearly 30,000 states | [16:9](https://drive.google.com/file/d/1g1ZRvAbBfr3G_dTaR5guYI8z3eTj6qCt/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1curbwG4Zqr1iNL5UhczN2F2p6XzZzjqX/view?usp=sharing) · [Beat sheets](value-decomposition/) | 2.0 |
| **Research, Engineering & Video Subtotal** | | | **21.0** |
| **Documentation** | README and RESULTS.md for the six-learner comparison; weekly report and Frictional log | [`3c4e2f3`](https://github.com/Nenyax-AI/team-work/commit/3c4e2f311ab335e1894b7c0bf7be3069ba704eaf) · [FRICTIONAL.md](FRICTIONAL.md) | 1.0 |
| **Meetings** | Weekly meeting | — | 1.0 |
| **Total** | | | **23.0** |
