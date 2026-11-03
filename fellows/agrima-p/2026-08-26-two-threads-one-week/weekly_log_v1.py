"""weekly_log_v1.py — Claude Code output.

Logs this week's real work across two threads (writing, the Loon
Project) — every item, its real status. No scoring, no tally, just
what happened.
"""

WEEK = {
    "writing": [
        {"item": "Fashion Just Got a Data Brain", "status": "published"},
        {"item": "The Open-Source AI Gap Basically Closed", "status": "published"},
    ],
    "loon_project": [
        {"item": "Drone acquired", "status": "done"},
        {"item": "FAA Part 107 requirements researched", "status": "done"},
        {"item": "Social media strategy written", "status": "done"},
        {"item": "Nina's FAA certification", "status": "in progress"},
        {"item": "First drone footage", "status": "in progress"},
        {"item": "CV model training", "status": "in progress"},
    ],
}


def log(week):
    for thread, items in week.items():
        print(f"\n{thread.upper().replace('_', ' ')}")
        for i in items:
            print(f"  - {i['item']} ({i['status']})")


if __name__ == "__main__":
    log(WEEK)
