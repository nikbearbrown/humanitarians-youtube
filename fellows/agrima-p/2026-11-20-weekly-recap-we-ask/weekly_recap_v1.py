WEEK = [
    {"part": "1. Writing",
     "item": "Published my weekly article on Substack: 'We Ask the AI Now'"},
    {"part": "2. Video production",
     "item": "Two Brutalist videos (AI topic + weekly recap), each in 16:9 and 9:16: four files"},
    {"part": "3. Weekly meeting",
     "item": "Attended the weekly team meeting"},
    {"part": "4. Homes of Hope",
     "item": "Continued my work on the documentary project with Yatra"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['part']}: {entry['item']}")


if __name__ == "__main__":
    log()
