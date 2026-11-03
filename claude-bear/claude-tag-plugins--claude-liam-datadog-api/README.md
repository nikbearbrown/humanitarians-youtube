# Claude, Datadog API. — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Claude Basics
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Remotion). No AI-generated video or imagery.

## Title

Claude, Datadog API — Does Claude Already Know an API It's Never Seen?

## Description

Does Claude already know how an outside system like Datadog's API works, or does
something have to tell it? Not quite the first — Claude reads a Skill, a file, before
acting, and that file is what carries the account-specific detail training alone
wouldn't reliably have: which API version covers which resource, which two headers
every request needs, and the regional-site trap that returns a flat permission error
even with valid credentials.

From Humanitarians AI: short, plain explanations of how Claude actually works, for a
general audience meeting Claude for the first time. Liam, in for Professor Bear.

In this one: the v1/v2 split by resource, not by version age; the three different
pagination schemes Datadog's API uses depending which endpoint you're calling; two
real JSON:API quirks that still trip things up even with the file in hand; and the
carry-out that matters: a skill doesn't make Claude know an API, it gives Claude a map
of where the traps are — and Claude only avoids the ones the map actually marks.

Try it yourself — the video ends with a paste-ready prompt for testing this on any API
you pick, today, in Claude.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-datadog-api

This is an educational explainer, not sponsored by or affiliated with Anthropic or
Datadog.

## Tags

Claude, Claude AI, Claude skills, Anthropic, AI basics, Humanitarians AI, Datadog,
API integration, developer tools, JSON:API, pagination, AI for beginners, Claude
tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — does Claude already know the Datadog API?
0:12 Anatomy — v1/v2 resource split + setup requirements
0:46 Design — three pagination schemes + JSON:API traps
1:22 Both directions — documented plainly vs. easy to miss
1:41 Carry-out
1:49 Your turn
2:09 Outro
2:11 Outro CTA
