"""weekly_recap_v2.py -- same week, tagged by category with a shipped-count."""

WEEK = [
    {"category": "Writing", "item": "Published \"The AI That Never Forgets\" on Substack"},
    {"category": "Video", "item": "Produced four Brutalist videos (16:9 + 9:16 each)"},
    {"category": "Meetings", "item": "Attended this week's team meeting"},
]


def log():
    print(f"This week: {len(WEEK)} things shipped")
    for entry in WEEK:
        print(f"  [{entry['category']}] {entry['item']}")


if __name__ == "__main__":
    log()
