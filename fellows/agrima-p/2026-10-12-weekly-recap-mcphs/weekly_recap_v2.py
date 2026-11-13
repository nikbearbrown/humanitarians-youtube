WEEK = [
    {"tag": "WRITING",
     "item": "Published 'AI Done Right' on Substack",
     "where": "what nonprofits built around AI can teach us"},
    {"tag": "VIDEO",
     "item": "Produced two Brutalist videos (16:9 + 9:16 each)",
     "where": "four files: the article video and this recap"},
    {"tag": "SPEAKING",
     "item": "Guest lecture on Humanitarians AI at MCPHS",
     "where": "built the full presentation with Yatra Rawat"},
]


def log():
    for entry in WEEK:
        print(f"[{entry['tag']}] {entry['item']}  ({entry['where']})")
    print(f"{len(WEEK)} things shipped this week")


if __name__ == "__main__":
    log()
