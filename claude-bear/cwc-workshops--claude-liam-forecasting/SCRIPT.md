# SCRIPT.md — Flags Decide The Path. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-forecasting` (Teardown, walks the Anthropic
`forecasting` cwc-workshops Skill — demand forecasting for a SKU, compute it
yourself vs. delegate to a subagent) — question, facts, and body argument
carried over; narration re-registered to Plain (explain, then stop, no
verdict); cold open replaced with the BrutalistHesitantWriter; close carries
the Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude always spawns a subagent to run a forecast. It
doesn't — only sometimes. So: does Claude sometimes spawn a subagent to
forecast?

*(Text typed on screen: "Does Claude / always spawn / a subagent / to
forecast?" — trigger word "always" corrects to "sometimes", landing on:
"Does Claude sometimes spawn a subagent to forecast?")*

## Body — anatomy, the two-path mechanism, the design tell

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it acts. This one is forecasting —
a demand forecast for one SKU. Inside are two small scripts:
rolling_mean.py, for a single item, and batch_days_of_cover.py, for ranking
many SKUs at once. The SKILL.md says which script to run, and when to skip
both and hand the job to a subagent instead.

**NB02 — Two paths, and flags decide** (source B02, pipeline)
Two paths, and flags decide which one. Path A: compute it yourself, a
rolling mean over recent sales — but only when the horizon is two weeks or
less, the SKU isn't seasonal, there's no promo next month, and nothing
suggests a trend break. One script, no subagent. Path B: hand it to a
forecasting subagent whenever any one of those flags flips — a longer
horizon, a seasonal item, a promo, a visible trend. Why delegate there? The
subagent needs ninety days of sales history to spot the pattern, and
loading that much history into your own context would crowd out the rest
of the task — the subagent gets its own context window instead.

**NB03 — The confidence threshold, and what the number is** (source B03
design tell + BVDT verdict, merged; re-registered Teardown → Plain)
One more flag matters after the forecast comes back: confidence. Below
0.6, the rule downstream is escalate, don't auto-order — a low score
doesn't mean the model is broken, it means a human should look before
ordering. A high score doesn't guarantee the number is right either — it
just means nothing in the inputs suggested otherwise. And the number
itself, forecast_qty, is not a fact about next month. It's what the rolling
mean, or the subagent's model, computed from the flags it was given. Same
flags, same path, same number — every time.

## Close

**BCRY — carry-out**
Claude picks compute-it-yourself or hand-it-to-a-subagent by the flags, not
by guesswork — and whichever path runs, the number it returns is a
computed estimate, not a fact about next month.

**BHTF — your turn**
Your turn. Paste this into Claude: I'm forecasting demand for a product
with a promotion next month, a thirty-day horizon. Should you compute this
yourself with a simple average, or delegate it — and why? Then walk me
through what confidence score you'd attach, and whether that's high enough
to auto-order or should escalate to a human instead. That's the actual test
of a forecasting design.

**BOUT — outro**
Flags Decide The Path. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a delegation question — does forecasting always mean spawning a subagent? |
| Wrong guess | B00 (WRITER LAW) | "always" corrected to "sometimes" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill folder's two scripts, and the exact flags (horizon, seasonal, promo, trend) that route to Path A vs. Path B |
| Anchor | the SKU-forecast decision itself, named at B00 and carried through NB01–NB03 without dropping it | source is a single worked mechanism throughout (one Skill, one decision), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB03 | "a low score doesn't mean the model is broken, it means escalate" / "a high score doesn't guarantee the number is right either — it just means nothing in the inputs suggested otherwise" — both failure directions of the confidence signal, stated together |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct restatement of the
`forecasting` Skill's own SKILL.md — the two scripts, the exact Path A / Path
B flag conditions (horizon, `is_seasonal`, `promo_next_month`, trend break),
the reason a subagent gets its own context window (the full 90-day history),
the confidence-below-0.6-escalates handoff to reorder-policy, and
`forecast_qty` being a computed output rather than a predicted fact. Per
`simple`'s ONE-FLAG LAW, when the source genuinely supports everything as
stated, no flag is fabricated.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro). This redo keeps that same 7-beat shape: B00 replaced 1:1 with
BrutalistHesitantWriter (carrying the wrong-guess pedagogy per WRITER LAW
instead of a dedicated beat); B01→NB01, B02→NB02 kept as one beat each;
B03's design-tell text (which had been corrupted by truncation in the
source — "compute it y", card body cut at "promos,") and BVDT's verdict
(flags/Path A-B, confidence < 0.6, forecast_qty as a model output, "same
flags, same path, same number") are merged into a single NB03, keeping the
two facts a general audience needs and can act on — the confidence
threshold and what the returned number actually is — and dropping the
Claude-harness-internals aside about `callable_agents` being a research-
preview feature with an inline fallback, which assumes a technical audience
simple/hai-simple doesn't target; Teardown framing is stripped to a plain
mechanism-and-consequence description, per the NO JUDGMENT register check;
BHTF kept as the your-turn handoff, rewritten as a fully self-contained
prompt (the source's version named "the forecasting skill" by file, which
only works if the viewer has that exact SKILL.md installed — this redo's
prompt instead states the scenario directly — a promo next month, a
30-day horizon — so it's runnable in any Claude conversation today, no
skill install required, while still testing the same reasoning: horizon +
promo routes to delegation, and promo-uplift uncertainty routes to a low
confidence score and an escalate, not auto-order); BOUT kept, re-skinned to
the Humanitarians AI outro. Total: B00 + NB01–NB03 + BCRY + BHTF + BOUT = 7
beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
