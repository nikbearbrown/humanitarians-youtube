WEEK = [
    {"item": "Published 'Rescue, Reinvented' on Substack",
     "where": "AI's real impact in animal shelters"},
    {"item": "Produced two Brutalist videos (16:9 + 9:16)",
     "where": "the rescue-work explainer + this recap"},
    {"item": "New project idea: a 'cat bot' -- research started",
     "where": "from this week's meetings"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
