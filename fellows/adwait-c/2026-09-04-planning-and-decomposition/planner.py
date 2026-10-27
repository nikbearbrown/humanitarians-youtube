"""planner.py — what a plan actually costs, and when it pays for itself.

Part of the Agentic AI series (Humanitarians AI Fellows).

Agent frameworks plan by default. Almost none of them ask whether planning is worth it
for the task in front of them. This file makes the trade measurable.

HONESTY NOTE, and it matters: this is a COST MODEL, not a benchmark. It counts model
calls, which is a fair proxy for latency and spend, under assumptions stated in the code
below. It does not measure answer quality, and it does not claim one strategy is smarter.
The point is the SHAPE of the trade, not the size of the numbers.

    python3 planner.py
"""

from __future__ import annotations

STEPS = 8   # a task with eight steps


# --- the two strategies ---------------------------------------------------
# PLAN-THEN-EXECUTE  writes the whole plan once, then runs it.
# STEP-BY-STEP       decides one step, runs it, looks, decides again.

def plan_then_execute(steps: int = STEPS, fails_at: int | None = None) -> dict:
    """One planning call up front, then one call per step.

    If reality diverges at `fails_at`, every step planned after that point was written
    for a world that no longer exists, so it is discarded and the remainder re-planned.
    """
    calls = 1 + steps                      # plan once, execute each step
    discarded = 0
    if fails_at is not None:
        discarded = steps - fails_at + 1   # this step and everything planned after it
        calls += 1 + discarded             # re-plan, then redo the discarded steps
    return {"strategy": "plan-then-execute", "calls": calls, "discarded": discarded}


def step_by_step(steps: int = STEPS, fails_at: int | None = None) -> dict:
    """Decide and execute one step at a time. Never commits to a future it cannot see.

    Costs two calls per step instead of one, but a surprise at any point discards
    nothing, because nothing beyond the current step was ever decided.
    """
    calls = 2 * steps                      # decide + execute, every step
    if fails_at is not None:
        calls += 2                         # re-decide the failed step and redo it
    return {"strategy": "step-by-step", "calls": calls, "discarded": 0}


# --- the three questions that decide it -----------------------------------
# This is the beat B05 shows on screen, verbatim.

def planning_pays(step_cost_is_high: bool, world_is_stable: bool,
                  steps_depend_on_each_other: bool) -> bool:
    """Planning earns its call only when all three hold.

    Expensive or irreversible steps mean you want the whole path before touching
    anything. A stable world means the plan survives contact. Dependent steps mean
    order matters, which is the only thing a plan actually buys you.
    """
    return step_cost_is_high and world_is_stable and steps_depend_on_each_other


if __name__ == "__main__":
    clean_p = plan_then_execute()
    clean_s = step_by_step()
    print("NOTHING GOES WRONG")
    print(f"  plan-then-execute   {clean_p['calls']:>3} calls")
    print(f"  step-by-step        {clean_s['calls']:>3} calls")
    print(f"  planning saves      {clean_s['calls'] - clean_p['calls']:>3} calls\n")

    print("SOMETHING GOES WRONG AT STEP k")
    print(f"{'k':>3}  {'plan-then-execute':>18}  {'step-by-step':>13}  {'plan discarded':>14}")
    for k in range(1, STEPS + 1):
        p, s = plan_then_execute(fails_at=k), step_by_step(fails_at=k)
        # Label the comparison precisely. An early failure erases the advantage; it does
        # not automatically reverse it, and saying so would overstate the case.
        if p["calls"] < s["calls"]:
            win = ""
        elif p["calls"] == s["calls"]:
            win = "   <- planning's advantage is GONE"
        else:
            win = "   <- planning now costs MORE"
        print(f"{k:>3}  {p['calls']:>18}  {s['calls']:>13}  {p['discarded']:>14}{win}")

    print("\nWHEN IS A PLAN WORTH THE CALL?")
    for cost, stable, dep in ((True, True, True), (True, True, False),
                              (True, False, True), (False, True, True)):
        print(f"  expensive={str(cost):<5} stable={str(stable):<5} "
              f"dependent={str(dep):<5} ->  {'PLAN' if planning_pays(cost, stable, dep) else 'do not plan'}")
