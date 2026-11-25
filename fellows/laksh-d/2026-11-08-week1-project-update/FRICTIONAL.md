# Frictional Log

## 2026-11-08: Project week 1

- **Work and expectation:** build a simulated server cluster as a Gymnasium environment, drive it with traffic, and show that a predictive policy beats the Kubernetes rule. I expected made-up traffic with slow ramps to be good enough for a first version.
- **What I tried:** a synthetic generator with a daily cycle, 5% noise and bursts that ramp up over 3 to 10 minutes; then real traffic from the Azure Functions Trace 2019.
- **Where it resisted:**
  - Real traffic does not ramp. About 15% noise every minute, and 72% of bursts reach their peak in the first minute. With a 3-minute boot delay, no policy can react to these bursts in time, so my first framing (react earlier than the Kubernetes rule) was the wrong question.
  - Near-duplicate apps in the trace passed an exact duplicate check. I added a correlation filter above 0.95, which took the set from 21 apps to 19.
  - The first fitted generator multiplied burst heights, which made even a fixed fleet sized for the peak drop requests. Bursts are now added on top of normal load.
  - The video toolkit's standard outro carries another channel's handle, so the outro is a custom title card.
- **AI and other contributions:** Claude Code wrote most of the code and the video under my direction; I approved the data source, the split and the baselines, and reviewed the results. Narration is an AI voice (Kokoro `af_bella`).
- **What I understand now:** with real traffic, the only defence against a one-minute burst is capacity that is already running. Many bursts repeat at the same time the next day, so the useful signal is yesterday's traffic. The RL agent's real bar is "same time yesterday" at equal cost, not the Kubernetes rule.
- **Evidence:** [README](README.md#watch-and-review), [beat_sheet.json](beat_sheet.json), [rl-autoscaler 8b126bd](https://github.com/lakshdhamija/rl-autoscaler/commit/8b126bd)
