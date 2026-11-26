# Weekly Hours: Week 3 — Cue Removal, PPO Timeout Fix and IPPO Explainer

**Project:** RL Environments (ant foraging, multi-agent RL)  
**Report & Friction Log:** [FRICTIONAL.md](FRICTIONAL.md)  
**Report Week:** Nov 2 to Nov 8, 2026  
**Total Hours:** 21.0 hrs

---

## Weekly Hours Breakdown

| Category | Activity / Task Description | Evidence | Hours |
|---|---|---|---:|
| **Removing the Scripted Cue** | Took out role assignment and the next-step cue; each ant sees its 5×5 window, its load and a home vector; reworked shaping so it cannot be farmed (grab bonus once per piece, progress only at a new closest distance) | [`e5295c0`](https://github.com/Nenyax-AI/team-work/commit/e5295c048a34e4195035dd522469eee5cc8574be) | 2.0 |
| **Checking the Cue-Free Result** | Found that the 8/12 result leaned on hand-coded syncing (paired ants disagreed on 0 of 988 steps); with both aids off IPPO fell to 4.33 | [Check](FRICTIONAL.md) | 1.0 |
| **PPO Timeout Fix and Honest Transport** | Fixed PPO bootstrapping through timeouts into the next episode; removed hand-coded holder syncing; added opt-in switches; trained to 1M steps (grid IPPO 11.77, MAPPO 11.48) | [`518d820`](https://github.com/Nenyax-AI/team-work/commit/518d820625477a1860d6f5869db98922fddd0d6c) | 2.0 |
| **Free-World Training** | IPPO and MAPPO at 1M steps in the free world (8.55 and 7.85) | [`800141b`](https://github.com/Nenyax-AI/team-work/commit/800141bdebc87aec3cbdbe0be1238821ef3fc604) | 8.0 |
| **Verification** | Re-ran all 12 saved models; trained against untrained baseline on the same states | [Results](FRICTIONAL.md) | 2.0 |
| **Project Update Video** | "Did They Learn It This Time?", 16:9 and 9:16 | [16:9](https://drive.google.com/file/d/1bYeYnU09Z8kUu756TaAfLYum6PsrVy25/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1EaL7K2FMit_EfwXLpZlWYme6vi4J-RwX/view?usp=sharing) · [Beat sheets](ant-head-rl-research/) | 2.0 |
| **STEM Explainer Video** | "How IPPO Learns", rebuilt on the cue-free code so every number comes from the trained models | [16:9](https://drive.google.com/file/d/1SRMySOFjF8a7hGapptrkMuDtkzn5o9Ue/view?usp=sharing) · [9:16](https://drive.google.com/file/d/1ous7hAZcaaa1Uxp69Tqf897_8IlOqxZu/view?usp=sharing) · [Beat sheets](ippo/) | 2.0 |
| **Research, Engineering & Video Subtotal** | | | **19.0** |
| **Documentation** | README update for the honest IPPO/MAPPO results and new switches; RESULTS.md; weekly report and Frictional log | [`151a140`](https://github.com/Nenyax-AI/team-work/commit/151a140769b8e653bfa4f5bb6942c4c699caa157) · [FRICTIONAL.md](FRICTIONAL.md) | 1.0 |
| **Meetings** | Weekly meeting | — | 1.0 |
| **Total** | | | **21.0** |
