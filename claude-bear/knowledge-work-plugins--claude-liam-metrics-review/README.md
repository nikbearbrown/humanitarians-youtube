# Claude, Metrics Review.

You hand Claude a week of numbers and ask for a review before the meeting.
The natural guess is that it eyeballs the numbers and calls out whatever
looks interesting — different each time, depending on what catches its
eye. It doesn't. `metrics-review` is a **skill**: a folder Claude reads
before it acts, containing one file, `SKILL.md`, that names what a review
covers (trend analysis, comparison against targets, a scorecard with
recommended actions) and exactly what triggers it (a weekly, monthly, or
quarterly review, or a request to investigate a spike or drop). Say
weekly active users drop twenty percent with no obvious cause — the
spike-or-drop case named in the file catches it, because that case is on
the list. A metric the file never tracks can slip straight through,
because it was never on the list to begin with.

**Topic:** METRICS-REVIEW · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-metrics-review

---

## Chapters

0:00 Claude, review my metrics — it catches everything, right?
0:10 Before the meeting, something decides what's worth flagging
0:17 The guess: freeform, different every time
0:25 Run it twice — same steps, same order, every time
0:33 A skill is a folder: one file, SKILL.md
0:44 Anchor planted — weekly active users drop twenty percent
0:49 What metrics-review checks: trend, targets, scorecard
0:57 It names its own cue
1:04 How the skill works: read, analyze, return
1:11 Anchor payoff — same drop, flagged
1:17 A flag is real signal
1:22 Clean isn't a clean bill of health
1:31 Carry-out: know the list, know the limit
1:40 Your turn
1:53 Outro

---

## YOUR TURN

"Before you review my metrics, read the metrics-review SKILL.md and tell
me exactly what you're about to check — the analysis, the targets, and the
phrase that triggers you. Then review this week's numbers: [paste them]"

Watch two things when Claude answers: does it name what it's about to
check before it looks at your numbers, and does its finding land inside
what it just told you — never outside the list it just gave you?

---

## Deliberately not claimed

Not a verdict on whether trend, targets, and a scorecard is the right
scope for a metrics review — that's Teardown territory; this reel states
the mechanism and its edges, and stops. Not that every skill works this
way — this reel describes `metrics-review` specifically, not skills in
general. Not a claim that a clean scorecard means nothing is wrong with
your numbers — only that nothing on this list tripped.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Remotion (motion graphics).
No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ProductMetrics #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
