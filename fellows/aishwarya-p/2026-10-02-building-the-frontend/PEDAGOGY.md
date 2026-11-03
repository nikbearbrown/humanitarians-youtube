# PEDAGOGY — Building the Frontend (patent agent progress video 9)

A progress-recap video documenting the React frontend built on top of the FastAPI backend, and a real configuration bug found and fixed along the way: a `.env` file that was never actually loaded because nothing in the codebase called `load_dotenv()`.

## Act structure

- B00A presenter intro ✓
- B00 cold open — the real anomaly (a config file sitting unused since day one) ✓
- B01 — the real motivation (API required knowing the exact URL/query string; frontend makes it usable by anyone) ✓
- B02 — the real design discipline (built against the actual JSON response shape, both classify states, not assumptions) ✓
- B03 — the real bug (`.env` present, never loaded — no `python-dotenv` import, no `load_dotenv()` call) ✓
- B04 — the real fix (one import, one function call) ✓
- B04B — real screen recording of the actual working UI, not animated — genuine evidence the fix and the frontend work together ✓
- B05 — HANDOFF, a concrete, checkable habit (verify `.env` files are actually loaded before shipping) ✓
- B06 — OUTRO ✓

## Evidence discipline

| Claim | Source | Verdict |
|---|---|---|
| ".env file never loaded — no python-dotenv, no load_dotenv()" | Directly inspected `api.py` imports (lines 13–22) in this session; confirmed absent | OK — directly observed, not inferred |
| "every session, manual export was the only reason it worked" | Directly experienced by presenter across prior sessions (export in one terminal tab, uvicorn in another, auth failing) | OK — presenter's own real experience |
| UI demo showing real `scope_readings` output | Presenter's own 15-second screen recording of the actual running app | OK — real footage, not staged or animated |

## Friction protected

- Kept: B04B is explicitly marked as real footage in the beat sheet, not a Manim-animated recreation — the video does not imply the UI demo is simulated.
- Kept: B03 attributes the bug to the actual code (absence of `load_dotenv()`), not to the `.env` file itself being wrong — the file was fine; nothing read it.

VERDICT: PASS
