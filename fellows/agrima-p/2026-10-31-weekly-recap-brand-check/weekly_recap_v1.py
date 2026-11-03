WEEK = [
    {"part": "1. Writing",
     "item": "Published my weekly article on Substack: 'Have You Asked the Chatbot About Your Brand Lately?'"},
    {"part": "2. Video production",
     "item": "Two Brutalist videos (AI topic + weekly recap), each in 16:9 and 9:16: four files"},
    {"part": "3. Homes of Hope documentary",
     "item": "Helped Yatra with the poster design"},
    {"part": "4. Organizing the work",
     "item": "AI videos pushed to GitHub; the week's videos attached on Drive"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['part']}: {entry['item']}")


if __name__ == "__main__":
    log()
