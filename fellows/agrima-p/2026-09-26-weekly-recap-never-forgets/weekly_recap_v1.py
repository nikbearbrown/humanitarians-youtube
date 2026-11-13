"""weekly_recap_v1.py -- log this week's real work, one flat list."""

WEEK = [
    {"item": "Published \"The AI That Never Forgets\" on Substack", "where": "substack.com"},
    {"item": "Produced four Brutalist videos (16:9 + 9:16 each)", "where": "brutalist.art"},
    {"item": "Attended this week's team meeting", "where": "weekly sync"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
