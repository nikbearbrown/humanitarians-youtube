# Solve-Verify Asymmetry — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Behind the Model
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Manim, Remotion). No AI-generated video or imagery.

## Title

Solve-Verify Asymmetry — Why Checking an AI's Answer Can Cost More Than Getting It

## Description

An AI can produce an answer in seconds. Checking that answer is correct is a
different story — for hard problems, a strict, deterministic check can take
three to a hundred times longer than the answer did, and the gap grows with
difficulty. It isn't a measurement quirk: one suspiciously low number (a
simple-arithmetic ratio that looked too small) traced back to a hidden
checker-startup cost — once removed, arithmetic ties out close to parity while
every harder ratio holds exactly where it was. A faster model doesn't close
that gap. It can widen it: more candidate answers arrive per second, and each
one still needs the same expensive check.

From Humanitarians AI: short, plain explanations of how Claude actually works,
for a general audience meeting Claude for the first time. Liam, in for
Professor Bear.

In this one: the natural assumption that checking should be about as fast as
solving; a ten-problem timed experiment that breaks it (arithmetic, algebra,
quadratic, combinatorics — and a full proof sketch, off the chart); the rigor
check that rules out a stopwatch artifact; and the two-sided limit of the
result — a big ratio doesn't mean the answer was wrong, and a faster model
doesn't shrink the gap, it just produces more answers that still need checking.

Try it yourself — the video ends with a paste-ready prompt for measuring the
solve-verify gap in your own AI workflow.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/behind-the-model--claude-liam-solve-verify-asymmetry

This is an educational explainer, not sponsored by or affiliated with Anthropic.

## Tags

Claude, Claude AI, Anthropic, AI verification, AI reasoning, LLM evaluation, AI
safety, model behavior, AI basics, Humanitarians AI, prompt engineering, AI for
beginners, Claude tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — is checking fast, or harder?
0:11 The ratio ladder — solve time vs. check time, by difficulty
0:27 The natural guess — confirming should be as fast as solving
0:34 The break — three to a hundred times longer, not the same
0:50 Is the gap real, or the stopwatch? — the rigor check
1:07 A ratio only measures the cost to confirm
1:17 The ladder, corrected — plus a proof sketch, off the chart
1:37 Carry-out
1:44 Your turn
2:02 Outro
