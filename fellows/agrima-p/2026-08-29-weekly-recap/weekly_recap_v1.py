"""weekly_recap_v1.py — log this week's real work, one flat list."""

WEEK = [
    {"item": "Published the AI nonprofit marketing article, with research behind it", "where": "published this week"},
    {"item": "Produced the accompanying Brutalist video (16:9 + 9:16)", "where": "brutalist.art"},
    {"item": "Suffolk University talk, with Yatra", "where": "this Wednesday"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
