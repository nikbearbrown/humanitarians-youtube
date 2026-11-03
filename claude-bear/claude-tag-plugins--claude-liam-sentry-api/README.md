# Claude, Sentry API. — YouTube metadata

**Channel:** @HumanitariansAI
**Playlist:** Claude Basics
**AI disclosure:** This video uses AI-generated narration (Kokoro text-to-speech, voice
"Liam") and AI-assisted animation (Remotion). No AI-generated video or imagery.

## Title

Claude, Sentry API — Is the ID in the URL the ID Claude Actually Sends?

## Description

When Claude looks at a Sentry issue you can see at a URL like PROJ-123, is that the ID
it hands to the API — or does something else have to happen first? It isn't the ID —
that visible code is a shortId, and Claude has to search for it first to get the
numeric ID the issue endpoint actually requires.

From Humanitarians AI: short, plain explanations of how Claude actually works, for a
general audience meeting Claude for the first time. Liam, in for Professor Bear.

In this one: the org → project → issue → event data model and the eight core
operations Claude has to know; four workflow patterns that keep Claude out of
trouble — resolving shortIds, following Link-header cursors, checking the `detail`
field even on a 200, and using `-L` for trailing-slash redirects; and the carry-out
that matters: the ID shown in the browser isn't the ID Claude sends, and a
two-hundred response isn't always the yes it looks like.

Try it yourself — the video ends with a paste-ready prompt for testing this on any API
you pick, today, in Claude.

**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-sentry-api

This is an educational explainer, not sponsored by or affiliated with Anthropic or
Sentry.

## Tags

Claude, Claude AI, Claude skills, Anthropic, AI basics, Humanitarians AI, Sentry,
API integration, error tracking, developer tools, pagination, AI for beginners, Claude
tutorial

## Chapters (approx., from beat timings)

0:00 Cold open — is the URL's ID the ID Claude sends?
0:12 Anatomy — data model + eight core operations
1:02 Design — workflow patterns + gotchas
1:50 Both directions — documented plainly vs. easy to miss
2:12 Carry-out
2:19 Your turn
2:39 Outro
2:41 Outro CTA
