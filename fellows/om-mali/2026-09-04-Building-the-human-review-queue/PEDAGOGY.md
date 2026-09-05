# PEDAGOGY — building-the-human-review-queue (week 6)
*Building the Human Review Queue — Week 6 progress update · ai-explainer / claude-hai*

Fifth episode of the Private AI Valuation Agent series. Same chassis, same channel, same
persistent voice as weeks 1, 2, 4 and 5. Source: `narration_script.md` (441 spoken words,
author-written, 3:00 target) plus `README.md`'s figure-to-beat map.

**The central claim is a negative one about the software.** It routed, it grouped, it
presented — it decided nothing. The README calls that "the one thing not to get wrong on
camera", so the cut is built to make it the first thing a viewer sees rather than a
disclaimer at the end.

---

## Act structure audit

| Beat | Act | Check |
|------|-----|-------|
| B00 | COLD OPEN | `ClaudeComposerAsk`. Opens on the Claude UI, ask lands **ANSWERED** with three output lines (COLD OPEN LAW). Carries the requested self-introduction: "Hi, I'm Om Mali. This video is about…" ✓ |
| B01 | EXECUTIVE SUMMARY | The BLUF: 78% resolved unaided, 22% stopped and waited, nothing dropped — and the verb the software never performed ✓ |
| B02 | WHAT STOPPED | The population and the split, then why each holding stopped ✓ |
| B03 | THE REPETITION | The problem's shape: 42 cards are only 8 questions, and X.AI's 24 real filed spellings ✓ |
| B04 | THE KEY | The mechanism: the answer is keyed on the company, so the queue shrinks instead of growing ✓ |
| B05 | DURABILITY | Where a paused question actually lives, and the two-process test ✓ |
| B06 | THE UNPLANNED TEST | The crash — the script's nominated strongest beat, given its own frame ✓ |
| B07 | WHAT IT CAUGHT | The one real split, and the crash it would have been ✓ |
| B08 | THREE CAUSES | The honest limit: one trigger, three causes, and two corrected counts ✓ |
| B09 | VERDICT | One-page recap; carries the Week 7 forward statement ✓ |
| B10 | HANDOFF | HANDOFF LAW: a real prompt, read ALOUD verbatim and then discussed ✓ |
| B11 | OUTRO | OUTRO LAW: title restate, `@HumanitariansAI` handle ✓ |

Act order: COLD OPEN → EXECUTIVE SUMMARY → POPULATION → PROBLEM → MECHANISM → DURABILITY →
PROOF → PAYOFF → LIMIT → VERDICT → HANDOFF → OUTRO ✓

**Where this cut departs from the script.** The script has six sections; they become eight
body beats. Each split is a genuine seam:

1. *0:55 carried both the repetition AND the fix* — 42-cards-to-8-questions with X.AI's 24
   spellings, and then the company-level key that clears all 24. Split into B03 and B04. One
   is the problem's shape; the other is the mechanism that dissolves it.
2. *1:30 carried both the designed test AND the accidental one* — `interrupt()` writing to
   Postgres and the two-process check, then the database crash. Split into B05 and B06,
   because the script's own note says the crash is the strongest beat, and a beat that is
   sharing a frame with a systems diagram is not the strongest anything.
3. *2:00 carried both the Perplexity split AND the two look-alikes.* Split into B07 and B08.
   B07 is the one real finding; B08 is the limit that makes it non-trivial.

**The script's cut-if-long instruction WAS taken.** The note offers the second opening
paragraph as the first cut — "the project gets re-explained every week". One clause of it
survives in B00, the one that frames the actual difficulty. That is the only content dropped.

No claim was added or dropped by the splits. Narration was expanded to fit eight body beats at
the 45–70 word budget; every added sentence is connective or judgment, and **every added
FIGURE is injected from `figdata_week6.json` under an assertion.** Five wording changes are
logged in `FACTCHECK.md`.

---

## Cold open + executive summary check

- B00 opens on the Claude UI, never a brand card ✓
- B00's ask lands answered — ASK→RESULT begins at the cold open ✓
- B00 carries the requested opening line: *"Hi, I'm Om Mali. This video is about the human
  review queue I built this week, the part of the pipeline that knows when to stop and ask a
  person."* ✓
- B01 states the whole result in plain language. No "interrupt", no "checkpointer", no
  "company-level key" until B04–B05 earn them ✓
- The reel does not jump from cold open into a detail beat ✓

---

## ILLUSTRATE LAW audit

| Beat | Visual scheme | UI? |
|---|---|---|
| B00 | ClaudeComposerAsk | UI — the interface IS the subject (cold open) ✓ |
| B01 | `W6Bluf` — two halves, three verb chips, and a fourth struck through | illustration ✓ |
| B02 | `W6Funnel` — one bar splits, then fans into triggers | illustration ✓ |
| B03 | `W6Collapse` — two counters + 24 real filed strings scrolling | illustration ✓ |
| B04 | `W6Key` — 24 question marks collapsing onto one key, then 24 ticks | illustration ✓ |
| B05 | `W6Durability` — node chain, halt, store, two process lanes | illustration ✓ |
| B06 | `W6Crash` — before/after blocks around an outage rule | illustration ✓ |
| B07 | `W6Split` — two filed rows, a bracketed identical value, a struck −90% | illustration ✓ |
| B08 | `W6ThreeCauses` — three flagged steps, each with its own magnitude and cause | illustration ✓ |
| B09 | ClaudeVerdictArtifact | UI — the verdict artifact page ✓ |
| B10 | ClaudeComposerAsk | UI — the handoff ✓ |
| B11 | ClaudeTitleOutro | UI — the outro ✓ |

Eight body beats, eight different schemes. No two consecutive body beats share one ✓
Typing appears in exactly two beats — B00 and B10 ✓

**B03 and B04 are adjacent and both about X.AI, and must not read as one idea twice.** B03 is
a scrolling list of real strings — the argument is repetition, and it is made by volume. B04
is a collapse diagram — the argument is *keying*, and it is made by 24 marks becoming one card
and then 24 ticks. Different scheme, different claim: one shows the cost, the other shows the
fix.

**B05 and B06 are adjacent and both about durability.** B05 is a systems diagram of a designed
test. B06 is a counted before/after of an accident. Splitting them is what lets B06 be the
beat the script says it should be.

---

## Utility-framing lint

- "is critical for" — NOT PRESENT ✓
- "important to understand" — NOT PRESENT ✓
- "we'll cover" — NOT PRESENT ✓
- "in this video" — NOT PRESENT as a framing device. B00 says "This video is about…" **once**,
  as the author's explicitly requested opening line, and then never again ✓

Style: narration written dash-free per the author's confirmed preference ✓

---

## Honesty check

The temptation this week is the opposite of week 5's. Week 5 was a negative result that could
have been dressed up; week 6 is a working system that could be oversold — particularly the
crash, which is the most quotable moment in the reel and the thinnest evidence in it.

- **The software's role is stated as a subtraction, not a boast.** B01 shows three verbs it
  performed and one it did not, struck through on screen. The README calls this the one thing
  not to get wrong; it is beat one, not a footnote ✓
- **The crash beat names its own weakness.** One unplanned outage, run by accident, is not a
  durability guarantee — and the beat says so beneath the number rather than in the paperwork
  only ✓
- **78/22 is framed as the design, not a shortfall.** The word "finished" appears nowhere, and
  neither does any claim that the remaining 22% will shrink ✓
- **The collapse claim is bounded.** One answer clearing 24 cards is true of X.AI; 3 of the 8
  questions are company-level keys and the rest are single cards. The screen says so, so the
  best case is not presented as the general case ✓
- **The corrected count is on screen, not buried.** An earlier write-up said four split
  questions and "wrong three times out of four". It is three, and two-of-three. B08 carries
  the correction as a footnote *in the frame*, and the ratio is derived from the asserted
  count so it cannot drift back ✓
- **A second correction, found by reading the rendered frame.** The script says the three
  steps "looked identical — a price falling by exactly ten". Two are ×10; Anthropic's is
  **×4.0**. The rendered beat labelled each magnitude and so contradicted its own narration.
  The claim is now what the data actually supports: three steps tripped the same detector,
  and the magnitudes differ. `FACTCHECK.md` records the change ✓
- **The canary is reported without being leaned on.** 28 holdings of a similarly-named
  business were planted two months ago and the queue found them. The reel states the finding;
  `FACTCHECK.md` row 19 records that the plant itself is an author assertion ✓
- **No invented figures on screen.** Every number is a prop injected from
  `figdata_week6.json`, under assertions that fail the build ✓

---

## Length law

**Measured: 199.7s (3:19.7)** across twelve beats, from the Kokoro MP3s. Duration is an OUTPUT.
The script targets 3:00; the four bookends are additive, and the series has run
2:35 → 3:00 → 3:22 → 3:35 → 3:20.

Per-beat narration budget, counted against the final narration (body beats only; bookends
exempt):

B01 63w · B02 60w · B03 49w · B04 49w · B05 48w · B06 49w · B07 54w · B08 61w

**All eight sit inside the 45–70 band.** B07 is deliberately the slowest per-word beat in the
reel (54 words over 15.3s) because the script asks for the Perplexity share counts to be said
slowly — the whole split-versus-crash distinction lives in hearing them.

---

## Both orientations, from one source

As week 5, at the author's standing request: **16:9 (3840×2160) and 9:16 (2160×3840)**. The
vertical cut is a **re-layout, not a crop**. Every week-6 component reads its orientation from
`useVideoConfig()` and lays itself out natively — the funnel's segment labels stack, the graph
chain in B05 runs downward instead of across, B08's three cases go from a row to a column.
Both cuts render from the same components and the same props, so a number cannot differ
between them, and they carry the identical narration MP3s.

---

## Source fidelity

Every number traces to `figdata_week6.json` — see `FACTCHECK.md`, 20 rows, with rows 6, 12, 18
and 19 flagged as the ones worth challenging. Two of those four are author assertions about
the project's own code and run history rather than anything the figures prove, and they are
labelled as such.

The five source PNGs and their SVG sources travel with this reel in `pantry/` as REFERENCE for
the rebuild; they are never slotted as media (REBUILD LAW). They were moved there from the
folder root because `run.sh` uses `images/` for compile OUTPUT and the series keeps reference
art in `pantry/`.

## Palette deviation (logged, deliberate)

Identical to weeks 1, 2, 4 and 5: the source figures use red as the primary series and ochre
for annotation; this rebuild renders in the Claude fidelity skin (cream `#F2F0E9`, ink
`#3D3929`, terracotta `#D97757` as the ONE accent) because `ai-explainer` is a fidelity brand
that may not be retinted. **Palette change only — no datum, ordering, or label altered.** The
README's rule that red is "never danger, here it marks the human's share of the work" is
preserved in effect: terracotta marks the human's share throughout.

---

**What the author is being asked to sign off on**, having watched
`building-the-human-review-queue-slate.mp4`:

1. The three structural splits above (6 script sections → 8 body beats), and in particular
   giving the crash its own beat.
2. Taking the script's own cut — the second opening paragraph is gone, one clause kept.
3. The five wording changes logged in `FACTCHECK.md` — in particular speaking the exact 4,537
   rather than "four and a half thousand", and dropping the script's claim that the three
   price steps "looked identical" (Anthropic's is ×4.0, not ×10).
4. `FACTCHECK.md` rows 6, 12, 18 and 19 — the "code rejects a decision missing either" claim,
   the accidental crash test, the corrected three-not-four split count, and the canary.
5. The B10 handoff prompt, which is new to this cut and is read aloud verbatim.
6. The palette deviation logged above, and the dual-orientation build.

VERDICT: PASS — signed by the author (Om Mali), 2026-09-04.

Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather
than passed silently; the gate was re-run WITHOUT the override after signing and passes on its
own. Measured runtime 200.63s (3:21.0), identical in both orientations — the two masters carry
the same narration files, not two renderings of the same script.
