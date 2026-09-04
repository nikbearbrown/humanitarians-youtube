# Fill The Template. Don't Write It.

Ask whether Claude writes each low-stock alert from scratch, and the
natural read is that notifications are a little creative-writing task —
Claude composing a message for the situation. It isn't. The
notify-templates skill's own instructions are blunt about it: notifications
are template fills, not creative writing, and the skill explicitly says not
to spawn a subagent for the job. Claude fills three fixed formats — a
low-stock Slack alert, a supplier email, an escalation for human review —
from data it already has, then appends the result. Where the message lands
is routed, not fixed: most things go to the ops channel by default, an
active stockout adds an @here, anything over $25,000 goes straight to a
purchasing lead instead of the channel, and finance only hears about it
past $100,000 outstanding or a suspected duplicate order. And for a daily
sweep across many SKUs, the rule is one summary message, not one per SKU —
even a request for a note to each SKU still collapses into a single batch
append, because sending a notification should never take more than two
tool calls.

**Topic:** NOTIFY-TEMPLATES · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-notify-templates

---

## Chapters

0:00 The naive framing: "does Claude write the alert template?"
0:09 Anatomy: three fixed templates, no subagent
0:26 Mechanism: where the message is routed (ops / purchasing / finance)
0:47 Batch, don't spam — one summary, one append, ≤ 2 calls
1:08 Carry-out
1:18 Your turn
1:37 Outro

---

## YOUR TURN

Paste this into Claude: I need a low-stock alert for SKU-0042 — 3 units on
hand, reorder point 20, days of cover 2. Also, 8 other SKUs dropped below
their reorder point today. Read the notify-templates skill and walk me
through what you'll send — one alert, or one for each of the 9 — and where
each one is routed, before you send anything.

Run that today, against your own notification scenario.

---

## Deliberately not claimed

Every claim in this reel restates the source SKILL.md's own text directly:
the three template formats (low-stock Slack alert, supplier email,
escalation); the explicit "do not spawn a subagent for this" instruction;
the routing table's exact tiers and thresholds (ops default, @here for an
active/imminent top-SKU stockout, a purchasing lead DM above $25k, finance
only above $100k outstanding or a suspected duplicate PO); the "batch,
don't spam" rule and its one-summary-per-sweep default, including the
per-SKU exception that still collapses into one batch append; and the
outbox append mechanism ("if you're making more than two calls to send a
notification, you've over-engineered it"). This redo drops the source
Teardown cut's generic "what it gets right / what it bites" framing, which
recapped the trigger keywords rather than the skill's actual routing and
batching mechanism — replaced here with the single most teachable fact the
source narration never got to. See BUILD-LOG.md for the full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
