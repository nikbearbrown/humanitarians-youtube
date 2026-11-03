#!/usr/bin/env python3
"""Short corridor with switched actions (Sutton & Barto 2nd ed., Example 13.1).

Three non-terminal states that the learner cannot tell apart: every state has the
same feature vector, x(s,right)=[1,0], x(s,left)=[0,1]. In state 1 the actions are
reversed. Reward -1 per step, gamma = 1. Pure stdlib, seeded, reproducible.

Runs three things:
  1. exact values for any fixed P(right)   (closed-form, no learning)
  2. an epsilon-greedy action-value learner (Sarsa, eps = 0.1)
  3. a policy-gradient learner (REINFORCE, softmax over the same features)
"""
import json, math, random, statistics, sys
from pathlib import Path

STEP_CAP = 1000  # an episode that runs this long is counted as never finishing


def step(s, right):
    if s == 0:
        return (1 if right else 0)
    if s == 1:                      # switched state
        return (0 if right else 2)
    return (3 if right else 1)      # state 2; 3 = goal


def exact_value(p):
    """Value of the start state under 'go right with probability p' (gamma = 1)."""
    if p <= 0 or p >= 1:
        return float("-inf")
    q = 1 - p
    v1 = (-2 - q) / (1 - q * q - p)
    return v1 - 1 / p


def episode(policy_p, rng):
    s, t, traj = 0, 0, []
    while s != 3 and t < STEP_CAP:
        right = rng.random() < policy_p()
        traj.append(right)
        s, t = step(s, right), t + 1
    return traj, s == 3


def sarsa(rng, episodes=1000, eps=0.1, alpha=0.01):
    w = [0.0, 0.0]                               # [q(right), q(left)], shared by all states
    def act():
        if rng.random() < eps:
            return rng.random() < 0.5
        return w[0] > w[1] if w[0] != w[1] else rng.random() < 0.5
    returns = []
    for _ in range(episodes):
        s, t, a = 0, 0, act()
        while s != 3 and t < STEP_CAP:
            s2 = step(s, a); t += 1
            i = 0 if a else 1
            if s2 == 3:
                w[i] += alpha * (-1 - w[i]); s = s2; break
            a2 = act()
            w[i] += alpha * (-1 + w[0 if a2 else 1] - w[i])
            s, a = s2, a2
        returns.append(-t)
    greedy_right = w[0] > w[1]
    p = 1 - eps / 2 if greedy_right else eps / 2
    return {"final_p_right": p, "greedy": "right" if greedy_right else "left",
            "value_of_learned_policy": exact_value(p), "mean_return_last_100": statistics.mean(returns[-100:])}


def sarsa_sees_state(rng, episodes=1000, eps=0.1, alpha=0.1):
    """Boundary run: same learner, but one value pair PER STATE (it can see where it is)."""
    w = [[0.0, 0.0] for _ in range(3)]
    def act(s):
        if rng.random() < eps:
            return rng.random() < 0.5
        r, l = w[s]
        return r > l if r != l else rng.random() < 0.5
    for _ in range(episodes):
        s, t, a = 0, 0, act(0)
        while s != 3 and t < STEP_CAP:
            s2 = step(s, a); t += 1
            i = 0 if a else 1
            if s2 == 3:
                w[s][i] += alpha * (-1 - w[s][i]); break
            a2 = act(s2)
            w[s][i] += alpha * (-1 + w[s2][0 if a2 else 1] - w[s][i])
            s, a = s2, a2
    greedy = ["right" if r > l else "left" for r, l in w]
    s, n = 0, 0                                   # walk the greedy route, no exploration
    while s != 3 and n < STEP_CAP:
        s, n = step(s, greedy[s] == "right"), n + 1
    return {"greedy_by_state": greedy, "greedy_steps_to_goal": n}


def reinforce(rng, episodes=1000, alpha=2 ** -13, p0=0.5):
    h = math.log(p0 / (1 - p0))
    th = [h, 0.0]                                # preferences for [right, left]; P(right) starts at p0
    def p_right():
        m = max(th); er, el = math.exp(th[0] - m), math.exp(th[1] - m)
        return er / (er + el)
    returns = []
    for _ in range(episodes):
        traj, done = episode(p_right, rng)
        T = len(traj)
        for k, right in enumerate(traj):
            G = -(T - k)
            pr = p_right()
            grad = [(1 - pr), -(1 - pr)] if right else [-pr, pr]   # grad ln pi for softmax
            th = [th[0] + alpha * G * grad[0], th[1] + alpha * G * grad[1]]
        returns.append(-T)
    p = p_right()
    return {"start_p_right": p0, "final_p_right": p, "curve_last_100": [statistics.mean(returns[i:i+100]) for i in range(0, episodes, 100)], "value_of_learned_policy": exact_value(p),
            "mean_return_last_100": statistics.mean(returns[-100:])}


def main():
    out = {}
    pstar = 2 - math.sqrt(2)
    out["exact"] = {"always_right": "never finishes (loops between states 0 and 1)",
                    "always_left": "never finishes (stays in state 0)",
                    "eps_greedy_mostly_right_p0.95": exact_value(0.95),
                    "eps_greedy_mostly_left_p0.05": exact_value(0.05),
                    "fair_coin_p0.5": exact_value(0.5),
                    "optimal_p": pstar, "optimal_value": exact_value(pstar)}
    out["curve"] = [[round(p, 2), exact_value(p)] for p in [i / 100 for i in range(5, 100, 5)]]
    seeds = range(30)
    out["sarsa"] = [sarsa(random.Random(s)) for s in seeds]
    out["reinforce"] = [reinforce(random.Random(s)) for s in seeds]
    out["reinforce_from_mostly_left"] = [reinforce(random.Random(s), p0=0.05, episodes=2000, alpha=2 ** -12) for s in seeds]
    out["sarsa_sees_state"] = [sarsa_sees_state(random.Random(s)) for s in seeds]
    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=1))

    e = out["exact"]
    print("EXACT  mostly-right %.2f | mostly-left %.2f | fair coin %.2f | optimum p=%.4f -> %.2f"
          % (e["eps_greedy_mostly_right_p0.95"], e["eps_greedy_mostly_left_p0.05"],
             e["fair_coin_p0.5"], pstar, e["optimal_value"]))
    g = [r["greedy"] for r in out["sarsa"]]
    sv = [r["value_of_learned_policy"] for r in out["sarsa"]]
    print("SARSA (eps=0.1, 30 seeds): greedy right %d / left %d | learned-policy value mean %.2f, best %.2f"
          % (g.count("right"), g.count("left"), statistics.mean(sv), max(sv)))
    rp = [r["final_p_right"] for r in out["reinforce"]]
    rv = [r["value_of_learned_policy"] for r in out["reinforce"]]
    print("REINFORCE (30 seeds): P(right) mean %.3f [%.3f..%.3f] | value mean %.2f, worst %.2f"
          % (statistics.mean(rp), min(rp), max(rp), statistics.mean(rv), min(rv)))
    L = out["reinforce_from_mostly_left"]
    rp = [r["final_p_right"] for r in L]; rv = [r["value_of_learned_policy"] for r in L]
    print("REINFORCE from P(right)=0.05 (value %.2f), 2000 ep, 30 seeds: P(right) mean %.3f [%.3f..%.3f] | value mean %.2f, worst %.2f"
          % (exact_value(0.05), statistics.mean(rp), min(rp), max(rp), statistics.mean(rv), min(rv)))
    B = out["sarsa_sees_state"]
    routes = {}
    for r in B: k = "-".join(r["greedy_by_state"]) + " (%d steps)" % r["greedy_steps_to_goal"]; routes[k] = routes.get(k, 0) + 1
    print("SARSA that SEES the state (30 seeds): greedy routes", routes)
    c = [statistics.mean(r["curve_last_100"][i] for r in L) for i in range(20)]
    print("  mean return per 100-episode block:", " ".join("%.0f" % x for x in c))


if __name__ == "__main__":
    main()
