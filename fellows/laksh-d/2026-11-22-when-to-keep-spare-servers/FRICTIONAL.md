# Frictional Log

## 2026-11-22: Project week 3

- **Work and expectation:** test the autoscaler on traffic several weeks long and give reinforcement learning another try. I expected PPO to struggle again.
- **What I tried:** two multi-week Huawei Cloud traces (34 functions, 26 and 33 days); rules that look at last week, which I then set aside because they are not production autoscalers; and a new agent that picks the Kubernetes HPA rule's target utilization (40% to 90%) every minute. 30 runs on Modal: 5 late penalties, 3 seeds, trained on normal history and with misleading history.
- **Where it resisted:**
  - Three public functions had days far above their normal load, likely load tests, beyond any 50-server cluster. A steadiness check drops them, but it also looked at the unseen days; the next data rebuild fixes that.
  - PPO beats HPA at equal cost in every run on 3 of the 4 test sets, but only in 8 of 15 runs on the 5 Azure held-out apps, which are 2 to 4 times burstier than the training traffic.
  - When yesterday or last week misleads, the agent trained on normal history beats HPA in only 58% of cases. Training it with misleading history raises that to 76%.
- **AI and other contributions:** Claude Code wrote the code, ran the training and made the video under my direction; I chose the data and the baseline and reviewed the results. Narration is an AI voice (Kokoro `af_bella`).
- **What I understand now:** tuning the target of a known rule is a task RL can do well. What it learns depends on what it trained on: bursty new apps and misleading history both need to be in training.
- **Evidence:** [README](README.md#watch-and-review), [FACTCHECK.md](FACTCHECK.md), [rl-autoscaler a886c1b](https://github.com/lakshdhamija/rl-autoscaler/commit/a886c1b)
