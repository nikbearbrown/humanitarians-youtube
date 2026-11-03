# Does Claude's Digest Skill Watch You All Week?

Ask for a digest after a week away and it's tempting to picture Claude as
having quietly kept tabs on everything the whole time — the way a person
who never left the office would have. That's not what's happening.
Anthropic's `digest` skill reads one instruction file and follows its steps
in order only when you ask: gather mentions and action items across your
connected sources, group updates by project, and check whether you asked
for daily or weekly. Leave that unset, and the file's own default line
fires — daily — so a digest asked for on a Monday after a week away comes
back covering Friday, one day out of seven. Ask again with the window still
unset and you get the same one-day default, identically, every time. Say
"weekly" once, and the same file runs the same steps across all seven days
instead, surfacing everything the daily default left out. A Claude digest
isn't Claude quietly watching all week — it's a file that runs when you
ask, and unless you say "weekly," it hands you one day and calls it done.

**Topic:** DIGEST · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-digest

---

## Chapters

0:00 All week I was away — was Claude quietly watching?
0:10 Tracking everything, or asked?
0:31 One Monday, four stops
0:57 Still unset, or said weekly?
1:17 Carry-out
1:26 Your turn
1:42 Outro

---

## YOUR TURN

"Run the digest skill on your own connected sources without saying whether
you want daily or weekly. See which window it defaults to. Then run it
again, saying 'weekly' explicitly, and compare what surfaces that the first
pass missed."

Watching exactly how much silently disappears behind an unset default —
and how simply naming the window recovers it — is the fastest way to see
that the digest runs from a written file with a stated default, not from
continuous awareness, rather than just trusting that it does.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-digest`) in the Plain register for a general audience. The
underlying facts are unchanged from the source: the skill generates a daily
or weekly digest of activity across connected sources — used when catching
up after time away, starting the day, or reviewing a week's decisions and
document updates grouped by project; it defaults to a daily window if no
flag is specified. This script makes no claim about any specific team,
tool, or connected source — only the general mechanism (a written procedure
with a stated default) and its two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
