# SCRIPT.md — One Script, Not One Call Each. (hai-simple redo)

Register: Plain. Persona: Liam, in for Bear. Voice: Kokoro `am_onyx`.
Redo of `claude-liam-weekly-report` (Teardown, walks the Anthropic
`weekly-report` cwc-workshops Skill — the weekly inventory report: which
sections to write, which files back them, and the one hard rule about how
to generate it) — question, facts, and body argument carried over;
narration re-registered to Plain (explain, then stop, no verdict); cold
open replaced with the BrutalistHesitantWriter; close carries the
Humanitarians AI skin.

## B00 — cold open (BrutalistHesitantWriter)
Someone assumed Claude calls a tool once per SKU to build this report. It
doesn't — it calls a tool only once, total. So: does Claude call a tool
once for the report?

*(Text typed on screen: "Does Claude / call a tool / per-SKU / for the
report?" — trigger word "per-SKU" corrects to "once", landing on: "Does
Claude call a tool once for the report?")*

## Body — anatomy, the one-script mechanism, both directions

**NB01 — A skill is a folder** (source B01, anatomy)
A skill is a folder Claude reads before it acts. This one is
weekly-report — the weekly inventory report. The file lays out four
sections to write every time: stockouts, low stock, open purchase orders,
and forecast risk. It also names exactly which files back each one — a
stock-levels file, a products file, a sales-history file, and an
open-orders file.

**NB02 — One script, not one call per SKU** (replaces source B02's generic
pipeline diagram + source B03's design tell; re-registered Teardown →
Plain)
The rule inside is explicit: write one script and run it once. The stock
file alone holds about sixty-seven thousand rows — far too many to check
SKU by SKU with separate tool calls. So one script loads every file,
computes stockouts and days of cover for all of them together, and prints
the finished report in a single pass. What that report actually contains
still depends on what's asked: the weekly version adds one more check —
any open purchase order older than its supplier's usual lead time gets
flagged as aging — while the daily sweep drops the open-orders and
forecast-risk sections and leads with whatever action was already taken.

## Close

**BCRY — carry-out**
Ask Claude for this report and it writes one script that reads every row
once, instead of checking each SKU by hand. Which sections that script
prints still depends on whether you asked for the full weekly review or
the shorter daily sweep.

**BHTF — your turn**
Your turn. Paste this into Claude: I have a stock-levels file with about
sixty thousand rows and a separate purchase-orders file. Give me this
week's inventory report — stockouts, low stock, open orders, and which of
those orders are now aging past their lead time. Would you check this row
by row with tool calls, or write one script that computes it in a single
pass? Show me what that script would need to read, and what the top of the
report would say.

**BOUT — outro**
One Script, Not One Call Each. Liam, in for Bear.

## Six-move audit

| Move | Beat | Note |
|---|---|---|
| Stakes first | B00 | the naive framing is a per-SKU-calls question — does building this report mean calling a tool once for every SKU? |
| Wrong guess | B00 (WRITER LAW) | "per-SKU" corrected to "once" IS the wrong-guess beat — hai-simple's hesitation IS the pedagogy; source has no separate wrong-guess beat to redistribute, so none is invented (beat-count discipline, see note below) |
| Mechanism | NB01–NB02 | the skill folder's four sections and four data files (NB01); the one-script rule and why (the ~67k-row stock file makes per-SKU tool calls impractical) (NB02) |
| Anchor | the weekly-report task itself, named at B00 and carried through NB01–NB02 without dropping it | source is a single worked mechanism throughout (one Skill, one report), not a planted-and-paid-off separate case — nothing to return to that hasn't stayed on screen the whole time |
| Both directions | NB02 | "the weekly version adds one more check — aging POs" / "the daily sweep drops the open-orders and forecast-risk sections and leads with actions taken" — both directions of the same cadence rule, stated together |
| Carry-out | BCRY | one sentence, survives repetition |

## One-flag audit

No inference flag in this reel: every claim is a direct restatement of the
`weekly-report` Skill's own SKILL.md — the four report sections, the four
backing data files, the "write one Python script via code execution... do
not make per-SKU tool calls" instruction, the ~67k-row size of
`stock_levels.csv`, the cadence table's exact contents dropped for the
daily sweep, and the aging-PO rule (elapsed days since placed compared
against the supplier's `lead_time_days`). Per `simple`'s ONE-FLAG LAW, when
the source genuinely supports everything as stated, no flag is fabricated.

## Beat-count note (redo)

Source is 6 beats: B00 (composer-ask cold open) + B01 (anatomy) + B02
(pipeline) + B03 (design tell) + BHTF (your turn) + BOUT (outro) — no BVDT
verdict beat in this source (unlike the `-forecasting` sibling). This redo
keeps that same 6-beat shape by finding the equivalent fat to trim: B00 is
replaced 1:1 with BrutalistHesitantWriter (carrying the wrong-guess
pedagogy per WRITER LAW instead of a dedicated beat); B01 becomes NB01
unchanged in scope (anatomy); B02's content — a generic "Read SKILL.md →
Execute → Return output" diagram that carries zero weekly-report-specific
facts (true of literally any skill teardown in the source's batch,
failing the "would still be true of a different video" test) — is dropped
outright rather than folded anywhere, freeing its slot; B03's design-tell
slot is replaced with NB02, which states the Skill's actual most
interesting fact (write one script, not one tool call per SKU, because the
stock file is ~67k rows) plus the cadence/aging-PO both-directions pair,
stripped of the source's generic Teardown verdict framing ("what it gets
right… what it bites") per the NO JUDGMENT register check; the freed B02
slot becomes BCRY, the mandatory carry-out beat this chassis requires that
the source (pre-dating the `simple`/`hai-simple` spine) never had; BHTF
kept as the your-turn handoff, rewritten as a fully self-contained prompt
(the source's version named "the weekly-report skill" by file, which only
works if the viewer has that exact SKILL.md installed — this redo's prompt
instead states the scenario directly — a ~60k-row stock file, a
purchase-orders file — so it's runnable in any Claude conversation today,
no skill install required, while still testing the same reasoning: one
script over per-SKU calls, and the report's exact sections); BOUT kept,
re-skinned to the Humanitarians AI outro. Total: B00 + NB01–NB02 + BCRY +
BHTF + BOUT = 6 beats, matching the source exactly.

No source beat was ai-video-prompt, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` /
`SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism`)
with B00 as a typed composer ask (REMOTION, not AI-VIDEO — the source never
called a generation service). NO-GENAI/NO-PANTRY LAW required no
substitution beyond B00's cold open, which this redo replaces per
hai-simple's mandate anyway.
