# Consensus Isn't Verification — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Behind the Model
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Manim, Remotion). No AI-generated video or imagery.

## Title

Consensus Isn't Verification — Why AI Judges Agreeing Doesn't Prove They're Right

## Description

It's increasingly common to have one AI system check another one's work — grading an
answer, reviewing code, auditing a claim. When several AI reviewers agree, that agreement
gets treated as proof. It feels like getting a second medical opinion. It isn't one.

The test: give an AI judge the same two answers twice, just with the order swapped.
Nothing about the answers changed — but the judge's verdict flips. It picked whichever
answer came first, not whichever was better. That's positional bias, one of three
documented, structural judging biases (position, length, style) that show up whenever an
AI checks another AI's output.

From Humanitarians AI: short, plain explanations of how Claude actually works, for a
general audience meeting Claude for the first time. Liam, in for Professor Bear.

In this one: the basic result that cross-checking only reduces error when the checkers
fail independently; why AI models sharing similar training and tuning share the same
blind spots, so their agreement is evidence of shared priors, not correctness; the fix —
pairing each kind of claim with a check that fails differently (retrieval for facts,
running the code for math, a validator for schema/format); the one flag worth knowing
(a "clean" check can quietly run on the same kind of model underneath); and both
directions — what independent agreement really proves, and what AI-judge agreement
(or disagreement) does not.

Try it yourself — the video ends with a paste-ready prompt for finding correlated-failure
seams in your own AI pipeline.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/behind-the-model--claude-liam-correlated-failure-research

This is an educational explainer, not sponsored by or affiliated with Anthropic.

## Tags

Claude, Claude AI, Anthropic, AI auditing, AI safety, LLM-as-judge, AI evaluation,
AI basics, Humanitarians AI, prompt engineering, AI for beginners, Claude tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — three AI judges agree, is that verified?
0:13 AI checking AI
0:27 The natural guess
0:40 THE ANCHOR — same answers, order swapped
0:53 Three documented biases
1:08 Where agreement actually lives
1:26 Pair with a different failure mode
1:43 One flag — is the check really independent?
1:57 Both directions — the anchor returns
2:17 Carry-out
2:23 Your turn
2:48 Outro
