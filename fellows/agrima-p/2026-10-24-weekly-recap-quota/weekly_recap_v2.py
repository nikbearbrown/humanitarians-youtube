WEEK = [
    {"role": "author",
     "item": "'The AI Colleague With a Quota' on Substack",
     "where": "AI agents on sales teams"},
    {"role": "attendee",
     "item": "Homes of Hope documentary meetings",
     "where": "a project supporting girls in India"},
    {"role": "support",
     "item": "Social media strategy for the documentary -- with Yatra",
     "where": "a supporting role"},
    {"role": "producer",
     "item": "Two Brutalist videos (16:9 + 9:16 each)",
     "where": "four files: the sales-AI video and this recap"},
]


def log():
    for entry in WEEK:
        print(f"[{entry['role'].upper()}] {entry['item']}  ({entry['where']})")
    support = [e for e in WEEK if e["role"] == "support"]
    print(f"{len(WEEK)} things done, {len(support)} in a supporting role")


if __name__ == "__main__":
    log()
