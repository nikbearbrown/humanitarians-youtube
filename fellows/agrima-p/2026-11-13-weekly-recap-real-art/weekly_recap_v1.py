WEEK = [
    {"part": "1. Writing",
     "item": "Published a new Substack article: 'Real Art, New Light'"},
    {"part": "2. Video production",
     "item": "Two Brutalist videos (AI topic + weekly recap), each in 16:9 and 9:16: four files"},
    {"part": "3. Organizing the work",
     "item": "Pushed my files to GitHub"},
    {"part": "4. A new project",
     "item": "Went through the CatBot and DogBot proposal at Humanitarians AI"},
]


def log():
    for entry in WEEK:
        print(f"- {entry['part']}: {entry['item']}")


if __name__ == "__main__":
    log()
