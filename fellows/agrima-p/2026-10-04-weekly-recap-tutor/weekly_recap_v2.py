DONE = [
    {"item": "Published 'The Tutor They Never Had' on Substack",
     "where": "AI tutoring for kids who have never had extra help"},
    {"item": "Produced four Brutalist videos (16:9 + 9:16 each)",
     "where": "planning, review, approvals, export"},
    {"item": "Finished the guest-lecture presentation",
     "where": "Humanitarians AI, with Yatra"},
]

NEXT = [
    {"item": "Deliver the guest lecture at a college -- Tuesday",
     "where": "alongside Yatra"},
]


def log():
    print("DONE THIS WEEK")
    for entry in DONE:
        print(f"- {entry['item']}  ({entry['where']})")
    print("NEXT")
    for entry in NEXT:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
