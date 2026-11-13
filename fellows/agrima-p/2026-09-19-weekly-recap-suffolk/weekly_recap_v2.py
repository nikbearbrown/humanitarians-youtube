DONE = [
    {"item": "Published 'No Face, No Problem' on Substack",
     "where": "faceless AI accounts, and why we trust them"},
    {"item": "Produced four Brutalist videos (16:9 + 9:16 each)",
     "where": "full pipeline: kickoff, plan review, approvals"},
]

NEXT = [
    {"item": "Suffolk University guest lecture -- with Yatra",
     "where": "presentation still being built"},
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
