# SOURCES — Background AI Agents: How AI Works While You Don't

**Source script:** supplied by Yeshwanth Balaji on 2026-11-10 (topic, audience, learning goals, five sections, recap, closing, four required visuals). It was fact-checked and rewritten in the Teardown register, not read verbatim.

## Corrections and changes to the supplied script

| Where | Supplied | Film | Why |
|---|---|---|---|
| Hook | "one of the biggest AI trends of 2026" | "one of the biggest in AI right now" | DOUBLE-CHECK LAW: strip what dates the film; "biggest trend" is opinion, not a measured fact |
| Section 3 | "3D/game asset work" | "a batch of game assets" | Plainer for the audience; same meaning |
| Section 2 | the loop as four steps | four steps, plus "a well-built agent caps the loop with a step limit or a budget" | Phrased as design guidance, not as a claim that every agent product does this |
| Section 4 | "agents can be tricked by malicious content (prompt injection)" | kept, plus a labelled illustrative example (B08) | The term needed a concrete picture for this audience |
| Added | — | B04 worked run, B06 "What You Come Back To", B10 "Hand It Off, or Keep It?" | Worked example, review literacy, and when *not* to delegate (the skill's teaching-arc checklist) |

## Executable evidence (B00, B04, B06)

`demo-repo/` is a three-test Python repository written for this film. Every output line on screen in B04 and B06 is copied from a real run on this machine:

- `evidence-run1.txt`: `python3 -m unittest -v` before the fix: 1 of 3 failing, `(2026, 1, 3) != (2026, 3, 1)`.
- `evidence-fix.diff`: the one-line fix (`year, day, month` → `year, month, day`).
- `evidence-run2.txt`: the same command after the fix: `Ran 3 tests … OK`.
- `evidence-unchecked.txt`: what the fixed parser still does not check: `"2026-02-30"` is accepted, `"20260301"` raises `ValueError`.

**What is reconstructed:** the agent session around those outputs. The fix was applied by a script during the film build, not by an AI agent running in the background. B04’s on-screen note says "Reconstructed session · real test output from demo-repo". B00's composer is labelled illustrative.

**B08 is illustrative only:** no real repository, issue or attack. Its on-screen note says "Illustrative · not a real repository or attack".

## Background references (well-established; cited from knowledge, not re-fetched for this film)

- **The agent loop** (reason → act with a tool → observe → repeat): Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models* (2022, arXiv:2210.03629). The film uses the plain four-step version from the supplied script.
- **Prompt injection:** OWASP Top 10 for LLM Applications, LLM01 "Prompt Injection". "A model can't always tell data from instructions" is the standard framing of why it works.
- **Least privilege:** Saltzer and Schroeder, *The Protection of Information in Computer Systems* (1975).

No product names, version numbers, prices or usage statistics appear in the film.

## Tools

Kokoro `am_onyx` (local, speed 0.95; narrating as Yeshwanth Balaji), faster-whisper word alignment (`runtime/scripts/align.py`), Remotion 4.0.535, ffmpeg, Python 3.14. No paid calls, nothing published.
