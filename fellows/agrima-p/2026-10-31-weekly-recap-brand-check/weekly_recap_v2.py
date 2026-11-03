WEEK = [
    {"role": "author", "part": "1. Writing",
     "item": "Weekly article on Substack: 'Have You Asked the Chatbot About Your Brand Lately?'"},
    {"role": "producer", "part": "2. Video production",
     "item": "Two Brutalist videos, each in 16:9 and 9:16: four files"},
    {"role": "support", "part": "3. Homes of Hope documentary",
     "item": "Poster design, with Yatra"},
    {"role": "organizer", "part": "4. Organizing the work",
     "item": "AI videos on GitHub; the week's videos on Drive"},
]


def log():
    for entry in WEEK:
        print(f"[{entry['role'].upper()}] {entry['part']}: {entry['item']}")
    support = [e for e in WEEK if e["role"] == "support"]
    print(f"{len(WEEK)} parts done, {len(support)} in a supporting role")


if __name__ == "__main__":
    log()
