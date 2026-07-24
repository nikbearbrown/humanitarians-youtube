# PEDAGOGY — claude-liam-skill-creator

Skill: `skill-creator` · Modifier: `skill-teardown`

## PREDICT (viewer question before watching)
"Isn't creating a skill just writing a good prompt? Why does it need its own workflow?"

## What the viewer will learn
1. Skill creation is a scientific loop: draft → parallel test runs (with-skill vs baseline) → quantitative grader → human review via built eval viewer → iterate
2. Description optimization is a separate phase: generate trigger evals, run an optimization loop, and update the frontmatter `description` field for better triggering accuracy
3. The skill handles Claude.ai, Claude Code, and Cowork environments differently — the core loop is the same, but subagent availability changes the mechanics

## CONFIRM (what the reel reveals)
- TRIGGER: "I want to make a skill for X", "turn this into a skill", "improve this skill", "run evals"
- 5 stages: Capture Intent → Interview & Research → Write SKILL.md → Test & Grade (eval viewer) → Improve & Repeat
- Eval architecture: spawn with-skill AND baseline runs in the same turn — parallel, honest comparison
- Viewer: `generate_review.py` → Outputs tab (qualitative) + Benchmark tab (quantitative assertions)
- Description optimization: trigger eval set (20 queries, should/should-not trigger) → `run_loop.py` → best_description

## LAWS CHECKED
- ✅ TRIGGER is clear: "make a skill" / "improve this skill" / "run evals"
- ✅ SELF-DEMO: B02 shows the eval architecture verbatim from SKILL.md
- ✅ HANDOFF LAW: BHTF narration reads prompt aloud AND explains what to watch for
- ✅ ILLUSTRATE LAW: UI only at B00 and BHTF bookends
- ✅ ASK→RESULT law: B00 shows ask + TRIGGER + result

## VERDICT: PASS
