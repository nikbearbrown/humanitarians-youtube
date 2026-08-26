# Their Numbers, My Arrows — Reading an AI Announcement Without Adding to It

> ### Case study
> ## `hsbc-agentic-adjacent-ai`
>
> | | |
> |---|---|
> | **Subject** | HSBC Holdings plc — AI in and around Corporate & Institutional Banking |
> | **Case study title** | *HSBC: Agentic-Adjacent AI in Investment & Commercial Banking* |
> | **Week** | Week 18 · work video |
> | **Primary sources** | HSBC FY2025 Annual Results (25 Feb 2026) — presentation and analyst-call transcript; FY2024 Annual Results (19 Feb 2025) |
> | **Reference implementation** | [`hsbc-reference-implementation/`](hsbc-reference-implementation/) |

An **8:33** film at **3840×2160**. Presented by Tanmay Kulkarni for Humanitarians AI.
Narration is local Kokoro (`af_bella`); no paid APIs in the build.

---

## What the film teaches

HSBC is unusually good source material. It publishes its AI figures in dated, primary,
self-labelled form — a results presentation, an analyst-call transcript, named speakers — and it
is careful to say which programmes are separate from each other. That precision is what makes the
film possible: **when a company is this exact, any imprecision left in the story is the reader's,
not theirs.**

So the film is about the reader. It builds a two-column ledger and audits it line by line:

| WHAT HSBC ACTUALLY SAID | WHAT I ADDED |
|---|---|
| 60% faster unit tests, 5x faster patching | *AI made them faster, so fewer people* |
| 1,165 applications retired, c.36% of target | *The numbers imply a method* |
| $1.2bn simplification savings realised | *$1.5bn means one thing* |
| $1.5bn saves, to the bottom line | *Somebody must have got this wrong* |
| $1.5bn reallocation, into growth | *Their coding tools are "not agentic"* |

Every entry on the left carries a dated source. Every entry on the right is **the author's own
inference**, and the film cancels them one at a time on screen. The last one survives only as a
labelled reading — *"my reading, revisable"* — with the condition that would overturn it stated
in the frame: *if HSBC describes these tools in agentic terms, this is wrong and changes.*

The teach is the ledger itself: a habit the viewer can run on any announcement they read.

## The turn

Two sentences from the **same transcript, the same morning**. In full, as HSBC said them:

> "We are taking $1.5 billion of annualised simplification saves straight to the bottom line,
> with immaterial revenue impact."
>
> "We are also making positive progress with the reallocation of circa $1.5 billion from
> non-strategic or low-returning businesses, the medium-term intent being to reallocate these
> costs to areas of competitive strength and generate accretive returns."

The film shows each sentence up to the point that carries the comparison, with the omission
marked — `saves straight to the bottom line …"` and `low-returning businesses …"` — attributed on
screen to the dated transcript. The words shown are exact and neither omitted clause changes what
the quoted span says, but a film arguing against adding to what someone said should not present a
shortened sentence as a whole one, so the ellipsis is on screen.

Same figure, two different things — money being **kept** and money being **moved**. Nobody
misreported it. It is simply what happens when one number does two jobs in one document, and it
is the strongest available argument for reading the source before drawing an arrow between facts.

**This beat replaced a weaker one.** The film was planned around two named outlets that had
allegedly conflated HSBC's $1.8bn severance figure with AI investment. Both were read directly.
**Neither had made that error** — one explicitly distinguishes reallocation from new spending. The
accusation was cut, and going back to HSBC's own transcript produced better evidence than the
original plan had. A film about not repeating other people's connections could not ship an
accusation it had taken on trust. The full record is in
[`VERIFICATION.md`](VERIFICATION.md).

## Files

- **`beat_sheet.json`** — the complete beat-by-beat build: narration, measured audio durations,
  and every Manim scene and Remotion component used across all 16 beats.
- **`FACTCHECK.md`** — the claim-by-claim audit: verdict, evidence, source and any correction
  applied, for every beat.
- **`VERIFICATION.md`** — the primary-source verification pass, including the two outlets that
  were cleared and the HSBC transcript quotes that replaced them.
- **`hsbc-agentic-adjacent-ai-CASE-STUDY.md`** — the primary-sourced case study the film is
  built from. Every HSBC figure traces here.
- **`hsbc-reference-implementation/`** — browsable source for the review-gated pipeline the film
  refers to: Intake → Assistant → Review Gate → Orchestrator, with its test suite.
- **`PEDAGOGY.md`** — thesis, method, structure, evidence discipline, the PROOF rubric score and
  the GATE P sign-off.
- **`QC-REPORT.md`** — the full build log: every defect found by looking at frames or measuring
  output, and the final verification.

The final cut is uploaded to the episode directly and is not committed here.

## How it was built

Free/local toolkit — Kokoro TTS, Manim and Remotion, no paid APIs. Motion is **62% Manim**
(the ledger changing state) and **38% Remotion**, a deliberate inversion of the previous film's
94% Remotion monoculture: variety comes from one artifact being audited, not from a new card per
beat.

Every figure on screen is HSBC's own, self-reported and unaudited, and the frame says so.

## Verification

| Check | Result |
|---|---|
| Resolution | 3840×2160 |
| Duration | 513.61s (8:33), equal to the sum of measured audio |
| Slots | 16/16 filled |
| Animation stretch | 1.00× on all 10 Manim beats |
| Gate V (frame QC) | 0 BLOCKER, 0 MAJOR across 32 frames |
| PROOF Phase 3 | clear-for-public · teaching 12/12 · production gate PASS |

This is a **deliverables-only** folder. The working folder — the narration script, the read-aloud
script, the shot list, the PROOF review, the Manim scene source and the per-beat renders, mp3s and
conformed clips — is kept outside the repo and deliberately not shipped here.
