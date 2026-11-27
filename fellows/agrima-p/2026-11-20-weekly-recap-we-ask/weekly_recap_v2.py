WEEK = [
    {"status": "published", "part": "1. Writing",
     "item": "Substack article: 'We Ask the AI Now'"},
    {"status": "produced", "part": "2. Video production",
     "item": "Two Brutalist videos, each in 16:9 and 9:16: four files"},
    {"status": "attended", "part": "3. Weekly meeting",
     "item": "Weekly team meeting"},
    {"status": "ongoing", "part": "4. Homes of Hope",
     "item": "Promotion and outreach, with Yatra"},
]


def log():
    for entry in WEEK:
        print(f"[{entry['status'].upper()}] {entry['part']}: {entry['item']}")
    ongoing = [e for e in WEEK if e["status"] == "ongoing"]
    print(f"{len(WEEK) - len(ongoing)} parts done, {len(ongoing)} ongoing")


if __name__ == "__main__":
    log()
