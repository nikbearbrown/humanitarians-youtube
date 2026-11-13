WEEK = [
    {"status": "published", "part": "1. Writing",
     "item": "Substack article: 'Real Art, New Light'"},
    {"status": "produced", "part": "2. Video production",
     "item": "Two Brutalist videos, each in 16:9 and 9:16: four files"},
    {"status": "saved", "part": "3. Organizing the work",
     "item": "Files on GitHub"},
    {"status": "planning", "part": "4. A new project",
     "item": "CatBot and DogBot: an early-stage plan"},
]


def log():
    for entry in WEEK:
        print(f"[{entry['status'].upper()}] {entry['part']}: {entry['item']}")
    planning = [e for e in WEEK if e["status"] == "planning"]
    print(f"{len(WEEK) - len(planning)} parts done, {len(planning)} in planning")


if __name__ == "__main__":
    log()
