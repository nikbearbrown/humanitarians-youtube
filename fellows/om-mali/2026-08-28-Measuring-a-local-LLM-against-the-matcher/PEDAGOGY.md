# PEDAGOGY — measuring-a-local-llm-against-the-matcher (week 5)
*Measuring a Local LLM Against the Matcher — Week 5 progress update · ai-explainer / claude-hai*

Fourth episode of the Private AI Valuation Agent series. Same chassis, same channel, same
persistent voice as weeks 1, 2 and 4. Source: `narration_script.md` (306 spoken words,
author-written, 2:00 target) plus `README.md`'s figure-to-beat map.

**This week is a negative result.** The model lost. The whole cut is built to report that
without apologising for it and without softening it into a "learning".

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | `ClaudeComposerAsk`. Opens on the Claude UI, ask lands **ANSWERED** with three output lines (COLD OPEN LAW). Opens with the requested self-introduction: "Hi, I'm Om Mali. This video is about…" ✓ |
| B01 | EXECUTIVE SUMMARY | The BLUF: the rules keep the job, the model lost about five points of precision, and it was wrong in exactly one direction. States the whole result before showing any of it — deliberately spends the ending in the first twenty seconds ✓ |
| B02 | THE TEST | Parity of evidence. Four fields given, two withheld, 322 calls, zero failures ✓ |
| B03 | THE RESULT | Five points, then the same error re-counted in records ✓ |
| B04 | HOW IT FAILS | The mechanism, at its worst: an invented corporate fact ✓ |
| B05 | HOW IT FAILS | The same mechanism, costing 32 holdings instead of 1 ✓ |
| B06 | NOTHING TO FIND | The row that proves there was never a right answer to get ✓ |
| B07 | THE FINDING | The one the script calls strongest: it was completely sure, and it was wrong ✓ |
| B08 | THE THING I TURNED OFF | The honest version of the one positive result ✓ |
| B09 | VERDICT | One-page recap; carries the pre-commitment and the Week 6 forward statement ✓ |
| B10 | HANDOFF | HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed ✓ |
| B11 | OUTRO | OUTRO LAW: title restate, `@HumanitariansAI` handle ✓ |

Act order: COLD OPEN → EXECUTIVE SUMMARY → SETUP → RESULT → MECHANISM ×3 → THE FINDING →
THE EXCEPTION → VERDICT → HANDOFF → OUTRO ✓

**Where this cut departs from the script.** The script has five body sections; they are split
into eight beats so no beat carries two ideas. Each split is a genuine seam:

1. *1:00 carried three failure examples in one section* — and the script's own shot note asks
   for "one example per beat", plus "let the Fidelity code sit on screen alone". Split into
   B04, B05 and B06 exactly as the note asks.
2. *0:42 and 1:32 stay whole* as B03 and B07 — neither carries a second idea.
3. The opening section is split into B00 (the ask, answered) and B01 (the BLUF), the standard
   series bookend structure rather than a content split.

The narration was expanded from 306 words to fit eight body beats at the 45–70 word budget.
Every added sentence is connective or judgment; **every added FIGURE is injected from
`figdata_week5.json` under an assertion.** Four wording changes are logged in `FACTCHECK.md`.

**The script's cut-if-long instruction was not needed.** The note says to drop the Scaled
Agile example at 1:00 to land on 2:00. Because the bookends are additive here and the series
has settled at 2:35–3:35, the beat is kept: it is the example where the cost jumps from 1
holding to 32, which is the evidence for B03's records argument.

---

## Cold open + executive summary check

- B00 opens on the Claude UI, never a brand card ✓
- B00's ask lands answered — ASK→RESULT begins at the cold open ✓
- B00 carries the requested opening line verbatim in form: *"Hi, I'm Om Mali. This video is
  about measuring a local language model against the rule based matcher that already works…"* ✓
- B01 states the whole result in plain language. No "macro precision", no "band policy", no
  "veto" until B03–B08 earn them ✓
- The reel does not jump from cold open into a detail beat ✓

---

## ILLUSTRATE LAW audit

| Beat | Visual scheme | UI? |
|---|---|---|
| B00 | ClaudeComposerAsk | UI — the interface IS the subject (cold open) ✓ |
| B01 | `W5Bluf` — two system cards, a drawn delta bar, a verdict stamp | illustration ✓ |
| B02 | `W5Setup` — four field cards + struck withheld chips + counting run stats | illustration ✓ |
| B03 | `W5Scoreboard` — precision rows, then a UNIT SWITCH into record bars | illustration ✓ |
| B04 | `W5InventedFact` — a verbatim quotation, struck left-to-right | illustration ✓ |
| B05 | `W5Substring` — shared characters lit in both strings + 32 record marks | illustration ✓ |
| B06 | `W5CodeAlone` — twelve character slots alone on the cream, three lit | illustration ✓ |
| B07 | `W5Confidence` — 322 dots; sure-and-wrong solid, unsure-and-wrong hollow | illustration ✓ |
| B08 | `W5Veto` — direction counters, four rows, a struck 1.0000 | illustration ✓ |
| B09 | ClaudeVerdictArtifact | UI — the verdict artifact page ✓ |
| B10 | ClaudeComposerAsk | UI — the handoff ✓ |
| B11 | ClaudeTitleOutro | UI — the outro ✓ |

Eight body beats, eight different schemes. No two consecutive body beats share one ✓
Typing appears in exactly two beats — B00 and B10 ✓

**B04, B05 and B06 are three failure beats in a row and must not read as three of the same
slide.** They are deliberately three different arguments: B04 is a QUOTATION struck (the model
asserted something false), B05 is a SUBSTRING lit in two strings and then priced in record
marks (the model matched on characters), B06 is a nearly empty frame with twelve slots (there
was nothing to match at all). Different scheme, different evidence, escalating cost: 1 holding
→ 32 → 8-with-no-right-answer.

---

## Utility-framing lint

- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT as a framing device. B00 says "This video is about…" **once**,
  as the author's explicitly requested opening line, and then never again ✓

Style: narration written dash-free per the author's confirmed preference ✓

---

## Honesty check (the core of this cut)

A negative result is easy to publish dishonestly — by burying it, by hedging it, or by
finding a silver lining and leading with that. The cut is built against all three.

- **The result is the first thing said.** B00 says "It lost" in the cold open; B01 is the whole
  verdict before any evidence. There is no reveal to protect and nothing is held back ✓
- **The one positive result is deliberately de-emphasised.** The veto policy scores a perfect
  1.0000 — and it is beat EIGHT, after every failure, with the sample size (four rows) rendered
  at the same visual weight as the score and struck by SWITCHED OFF. Leading with it would have
  been the dishonest cut ✓
- **The flattering number is excluded on purpose.** On the hardest-cases subset every model
  policy scores 100%, because that subset excludes the rows where nothing should match — the
  only rows the model damages. It is true and misleading at once, so it is in `FACTCHECK.md`
  and nowhere on screen ✓
- **B07 kills the author's own stated plan.** The review queue was going to be sorted by model
  confidence. It cannot be. The beat says so and does not propose a replacement it has not
  tested ✓
- **The model is not called useless.** B08 lands on "a decent sceptic and a poor proposer" —
  mis-scoped, not worthless. The script's note asks for exactly this distinction ✓
- **The scope of the claim is kept narrow.** One model, one size, one quantization. The reel
  never says AI cannot do this; `FACTCHECK.md` records that no larger model was tried and
  calls it an open question ✓
- **The pre-commitment is the point, and it is stated as one.** B09: "The plan said keep the
  rules if there is no lift. There is no lift." A negative result decided in advance is
  evidence; one rationalised afterwards is not ✓
- **The one unproven line is flagged rather than smoothed.** B04's rebuttal — that no
  parent-company relationship exists — rests on the author's own knowledge, not on a committed
  artifact. `FACTCHECK.md` row 13 says so explicitly ✓
- **No invented figures on screen.** Every number is a prop injected from `figdata_week5.json`,
  under assertions that fail the build ✓

---

## Length law

**Measured: 215.5s (3:35.5)** across twelve beats, from the Kokoro MP3s. Duration is an OUTPUT.
The script targets 2:00 for the body; the four bookends are additive, and the series has run
2:35 → 3:00 → 3:22 → 3:35.

Per-beat narration budget, counted against the final narration (body beats only; bookends
exempt):

B01 67w · B02 58w · B03 51w · B04 67w · B05 53w · B06 65w · B07 67w · B08 63w

**All eight sit inside the 45–70 band.** The reel runs longer than week 4 not because the beats
are longer but because there are three failure beats where week 4 had two mechanism beats.

---

## Both orientations, from one source

New this week, at the author's request: the reel ships in **16:9 (3840×2160) and 9:16
(2160×3840)**. The vertical cut is a **re-layout, not a crop**. Every week-5 component reads its
orientation from `useVideoConfig()` and lays itself out natively — side-by-side pairs become
stacked, the 322-dot grid reflows from 26 columns to 16, type is re-sized rather than scaled
down. Both cuts render from the same components and the same props, so a number cannot differ
between them. The `-916` compositions are registered under the toolkit's existing ONDA-CHECK
naming so `shorts.py` will find them rather than centre-cutting a landscape frame.

Both cuts carry the identical narration MP3s, so the two masters are the same edit.

---

## Source fidelity

Every number traces to `figdata_week5.json` — see `FACTCHECK.md`, 20 rows, with rows 3, 9, 13
and 18 flagged as the ones worth challenging.

The five source PNGs and their SVG sources travel with this reel in `pantry/` as REFERENCE for
the rebuild; they are never slotted as media (REBUILD LAW). `README.md`'s rule that they must
not be copied into `images/` is observed — the toolkit writes compile output there.

## Palette deviation (logged, deliberate)

Identical to weeks 1, 2 and 4: the Mycroft figures use crimson `#C8102E` as the primary series
and ochre `#C8860E` for annotation; this rebuild renders in the Claude fidelity skin (cream
`#F2F0E9`, ink `#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a
fidelity brand that may not be retinted. **Palette change only — no datum, ordering, or label
altered.** The README's note that red is "never danger" in the source figures is preserved in
effect: terracotta here marks the subject of each beat, not a warning.

---

**What the author is being asked to sign off on**, having watched
`measuring-a-local-llm-against-the-matcher-slate.mp4`:

1. The three-way split of the 1:00 failures section into B04/B05/B06, and the connective
   narration added to fill eight body beats at the 45–70 word budget.
2. Keeping the Scaled Agile example the script offers to cut, and why (it is the evidence for
   B03's records argument).
3. The four wording changes logged in `FACTCHECK.md` — in particular the on-screen qualifier
   that stops 1 → 196 reading as a 196× multiplier, and the shortening of the veto holding
   names at the exposure clause.
4. `FACTCHECK.md` rows 3, 9, 13 and 18 — the 11 candidates, the micro/macro record count, the
   unproven parent-company rebuttal at B04, and the 12-of-15 confidence finding.
5. The decision to exclude the flattering hardest-cases 100% entirely.
6. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
7. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS — signed by the author (Om Mali), 2026-08-28.

Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather
than passed silently; the gate was re-run WITHOUT the override after signing and passes on its
own. Measured runtime 215.11s (3:35.1), identical in both orientations — the two masters carry
the same narration files, not two renderings of the same script.
