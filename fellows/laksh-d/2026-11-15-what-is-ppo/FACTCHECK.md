# FACTCHECK: What PPO Is, In Plain Words

Sources: lakshdhamija/rl-autoscaler @ 8b126bd `src/rl_autoscaler/env.py` (unchanged in the working tree);
stable-baselines3 2.9.2 installed in the rl-autoscaler venv (`PPO.__init__` defaults, `PPO.train`);
Schulman et al., "Proximal Policy Optimization Algorithms", OpenAI, 2017, arXiv:1707.06347.
Recorded run: `evidence/facts_stdout.txt` (`evidence/check_facts.py`, read-only). Checked 2026-11-11.

| Claim (beat) | Verdict | Source / derivation |
|---|---|---|
| Every minute the agent sees 25 numbers (B02, B04) | ✓ | `observation_space` shape (25,) = 10 past minutes + 10 of yesterday + running, booting, queue, sin and cos of time of day |
| Groups shown: last 10 minutes of requests, yesterday's next 10, servers running, servers booting, queue, time of day (2) | ✓ | `env.py _obs()` |
| 11 actions, from remove 5 servers to add 5 (B02, B04) | ✓ | `Discrete(2 * max_step + 1)`, `max_step = 5` |
| Reward = minus server cost minus a penalty per late request (B03) | ✓ | `reward = -(cost + c.late_penalty * late)` (quoted on screen); cost counts running + booting servers; late = requests not served in the minute they arrive |
| Reinforcement learning = learning by trial and error to collect the most reward (B03) | ✓ | plain-words definition |
| The policy is a small neural network that turns the 25 numbers into a probability per action (B04) | ✓ | SB3 default `ActorCriticPolicy` (MlpPolicy) for flat observations: `net_arch = dict(pi=[64, 64], vf=[64, 64])`, tanh. Not stated on screen; the drawing shows two hidden layers, unlabelled sizes |
| The 11 bar heights in B04 | illustration | constructed example odds that sum to 1, labelled "example odds, for illustration"; not a trained policy |
| Collect 2,048 steps per environment by default (B05) | ✓ | SB3 2.9.2 `n_steps = 2048` |
| Advantage = how much better an action did than the critic expected; the critic is a second network (B05) | ✓ | SB3 computes advantages with GAE (`gamma = 0.99`, `gae_lambda = 0.95`) against the value network (`vf`); plain-words simplification of GAE |
| Make good actions more likely (B05) | ✓ | the policy gradient step on the clipped objective |
| The first P is proximal, meaning close by (B06) | ✓ | paper title |
| Ratio = new probability / old probability (B06, B07) | ✓ | `ratio = th.exp(log_prob - rollout_data.old_log_prob)` in `PPO.train`; paper eq. 6 |
| Ratio clipped to 0.8 to 1.2 (B06, B07, B08) | ✓ | `clip_range = 0.2`; `th.clamp(ratio, 1 - clip_range, 1 + clip_range)` |
| B06 example 0.20 -> 0.30, r = 1.5 | illustration | labelled "one example action, for illustration"; 0.30 / 0.20 = 1.5 |
| L = E[min(r A, clip(r, 1-eps, 1+eps) A)] (B07) | ✓ | paper eq. 7; `policy_loss = -th.min(policy_loss_1, policy_loss_2).mean()` (SB3 minimises the negative) |
| Algebra check (numerical) | ✓ | eps = 0.2: r=1.5, A=+1 -> 1.20; r=1.1, A=+1 -> 1.10; r=0.5, A=-1 -> -0.80; r=0.9, A=-1 -> -0.90 (`evidence/facts_stdout.txt`) |
| E = average over the batch (B07) | ✓ | `.mean()` over the minibatch (expectation estimated by the sample mean) |
| Each batch reused for 10 passes (B07) | ✓ | SB3 `n_epochs = 10` |
| Other defaults (not on screen) | ✓ | learning_rate 0.0003, batch_size 64, gamma 0.99, gae_lambda 0.95 |
| Takeaway (B08): if RL training suddenly collapses, check the size of each update first | advice | from the brief; consistent with the purpose of clipping in the paper |
| B01: small, clipped steps, "so one update is less likely to wreck a policy that already works" | ✓ (corrected) | reworded 2026-11-11 from "cannot wreck": the clip removes the objective's incentive to move r outside 0.8 to 1.2 (paper section 3); it does not guarantee the policy stays good, and the ratio itself can still leave the band during the 10 passes |
| B06: "PPO limits how far a single update can move the policy" (narration and screen) | ✓ (corrected) | reworded 2026-11-11 from "no single update can move the policy far": same reason; the clip limits the incentive per update, it is not a hard bound on the change |
| B07 glossary and B08 card: "r is clipped to 0.8 to 1.2" / "PPO clips the new-to-old probability ratio to 0.8 to 1.2" (screen only) | ✓ (corrected) | reworded 2026-11-11 from "r stays in" / "ratio stays between": the clip acts on the ratio inside the objective; the ratio itself is not bounded (same reason as B01 and B06) |
| No PPO results for the autoscaler | ✓ | none stated anywhere |
