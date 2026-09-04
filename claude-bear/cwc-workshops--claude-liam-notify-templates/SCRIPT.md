# SCRIPT.md — Fill The Template. Don't Write It. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-notify-templates` (Teardown, walks the Anthropic
`notify-templates` cwc-workshops Skill — fixed-format templates for Slack
alerts, supplier emails, and escalations) — question, facts, and body
argument carried over; narration re-registered to Plain (explain, then
stop, no verdict); cold open replaced with the BrutalistHesitantWriter;
close carries the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude writes each low-stock alert from scratch. It
doesn't — it fills a fixed template. So: does Claude fill the low-stock
alert template?

*(Text typed on screen: "Does Claude / write the / low-stock alert /
template?" — trigger word "write" corrects to "fill", landing on: "Does
Claude fill the low-stock alert template?")*

## Body — anatomy, routing, and the batching rule

**NB01 — Three templates, no subagent** (source B01, anatomy)
A skill is a folder Claude reads before it acts. This one is
notify-templates — three fixed formats: a low-stock Slack alert, a
supplier email, and an escalation for human review. Fill the slots from
data already at hand, append the result, and stop — the file says
explicitly: do not spawn a subagent for this.

**NB02 — Where it's routed** (source B02, pipeline)
Where the message lands isn't fixed either — it's routed. Most things go
to the ops channel by default. An active stockout on a top SKU adds an
at-here. Anything over twenty-five thousand dollars goes straight to a
purchasing lead, not the channel. Finance only hears about it past one
hundred thousand dollars outstanding, or a suspected duplicate order.
Cross a threshold, and the message says which one.

**NB03 — Batch, don't spam** (source B03 design tell + BVDT verdict,
merged; re-registered Teardown → Plain)
For a daily sweep across many SKUs, the rule is one summary message, not
one per SKU — even when the task asks for a note to each, every line still
goes into a single batch append. Sending it is one append to an outbox
file, in JSON, one line per notification. If sending an alert takes more
than two tool calls, something's gone wrong. Same data, same template,
same append — every time.

## Close

**BCRY — carry-out**
Claude doesn't write these alerts — it fills three fixed templates from
data it already has. A sweep becomes one summary and one append, never one
call per SKU.

**BHTF — your turn**
Your turn. Paste this into Claude: I need a low-stock alert for SKU-0042 —
3 units on hand, reorder point 20, days of cover 2. Also, 8 other SKUs
dropped below their reorder point today. Read the notify-templates skill
and walk me through what you'll send — one alert, or one for each of the
9 — and where each one is routed, before you send anything.

**BOUT — outro**
Fill The Template. Don't Write It. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a composition question — does Claude write the alert, or fill a template? |
| Wrong guess | B00 (WRITER LAW) | "write" corrected to "fill" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the three fixed templates, the no-subagent rule, and the exact routing thresholds (ops default, at-here, $25k purchasing lead, $100k finance) |
| Anchor | the low-stock alert decision itself, named at B00 and carried through NB01–NB03 without dropping it | source is a single worked mechanism throughout (one Skill, one decision), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB03 | "one alert per SKU when a sweep runs" is wrong (batch it) / "always send exactly one message no matter what's asked" is also wrong (an explicit per-SKU request still gets filled per-SKU, just batched into one append) — both misreadings of the batching rule, stated together |
| Carry-out | BCRY | one sentence, two at most, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct restatement of the
`notify-templates` Skill's own SKILL.md — the three template formats
(low-stock Slack alert, supplier email, escalation), the explicit "do not
spawn a subagent for this" instruction, the routing table's four tiers and
their exact dollar/urgency thresholds, the "batch, don't spam" rule and its
one-summary-per-sweep default, the per-SKU exception that still collapses
into a single batch append, and the outbox append mechanism ("if you're
making more than two calls to send a notification, you've over-engineered
it"). Per `simple`'s ONE-FLAG LAW, when the source genuinely supports
everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's design-tell text (generic Teardown framing — "what it gets right:
repeatable results. What it bites: anything outside the spec.") and BVDT's
verdict (same restatement of the trigger keywords and "same input, same
output, every run") are merged into a single NB03, replaced with the
skill's actual batching mechanism — the "batch, don't spam" rule and the
outbox append — which the source's own narration never got to (it recapped
the trigger keywords instead); this keeps the body argument (what the
skill does, and its one hard constraint) while trading a generic
Teardown-style recap for the single most teachable fact the source left on
the table. BHTF kept as the your-turn handoff, rewritten as a
fully self-contained scenario (single alert + an 8-SKU sweep in the same
prompt) so the viewer tests both the template-fill and the
batch-vs-one-per-SKU reasoning in one paste, no skill install required.
BOUT kept, re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB03
+ BCRY + BHTF + BOUT = 7 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`
/ `ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
