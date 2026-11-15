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
| 9–15 Nov | PPO agents, plain and residual, 30 runs on Modal | No agent beats "same time yesterday" at equal cost; the best ties it. The data has a weekly shape, so next comes multi-week data | [Week 2 update](2026-11-15-week2-project-update/README.md) · [code](https://github.com/lakshdhamija/rl-autoscaler/commit/35e922d) | [Frictional](2026-11-15-week2-project-update/FRICTIONAL.md) |

## Topic explainers

Narration voice: Kokoro `af_bella`, kept for the whole series.

| Week | Topic | Evidence | Log |
|---|---|---|---|
| 2–8 Nov | What real cloud traffic looks like | [Explainer](2026-11-08-what-real-cloud-traffic-looks-like/README.md) | [Frictional](2026-11-08-what-real-cloud-traffic-looks-like/FRICTIONAL.md) |
| 9–15 Nov | What PPO is, in plain words | [Explainer](2026-11-15-what-is-ppo/README.md) | [Frictional](2026-11-15-what-is-ppo/FRICTIONAL.md) |

## Next steps

- Week of 2 Nov: environment, baselines, real traffic, fitted synthetic traffic, tests (done).
- Week of 9 Nov: PPO with Stable-Baselines3 on Modal, plain and residual (done).
- Week of 16 Nov: real traces several weeks long with weekday and weekend patterns; a "same time last week" baseline; test the baselines on them first.
- Week of 23 Nov: PPO on the new traces, with a validation split for choosing settings; final tests, report and `SKILL.md`.

## Hours

- [Weekly hours](HOURS.md)
