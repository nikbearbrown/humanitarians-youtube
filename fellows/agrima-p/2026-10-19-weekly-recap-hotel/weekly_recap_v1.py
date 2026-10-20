WEEK = [
    {"item": "Published 'The Hotel Phone Gets a Helper' on Substack",
     "where": "AI voice assistants and front desk teams"},
    {"item": "Attended Homes of Hope meetings",
     "where": "a project supporting girls in India"},
    {"item": "Drafted documentary promotion strategies -- with Yatra",
     "where": "a first draft"},
    {"item": "Produced two Brutalist videos (16:9 + 9:16 each)",
     "where": "four files: the hotel video and this recap"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
