WEEK = [
    {"item": "Published 'The Tutor They Never Had' on Substack",
     "where": "AI tutoring for kids who have never had extra help"},
    {"item": "Produced four Brutalist videos (16:9 + 9:16 each)",
     "where": "planning, review, approvals, export"},
    {"item": "Guest lecture on Humanitarians AI -- with Yatra",
     "where": "presentation finished; lecture is Tuesday"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
