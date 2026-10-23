# PEDAGOGY — entity-resolution-and-the-golden-set (week 4)
*Entity Resolution and the Golden Set — Week 4 progress update · ai-explainer / claude-hai*

Third episode of the Private AI Valuation Agent series (there is no week 3 video). Same
chassis, same channel, same persistent voice as weeks 1 and 2. Source: `narration_script.md`
(271 spoken words, author-written, 2:00 target) plus `README.md`'s figure-to-beat map.

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | `ClaudeComposerAsk`. Opens on the Claude UI, ask lands **ANSWERED** with three output lines (COLD OPEN LAW). Personal intro kept short — week 1 did the introducing ✓ |
| B01 | EXECUTIVE SUMMARY | The BLUF: names are written freely, so if you cannot resolve them you cannot price anything. Two halves — a matcher and a test — and the test is the deliverable. States the whole idea, spends no reveals ✓ |
| B02 | WHY IT'S HARD | The problem's size: 128 spellings across seven companies, inside 3,204,853 names, with the real strings shown ✓ |
| B03 | THE GROUND TRUTH | The instrument: one labelled set, judging both systems ✓ |
| B04 | THE SCOREBOARD | The result — and the beat that refuses the flattering reading of it ✓ |
| B05 | ONE DOT | Why recall moved: one character, 85 holdings, the largest holder ✓ |
| B06 | THE REVERSAL | The author's own approved judgment overturned by the evidence ✓ |
| B07 | THE RETRACTION | What was done about it, and the rule that follows ✓ |
| B08 | NO THRESHOLD | The honest limit: four cases a run cannot be resolved by any cut-off ✓ |
| B09 | VERDICT | One-page recap; carries the Week 5 forward statement ✓ |
| B10 | HANDOFF | HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed ✓ |
| B11 | OUTRO | OUTRO LAW: title restate, `@HumanitariansAI` handle ✓ |

Act order: COLD OPEN → EXECUTIVE SUMMARY → PROBLEM → INSTRUMENT → RESULT → MECHANISM →
REVERSAL → RETRACTION → LIMIT → VERDICT → HANDOFF → OUTRO ✓

**Where this cut departs from the script.** The script has four body sections; they are split
into eight beats so no beat carries two ideas. Each split is a genuine seam:

1. *0:18 carried both the spelling problem AND the ground-truth set.* Split into B02 and B03.
   One is the problem's size; the other is the instrument built to measure it.
2. *0:42 carried both the scoreboard AND the dot that explains it* — the script's own shot note
   asks for two shots ("hold on the two numbers. Then just the two spellings"). Split into B04
   and B05.
3. *1:38 carried the retraction AND the threshold question* (the latter living in the Notes,
   with `w4-tie` mapped to that beat in the README). Split into B07 and B08.

No claim was added or dropped by the splits. The narration was expanded from 271 words to fit
eight body beats at the 45–70 word budget; every added sentence is connective or judgment, and
every added FIGURE is sourced from `figdata_week4.json`. Three wording changes are logged in
`FACTCHECK.md` ("Wording changed from the script, and why").

---

## Cold open + executive summary check

- B00 opens on the Claude UI, never a brand card ✓
- B00's ask lands answered — ASK→RESULT begins at the cold open ✓
- B01 states the whole idea in plain language. No "entity resolution", no "macro recall", no
  "confidence band" until B03–B08 earn them ✓
- The reel does not jump from cold open into a detail beat ✓

---

## ILLUSTRATE LAW audit

| Beat | Visual scheme | UI? |
|---|---|---|
| B00 | ClaudeComposerAsk | UI — the interface IS the subject (cold open) ✓ |
| B01 | `W4Bluf` — kinetic type + a dependency chain | illustration ✓ |
| B02 | `W4Spellings` — bar chart + a scrolling column of real strings | illustration ✓ |
| B03 | `W4GoldenSet` — one card forking into two systems | illustration ✓ |
| B04 | `W4Scoreboard` — metric table + a hardest-cases strip | illustration ✓ |
| B05 | `W4Dot` — two display-size spellings around an empty slot | illustration ✓ |
| B06 | `W4Reversal` — filed string, stamp, rows, anchor | illustration ✓ |
| B07 | `W4Retraction` — struck reason, three acts, two scores | illustration ✓ |
| B08 | `W4Tie` — tied rows + a failing cut-off | illustration ✓ |
| B09 | ClaudeVerdictArtifact | UI — the verdict artifact page ✓ |
| B10 | ClaudeComposerAsk | UI — the handoff ✓ |
| B11 | ClaudeTitleOutro | UI — the outro ✓ |

Eight body beats, eight different schemes. No two consecutive body beats share one ✓
Typing appears in exactly two beats — B00 and B10 ✓

**B03 and B08 are the pair that carries the episode's real argument.** B03 builds the
instrument; B08 shows the instrument's own limit. A reel that showed only B03 and B04 would be
a product demo. The reel earns the claim by keeping B08 in.

---

## Utility-framing lint

- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT ✓

Style: narration written dash-free per the author's confirmed preference ✓

---

## Honesty check (the core of this cut)

This is the most self-incriminating episode in the series so far, and the cut is built to keep
it that way rather than soften it.

- **B04 argues against its own author.** The narration says precision barely moved and that on
  the hardest cases the OLD system was cleaner. The scene renders that loss as a strip with the
  matcher's number beside the patterns' better one. The script's note ("Do not claim the matcher
  beat the patterns on precision") is obeyed literally ✓
- **B06 is the author's own approved judgment being wrong**, narrated in the first person: "I
  wrote a confident reason. I approved my own judgment." No hedging, no passive voice ✓
- **B07 keeps BOTH scores on screen at once.** Publishing only the post-fix number is precisely
  the failure the beat names, so the scene cannot show only one ✓
- **B08 shows a cut-off failing**, rather than implying a better threshold exists. Four cases a
  run going to a person is framed as the design, not an embarrassment ✓
- **B09 names the 8-of-322 figure out loud.** "Golden set" is a flattering phrase; the verdict
  card states that only eight labels are human-reviewed, and `FACTCHECK.md` row 20 records that
  one of those eight already turned out wrong ✓
- **B02's seven companies are asserted, not assumed.** The worklog records the source figure
  silently showing two watchlisted companies instead of Cerebras and Figure AI. The injection
  script asserts the count and the total and fails the build otherwise ✓
- **The LEI wording is the corrected wording.** Only one of the eight anchor holdings carries
  OpenAI's registered identifier; the on-screen note says "name OpenAI, **or** carry its
  registered identifier" (`FACTCHECK.md` row 16) ✓
- **No invented figures on screen.** Every number is a prop injected from `figdata_week4.json` ✓

---

## Length law

**Measured: 201.75s (3:21.8)** across twelve beats. Duration is an OUTPUT. The script targets
2:00 for the body; the four bookends are additive, and the series has settled around 2:35–3:22.

Per-beat narration budget, recounted against the final narration (body beats only; bookends
exempt):

B01 53w · B02 **43w** · B03 51w · B04 45w · B05 49w · B06 **71w** · B07 54w · B08 **67w**

Six of the eight sit inside 45–70. Two sit just outside, both deliberately, and the earlier
draft of this file wrongly claimed all eight were inside — corrected here:

- **B02 at 43w (2 under).** The script's own note nominates the Databricks-spellings sentence as
  the first thing to cut if the reel runs long. The beat is deliberately tight and the screen
  carries the evidence — seven bars, a total, and a scrolling column of real strings ✓
- **B06 at 71w (1 over).** The beat the script names as the strongest ("the strongest beat is
  *it was OpenAI the whole time*"). It needs the room to land, then pause ✓
- **B08 at 67w** — up from 57w in the first cut. The trailing-space finding was added to the
  narration after QC (see `BUILD-LOG.md` decisions 5–7), and the beat was re-voiced. Still
  inside the band ✓

---

## Source fidelity

Every number traces to `figdata_week4.json`, `README.md`, or `docs/worklog.md` — see
`FACTCHECK.md`, 20 rows, with rows 2, 12 and 16 flagged as the ones worth challenging.

The four source PNGs and their SVG sources travel with this reel in `pantry/` as REFERENCE for
the rebuild; they are never slotted as media (REBUILD LAW). They were moved out of the reel's
`images/` directory because `run.sh` uses `images/` for compile OUTPUT and would have mixed
them with rendered stills.

## Palette deviation (logged, deliberate)

Identical to weeks 1 and 2: the Mycroft figures use crimson `#C8102E` and ochre `#C8860E`; this
rebuild renders in the Claude fidelity skin (cream `#F2F0E9`, ink `#3D3929`, terracotta
`#D97757` as the ONE accent) because `ai-explainer` is a fidelity brand that may not be
retinted. **Palette change only — no datum, ordering, or label altered.**

---

**What the author signed off on**, having watched
`entity-resolution-and-the-golden-set-slate.mp4`:

1. The three structural splits above (4 script sections → 8 body beats), and the ~130 words of
   connective narration added to fill them.
2. The three wording changes logged in `FACTCHECK.md` — in particular dropping "last month's"
   as a datable claim, and rephrasing the ground-truth line so it does not imply the 322 labels
   are hand-made.
3. `FACTCHECK.md` rows 2, 12 and 16 — the universe-v1 filter, the hardest-cases precision loss,
   and the corrected LEI wording.
4. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
5. The palette deviation logged above.

VERDICT: PASS — signed by the author (Om Mali), 2026-08-23.