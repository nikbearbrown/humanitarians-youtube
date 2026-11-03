# Bridging the Pixel Gap in Browser Automation.

**Channel:** @HumanitariansAI
**Playlist:** Claude Basics

## Description

Claude's browser tool hands back a click coordinate — but that number was measured
on a resized copy of your screen, not your actual screen. Why doesn't clicking it
directly land on the button?

Claude's vision encoder resizes every 16:9 screenshot to a fixed 1456×819 before
the model ever looks at it. Your real viewport — 1920×1080, or whatever size your
screen actually is — is a different canvas. The fix is the inverse of the resize
ratio: multiply Claude's coordinate by (your width / 1456) and (your height / 819),
clamp to the screen's edges, and the click lands exactly where Claude meant it to.

This is Professor Bear's Claude-basics series, narrated by Liam — one real question,
answered simply, no jargon left unexplained.

**Your turn:** paste this into Claude — "My model clicks at (700, 410) on a
1456x819 screenshot but my screen is 1920x1080 — write the scaling and land the
click exactly." Then check: does it clamp to the screen's edges? Does it handle a
screen that isn't 16:9?

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-quickstarts--browser-coordinate-scaling

---
*AI disclosure: this video's narration is synthesized (Kokoro, voice `am_onyx`) and
its visuals are entirely programmatically generated (Remotion + Manim) from a
scripted beat sheet — no filmed footage, no generative video or image models.*
