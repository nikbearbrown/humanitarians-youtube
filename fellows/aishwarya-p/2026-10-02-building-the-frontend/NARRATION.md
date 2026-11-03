# Video 9: Building the Frontend — Narration Draft

## B00A — Presenter intro
Hi, I'm Aishwarya
from the Mycroft team.
This video covers building a real React frontend on top of last week's API, and a real config bug that had been sitting there the whole time.

## B00 — Cold open
One file sat in the project folder since the very beginning. It had the key in it the whole time. Nothing was ever reading it.

## B01 — Why a frontend
The API worked, but only if you knew the exact URL and query string to type into a browser or curl. One input, one toggle, one button — the same real claims and lineage data, readable by anyone, not just someone who remembers the endpoint shape.

## B02 — Building against the real shape, not a guess
Method: design the screen from the actual JSON the API returns, not from assumptions. Tested against both the classify-off response (claim counts, citation counts) and the classify-on response (the real scope reading — claim, breadth, posture, and the model's own confidence caveat) before writing a single line of the result view.

## B03 — The real bug
A `.env` file with the Anthropic key had been sitting in the backend folder since day one. The code never actually loaded it — no `python-dotenv`, no `load_dotenv()` call anywhere. Every session, the only reason it worked was a manual `export` in the terminal, which silently stopped working the moment that terminal tab closed.

## B04 — The real fix
One import, one function call: `load_dotenv()` at the top of `api.py`. Now the key loads from the file itself, every session, no manual export, no silent failure the next time a terminal tab closes.

## B04B — UI Demo
Same backend, now with a real screen instead of a URL. Classify on, and the real scope reading comes back — right there, instead of in a terminal.

## B05 — Handoff
Your turn: if a project has a `.env` file, check that something in the code actually calls `load_dotenv()` — a config file nobody reads is worse than no config file, because it looks like it should be working.

## B06 — Outro
