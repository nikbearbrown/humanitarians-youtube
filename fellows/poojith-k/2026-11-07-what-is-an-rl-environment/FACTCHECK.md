# Fact check

| Script beat | Claim or on-screen statement | Evidence and scope |
| --- | --- | --- |
| B00 | Name, topic and planned AI narration. | User-approved intro and planned production method. The broom is a teaching analogy. |
| B01 | RL learns by trial and error. The agent chooses actions and the environment responds with observations and rewards. | S1 §§1.1, 1.3 and 3.1. S2 Env overview and `step()`. |
| B01 | Gymnasium is open source. CartPole simulates a cart and attached pole, with left and right push actions. | S5 abstract for the library. S3 Description and Action Space for CartPole. S2 `step()` for the response. |
| B02 | State is the underlying situation. Observations are what the agent gets and may be partial. | S1 §3.1. S2 Env overview explicitly distinguishes full and partial observation. |
| B02 | CartPole reports cart position and velocity, and pole angle and angular velocity. | S3 Observation Space. “Speed” and “how fast it's tipping” are plain-language descriptions of the two velocity values. |
| B03 | Reset starts an episode and returns an initial observation. Step applies one action and returns a new observation, reward and ending status. Reset after either ending. | S2 `reset()` and `step()`. The complete API also returns `info` and distinguishes `terminated` from `truncated`. The spoken line groups those outcomes for a general audience. |
| B03 | CartPole-v1 terminates if the pole tips too far or the cart leaves its allowed range. Its time limit is 500 steps. | S3 Episode End and Version History. The thresholds are ±12° for the pole angle and ±2.4 for cart position. The 500-step limit is specific to v1. |
| B04 | Default CartPole-v1 gives +1 per step, including the termination step. Remaining upright longer while staying on track earns more points. | S3 Rewards and Episode End. The graphic's three steps give a total of 3 without discounting. The three steps illustrate arithmetic. |
| B04 | A reward is immediate feedback. An episodic return combines rewards and can discount later rewards. A move can affect later rewards. | S1 §§1.1 and 3.1–3.3. |
| B05 | A policy is the rule for choosing actions. Algorithms can improve it directly or estimate action values from experience. | S1 §§1.3 and 3.1 and Ch. 13. S4 The Training Loop and Understanding the Q-Learning Update for an action-value example. |
| B05 | Exploring unfamiliar actions can gather evidence, while exploiting uses what has been learned to earn reward. | S1 Ch. 1, §1.1. S4 Exploration vs Exploitation. |
| B06 | A common interface supports using compatible training code across environments. | S5 abstract. The reset and step labels illustrate interface compatibility. |
| B06 | Held-out situations test generalization. CoinRun separated practice and testing levels, and the study reported overfitting even with large training sets. | S6 abstract and evaluation protocol. The claim concerns the agents studied there. |
| B06 | The presenter's project set aside worlds for evaluation. | S7 Relief Dispatch project records, frozen preregistration and validity report. The confirmation population was separate from exploration. |
| B06 | Ask what was rewarded and what was held back. | Editorial takeaway from S1 §3.2 on the reward signal and S6 on train/test separation. |
| B06 | The environment defines how actions change its state, supplies rewards and signals the end of an episode. | S1 §3 on the agent/environment interface, returns and episodes, and S2 on rewards, termination and truncation. |

Sources are listed in [SOURCES.md](SOURCES.md).
