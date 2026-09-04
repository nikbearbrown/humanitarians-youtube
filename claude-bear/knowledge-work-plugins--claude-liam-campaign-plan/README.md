# Claude, Campaign Plan.

You ask Claude for a marketing campaign plan, and it's tempting to picture
it inventing a bespoke strategy from creative judgment, the way a
strategist would. It doesn't invent — it assembles. The `campaign-plan`
skill is a `SKILL.md` file Claude reads before it acts: instructions, not
strategy. Its job, fixed: generate a full campaign brief with six pieces —
objectives, audience, messaging, channel strategy, content calendar, and
success metrics — every time, for every product. It only fires when your
words match its stated triggers: planning a product launch, a lead-gen
push, an awareness campaign, needing a week-by-week content calendar, or
translating a marketing goal into a structured plan. Once matched,
execution is linear: read the file, execute each step in order, return the
result. Run the same request again later and Claude walks the same file,
in the same order — the same six pieces come back. Phrase it outside the
trigger list, and the pipeline never starts; you're back to Claude
answering from what it already knows, which is exactly the guess this reel
opens by questioning.

**Topic:** CAMPAIGN-PLAN · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-campaign-plan

---

## Chapters

0:00 You ask for a campaign plan — Claude must assemble the whole strategy, right?
0:10 Same six pieces, different products
0:29 Matched, then walked step by step
0:50 Same steps again, then nothing starts
1:14 Carry-out
1:23 Your turn
1:53 Outro

---

## YOUR TURN

"I want a campaign plan for a product I'm describing to you now. Read the
campaign-plan skill and walk me through what you'll do, step by step,
before you do it."

Watch for two things when Claude answers: does it name the six pieces
before writing them, and does it match your request to one of its own
stated triggers?

---

## Deliberately not claimed

Not a verdict on the trigger-phrase design — the source framed the spec as
"what it gets right" against "where it bites," a Teardown trade-off
judgment; this reel keeps only the mechanism fact: matching words run the
pipeline, non-matching words don't. Not a claim that Claude has no
marketing knowledge — it plainly can discuss strategy generally; the point
is that the skill's deliverable shape is fixed by the file, not chosen
fresh by creative judgment each time. Not a claim that a missed trigger
errors loudly — the source describes no error state for an out-of-spec
request; the pipeline simply never starts.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
