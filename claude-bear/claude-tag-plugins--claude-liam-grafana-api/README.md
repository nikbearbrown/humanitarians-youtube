# Claude, Grafana API. — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Claude Basics
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Remotion). No AI-generated video or imagery.

## Title

Claude, Grafana API — Does Claude Already Know an API It's Never Seen?

## Description

Does Claude already know how an outside system like Grafana's API works, or does
something have to tell it? Not quite the first — Claude reads a Skill, a file, before
acting, and that file is what carries the account-specific detail training alone
wouldn't reliably have: which of three time formats each endpoint expects, which two
alert-rule surfaces answer different questions, and why updating a dashboard means
replacing the whole thing rather than patching a piece of it.

From Humanitarians AI: short, plain explanations of how Claude actually works, for a
general audience meeting Claude for the first time. Liam, in for Professor Bear.

In this one: three time formats by endpoint (wrong one returns empty results, not an
error); the Prometheus API for live alert state vs. the provisioning API for alert
definitions; the GET-then-full-replace dashboard update and its 412 version conflict;
and the carry-out that matters: a skill doesn't make Claude know an API, it gives
Claude a map of where the traps are — and Claude only avoids the ones the map actually
marks.

Try it yourself — the video ends with a paste-ready prompt for testing this on any API
you pick, today, in Claude.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-grafana-api

This is an educational explainer, not sponsored by or affiliated with Anthropic or
Grafana Labs.

## Tags

Claude, Claude AI, Claude skills, Anthropic, AI basics, Humanitarians AI, Grafana,
Prometheus, API integration, observability, monitoring, AI for beginners, Claude
tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — does Claude already know the Grafana API?
0:12 Anatomy — three time formats + role model + request setup
1:08 Design — two alert surfaces + dashboard replace + batching
1:55 Both directions — documented plainly vs. easy to miss
2:15 Carry-out
2:23 Your turn
2:43 Outro
2:46 Outro CTA
