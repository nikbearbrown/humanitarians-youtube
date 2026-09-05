# Self-Check Isn't Verification — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Behind the Model
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Manim, Remotion). No AI-generated video or imagery.

## Title

Self-Check Isn't Verification — Why Claude Checking Its Own Work Isn't Enough

## Description

Ask Claude for a five-claim research summary, one citation per claim — then ask it to
self-check each claim against the source it just cited. The first pass comes back clean:
all five, verified. That looks like verification. It isn't. Swap claim three's citation for
a paper that doesn't actually support it and rerun the self-check — it still comes back
"verified," because the check reasons from the same claim it's supposed to be testing, not
from the paper itself. Only opening the actual paper catches the mismatch, immediately.

From Humanitarians AI: short, plain explanations of how Claude actually works, for a general
audience meeting Claude for the first time. Liam, in for Professor Bear.

In this one: the natural assumption that a clean self-check settles the matter; the anchor
example — a five-claim table, self-checked twice; the planted citation swap that a self-check
misses but an outside check catches instantly; both directions — catching one wrong citation
doesn't mean every claim got equal scrutiny, and a clean self-check elsewhere isn't proof
either; and the carry-out: a self-check can only confirm what it already believes —
verification means checking against a source the agent never wrote.

Try it yourself — the video ends with a paste-ready prompt for running this exact test on
your own Claude output.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/behind-the-model--claude-liam-self-check-vs-independent-verification

This is an educational explainer, not sponsored by or affiliated with Anthropic.

## Tags

Claude, Claude AI, Anthropic, agentic AI, AI verification, self-check vs verification, AI
agent supervision, AI safety, model behavior, AI basics, Humanitarians AI, prompt engineering,
AI for beginners, Claude tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — is a self-check verification, or just a first pass?
0:10 The anchor — five claims, self-checked, all come back clean
0:22 The natural guess — three passes over the same material looks like verification
0:31 The break — swap one citation for a paper that doesn't support it; still "verified"
0:44 The independent check — opening the actual paper catches it immediately
0:57 Direction A — catching one error doesn't mean every claim got equal scrutiny
1:08 Direction B — the anchor returns: checked for real, only the planted error diverges
1:21 Carry-out
1:28 Your turn
1:44 Outro
