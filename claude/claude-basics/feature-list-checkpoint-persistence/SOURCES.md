# SOURCES — feature-list-checkpoint-persistence

Every on-screen claim, number, and code snippet mapped to its source.

## Core facts

| Claim | Value | Source |
|---|---|---|
| 200 features total | exact per card | video-ideas.md Candidate 4 example seed |
| Session 1 implements features 1–50 | exact per card | same |
| Session 2 reads file, starts at feature 51 | exact per card | same |
| Session 2 completes features 51–100 | exact per card | same |
| feature_list.json structure: [{id, status}] | per card | autonomous-coding/progress.py — `count_passing_tests()` reads `feature_list.json` |
| `passes` field (boolean) | per source | autonomous-coding/progress.py — `test.get("passes", False)` |
| Git as immutable ledger | per card | autonomous-coding/autonomous_agent_demo.py context |

## Beat-level citations

- B02 code snippet: adapted from progress.py pattern — `json.load(open('feature_list.json'))`, `next(f for f in features if not f['passes'])`
- B03 session boundary: 1–50 / 51–100 split from the card's example seed exactly

Source credit shown on screen: "Source: Claude Quickstarts (Anthropic)"
