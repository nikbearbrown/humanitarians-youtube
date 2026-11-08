# Laksh D.

- **Role:** Software Engineer
- **Project:** Predictive Autoscaling with Reinforcement Learning
- **Group:** RL Environment
- **GitHub:** [@lakshdhamija](https://github.com/lakshdhamija)
- **Repository:** [rl-autoscaler](https://github.com/lakshdhamija/rl-autoscaler)
- **Agreement period:** 28 Oct to 30 Nov 2026
- **Drive:** [project videos folder](https://drive.google.com/drive/folders/1IqLdBcMUEMXJP-JBYhMP7OVyV81zTXX3?usp=drive_link)

## Research question

Can a reinforcement learning (RL) policy scale servers up before traffic spikes arrive, and miss fewer latency targets than threshold autoscaling at equal or lower cost?

Threshold autoscalers, such as the Kubernetes Horizontal Pod Autoscaler, react to load after it arrives. New servers take time to boot, so the extra capacity comes online after a spike has already caused latency misses. This project builds a simulated backend service with a server boot delay, driven by real traffic from the Azure Functions Trace 2019, trains a PPO policy on it, and compares the policy against threshold, fixed-capacity and simple forecast baselines on traffic patterns it was not trained on.

## Project work

| Week | Work | Result | Evidence | Log |
|---|---|---|---|---|
| 2–8 Nov | Environment, real Azure traffic, baselines | "Same time yesterday" cut late requests from 5.47% (Kubernetes rule) to 1.17% on 5 held-out apps | [Week 1 update](2026-11-08-week1-project-update/README.md) · [code](https://github.com/lakshdhamija/rl-autoscaler/commit/8b126bd) | [Frictional](2026-11-08-week1-project-update/FRICTIONAL.md) |

## Topic explainers

Narration voice: Kokoro `af_bella`, kept for the whole series.

| Week | Topic | Evidence | Log |
|---|---|---|---|
| 2–8 Nov | What real cloud traffic looks like | [Explainer](2026-11-08-what-real-cloud-traffic-looks-like/README.md) | [Frictional](2026-11-08-what-real-cloud-traffic-looks-like/FRICTIONAL.md) |

## Next steps

- Week of 2 Nov: environment, baselines, real traffic, fitted synthetic traffic, tests (done).
- Week of 9 Nov: PPO with Stable-Baselines3, trained on fitted synthetic and real training days. Its bar: beat "same time yesterday" at equal cost.
- Week of 16 Nov: reward tuning; cost against late requests across reward weights; boot delays of 1, 3 and 5 minutes.
- Week of 23 Nov: final tests on unseen days and held-out apps, report and `SKILL.md`.

## Hours

- [Weekly hours](HOURS.md)
