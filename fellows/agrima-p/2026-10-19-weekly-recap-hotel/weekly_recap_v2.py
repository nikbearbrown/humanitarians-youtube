WEEK = [
    {"status": "published",
     "item": "'The Hotel Phone Gets a Helper' on Substack",
     "where": "AI voice assistants and front desk teams"},
    {"status": "attended",
     "item": "Homes of Hope meetings",
     "where": "a project supporting girls in India"},
    {"status": "first draft",
     "item": "Documentary promotion strategies -- with Yatra",
     "where": "a first draft"},
    {"status": "produced",
     "item": "Two Brutalist videos (16:9 + 9:16 each)",
     "where": "four files: the hotel video and this recap"},
]


def log():
    for entry in WEEK:
        print(f"[{entry['status'].upper()}] {entry['item']}  ({entry['where']})")
    drafts = [e for e in WEEK if e["status"] == "first draft"]
    print(f"{len(WEEK) - len(drafts)} finished, {len(drafts)} first draft")


if __name__ == "__main__":
    log()
