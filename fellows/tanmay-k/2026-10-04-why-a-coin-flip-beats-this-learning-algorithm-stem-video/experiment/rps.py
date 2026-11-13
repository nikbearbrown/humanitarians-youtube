#!/usr/bin/env python3
"""Rock-paper-scissors: the blindfold test's other outcome.

There is nothing hidden here: the player knows the whole game. The question is whether a fixed rule
can still be best. The opponent ADAPTS: it counts the player's past moves and plays whatever beats the
player's most frequent move so far (fictitious play). Stdlib, seeded, reproducible.

Player payoff per round: +1 win, 0 draw, -1 loss. Averaged over rounds, then over seeds.
"""
import json, random, statistics
from pathlib import Path

MOVES = ["rock", "paper", "scissors"]
BEATS = {"rock": "paper", "paper": "scissors", "scissors": "rock"}   # value beats key


def payoff(me, them):
    if me == them:
        return 0
    return 1 if BEATS[them] == me else -1


def play(player_probs, rng, rounds=1000, adaptive=True):
    counts = {m: 0 for m in MOVES}
    total = 0
    for _ in range(rounds):
        if adaptive and sum(counts.values()):
            top = max(MOVES, key=lambda m: (counts[m], rng.random()))
            them = BEATS[top]
        else:
            them = rng.choice(MOVES)
        me = rng.choices(MOVES, weights=player_probs)[0]
        counts[me] += 1
        total += payoff(me, them)
    return total / rounds


def main():
    players = {"always rock": [1, 0, 0], "lean rock 50/30/20": [0.5, 0.3, 0.2],
               "uniform 1/3 each": [1, 1, 1]}
    out = {}
    for name, probs in players.items():
        adapt = [play(probs, random.Random(s)) for s in range(30)]
        fixed = [play(probs, random.Random(1000 + s), adaptive=False) for s in range(30)]
        out[name] = {"vs_adaptive_mean": statistics.mean(adapt), "vs_adaptive_min": min(adapt),
                     "vs_adaptive_max": max(adapt), "vs_random_opponent_mean": statistics.mean(fixed)}
        print(f"{name:20} vs adaptive opponent: mean {statistics.mean(adapt):+.3f} "
              f"[{min(adapt):+.3f}..{max(adapt):+.3f}] | vs non-adaptive random opponent: "
              f"{statistics.mean(fixed):+.3f}")
    Path(__file__).with_name("rps_results.json").write_text(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
