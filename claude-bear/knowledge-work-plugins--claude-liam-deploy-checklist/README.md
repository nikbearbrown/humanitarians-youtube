# Claude, Deploy Checklist.

You're about to ship a release and ask Claude if it's ready to go. The
natural guess is that it weighs it the way a release manager would — a gut
call on risk, made in the moment. It doesn't. `deploy-checklist` is a
**skill**: a folder Claude reads before it acts, containing one file,
`SKILL.md`, that names exactly three things to check (CI status &
approvals, database migrations or feature flags, and rollback triggers
documented ahead of time) and exactly what triggers it (about to ship a
release, or a change with a migration or feature flag). A release that adds
a live database migration gets flagged, because migrations are on the
list. A failure the file never mentions can still ship straight through,
because it was never on the list to begin with.

**Topic:** DEPLOY-CHECKLIST · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-deploy-checklist

---

## Chapters

0:00 Claude, just use your judgment on this release — wait, what does the file check?
0:10 Before you ship, something decides what "ready" means
0:16 The guess: a human-style risk call
0:22 Run it twice — same list, every time
0:35 A skill is a folder: one file, SKILL.md
0:44 Anchor planted — a live migration
0:49 What deploy-checklist checks: CI, migrations, rollback triggers
1:00 It names its own cue
1:07 How the skill works: read, check, return
1:14 Anchor payoff — same migration, flagged
1:19 A flag is real signal
1:24 Clean isn't a certificate
1:32 Carry-out: know the list, know the limit
1:41 Your turn
1:53 Outro

---

## YOUR TURN

"Before you say this release is ready, read the deploy-checklist SKILL.md
and tell me exactly what you're about to check — the items, and the phrase
that triggers you. Then walk me through this release: [describe it]"

Watch two things when Claude answers: does it name the checklist items
before it looks at your release, and does its finding land inside one of
those items — never outside the list it just gave you?

---

## Deliberately not claimed

Not a verdict on whether a three-item checklist is the right scope for a
pre-deploy check — that's Teardown territory; this reel states the
mechanism and its edges, and stops. Not that every skill works this way —
this reel describes `deploy-checklist` specifically, not skills in general.
Not a claim that a clean checklist means the release is safe — only that
nothing on this list tripped.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #DeployChecklist #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
