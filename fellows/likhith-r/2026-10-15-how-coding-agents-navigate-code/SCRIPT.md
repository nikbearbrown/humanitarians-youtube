# SCRIPT — How Coding Agents Navigate Code

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about how AI coding agents navigate a codebase.

**B01 · BLUF** — Here's the whole idea. A coding agent doesn't read everything and guess. It searches first, makes a small edit, tests the fix, and tries again until the tests pass. That's the loop.

**B02 · HOOK** — A bug, in code the agent has never seen. Where does it even look?

**B03 · EXPLORE** — Step one: explore. It lists folders and files to map the project first.

**B04 · SEARCH** — Step two: targeted reading. It searches a keyword from the bug, and opens only the matches.

**B05 · EDIT** — Step three: a scoped edit. One line changes. The rest stays.

**B06 · VERIFY** — Step four, verify. It runs the test suite. One test still fails.

**B07 · ITERATE** — Step five: iterate. It reads the failure, adds rounding, reruns. Four pass, no human needed.

**B08 · LOOP** — That's the loop: explore, edit, verify, iterate. It's how an agent works largely on its own.

**B09 · VERDICT** — It's not knowing the code. It's the loop, and it's only as good as the tests.

**B10 · YOUR_TURN** — Your turn. Ask your agent: before you change anything, show me how you'd explore this repo and which tests prove the fix. Then watch it search first.

**B11 · OUTRO** — How coding agents navigate code. At Humanitarians A I.
