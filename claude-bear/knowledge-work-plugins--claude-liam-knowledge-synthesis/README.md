# Combine, Don't Pick. — The Knowledge-Synthesis Skill (Multi-Source Search)

Feed Claude several search results on the same topic and you might assume it
just picks the one best result. It doesn't — knowledge-synthesis is a skill
file (SKILL.md) that runs as a fixed, ordered pipeline: gather the results,
then combine them. Combining means merging repeated claims into one, dropping
duplicates, and keeping a record of exactly which source each surviving claim
came from. When sources disagree, the skill doesn't average them — it weighs
each claim by how fresh and how authoritative its source is, and the
higher-weighted claim wins. Same sources in, same answer out, every run.

**Topic:** KNOWLEDGE SYNTHESIS · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-knowledge-synthesis

---

## Chapters

0:00 The naive framing: "does Claude just pick the best source?"
0:10 One job, run as steps
0:37 Dedupe, then attribute
1:04 Weighed, not averaged
1:32 Carry-out
1:42 Your turn
2:06 Outro

---

## YOUR TURN

Paste this into Claude: I have three write-ups on the same topic that overlap
and disagree in a few places. Read all three, combine what's true across them
into one answer, remove anything repeated, and for each claim you keep, tell
me exactly which write-up it came from and why you trusted it over the others
where they disagreed.

Then check what comes back: does every claim carry a source, and does it
explain the call it made when two write-ups disagreed?

Run that today, on your own overlapping write-ups, not the video's example.

---

## Deliberately not claimed

No claim about the exact scoring formula behind "freshness" and "authority"
(weights, thresholds) — the source material names the two factors, not the
arithmetic, and this video doesn't invent one. No claim that summarization is
a separate mechanism from combine/dedupe/attribute — the source treats
"summarizes large result sets effectively" as part of the same job.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
