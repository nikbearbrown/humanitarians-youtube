"""integrations.py — the arithmetic MCP is an answer to.

Runnable, no dependencies, no API key. Every figure in the video is printed here.

HONESTY NOTE: this counts integrations, which is a structural property of how
things connect. It is not a benchmark, and it does not measure how long any
particular integration takes to build.
"""
from __future__ import annotations


def direct(apps: int, tools: int) -> int:
    """Every app writes its own connector to every tool."""
    if apps < 0 or tools < 0:
        raise ValueError("counts must not be negative")
    return apps * tools


def via_protocol(apps: int, tools: int) -> int:
    """Each app speaks the protocol once; each tool is exposed once."""
    if apps < 0 or tools < 0:
        raise ValueError("counts must not be negative")
    return apps + tools


def new_tool_cost(apps: int) -> tuple[int, int]:
    """Connectors needed to add ONE more tool: direct, then via a protocol."""
    return apps, 1


if __name__ == "__main__":
    print("CONNECTORS TO BUILD")
    print(f"{'apps':>5}  {'tools':>5}  {'direct':>7}  {'protocol':>9}")
    for a, t in ((2, 3), (3, 5), (5, 10), (10, 20)):
        print(f"{a:>5}  {t:>5}  {direct(a,t):>7}  {via_protocol(a,t):>9}")

    print("\nADDING ONE MORE TOOL")
    print(f"{'existing apps':>14}  {'direct':>7}  {'protocol':>9}")
    for a in (3, 5, 10, 50):
        d, p = new_tool_cost(a)
        print(f"{a:>14}  {d:>7}  {p:>9}")

    print("\nWHERE THE PROTOCOL LOSES")
    for a, t in ((1, 1), (1, 3), (2, 2)):
        d, p = direct(a, t), via_protocol(a, t)
        verdict = "protocol wins" if p < d else ("tie" if p == d else "DIRECT wins")
        print(f"  {a} app(s), {t} tool(s):  direct {d}, protocol {p}  ->  {verdict}")
