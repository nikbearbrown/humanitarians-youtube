"""agent_loop.py — the smallest honest agent loop.

Episode 1 of "Agentic AI: From the Loop to MCP" (Humanitarians AI Fellows).

The point of this file is that it is REAL and it RUNS. There is no model call and
no API key: `think()` is a deterministic stand-in so the loop's SHAPE is what you
study, not a provider's SDK. Swap `think()` for a model call and nothing else in
`run()` has to change — that substitution is the whole argument of the episode.

    python3 agent_loop.py
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Decision:
    """What one pass of 'think' produces: either a tool call, or an answer."""
    done: bool = False
    answer: str = ""
    tool_name: str = ""
    arguments: dict = field(default_factory=dict)


# --- the loop -------------------------------------------------------------
# This is the beat B06 shows on screen, verbatim.

def run(goal: str, tools: dict, max_steps: int = 8) -> str:
    observations: list[str] = []
    for step in range(max_steps):
        decision = think(goal, observations)      # pick ONE next step
        if decision.done:
            return decision.answer
        tool = tools[decision.tool_name]
        result = tool(**decision.arguments)       # the act — something real happens
        observations.append(f"{decision.tool_name} -> {result}")
    return "stopped: step budget exhausted"


# --- the stand-in "model" -------------------------------------------------

def think(goal: str, observations: list[str]) -> Decision:
    """Deterministic stand-in for a model call.

    A real implementation sends `goal` plus `observations` to a language model and
    parses a structured decision back. The contract is identical: read the goal and
    everything observed so far, return either a tool call or a final answer.
    """
    seen = {line.split(" -> ")[0] for line in observations}

    if "read_file" not in seen:
        return Decision(tool_name="read_file", arguments={"path": "sales.csv"})
    if "count_rows" not in seen:
        return Decision(tool_name="count_rows", arguments={"text": _last(observations)})

    return Decision(done=True, answer=f"{goal}: {_last(observations)}")


def _last(observations: list[str]) -> str:
    return observations[-1].split(" -> ", 1)[1] if observations else ""


# --- the tools ------------------------------------------------------------

def read_file(path: str) -> str:
    """Stand-in for real I/O; returns a fixed three-row CSV so runs are reproducible."""
    return "region,units\nnortheast,12\nmidwest,9\nsouth,14"


def count_rows(text: str) -> str:
    return str(len(text.strip().splitlines()) - 1)  # minus the header


TOOLS = {"read_file": read_file, "count_rows": count_rows}


if __name__ == "__main__":
    print(run("rows in the sales file", TOOLS))
