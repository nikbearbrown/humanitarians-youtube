# Teaching an AI to Grade Its Own Homework — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Behind the Model
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Manim, Remotion). No AI-generated video or imagery.

## Title

Teaching an AI to Grade Its Own Homework — Constitutional AI's Self-Critique Loop

## Description

Claude is partly trained by critiquing and revising its own harmful answers. If the
same model both answers and grades, isn't that just an AI grading its own homework —
and why would anyone trust the grade? Human harmlessness labeling is expensive,
inconsistent, and doesn't generalize to new harms. Constitutional AI replaces most of
it with a loop: elicit a problematic response, critique it against one specific written
principle from a fixed list of sixteen, revise it to follow that principle, then use the
revision as the training example — AI feedback instead of human feedback.

The result matched human-labeled training on harmlessness and beat it on helpfulness,
because human graders reward caution and over-refuse. And the model can cite the exact
rule it followed — a human grader's gut feeling can't be cited that way.

But two things this doesn't prove: matching on harmlessness doesn't mean the check is
unbiased, since the same model both answers and grades — a shared blind spot isn't
caught by that same model applying the rule to itself. That's flagged by researchers,
not resolved. And beating on helpfulness doesn't mean the model is more correct, only
that it refuses less; telling those apart takes a separate check.

From Humanitarians AI: short, plain explanations of how Claude actually works, for a
general audience meeting Claude for the first time. Liam, in for Professor Bear.

Try it yourself — the video ends with a paste-ready prompt for applying the same
"check against one written rule" idea to something you wrote.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/behind-the-model--constitutional-ai-self-critique

This is an educational explainer, not sponsored by or affiliated with Anthropic.

## Tags

Claude, Claude AI, Anthropic, Constitutional AI, AI safety, RLHF, RLAIF, AI alignment,
Claude Constitution, AI basics, Humanitarians AI, AI for beginners, Claude tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — is self-grading cheating, or checkable?
0:10 Three problems with human labeling
0:27 The natural skepticism — pass itself?
0:39 The written rule — THE ANCHOR
0:53 The four-step loop
1:11 The result — matched, then beat it
1:25 What this doesn't prove — the anchor returns
1:53 Carry-out
2:04 Your turn
2:20 Outro
