WEEK = [
    {"item": "Published 'AI Done Right' on Substack",
     "where": "what nonprofits built around AI can teach us"},
    {"item": "Produced two Brutalist videos (16:9 + 9:16 each)",
     "where": "four files: the article video and this recap"},
    {"item": "Guest lecture on Humanitarians AI at MCPHS",
     "where": "built the full presentation with Yatra Rawat"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['item']}  ({entry['where']})")


if __name__ == "__main__":
    log()
