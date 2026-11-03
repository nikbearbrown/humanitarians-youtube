"""weekly_recap_v2.py — same week, split into DONE vs STARTING NEXT."""

DONE = [
    {"item": "Published the AI nonprofit marketing article, with research behind it", "where": "published this week"},
    {"item": "Produced the accompanying Brutalist video (16:9 + 9:16)", "where": "brutalist.art"},
]

NEXT = [
    {"item": "Suffolk University talk, with Yatra", "where": "this Wednesday"},
]


def log():
    print("DONE THIS WEEK")
    for entry in DONE:
        print(f"  - {entry['item']}  ({entry['where']})")
    print("STARTING NEXT WEEK")
    for entry in NEXT:
        print(f"  - {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
