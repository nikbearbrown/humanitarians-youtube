# Two Resolutions, One Click — The macOS Coordinate Roundtrip.

**Channel:** @HumanitariansAI
**Playlist:** Claude Basics

## Description

Claude clicks at a coordinate on your MacBook's screenshot — but that number was
measured on a resized copy of your Retina screen, not your actual screen. Why
doesn't clicking it directly land on the button?

macOS Retina screenshots are far bigger than the API's image budget: the long edge
has to stay under 1568 pixels, and the image can't cut into more than 1568 of its
28×28 tiles. The reference implementation resizes first — for a 2560×1600 screen,
down to 1344×840 — before Claude ever looks. The fix is the inverse of that resize:
multiply Claude's coordinate by (native / sent) for both x and y, and the click
lands exactly where you meant.

This is Professor Bear's Claude-basics series, narrated by Liam — one real question,
answered simply, no jargon left unexplained.

**Your turn:** paste this into Claude — "My MacBook's screenshot is 2560x1600, but
Claude sees it resized to 1344x840 — write the inverse transform so a click Claude
makes lands on my real screen." Then check: does it handle a screen that isn't the
same shape as yours? Does it recompute the transform if you plug in an external
monitor?

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-quickstarts--macos-computer-use-coordinate-roundtrip

---
*AI disclosure: this video's narration is synthesized (Kokoro, voice `am_onyx`) and
its visuals are entirely programmatically generated (Remotion + Manim) from a
scripted beat sheet — no filmed footage, no generative video or image models.*
