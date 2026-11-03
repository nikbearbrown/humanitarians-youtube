"""weekly_log_v2.py — Claude Code output (revision).

Turns the dump into an actual log: a standout line per thread (this
week's real headline), then every item in order with its real status.
Still every entry, still every real status — just readable.
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
        standout = next(i for i in items if i["status"] in ("done", "published"))
        print(f"  * highlight: {standout['item']}")
        for i in items:
            print(f"  - {i['item']} ({i['status']})")


if __name__ == "__main__":
    log(WEEK)
