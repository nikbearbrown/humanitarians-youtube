# Flags Decide The Path.

Ask whether Claude always spawns a subagent to forecast demand, and the
natural read is a coin flip between "it always does" and "it never needs
to." Neither is right. The forecasting skill checks four flags first —
horizon, seasonality, next-month promo, and a mentioned trend break. Clear
of all four (two weeks or less, nothing seasonal, no promo, no trend
break) and it computes a rolling mean itself, one script, no subagent. Trip
any one of them and it delegates to a forecaster subagent instead — not
because the math gets harder, but because the subagent needs ninety days
of sales history in its own context window, and loading that much history
into the main conversation would crowd out the rest of the task. Either
way, the number that comes back — forecast_qty — is a computed estimate,
not a fact about next month, and a confidence score under 0.6 means
escalate to a human, not auto-order.

**Topic:** FORECASTING · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-forecasting

---

## Chapters

0:00 The naive framing: "does Claude always spawn a subagent?"
0:09 Anatomy: a skill is a folder (two scripts + SKILL.md)
0:28 Mechanism: flags decide the path (Path A vs. Path B)
1:02 Confidence < 0.6 -> escalate; the number is an estimate, not a fact
1:29 Carry-out
1:40 Your turn
1:59 Outro

---

## YOUR TURN

Paste this into Claude: I'm forecasting demand for a product with a
promotion next month, a 30-day horizon. Should you compute this yourself
with a simple average, or delegate it — and why? Then tell me what
confidence score you'd attach, and whether that's high enough to
auto-order or should escalate to a human instead.

Run that today, against your own forecasting scenario.

---

## Deliberately not claimed

Every claim in this reel restates the source SKILL.md's own text directly:
the two scripts (rolling_mean.py for a single SKU, batch_days_of_cover.py
for ranking many); the exact Path A conditions (horizon ≤ 14 days, not
seasonal, no promo next month, no mentioned trend break) and Path B
conditions (any one of those flags flipped); the reason a subagent gets
its own context window (the full 90-day sales history); the
confidence-below-0.6-escalates handoff to the reorder-policy skill; and
forecast_qty being a computed output, not a predicted fact. This redo
drops the source Teardown cut's aside about `callable_agents` being a
research-preview feature with an inline fallback, and the promotional
seasonal-calendar detail — both assume a technical audience this series
doesn't target. See BUILD-LOG.md for the full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
