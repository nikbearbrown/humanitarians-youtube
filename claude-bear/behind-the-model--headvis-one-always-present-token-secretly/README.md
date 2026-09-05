# Why One Always-Present Token Secretly Hijacks Every Attention Statistic — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Behind the Model
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Manim, Remotion). No AI-generated video or imagery.

## Title

Why One Always-Present Token Secretly Hijacks Every Attention Statistic

## Description

Attention weights have to sum to one on every single row, whether or not any
position actually deserves the mass. Look at one real head — layer four, head
three, across fifty thousand sentences — and token zero, the sentence-start
marker, wins the max-attention position in 91% of them, with more than half
the weight every time. It isn't a discovery about meaning: token zero is
present in every sequence and carries no sentence-specific content, so it's
the cheapest place for a head to park leftover attention when nothing else is
strongly preferred. Any statistic built from the max — "which position gets
the most attention" — reports that sink, not the sentence structure you
actually wanted to see. In a worked example, the real verb-to-subject
dependency only shows up once the sink position is excluded from the count.

From Humanitarians AI: short, plain explanations of how Claude actually works,
for a general audience meeting Claude for the first time. Liam, in for
Professor Bear.

In this one: the natural assumption that a position winning the attention max
almost every time must be carrying real meaning; the mechanism that breaks
it (softmax must spend its mass somewhere, and an always-present, meaning-
empty token is the low-resistance seat); a worked example with the raw
numbers; and the two-sided limit of the result — a dominant sink doesn't mean
a head learned nothing, and a head that avoids one sink token may just be
parking on a different one.

Try it yourself — the video ends with a paste-ready prompt for checking
whether a position dominating your own attention statistics is a real signal
or a sink.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/behind-the-model--headvis-one-always-present-token-secretly

This is an educational explainer, not sponsored by or affiliated with Anthropic.

## Tags

Claude, Claude AI, Anthropic, attention mechanism, transformer internals,
attention sink, AI interpretability, LLM internals, AI basics, Humanitarians
AI, AI for beginners, Claude tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — signal, or sink?
0:09 The attention heatmap — one head, fifty thousand sentences
0:27 The natural guess — it must be the real signal
0:40 The break — softmax has to spend its mass somewhere
0:58 The worked example — raw weights, then excluded
1:18 The sink doesn't erase the row
1:30 Masked — the real patterns light up
1:50 Carry-out
2:00 Your turn
2:20 Outro
