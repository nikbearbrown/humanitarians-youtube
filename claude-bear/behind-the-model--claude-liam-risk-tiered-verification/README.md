# Reading Isn't Reviewing — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Behind the Model
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Manim, Remotion). No AI-generated video or imagery.

## Title

Reading Isn't Reviewing — Build a Risk-Tiered Verification Checklist with Claude

## Description

Claude can hand you a citation, a number, a chart, code, or a recommendation — and every
one of those can be wrong in a way that reads perfectly clean. The natural instinct is
that a careful read-through counts as a review. It doesn't: a fabricated citation,
formatted exactly like a real one, passes every read-through. Only opening the actual
source catches it.

The fix isn't reading more carefully — it's a small tool. `verification_gate.py` takes an
output type and a risk level and prints back three to five concrete, checkable steps,
tailored to the combination: a citation always includes opening the source, a number at
strict risk always includes an independent recalculation, a chart always gets its axis
labels and denominator checked. Add a `--log` flag and the completed checklist writes out
as a timestamped markdown record that travels with the output.

From Humanitarians AI: short, plain explanations of how Claude actually works, for a
general audience meeting Claude for the first time. Liam, in for Professor Bear.

In this one: why "looks right" isn't the same thing as "reviewed"; how a risk-tiered
checklist turns a feeling into a protocol; the one flag worth knowing (a checklist only
works if every step stays genuinely checkable); and both directions — what a completed
checklist proves, and what a single failed step does not.

Try it yourself — the video ends with a paste-ready prompt for building your own
risk-tiered verification checklist.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/behind-the-model--claude-liam-risk-tiered-verification

This is an educational explainer, not sponsored by or affiliated with Anthropic.

## Tags

Claude, Claude AI, Anthropic, AI verification, AI auditing, prompt engineering, AI
literacy, AI basics, Humanitarians AI, fact-checking AI, AI for beginners, Claude tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — if it looks right, have I reviewed it?
0:09 Five outputs, one question
0:22 The natural guess
0:33 THE ANCHOR — a clean-reading fake
0:47 A tool, not a feeling
0:59 Every combination has its own rule
1:15 Three genuinely different depths
1:29 One flag — still checkable?
1:40 The record, then both directions — the anchor returns
2:02 Carry-out
2:09 Your turn
2:29 Outro
