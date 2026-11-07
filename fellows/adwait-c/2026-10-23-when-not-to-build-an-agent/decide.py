"""decide.py — the three conditions, applied to tasks people actually automate.

Runnable, no dependencies, no API key. The scoring is a stated rubric, not a
measurement: it encodes a judgement so the judgement can be argued with.

Conditions, all three required:
  DOING      the task needs an action taken, not a description produced
  UNDOABLE   a wrong step is cheap to reverse
  CHECKABLE  success is distinguishable from failure without reading every step
"""
from __future__ import annotations

TASKS = {
    "Reformat a folder of CSVs":            (True,  True,  True),
    "Draft a reply for me to send":         (False, True,  True),
    "Triage and close support tickets":     (True,  False, False),
    "Research and summarise a topic":       (False, True,  False),
    "Run the test suite and fix failures":  (True,  True,  True),
    "Email the quarterly numbers to board": (True,  False, True),
}


def verdict(doing: bool, undoable: bool, checkable: bool) -> str:
    """All three or it is not an agent-shaped task."""
    return "AGENT" if (doing and undoable and checkable) else "NOT YET"


def missing(doing: bool, undoable: bool, checkable: bool) -> list[str]:
    names = (("doing", doing), ("undoable", undoable), ("checkable", checkable))
    return [n for n, ok in names if not ok]


if __name__ == "__main__":
    print(f"{'task':<38} {'verdict':<8} missing")
    for task, flags in TASKS.items():
        gap = ", ".join(missing(*flags)) or "-"
        print(f"{task:<38} {verdict(*flags):<8} {gap}")

    agents = sum(1 for f in TASKS.values() if verdict(*f) == "AGENT")
    print(f"\n{agents} of {len(TASKS)} pass all three.")

    print("\nWHICH CONDITION FAILS MOST OFTEN?")
    for i, name in enumerate(("doing", "undoable", "checkable")):
        fails = sum(1 for f in TASKS.values() if not f[i])
        print(f"  {name:<10} fails {fails} of {len(TASKS)}")
