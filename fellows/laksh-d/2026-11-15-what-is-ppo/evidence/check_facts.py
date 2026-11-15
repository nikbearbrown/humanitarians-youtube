"""Record the facts the PPO explainer states, from the installed packages (read-only).

Run in the rl-autoscaler venv: python <reel>/evidence/check_facts.py > <reel>/evidence/facts_stdout.txt
"""
import inspect
import subprocess

import numpy as np
import stable_baselines3 as sb3
from stable_baselines3 import PPO
from stable_baselines3.common.policies import ActorCriticPolicy

from rl_autoscaler.env import AutoscaleEnv, ClusterConfig

print("rl-autoscaler commit", subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip())
env = AutoscaleEnv(np.zeros(2880))
c = ClusterConfig()
print("observation numbers", env.observation_space.shape[0], "= window", c.window, "+ yesterday", c.yesterday_window,
      "+ running, booting, queue, sin(time), cos(time)")
print("actions", env.action_space.n, "= change in servers from", -c.max_step, "to", c.max_step)
print("reward = -(server_cost * billed servers + late_penalty * late requests);", "server_cost", c.server_cost,
      "late_penalty", c.late_penalty)
print("stable-baselines3", sb3.__version__)
sig = inspect.signature(PPO.__init__)
for k in ("learning_rate", "n_steps", "batch_size", "n_epochs", "gamma", "gae_lambda", "clip_range"):
    print(f"PPO default {k} = {sig.parameters[k].default}")
for line in inspect.getsource(ActorCriticPolicy.__init__).splitlines():
    if "net_arch = dict(" in line or "activation_fn: type" in line:
        print("policy default:", line.strip())
for line in inspect.getsource(PPO.train).splitlines():
    if "th.clamp(ratio" in line or "th.min(policy_loss_1" in line or "ratio = th.exp" in line:
        print("PPO.train:", line.strip())
eps = 0.2
L = lambda r, A: min(r * A, float(np.clip(r, 1 - eps, 1 + eps)) * A)
for r, A in ((1.5, 1.0), (1.1, 1.0), (0.5, -1.0), (0.9, -1.0)):
    print(f"clipped objective check: r={r}, A={A:+} -> min(rA, clip(r)A) = {L(r, A):+.2f}")
