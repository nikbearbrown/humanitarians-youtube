WEEK = [
    {"item": "Published 'No Face, No Problem' on Substack",
     "where": "faceless AI accounts, and why we trust them"},
    {"item": "Produced four Brutalist videos (16:9 + 9:16 each)",
     "where": "full pipeline: kickoff, plan review, approvals"},
    {"item": "Suffolk University guest lecture -- with Yatra",
     "where": "meetings + building the presentation"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
