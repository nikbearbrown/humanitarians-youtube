# Weekly hours: Laksh D.

Reconstructed after each week from dated work records (commits, documents, messages), not logged live.

| Week | Project work | Eng. hrs | Topic explainer | Reporting hrs | Total |
|---|---|---|---|---|---|
| 28 Oct – 1 Nov | Onboarding and project research | 12.0 | | 1.5 | 13.5 |
| 2–8 Nov | [Project week 1: environment, real traffic, baselines](2026-11-08-week1-project-update/README.md) | 21.5 | [What real cloud traffic looks like](2026-11-08-what-real-cloud-traffic-looks-like/README.md) | 3.0 | 24.5 |
| 9–15 Nov | [Project week 2: PPO agents, weekly pattern](2026-11-15-week2-project-update/README.md) | 16.5 | [What PPO is, in plain words](2026-11-15-what-is-ppo/README.md) | 3.5 | 20.0 |
| **To date** | | **50.0** | | **8.0** | **58.0** |

**Eng. hrs** is engineering, research and onboarding for the predictive autoscaling project. **Reporting hrs** is the weekly progress video, explainer production and documentation.

Evidence for each week's work (reports, videos, Frictional logs) is in [README.md](README.md).

## Weekly breakdown

### 28 Oct – 1 Nov (onboarding)

| Activity | Hours | Record / artifact |
|---|---|---|
| Onboarding: agreement and HR paperwork | 3.5 | |
| Coordination with the project managers on project direction | 0.5 | |
| Independent research: RL environments, Gymnasium, autoscaling approaches, candidate project ideas | 8.0 | |
| Learning the video pipeline (HR walkthrough, Brutalist workflow docs) | 1.5 | |
| **Total** | **13.5** | |

### 2–8 Nov (project week 1)

| Activity | Hours | Record / artifact |
|---|---|---|
| Onboarding: PM sync, team-work repo rules, Drive and Discord setup, HR paperwork | 5.0 | team-work project folder |
| Research and proposal: existing RL environments, AIOpsLab, other fellows' projects; proposal approved | 5.5 | team-work project README |
| Simulator: Gymnasium environment, baselines, 13 tests | 4.0 | [rl-autoscaler commit 8b126bd](https://github.com/lakshdhamija/rl-autoscaler/commit/8b126bd) |
| Real Azure traffic: analysis, fitted traffic generator, "same time yesterday" baseline | 4.5 | [rl-autoscaler README](https://github.com/lakshdhamija/rl-autoscaler#results-so-far) |
| Weekly RL meeting and demo | 2.5 | |
| Brutalist toolkit setup | 1.5 | |
| Progress video and topic explainer | 1.5 | week folders |
| **Total** | **24.5** | |

### 9–15 Nov (project week 2)

| Activity | Hours | Record / artifact |
|---|---|---|
| PPO training code: plain and residual PPO, 4 new tests | 4.5 | [rl-autoscaler commit 35e922d](https://github.com/lakshdhamija/rl-autoscaler/commit/35e922d) |
| Modal setup and two training batches (60 runs), cost against late requests chart | 3.5 | [rl-autoscaler README](https://github.com/lakshdhamija/rl-autoscaler#ppo-week-of-9-nov) |
| Results analysis, weekly pattern check, research on multi-week traces | 3.5 | rl-autoscaler README Plan |
| Learning PPO; reviewing the results (reward, late penalty, wait times of late requests) | 2.5 | [What PPO is](2026-11-15-what-is-ppo/README.md) |
| Weekly RL meeting, demo prep, PM communication | 2.5 | |
| Progress video and topic explainer | 3.5 | week folders |
| **Total** | **20.0** | |
