# FACTCHECK — How Coding Agents Navigate Code

Status: claims checked by Claude Code against the primary sources in SOURCES.md. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Sign-off: I, Likhith, reviewed the 16:9 and 9:16 review cuts and approve the claims above as spoken and shown. I'm signing off for the final master.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B01 | An agent doesn't read everything and guess; it searches, edits small, tests, retries | PASS | Claude Code docs (agentic search, Edit, Bash); best-practices post | — |
| 2 | B03 | Step 1: lists folders and files to map the project first | PASS | docs: file-pattern search / listing tools; evidence `find` output | — |
| 3 | B04 | Step 2: searches a keyword from the bug, opens only matches | PASS | docs: content search (grep); evidence: 6 hits in 3 of 9 files | "opens only the matches" = reads are search-driven |
| 4 | B05 | Step 3: one line changes, the rest stays | PASS | Claude Code Edit = exact string replacement; evidence: 1 line changed, 9 untouched | demo-specific wording on screen |
| 5 | B06 | Step 4: runs the test suite; one test fails | PASS | evidence: `..F.` 1 failed, 3 passed, `assert 16.9915 == 16.99` | — |
| 6 | B07 | Step 5: reads failure, adds rounding, reruns, four pass, no human | PASS | evidence: second edit → 4 passed; scripted replay, no human input | labelled real output of a replay |
| 7 | B08 | The loop lets an agent work largely on its own | PASS | "Building effective agents": environment feedback each step | "largely" kept |
| 8 | B09 | Only as good as the tests; a person still reviews | PASS | caveat (de-sensationalising) | added on verdict card |
