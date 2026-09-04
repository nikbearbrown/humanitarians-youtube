# Four Layers, Not One File. — The Claude Config Guide Skill

Claude's configuration model has four layers: agents at the top, agent
scopes that control how settings resolve and inherit across a workspace,
identity profiles that carry scopes, rules, credentials, and repo
permissions, and presets, connections, GitHub repos, and custom
instructions attached to each profile. The config-guide skill itself
doesn't hold the answer — it's an index that routes a question to one of
five reference files: agents and scopes, identity profiles, connections
and presets, GitHub and instructions, or best practices. Splitting it into
five short files instead of one long one is deliberate; right now the
guide covers only the Slack surface, and it always closes by pointing you
to debug-plugins in a brand-new thread, since a fresh thread means a fresh
container reflecting your current configuration. The risk worth knowing:
this only works because all five reference files are actually there — if
one goes missing, the skill doesn't error, it just quietly doesn't answer
that part of your question.

**Topic:** CLAUDE CONFIG GUIDE · INDEX SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-config-guide

---

## Chapters

0:00 The naive framing: "where's the file with my settings?"
0:11 Four layers, one index
0:40 Slack only — verify fresh
1:02 Quiet when a file's missing
1:16 Carry-out
1:25 Your turn
1:45 Outro

---

## YOUR TURN

Paste this into Claude: I'm designing settings for an app with
company-wide defaults, team overrides, and per-user overrides layered on
top of each other. Walk me through structuring that as layered objects —
like agents, scopes, and profiles — so a user's change never gets
silently overwritten by a team default. Then show me one way the design
could quietly fail if a piece of it goes missing.

Run that today, on your own settings design, not the video's example.

---

## Deliberately not claimed

No claim about how Claude's configuration works outside the config-guide
skill's own scope — the four-layer model, the five reference files, and
the Slack-only surface are what this particular skill specifies today.
No claim that the debug-plugins new-thread step is unnecessary busywork;
the video states the opposite — a new thread is what gets you a fresh
container instead of cached state.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
