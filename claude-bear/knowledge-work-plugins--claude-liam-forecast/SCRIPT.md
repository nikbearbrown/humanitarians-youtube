# SCRIPT.md — Weighed, Not Predicted. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-forecast` (Teardown, walks the Anthropic `forecast` sales
skill — a weighted sales forecast with best/likely/worst scenarios, commit vs.
upside, and gap analysis) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold open
replaced with the BrutalistHesitantWriter; close carries the Humanitarians AI
skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed the forecast skill predicts which deals will actually close.
It doesn't — it weighs them. So: does Claude predict which deals close, or
just weigh the odds?

*(Text typed on screen: "Does Claude / predict / which deals / will close?" —
trigger word "predict" corrects to "weigh", landing on: "Does Claude weigh
which deals will close?")*

## Body — the mechanism, the anchor, the one flag, both directions

**NB01 — Pipeline becomes a number** (source B01/B02 anatomy+pipeline)
Forecast turns your pipeline into one number. You hand it deals — name,
amount, stage, close date — plus your quota. Each stage carries a default
probability: negotiation eighty percent, discovery twenty. Multiply amount by
probability, stage by stage, and add it up. That sum is the weighted
forecast.

**NB02 — One deal, weighed (THE ANCHOR, planted)**
Take one deal from that pipeline: Acme Corp, fifty thousand dollars, in
Negotiation, closing January thirty-first. At eighty percent, it adds forty
thousand to the weighted forecast — confident enough to sit in Commit, the
deals you'd stake your number on. Lower-confidence deals go in a separate
pile: Upside.

**NB03 — The one flag: your own data**
One flag: connect your CRM, and those stage probabilities stop being
defaults. The skill pulls your pipeline automatically, uses your team's
actual historical win rates instead, and tracks how the forecast moves over
time. Until then, every probability above is a generic assumption.

**NB04 — Commit can still slip (THE ANCHOR, paid off; direction A)**
Back to Acme Corp: no activity in fourteen days flags it for a re-engage,
even though it's sitting in Commit. A committed deal isn't a closed deal —
it's just the one you'd bet on, and the bet can still go wrong.

**NB05 — Low odds can still land (direction B)**
The other direction holds too. A Discovery-stage deal at twenty percent
isn't written off — it can still close, it's just not what you'd plan
around. And the gap analysis only tells you how far short of quota you are.
It never tells you which deals will close it.

## Close

**BCRY — carry-out**
The forecast weighs probability, not certainty — a stage-weighted number
tells you how big your pipeline is, never which deals inside it will
actually close.

**BHTF — your turn**
Your turn. Paste this into Claude: Here's my pipeline. Acme Corp, fifty
thousand dollars, in Negotiation, closing this month. TechStart, twenty-five
thousand, in Discovery. My quota is one hundred thousand this quarter. Give
me a weighted forecast — best, likely, and worst case — split into commit
versus upside, and flag anything at risk. That's the actual test of what a
forecast promises, and what it doesn't.

**BOUT — outro**
Weighed, Not Predicted. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a prediction question — does the forecast skill predict which deals close? |
| Wrong guess | B00 (WRITER LAW) | "predict" corrected to "weigh" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy |
| Mechanism | NB01 | the exact arithmetic: amount × the stage's default probability, summed |
| Anchor planted / paid off | NB02 → NB04 | Acme Corp, $50K, Negotiation, 80% — planted sitting confidently in Commit at NB02, returned at NB04 flagged for no-activity re-engage: same deal, same composition, the confidence turns out not to be a guarantee |
| One flag | NB03 | connecting a CRM swaps the generic default stage-probability table for the team's own historical win rates — everything upstream of that is a stated assumption, not measured fact |
| Both directions | NB04 / NB05 | NB04: a high-confidence (Commit) deal can still slip; NB05: a low-confidence (Discovery, 20%) deal can still land — stated as a pair |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

Exactly one inference flag, at NB03: the stage-probability table (negotiation
80%, discovery 20%, etc.) is the skill's own stated *default* — true only
until a CRM connection supplies the team's real historical win rates instead.
Everywhere else, the reel states the skill's arithmetic and its two named
buckets (Commit / Upside) as read directly from the source SKILL.md, with no
further hedging.

## Deliberately not claimed

- **Not "the model learns your team's patterns automatically."** The default
  probability table is generic until a CRM is connected — NB03 states this
  as the one flag rather than implying the forecast is always tailored.
- **No accusation that a rep is gaming the forecast.** Commit vs. Upside and
  the risk flags (stale close date, no activity, close-date-this-week-but-
  still-early) are the skill's own categories for managing uncertainty, not
  a judgment on anyone's honesty — Plain register states the mechanism and
  stops.
- **The Acme Corp deal is illustrative, not a real customer.** It is the
  worked example straight out of the SKILL.md's own "Option B: Paste your
  deals" sample block, reused as the reel's anchor.

## Handoff prompt (BHTF, read aloud)

> "Here's my pipeline. Acme Corp, fifty thousand dollars, in Negotiation,
> closing this month. TechStart, twenty-five thousand, in Discovery. My quota
> is one hundred thousand this quarter. Give me a weighted forecast — best,
> likely, and worst case — split into commit versus upside, and flag anything
> at risk."

Why it's worth running: it's fully self-contained (no skill install required,
no real CRM data needed) and tests the exact reasoning this reel just walked
through — a stage-weighted number, a Commit/Upside split, and a risk flag for
a deal that looks fine on paper but has no recent activity.

## Beat-count note (redo)

Source is 7 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BVDT (verdict) + BHTF (your turn) + BOUT
(outro), ~117s total. hai-simple's mandatory six-move spine (stakes, wrong
guess, mechanism, one flag, one anchor *planted and paid off as a pair*,
both directions, carry-out) needed a genuine anchor pair the source's spare
7-beat shape had no room for, so this redo expands the body from 3 beats to
5: NB01 (source B01+B02 merged — anatomy and pipeline collapsed into one
mechanism beat, since Plain register doesn't need the source's separate
"anatomy" vs. "pipeline" framing) then NB02–NB05, newly authored to carry a
concrete anchor (the SKILL.md's own "Acme Corp" sample deal, planted in
Commit, paid off flagged for re-engage) and both failure directions
explicitly, which the source's Teardown verdict (BVDT) never stated as a
pair. BVDT's "design tell"/verdict framing is dropped entirely (Teardown
judgment, not Plain) — its two true facts (same input → same output; the
skill's output is bounded by what the SKILL.md specifies) survive
redistributed into NB01 (the exact arithmetic) and BCRY (the carry-out's
"never which deals... will actually close"). BHTF is rewritten as a fully
self-contained prompt (the source's version named "the forecast skill" by
file, which only works if the viewer has that exact SKILL.md installed —
this redo's prompt instead states the pipeline directly, so it's runnable
in any Claude conversation today). BOUT kept, re-skinned to the
Humanitarians AI outro (`OutroSeries`). Total: B00 + NB01–NB05 + BCRY + BHTF
+ BOUT = 9 beats.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` /
`ClaudeVerdictArtifact`) with B00 as a typed composer ask (REMOTION, not
AI-VIDEO — the source never called a generation service). NO-GENAI/
NO-PANTRY LAW required no substitution beyond B00's cold open, which this
redo replaces per hai-simple's mandate anyway.
