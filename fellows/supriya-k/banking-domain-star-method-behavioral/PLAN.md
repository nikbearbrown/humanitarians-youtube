# PLAN — banking-domain-star-method-behavioral (Deep Explainer)

**Status: DRAFT — awaiting user gate approval. Nothing past this file is generated yet.**

## Pattern being followed

`skills/make/deep-explainer/SKILL.md` (extends `ai-explainer` → `explainer`; pacing from
`duration-planner`; closing block from `your-turn`). Structural reference:
`projects/data-analyst-book/hai-interview-end-to-end/` — the only real precedent for this skill in
this toolkit, confirmed **fully rendered** on disk (27/27 beats, both final cuts exist) despite its
own stale `OVERVIEW.md` claiming otherwise. No `_qc/` folder was found for it, so its Gate V status
is unconfirmed — we hold ourselves to the same rigor fresh, not inherited "it must be fine."

Required spine: `B00` cold open → **ACT I…N** (documentary body, 4-8 beats/act) → **VERDICT** recap
→ **YOUR TURN** handoff → **OUTRO**. This is a materially different shape from the `cli-explainer`
video we just built — no CLI/code loop; the body is argument + worked example, not ask→code→run.

## Source

- **Framework**: `chapters/12-behavioral-round.md` — the universal STAR method (Situation, Task,
  Action, Result), the banking-specific competency layer (risk awareness, regulatory/control
  judgment, audit/examiner comfort), the three behavioral archetypes, the weak-answer vs.
  STAR-rewrite worked example ("Tell me about a time you found an error…").
- **Capstone application**: `chapters/14-full-loop-mock-interviews.md` — Daniel's five-stage mock
  loop, specifically **Stage 4 (Behavioral)**: his actual answer, scored 1/3 against the book's own
  rubric, and the resulting final-week time-allocation lesson.
- **Fact-check status**: `factchecks/MASTER_REPORT.md` lists Ch. 12 among the chapters with **zero
  errors found**; Ch. 14's one correction (a cross-reference/labeling drift in Stages 1 and 3) does
  not touch Stage 4 (Behavioral) at all — the material this video uses is untouched by that fix.

## Output location

`brutalist.art/projects/banking-data-analyst-interview-prep/banking-domain-star-method-behavioral/`
— same book-project folder as the SQL video, matching the established convention.

## Decisions from your last message (locked in)

- **Voice**: Kokoro `af_bella` (same as the SQL video, series continuity).
- **Register**: `Pragmatist` — the register `af_bella` is normally paired with in this toolkit
  (dry, practical, no-nonsense); this is a narration *style* choice, independent of the "hai"
  channel identity/handle, which we are still dropping entirely.
- **Persona/branding**: no persona name, no channel, no `@handle` — narration says "in for Supriya"
  in B00 and the OUTRO only, identical convention to both prior videos.
- **Paperwork**: matching the reference's *actual practice*, not the skill doc's fuller stated
  contract — i.e. `SHOTLIST.md`, `PROMPTS.md`, `FACTCHECK.md`, `PEDAGOGY.md`, `NARRATION-SCRIPT.md`,
  `RESEARCH-SUMMARY.md`, `VISUAL-PLAN.md`, `STATUS.md`, `ToDo.md`. **Skipping** `BUILD-PROMPT.md`,
  `BUILD-LOG.md`, and `SOURCES.md` (named in the skill doc, absent from the one real precedent).
  Also skipping the reference's redundant `SOURCES-FACTCHECK.md` duplicate of `FACTCHECK.md` — one
  copy of that content is enough.
- **VOX = 0% deviation**: disclosed explicitly in both `VISUAL-PLAN.md` (a "Lane-mix decision"
  section, matching the reference's exact section name) and `PEDAGOGY.md` (a "Deviation logged"
  section) — same justification as the reference: a framework/mock-interview topic has no
  archival-photo referent for the VOX (pantry-still) lane to animate.

## Open decision — palette (flag, not yet locked)

The reference used the `humanitarians` palette, tied to the `hai` persona we're dropping. I'm
defaulting to **`claude`** (cream `#FAF9F5` / ink `#3D3929` / one terracotta `#D97757` accent) for
series consistency with the SQL video, which already established this palette for this book's
video family in this toolkit. Flag if you'd rather use a different one (e.g. `newsprint`, matching
the whole-book trailer in the other repo).

## Beat arc — 4 acts + bookends, 22 beats total

| # | Beat | Act | Lane | Content |
|---|---|---|---|---|
| B00 | INTRO | — | (exempt) | Cold open — "in for Supriya" + the hook: banks don't grade STAR answers differently, they listen to a different half of the same story |
| 1 | Act card | I — The STAR Framework | CARD | "Act I — The STAR Framework" |
| 2 | Define S-T-A-R | I | MANIM | Situation/Task/Action/Result, four parts building on screen |
| 3 | The generic failure | I | REMOTION (QuoteCard) | "All Situation, no Result" — the universal STAR failure |
| 4 | Act card | II — What a Banking Panel Listens For | CARD | "Act II — What a Banking Panel Listens For" |
| 5 | Three competencies | II | MANIM | Risk awareness · regulatory/control judgment · audit/examiner comfort |
| 6 | The banking-specific failure | II | REMOTION (QuoteCard) | "I noticed the numbers looked off" (rejected) vs. the accepted version that names the escalation |
| 7 | Three archetypes | II | REMOTION (LabelChip) | Data-quality flag · audit/examiner request · stakeholder-vs-control conflict |
| 8 | Act card | III — Weak Answer, STAR Rewrite | CARD | "Act III — Weak Answer, STAR Rewrite" |
| 9 | The weak answer | III | REMOTION (QuoteCard) | The book's actual weak-answer quote (Ch. 12) |
| 10 | STAR rewrite — S+T | III | MANIM | Situation + Task from the book's rewrite |
| 11 | STAR rewrite — A+R, control named | III | MANIM | Action + Result, ending on the actual control named ("wrote a data-quality check into our dbt test suite…") — teal, matching the SQL video's right/wrong color convention |
| 12 | What's scored | III | REMOTION (StateCardPair) | Risk awareness · escalation · outcome/control — the three things the weak version omitted entirely |
| 13 | Act card | IV — Daniel's Full-Loop Mock | CARD | "Act IV — Daniel's Full-Loop Mock" |
| 14 | The five-stage loop | IV | MANIM | Domain vocab → SQL → Case → **Behavioral** → Systems design, Stage 4 highlighted |
| 15 | The prompt | IV | REMOTION (QuoteCard) | "Tell me about a time you found an error in your own or a colleague's work" |
| 16 | Daniel's answer | IV | REMOTION (QuoteCard) | His actual answer, stopping at "I fixed it and let my manager know" |
| 17 | The score: 1/3 | IV | MANIM | The book's own rubric row — STAR shape, no named escalation or outcome |
| 18 | The lesson | IV | MANIM | "Finish the thought out loud" — Behavioral gets the bulk of Daniel's final-week hours |
| VERDICT | Recap | — | (exempt) | STAR + the banking layer + Daniel's lesson, one artifact |
| YOUR TURN | Handoff | — | (exempt) | Draft your own STAR story for one archetype; explicitly name the control/escalation in the Result |
| OUTRO | Title re-read | — | (exempt) | Title restate + "in for Supriya" sign-off |

**Lane mix (body beats, 18 total, excluding bookends):** MANIM 7 (38.9%), REMOTION 7 (38.9%), CARD 4
(22.2%), VOX 0 — within the contract's MANIM 25-40% / REMOTION 30-45% bands; CARD absorbs the
remainder exactly as the reference's own histogram did (its actual split was manim 10/23, remotion
9/23, card 4/23 — same card count, same shape). No run exceeds 2 consecutive same-lane beats,
checked against the full sequence order above.

Target duration: the skill treats 5-10 min as the natural landing zone, not a padding target — at
roughtly ~2.9 words/sec planning rate and this act structure's content weight, I expect this to land
around 6-8 minutes once real narration is written and measured; final number is whatever the actual
audio locks to.

## Schema note (for the next gate, not this one)

Manim beats use `shot.graphic.manim: "B0X_ClassName"` (this skill's own key) — **not**
`shot.manim.scene_class` like the cli-explainer video used. Scene classes will still be named
`B0X_DescriptiveName(Scene)` for `run.sh`'s regex. Remotion beats will use `StateCardPair`,
`QuoteCard`, and `LabelChip` (all confirmed real, registered components) plus `ClaudeComposerAsk`
(bookends) and `ClaudeVerdictArtifact` (VERDICT beat).

## Gates (in order)

1. **This plan** — you review and mark it passed. *(current gate)*
2. **Paperwork set + `beat_sheet.json`** — written together, same as the SQL video's process.
3. **`scenes.py`** — the 7 Manim scene classes; smoke-tested before you review.
4. **Render gate** — `generate_audio_kokoro.py` (Gate P, blocked until you sign `PEDAGOGY.md`) →
   **Gate D1** (first compile is always the full-length slate previz — this is just `run.sh`'s
   existing `-slate.mp4` step, no extra action needed) → GATE F/A/W/L → Manim render → GATE B →
   Remotion render → GATE V → compile. **Gate D2** (`SHOPPING.md`) does not apply — VOX is 0%.

No paperwork, beat sheet, or scene code is written before you approve this plan.
