# Snapshot, Not Sensor. — The Project Artifact Skill (Status Pages)

Open a Claude-built project status page and two tabs are always there —
Overview and Workstreams — with five more (Attention, Background, Plan,
Risks, Decisions/FAQ) that only appear when a config file actually has
content for them. All of it comes from one config file, and every publish
also saves a stored state block inside the page itself. Here's the part
that surprises people: nothing updates on its own. The page doesn't watch
your data — it waits. You have to ask for a refresh, and only then does it
look for that stored block: found, it computes a delta of what changed;
missing, the whole page rebuilds from scratch with no change summary at
all.

**Topic:** PROJECT ARTIFACT · CLAUDE CODE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-project-artifact

---

## Chapters

0:00 The naive framing: "does my page watch and update itself?"
0:10 Two tabs, always on
0:35 One config file, a saved record
1:02 Nothing updates on its own
1:23 Carry-out
1:35 Your turn
1:57 Outro

---

## YOUR TURN

Paste this into Claude: Build a project status page for my API migration,
with workstreams, an open risk, and a decisions log. Once it's built, ask
for a refresh without changing anything — does it say nothing changed, or
does it silently rewrite the whole page? Then close out that risk and
refresh again. Does it call out exactly that change, or does it act like
it's starting from zero?

Run that today, on your own project, not the video's example.

---

## Deliberately not claimed

No claim about how the Artifact tool's account/login requirements or the
config file's machine-local storage behave — those are real properties of
the Skill but assume a technical/build-time audience this video doesn't
target. No claim that every possible refresh implementation works this way;
the delta-vs-rebuild behavior described is a property of this specific
Skill's design, not a claim about status pages in general.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
