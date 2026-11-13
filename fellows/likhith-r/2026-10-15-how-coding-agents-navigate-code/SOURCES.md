# SOURCES — How Coding Agents Navigate Code

Brief supplied by the requester (Likhith): 7 points (hook, explore, targeted reading, scoped edits, verify, iterate, close). Checked 2026-10-21 against:

- Anthropic, Claude Code docs: overview and tools reference (agentic search over the repo with file-pattern and content search, Read, exact-string Edit, Bash for running tests). https://docs.anthropic.com/en/docs/claude-code/overview
- Anthropic Engineering, "Claude Code: Best practices for agentic coding" (explore → plan → code → commit; write tests, then iterate until they pass). https://www.anthropic.com/engineering/claude-code-best-practices
- Anthropic Engineering, "Building effective agents" (agents get "ground truth" from the environment at each step, e.g. tool results and code execution, and loop on it). https://www.anthropic.com/engineering/building-effective-agents
- These links were not re-fetched in this session. The reviewer should open them once before sign-off.

## Executable evidence
- `evidence/agent_loop.py` → `evidence/agent_loop.out.txt`. It builds a toy shop repo (6 source files, 3 test files, 4 tests) in a temp dir and replays the agent's tool calls: `find`, `grep -rn 'discount'`, read lines 4–6, exact-string edit, `pytest -q` (1 failed, 3 passed: `assert 16.9915 == 16.99`), a second edit adding `round(…, 2)`, `pytest -q` (4 passed).
- Run with `uv run --no-project --with "pytest==8.3.3" python -I evidence/agent_loop.py` (throwaway env, not a toolkit dependency).
- B03–B08 show this output verbatim. It is a **scripted replay** of the tool calls, not a live model session. The on-screen caption says "real output · toy shop repo".

## Corrections / de-sensationalising
- "Largely on its own" is kept, and not upgraded to "on its own". The verdict card adds that a person still reviews the change, and that the loop is only as good as the tests.
- "Rather than reading every file" does not mean the agent never reads broadly. It means reads are driven by search results. B04 shows 3 of 9 files matching and only one opened.
- Exact-string replacement (match once, replace) describes Claude Code's Edit tool. Other agents use patches or diffs. B05's note says "replace one exact string, matched once" for the demo.
- No model names, version numbers or benchmark scores, so the video won't date.
