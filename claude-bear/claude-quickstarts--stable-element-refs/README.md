# Stable Reference IDs Survive Viewport Chaos.

**Channel:** @HumanitariansAI
**Playlist:** Claude Basics

## Description

Your browser automation clicks a button at pixel (960, 540). Someone resizes the
window, the page reflows, and the click starts missing. Why does that happen, and
what actually keeps working across the resize?

A pixel coordinate only describes where a button was, at one moment, in one
layout. Resize the browser and the page reflows — the button can end up almost
anywhere. The fix runs before Claude ever looks at the page: a script tags every
clickable element with a stable reference id, independent of its position on
screen. Claude targets the id, not a pixel, so the tag travels with the button no
matter where the layout puts it — while any element that appears only after page
load still needs its own tagging pass to be reachable at all.

This is Professor Bear's Claude-basics series, narrated by Liam — one real
question, answered simply, no jargon left unexplained.

**Your turn:** paste this into Claude — "Assign stable refs to every clickable
element on this page so my automation survives a resize." Then check: does it tag
elements that load in later? Does it guard against duplicate ids?

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-quickstarts--stable-element-refs

---
*AI disclosure: this video's narration is synthesized (Kokoro, voice `am_onyx`) and
its visuals are entirely programmatically generated (Remotion + Manim) from a
scripted beat sheet — no filmed footage, no generative video or image models.*
