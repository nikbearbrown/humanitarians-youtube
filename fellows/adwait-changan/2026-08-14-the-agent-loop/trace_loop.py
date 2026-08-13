"""trace_loop.py — the same loop as Episode 1, with the observation made honest.

Episode 2 of "Agentic AI: From the Loop to MCP" (Humanitarians AI Fellows).

Episode 1 shipped `agent_loop.py` and argued that an agent is a model inside a loop.
This file extends that loop rather than replacing it — the only thing that changes is
how an observation is RECORDED, and the episode's claim is that this one change is
what makes the loop work at all.

Run both halves and read the difference:

    python3 trace_loop.py
"""

from __future__ import annotations


# --- the tools ------------------------------------------------------------
# read_file is deliberately broken for "sales.csv" so we can watch an error
# either survive into the observation, or get swallowed by it.

def read_file(path: str) -> str:
    if path == "sales.csv":
        raise FileNotFoundError("sales.csv")
    return "region,units\nnortheast,12\nmidwest,9\nsouth,14"


def count_rows(text: str) -> str:
    return str(len(text.strip().splitlines()) - 1)  # minus the header


TOOLS = {"read_file": read_file, "count_rows": count_rows}


# --- the bad observation --------------------------------------------------

def record_badly(name: str, arguments: dict, call) -> str:
    """Throws away everything the next pass needs: the args, the value, the error."""
    try:
        call(**arguments)
        return "ok"
    except Exception:
        return "ok"          # the failure is now invisible to the model


# --- the good observation -------------------------------------------------
# This is the beat B06 shows on screen, verbatim.

def record(name: str, arguments: dict, call) -> str:
    """Turn one tool call into an observation the model can actually act on."""
    try:
        result = call(**arguments)
    except Exception as err:                      # the error IS the observation
        return f"{name}({arguments}) -> ERROR {type(err).__name__}: {err}"
    return f"{name}({arguments}) -> {result!r}"


# --- one turn, traced -----------------------------------------------------

def one_turn(name: str, arguments: dict, recorder) -> str:
    thought = f"I need {name} to make progress on the goal."
    observation = recorder(name, arguments, TOOLS[name])
    return f"  THOUGHT      {thought}\n  ACTION       {name}({arguments})\n  OBSERVATION  {observation}"


# --- the whole loop, run with the lazy recorder ---------------------------
# Episode 1's `think()` decides what to do next by reading the observations for
# tool names it has already tried. A lazy observation carries no tool name, so
# `seen` stays empty, so it picks the same call every pass. Nothing here is
# rigged: the repetition falls out of the recorder, which is the episode's claim.

def think_names(observations: list[str]) -> str:
    seen = {line.split(" -> ")[0] for line in observations if " -> " in line}
    return "read_file" if "read_file" not in seen else "count_rows"


def run_lazy(max_steps: int = 8) -> list[str]:
    observations: list[str] = []
    log: list[str] = []
    for step in range(1, max_steps + 1):
        name = think_names(observations)
        obs = record_badly(name, {"path": "sales.csv"}, TOOLS[name])
        observations.append(obs)
        log.append(f"pass {step}   {name}({{'path': 'sales.csv'}}) -> {obs}")
    log.append("stopped: step budget exhausted")
    return log


if __name__ == "__main__":
    call = ("read_file", {"path": "sales.csv"})

    print("WITH A LAZY OBSERVATION")
    print(one_turn(*call, record_badly))
    print("  NEXT PASS    sees 'ok' and moves on. The file was never read.\n")

    print("WITH AN HONEST OBSERVATION")
    print(one_turn(*call, record))
    print("  NEXT PASS    sees the error, and can try a different path.\n")

    print("THE LAZY OBSERVATION, RUN TO THE STEP BUDGET")
    for line in run_lazy():
        print(f"  {line}")
