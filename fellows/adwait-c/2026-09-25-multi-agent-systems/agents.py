"""agents.py — what a second agent actually costs.

Runnable, no dependencies, no API key. Every figure in the video is printed here.

HONESTY NOTE: this is arithmetic about coordination and compounding reliability,
not a benchmark. It shows what the structure of a multi-agent system implies,
given a per-agent success rate you supply.
"""
from __future__ import annotations


def handoffs(n: int, topology: str = "supervisor") -> int:
    """Coordination links. A supervisor fans out; a mesh connects everyone."""
    if n < 1:
        raise ValueError("need at least one agent")
    if topology == "supervisor":
        return 2 * (n - 1)          # down to each worker and back
    if topology == "mesh":
        return n * (n - 1) // 2     # every pair talks
    raise ValueError("topology must be supervisor or mesh")


def end_to_end(per_agent: float, n: int) -> float:
    """Chance the whole chain succeeds when every step must succeed."""
    if not 0 <= per_agent <= 1:
        raise ValueError("per_agent must be between 0 and 1")
    return per_agent ** n


if __name__ == "__main__":
    print("COORDINATION LINKS")
    print(f"{'agents':>7}  {'supervisor':>11}  {'mesh':>5}")
    for n in (1, 2, 3, 5, 8):
        print(f"{n:>7}  {handoffs(n):>11}  {handoffs(n,'mesh'):>5}")

    print("\nEVERY STEP MUST SUCCEED  (95% each)")
    print(f"{'agents':>7}  {'end to end':>11}  {'failures/100 runs':>18}")
    for n in (1, 2, 3, 5, 8):
        p = end_to_end(0.95, n)
        print(f"{n:>7}  {p:>10.1%}  {100*(1-p):>18.0f}")

    print("\nHOW GOOD MUST EACH AGENT BE FOR 95% END TO END?")
    for n in (2, 3, 5, 8):
        need = 0.95 ** (1 / n)
        print(f"  {n} agents  ->  each must be {need:.2%}")
