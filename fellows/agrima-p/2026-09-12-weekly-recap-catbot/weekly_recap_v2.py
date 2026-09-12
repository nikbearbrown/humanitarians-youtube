DONE = [
    {"item": "Published 'Rescue, Reinvented' on Substack",
     "where": "AI's real impact in animal shelters"},
    {"item": "Produced two Brutalist videos (16:9 + 9:16)",
     "where": "the rescue-work explainer + this recap"},
]

NEXT = [
    {"item": "New project idea: a 'cat bot'",
     "where": "cat-shelter research just starting"},
]


def log():
    print("DONE THIS WEEK")
    for entry in DONE:
        print(f"- {entry['item']}  ({entry['where']})")
    print("STARTING NEXT WEEK")
    for entry in NEXT:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
