WEEK = [
    {"item": "Published 'The AI Colleague With a Quota' on Substack",
     "where": "AI agents on sales teams"},
    {"item": "Attended Homes of Hope documentary meetings",
     "where": "a project supporting girls in India"},
    {"item": "Helped Yatra with the documentary's social media strategy",
     "where": "a supporting role"},
    {"item": "Produced two Brutalist videos (16:9 + 9:16 each)",
     "where": "four files: the sales-AI video and this recap"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
