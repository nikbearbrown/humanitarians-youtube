# Renewal request: Laksh D.

- **Request date:** 25 Nov 2026
- **Role:** Software Engineer
- **Group:** RL Environment
- **Project:** Predictive Autoscaling with Reinforcement Learning
- **Project Manager:** Dhruv P.
- **Current agreement:** 28 Oct 2026 to 30 Nov 2026
- **Requested renewal:** 1 Dec 2026 to 28 Feb 2027
- **Reporting period:** 28 Oct 2026 to 22 Nov 2026 (23 to 30 Nov is in progress and will be added to [HOURS.md](../HOURS.md) at the end of the week)

## Executive summary

I am building a simulated backend service with a server boot delay, driven by real cloud traffic, to test whether a reinforcement learning (RL) policy can add servers before traffic spikes and miss fewer latency targets than the Kubernetes autoscaler (HPA) at equal or lower cost. In this period I built the environment and baselines on real Azure traffic, trained PPO agents on Modal, and moved to multi-week Huawei Cloud traces. The current result: a PPO agent that sets HPA's target beats HPA at equal cost in every run on 3 of 4 test sets, with up to 57% fewer late requests. The project, code, videos and reports are my own work, built with Claude Code's help as recorded in each Frictional log. I documented 78.0 hours through 22 Nov; the first, partial week is below 20 hours (see below).

## Completed results

| Result | My contribution | Evidence |
|---|---|---|
| Autoscaling environment on real Azure Functions traffic, with threshold, fixed-capacity and forecast baselines. A "same time yesterday" forecast cut late requests from 5.47% (Kubernetes rule) to 1.17% on 5 held-out apps. | Designed and wrote the Gymnasium environment, traffic analysis, fitted traffic generator, baselines and 13 tests. | [Commit 8b126bd](https://github.com/lakshdhamija/rl-autoscaler/commit/8b126bd) · [Week 1 report](../2026-11-08-week1-project-update/README.md) |
| Plain and residual PPO agents trained on Modal (60 runs). No agent beat "same time yesterday" at equal cost; the best tied it. The traffic has a weekly shape, which set the next step: multi-week data. | Wrote the training code and 4 tests, ran both batches, analysed cost against late requests. | [Commit 35e922d](https://github.com/lakshdhamija/rl-autoscaler/commit/35e922d) · [Week 2 report](../2026-11-15-can-ppo-beat-yesterday/README.md) |
| Multi-week Huawei Cloud traces, HPA as the baseline, and a PPO agent that sets HPA's target. At equal cost it beats HPA in every run on 3 of 4 test sets (up to 57% fewer late requests) and in 8 of 15 on the bursty Azure held-out apps. Trained for misleading history, it still wins 76% of 360 cases. | Prepared the traces, built the 7-day-history environment, the HPA-target agent and the misleading-history test, ran 60 Modal runs, analysed results per app. | [Commit a886c1b](https://github.com/lakshdhamija/rl-autoscaler/commit/a886c1b) · [Week 3 report](../2026-11-22-when-to-keep-spare-servers/README.md) |

## Weekly evidence index

Each week has one progress video and one STEM topic video, in 16:9 and 9:16. Every video link opens for anyone with the link.

| Week | Hours | Videos | Log and work evidence |
|---|---|---|---|
| 28 Oct to 1 Nov | 13.5 (below 20; see Hours status) | None (onboarding week, before the project was chosen) | [Hours breakdown](../HOURS.md#28-oct--1-nov-onboarding) |
| 2 to 8 Nov | 24.5 | Progress: Why Autoscalers Need Yesterday's Traffic ([16:9](https://drive.google.com/file/d/18PRe64Td3teAoGeuLVXYzq6qUVBk5kYf/view), [9:16](https://drive.google.com/file/d/1OwD4uLNosMEb2gWjDCfom9SPkF_5rQBr/view)) · STEM: What Real Cloud Traffic Looks Like ([16:9](https://drive.google.com/file/d/1HalRkUyoA4seGmRLVJlRTFSEElEl3gtm/view), [9:16](https://drive.google.com/file/d/1JpfecEUjuMVQDpT9Y7D-cGNhEbQQWIep/view)) | Frictional: [progress](../2026-11-08-week1-project-update/FRICTIONAL.md), [explainer](../2026-11-08-what-real-cloud-traffic-looks-like/FRICTIONAL.md) · [commit 8b126bd](https://github.com/lakshdhamija/rl-autoscaler/commit/8b126bd) |
| 9 to 15 Nov | 20.0 | Progress: Can PPO Beat Yesterday? ([16:9](https://drive.google.com/file/d/1k6oE6ntjquTt4qxyr8x_3E3qp5g9F80l/view), [9:16](https://drive.google.com/file/d/14UkPbvmyEN9wF47zUuyz84TKae3iLDta/view)) · STEM: What PPO Is, In Plain Words ([16:9](https://drive.google.com/file/d/1rKEriNa5ZAZvtrKyMWwFxPWc-gx5Y_85/view), [9:16](https://drive.google.com/file/d/1X4rZsIutd4YsGuadmohhzFcgp5UfUXWT/view)) | Frictional: [progress](../2026-11-15-can-ppo-beat-yesterday/FRICTIONAL.md), [explainer](../2026-11-15-what-is-ppo/FRICTIONAL.md) · [commit 35e922d](https://github.com/lakshdhamija/rl-autoscaler/commit/35e922d) |
| 16 to 22 Nov | 20.0 | Progress: When to Keep Spare Servers ([16:9](https://drive.google.com/file/d/1IHm2ARrY_TSykFNp8EEzNcjtB90_bz8D/view), [9:16](https://drive.google.com/file/d/1hxhiaQS1up6oThQuOE5cZ_btOgHKPLKF/view)) · STEM: When History Misleads ([16:9](https://drive.google.com/file/d/1hgBikpO5NdV1lO7e2PL9UCD8r0su7FBj/view), [9:16](https://drive.google.com/file/d/17XSAqHh67kl-I4W6fDteaeEkCYbgAIXr/view)) | Frictional: [progress](../2026-11-22-when-to-keep-spare-servers/FRICTIONAL.md), [explainer](../2026-11-22-when-history-misleads/FRICTIONAL.md) · [commit a886c1b](https://github.com/lakshdhamija/rl-autoscaler/commit/a886c1b) |

## Hours status

78.0 hours documented through 22 Nov, with a per-activity breakdown for each week in [HOURS.md](../HOURS.md). The three full weeks each reach 20 or more hours. The first week, 28 Oct to 1 Nov, covers only five days from the agreement start and has 13.5 hours of onboarding and project research. As HOURS.md states, the weekly tables were written after each week from dated work records (commits, documents, messages), not logged live.

## Degree relevance and supervision

- **Degree relevance:** the work is software engineering for cloud systems: a simulator, training and evaluation code with tests, and benchmarks against the production Kubernetes autoscaler. It applies my Master of Science in Computer Software Engineering.
- **Supervision:** I report weekly to my Project Manager, Dhruv P., in the weekly RL group meeting and through the weekly reports in this folder.

## Authorization

Post-completion OPT. Authorization documents go privately to HR, not in this folder.

## Plan for 1 Dec 2026 to 28 Feb 2027

| Target date | Deliverable |
|---|---|
| 13 Dec 2026 | More varied traffic beyond serverless (web server logs, LLM serving requests), training balanced across datasets, a validation group for choosing the late penalty, and a bigger held-out set with one whole dataset left out of training. |
| 3 Jan 2027 | Servers with different capacities and boot delays; server capacity and request cost from measured Huawei instance and CPU metrics, so HPA scales on CPU as in production. |
| 24 Jan 2027 | Which history inputs help: none, yesterday and last week, a longer window, or a model with memory. |
| 14 Feb 2027 | Final tests, written report and `SKILL.md`. |
| 28 Feb 2027 | If RL keeps beating HPA: the same method on one LLM serving decision (KV-cache eviction or quantization choice). |

From 1 Dec, each weekly presentation deck goes in its own dated folder as `slides.html`.

## Outstanding issues

- The first week (28 Oct to 1 Nov) is below 20 hours, as noted above.
- The videos are in the project's shared Drive folder. None is on the Humanitarians AI channel yet.
