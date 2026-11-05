"""server.py — the smallest honest MCP-shaped server.

Runnable, no dependencies, no network, no API key. It speaks the three calls
that matter — list the tools, describe one, run one — over plain JSON, so the
SHAPE is visible without a transport getting in the way.

HONESTY NOTE: this is not the Model Context Protocol wire format. It is the
protocol's shape reduced to what fits on screen: discovery, description,
invocation. A real server adds a transport, a session and error semantics.

    python3 server.py
"""
from __future__ import annotations

import inspect
import json
from typing import Any, Callable

REGISTRY: dict[str, Callable] = {}


def tool(fn: Callable) -> Callable:
    """Register a function as a tool. Its docstring becomes its description."""
    if not inspect.getdoc(fn):
        raise ValueError(f"{fn.__name__} has no docstring, so it cannot be described")
    REGISTRY[fn.__name__] = fn
    return fn


@tool
def row_count(path: str) -> str:
    """Count data rows in a CSV file, excluding the header.

    Use this when you need the size of a file. Do NOT use it to read values.
    """
    return "3"


@tool
def column_names(path: str) -> str:
    """List the column headers of a CSV file, in order.

    Use this to discover the shape of a file before reading it. Do NOT use it
    to count rows.
    """
    return "region, units"


def list_tools() -> list[dict[str, Any]]:
    """Discovery: what can this server do? The client was told nothing in advance."""
    return [describe(name) for name in sorted(REGISTRY)]


def describe(name: str) -> dict[str, Any]:
    """The contract for one tool: name, description, parameter schema."""
    if name not in REGISTRY:
        raise KeyError(f"no such tool: {name}")
    fn = REGISTRY[name]
    params = inspect.signature(fn).parameters.values()
    return {
        "name": name,
        "description": inspect.getdoc(fn),
        "input_schema": {
            "type": "object",
            "properties": {p.name: {"type": "string"} for p in params},
            "required": [p.name for p in params],
        },
    }


def call(name: str, arguments: dict[str, Any]) -> str:
    """Invocation. Unknown tools are refused, not guessed at."""
    if name not in REGISTRY:
        raise KeyError(f"no such tool: {name}")
    return REGISTRY[name](**arguments)


if __name__ == "__main__":
    print("1. CLIENT CONNECTS AND ASKS WHAT EXISTS")
    for entry in list_tools():
        first = entry["description"].split("\n")[0]
        print(f"   {entry['name']:<13} {first}")

    print("\n2. CLIENT ASKS FOR ONE CONTRACT IN FULL")
    print(json.dumps(describe("row_count"), indent=2)[:420])

    print("\n3. CLIENT CALLS IT")
    print(f"   row_count(path='sales.csv')  ->  {call('row_count', {'path': 'sales.csv'})}")

    print("\n4. CLIENT CALLS SOMETHING THAT DOES NOT EXIST")
    try:
        call("delete_everything", {})
    except KeyError as err:
        print(f"   {err}")
