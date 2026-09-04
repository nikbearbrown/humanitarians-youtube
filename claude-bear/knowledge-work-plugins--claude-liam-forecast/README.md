# Weighed, Not Predicted. — The Forecast Skill (Stage-Weighted Pipeline)

Forecast turns your pipeline into one number: hand it deals — name, amount,
stage, close date — plus your quota, and it multiplies each deal's amount by
its stage's default probability (negotiation 80%, discovery 20%, and so on)
and adds the results up. Take one deal, Acme Corp at $50K in Negotiation: at
80% it adds $40K to the forecast, confident enough to sit in Commit. One
flag — connect a CRM and those defaults get replaced by your team's real
historical win rates. But confidence isn't certainty in either direction: a
Commit deal can still go quiet and need a re-engage, and a 20%-odds Discovery
deal isn't written off either. The gap analysis tells you how far short of
quota you are. It never tells you which deals will close it.

**Topic:** FORECAST · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-forecast

---

## Chapters

0:00 The naive framing: "does Claude predict which deals close?"
0:09 Pipeline becomes a number
0:26 One deal, weighed (the anchor)
0:43 The one flag: your own data
0:59 Commit can still slip
1:11 Low odds can still land
1:25 Carry-out
1:34 Your turn
1:55 Outro

---

## YOUR TURN

Paste this into Claude: Here's my pipeline. Acme Corp, $50K, in Negotiation,
closing this month. TechStart, $25K, in Discovery. My quota is $100K this
quarter. Give me a weighted forecast — best, likely, and worst case — split
into commit versus upside, and flag anything at risk.

Run that today, with your own numbers, not the video's example.

---

## Deliberately not claimed

No claim that the model "learns" a team's patterns automatically — the
default stage-probability table is generic until a CRM connection supplies
real historical win rates, which is this video's one stated flag. No
suggestion that Commit vs. Upside or the risk flags are a judgment on any
rep's honesty; they are the skill's own categories for managing uncertainty.
The "Acme Corp" deal is the SKILL.md's own illustrative sample, not a real
customer.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #SalesForecast #LLM #HumanitariansAI #ProfessorBear

---
