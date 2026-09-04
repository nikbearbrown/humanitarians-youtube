# Web Artifacts Builder

Ask Claude for a complex claude.ai artifact — a dashboard, a multi-tab tool —
and it feels like Claude just handwrites one HTML file. It doesn't. The Web
Artifacts Builder first provisions a real React 18 + TypeScript + Tailwind +
shadcn/ui project with one init script, develops inside it, then runs a
separate bundle script that inlines everything — JS, CSS, every dependency —
into one self-contained bundle.html. The single file at the end is a
compiled output, not a first draft.

**Topic:** WEB ARTIFACTS BUILDER · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-web-artifacts-builder

---

## Chapters

0:00 The naive framing: "it just handwrites one HTML file"
0:11 Anatomy — the 4-step pipeline + tech stack
0:53 Design mandate — anti-slop rule + bundle anatomy
1:17 The mechanism: provisioned first, bundled after
1:46 Carry-out
1:59 Your turn
2:32 Outro

---

## YOUR TURN

Build a note-taking app with tags, search, and a markdown editor, as a
shareable claude.ai artifact. Use the Web Artifacts Builder.

Watch four things: does Claude run init-artifact.sh before writing any
component code? Does it use shadcn/ui components from the pre-installed set
instead of writing its own UI from scratch? Does it run bundle-artifact.sh
and share bundle.html at the end, not a raw index.html or a dev server link?
And does the result actually avoid the four named patterns — no dominant
centered layout, no purple gradient, no every-corner-the-same-radius, no
Inter font?

---

## Deliberately not claimed

No ranking of what the Web Artifacts Builder "gets right" or "where it
bites" — the source reel's Teardown-register judgment card is dropped here.
The two hard requirements (Node 18+ and index.html in project root for
bundling, no react-router pre-wired despite routing being named in the
skill's description) are stated as fact, straight from the skill's own
specification, not as a verdict on the design.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear #WebArtifactsBuilder

---
