"""context.py — the budget you re-pay every single turn.

Episode 4 of "Agentic AI: From the Loop to MCP" (Humanitarians AI Fellows).

Episode 3 showed what one tool definition costs to describe. This file adds them up
across a run, because that is where the surprise is: an agent has no memory. It has a
context window, and every turn re-sends the whole thing from scratch. What looks like
forgetting is overflow.

HONESTY NOTE, and it matters: this measures CHARACTERS, not tokens, and BUDGET below is
deliberately small so the arithmetic is visible in a 4-minute video. Real windows are far
larger. The numbers here are real measurements of real strings — but the point is the
SHAPE of the curve, not the size of the budget.

    python3 context.py
"""

from __future__ import annotations

import json
import os
import sys

# Carry forward Episode 3's real tool definitions rather than restating them.
_EP3 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "..", "2026-08-21-tools-and-function-calling")
sys.path.insert(0, os.path.abspath(_EP3))
import tools  # noqa: E402  — tools.py from Episode 3, unchanged

BUDGET = 2000  # characters. Small on purpose; see the honesty note above.

SYSTEM = ("You are an agent. Think, act, observe, repeat. "
          "Stop when the goal is met or the step budget runs out.")

TOOLSET = (tools.read_file, tools.count_rows)


# --- the three claims on one budget ---------------------------------------
# This is the beat B05 shows on screen, verbatim.

def budget_row(turn: int, history: int) -> dict:
    """What the three parts cost on this turn. Instructions are re-sent every time."""
    instructions = len(SYSTEM) + sum(
        len(json.dumps(tools.to_schema(fn))) for fn in TOOLSET)
    return {
        "turn": turn,
        "instructions": instructions,   # FIXED — but paid again, every turn
        "history": history,             # GROWS — every observation is kept
        "room": BUDGET - instructions - history,
    }


def observation(turn: int) -> str:
    """One realistic observation, in the honest format Episode 2 argued for."""
    return (f"read_file({{'path': 'sales_{turn:02d}.csv'}}) -> "
            f"'region,units\\nnortheast,12\\nmidwest,9\\nsouth,14'")


def run(turns: int = 8, budget: int = BUDGET) -> list[dict]:
    history, rows = 0, []
    for turn in range(1, turns + 1):
        history += len(observation(turn))
        row = budget_row(turn, history)
        row["room"] = budget - row["instructions"] - row["history"]
        rows.append(row)
    return rows


def first_overflow(budget: int, turns: int = 500) -> int | None:
    """The turn where room goes negative.

    The horizon is deliberately long: history grows linearly and the budget is fixed, so
    EVERY budget overflows eventually. A short horizon would report a false "never".
    """
    for row in run(turns, budget):
        if row["room"] < 0:
            return row["turn"]
    return None


if __name__ == "__main__":
    rows = run()
    print(f"THE BUDGET, TURN BY TURN   (budget = {BUDGET} chars)")
    print(f"{'turn':>4}  {'instructions':>12}  {'history':>7}  {'room to answer':>14}")
    for r in rows:
        flag = "  <- OVERFLOW" if r["room"] < 0 else ""
        print(f"{r['turn']:>4}  {r['instructions']:>12}  {r['history']:>7}  {r['room']:>14}{flag}")

    print("\nDOES A BIGGER WINDOW FIX IT?")
    for b in (BUDGET, BUDGET * 2, BUDGET * 4):
        t = first_overflow(b)
        print(f"  budget {b:>5} chars  ->  first overflow at turn {t}")
    print("\n  Doubling the budget does not remove the overflow. It moves it.")
