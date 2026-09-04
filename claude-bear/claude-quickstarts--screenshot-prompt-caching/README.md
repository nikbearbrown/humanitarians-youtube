# Caching Pixels You've Already Seen.

**Channel:** @HumanitariansAI
**Playlist:** Claude Basics

## Description

If Claude already looked at a screenshot once, does sending it again cost
nothing? It doesn't work that way — and the reason is worth ten seconds to
understand before you build a computer-use agent.

A 50-turn computer-use task takes a screenshot every turn. Most of the time
nothing has moved — a dialog is still open, a progress bar is still
crawling — but the API tokenizes the identical image again anyway, at
roughly 2,000 tokens each. In a worked case with only 5 unique desktop
states across those 50 turns, that's 100,000 tokens billed to describe a
screen that only actually changed 5 times. One field fixes it:
`cache_control: {"type": "ephemeral"}` on the image block. Flag it once, and
every identical repeat becomes a cache hit — 10,000 tokens instead of
100,000, a 90% cut. It's requested, not automatic, and it only lasts until
the picture or the session changes.

This is Professor Bear's Claude-basics series, narrated by Liam — one real
question, answered simply, no jargon left unexplained.

**Your turn:** paste this into Claude — "My computer-use agent resends an
identical screenshot up to 35 times across a 50-turn task. Add ephemeral
prompt caching to the screenshot blocks and report the token cost with and
without it." Then ask it the harder question: what happens if the
screenshot changes by one pixel — does a naive cache check still call that
a hit?

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-quickstarts--screenshot-prompt-caching

---
*AI disclosure: this video's narration is synthesized (Kokoro, voice `am_onyx`) and
its visuals are entirely programmatically generated (Remotion + Manim) from a
scripted beat sheet — no filmed footage, no generative video or image models.*
