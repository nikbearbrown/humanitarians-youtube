WEEK = [
    {"status": "published", "part": "1. Writing",
     "item": "Weekly article on Substack: 'Your Foundation Search Is Doing Market Research'"},
    {"status": "produced", "part": "2. Video production",
     "item": "Two Brutalist videos, each in 16:9 and 9:16: four files"},
    {"status": "ongoing", "part": "3. Homes of Hope documentary",
     "item": "Posting and outreach, with Yatra"},
    {"status": "saved", "part": "4. Organizing the work",
     "item": "All project files on GitHub"},
]


def log():
    for entry in WEEK:
        print(f"[{entry['status'].upper()}] {entry['part']}: {entry['item']}")
    ongoing = [e for e in WEEK if e["status"] == "ongoing"]
    print(f"{len(WEEK) - len(ongoing)} parts done, {len(ongoing)} ongoing")


if __name__ == "__main__":
    log()
