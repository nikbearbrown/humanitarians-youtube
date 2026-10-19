# BUILD-LOG — grounding-an-ai-debt-tracker-in-real-sec-filings

AI Debt Tracker, **week 1**. `brutalist.art`, skill `ai-explainer`, channel `claude-hai`.
Free and local end to end — Kokoro TTS, Remotion, ffmpeg. **`$0.00` spent, no API key used.**

---

## What the source material was, and what it wasn't

The folder arrived with `narration_script.md` (author-written, 3:00 target, 438 words), a
short `description.txt`, an empty `images/`, and six figures in `pantry/` — four carried
forward from week 0 (`adt-w0-borrowing`, `-pipeline`, `-feasibility`, `-model`) and two new
(`adt-w1-levels`, `adt-w1-bakeoff`).

**There was no `figdata.json`.** The script's "Where every number comes from" table names the
project files each figure was generated from, but those live in the AI Debt Tracker repo, not
here. `figdata.json` was therefore written by transcribing the author's own published results
out of the six SVGs — which carry every datum as geometry *and* as text — and cross-checking
each against the script's source table. Where the two disagreed, neither was taken on trust:
the SVG's bar geometry was recomputed as a ratio and both readings had to agree. All of them
did (e.g. `adt-w1-bakeoff`'s 295.8/300 = 0.986 = 141/143; its pass rule at x=445 over a track
from 190 to 490 = 0.85).

`description.txt` was preserved as **`description-source.txt`** before this build wrote the
long-form version over it.

## The week-0 reel is gone

`2026-10-16-Feasibility-testing-an-AI-debt-tracker` was not on disk when this build started —
masters, beat sheet and paperwork with it. Its four figures survive here in `pantry/` as
`adt-w0-*`, and its Remotion components survive in the toolkit as
`runtime/remotion/src/AiDebtTracker.tsx` with their `Root.tsx` registrations intact. Nothing
was recreated; this is recorded so a later reader does not conclude the week-0 scenes are dead
code. `adt-w0-model.png` is retired by the author's own note — its 8B baseline is superseded
by this week's bake-off — and does not appear in this reel.

## Structure: 7 script sections → 8 body beats

| Decision | Why |
|---|---|
| **0:32 split into B02 (the design) and B03 (the cut-off)** | The script's own shot note says the section has two movements and that the second "is the line that makes every later number trustworthy". At ~75 spoken words it is also the longest section. One frame cannot hold a four-stage pipeline *and* a grading relation without one of them becoming decoration. |
| **1:18 and 1:50 kept as separate beats (B05, B06)** | `adt-w1-levels.png` carries both the partition and the bottom strip. They are two arguments — a recount, and a split with a score — and the second is not a caption on the first. |
| **B08 added — a limits beat** | Not in the script's section list. Every episode in this series ends on its own limits, and the content is entirely from the script's Notes, which otherwise reach no frame. |
| **Oracle's partial 10-Qs moved from the voice to the frame** | The script marks that line as the one to drop if the cut runs long. It survives as a written example beside Microsoft's, costing no seconds. |
| **"Wrong almost half the time" → "wrong in twenty-one of those forty-six"** | "Almost half" is true of the conservative count and of nothing else said aloud. The raw 33 of 46 is printed beside it. |

Resulting edit: **12 beats** — B00 cold open, B01–B08 body, B09 verdict, B10 handoff, B11 outro.
Body beats 54–68 words (band 45–68), 731 words total, **213.74 s (3:33.7)** measured.

The script targets 3:00 for its own seven sections. The four bookends this channel requires are
additive, as in every episode of the series (week 11 ran 212 s on the same structure).

## Scenes

`runtime/remotion/src/GroundingTheDebtTracker.tsx` — eight components, registered twice in
`Root.tsx` (1920×1080 and 1080×1920 under the `916` name). The file imports nothing from
`AiDebtTracker.tsx` or the week 1–11 reel files, by series convention: every earlier signed
master stays re-renderable byte-identically whatever this week needs.

The chassis (`Stage`, `Header`, `Source`, `FootNote`, `MarkedBar`, the `f(landscape, portrait)`
helper) was copied forward from `AiDebtTracker.tsx`, including its two hard-won fixes: the
value column in `GDTBorrowing` that stops `$121bn` bleeding past the title-safe edge, and the
verdict line that takes its own full-width row in portrait rather than relying on `flexWrap`.

**B05 is the one new drawing idea.** Three bars would invite a comparison of 15 against 4
against 6, which is not the beat. The beat is that *one fixed set of 25 companies splits
differently once coverage is measured*, so the 25 is drawn once, whole, as a single partitioned
row, and the assumption is drawn as a dashed bracket **over** it.

## Defects found and fixed

1. **GATE V FAILED on 16:9 — 2 BLOCKERs, `edge-bleed` on B05.** The "assumed 21" caption was
   placed to the *right* of the bracket's end. At 21 of 25 the bracket already reaches 84% of
   the content width, so there is no room out there for a caption of any length — this was a
   design error, not a text-length error. The caption now sits **above** the bracket in a box
   exactly as wide as the bracket and right-aligned to its end, which also reads better: it
   belongs to the bracket rather than floating beside it.

2. **B09 read "4.3× their 28bn five-year average"** — a missing dollar sign in one f-string,
   on a frame where every other money figure carries one. Caught by reading the frame; no gate
   checks currency symbols.

3. **The 4–4 tie rendered with an ASCII hyphen** against en-dashes everywhere else in the reel
   (`2020–2024`, `1–2 years`). Fixed in `figdata.json` so B05's gate note and B08's limit both
   pick it up — the same class of defect as week 11's `->`.

4. **Portrait underfilled on six of eight body beats** (B01, B02, B04, B05, B06, B07) on the
   first portrait read. Not wrong, just small — the failure mode caught early for the fourth
   week running. 73 `f(landscape, portrait)` values were raised; the landscape half of every
   one is unchanged, so the 16:9 master did not need re-rendering. Details in
   `vertical/README.md`.

5. **`make_vertical.py` would have refused this reel** under the regex it shipped with in week
   11. That version matched `W\d+[A-Za-z]\w*` — a naming convention from the Private AI
   Valuation series — so `GDTBakeoff` and `GDTLevels` looked unregistered. It now matches the
   **registration tuple shape** Root.tsx actually uses, `['<Id>', <Component>, <schema>],`,
   which is the thing that is stable. This is the second time that regex has refused a reel
   whose 916 compositions were present; widening it by one character in week 10 was treating
   the symptom.

6. **GATE P did not hold, and the cause was in this reel's own paperwork.** Audio was
   generated with the gate ON while `PEDAGOGY.md` read `VERDICT: PENDING`, and the gate
   reported pass. `generate_audio_kokoro.py` searched the WHOLE FILE for the substring
   `VERDICT: PASS`; the PENDING block I had written underneath the verdict carried the
   instruction *"Replace this line with `VERDICT: PASS — signed by the author…`"*, so the
   magic string was present in an unsigned document. The gate was satisfied by its own
   instructions for satisfying it.

   Hardened: `gate_p_signed()` now finds the **first VERDICT token on a line** and requires
   that *it* says PASS. A line whose verdict is PENDING no longer counts however many times
   it quotes the word PASS afterwards; a line where the phrase is backticked or quoted, or
   buried more than three words into a sentence, is prose about the gate rather than a
   signature. A short label before it is fine, so `**GATE P VERDICT: PASS**` still signs.

   **Checked against all 134 `PEDAGOGY.md` files in the fellows tree before keeping it.**
   Exactly four change behaviour, and all four say `VERDICT: PENDING` in as many words:
   `Muskan-k/2026-08-09-vendor-intel-identity-fix`, `Muskan-k/2026-08-22-brief-eval-harness`,
   `Muskan-k/2026-08-28-open-vs-closed` and `chaitanya-m/2026-08-28-what-is-a-concept-map`,
   each of which ends its PENDING line with *sign "VERDICT: PASS" after review*. The old gate
   passed all four. **No signed reel is newly refused** — including five of Divij Pawar's,
   which sign as `**GATE P VERDICT: PASS**`, and two of Mohammed H's, which sign as
   `VERDICT: [ PASS ]`. A first draft of this fix did refuse the `GATE P` form; the sweep is
   what caught it.

   Nothing downstream changed here: the author has since signed, the audio was never
   regenerated, and the delivered masters are the ones that cleared GATE V.

## What GATE V did not catch, again

The gate checks edge bleed, canvas fill and contrast. Across twelve episodes it has been blind
to: overlap; whether a number is the *right* number; whether a source line cites a file
containing the claim; whether a caption describes the chart beneath it; an empty element versus
an intentional one; whose words are on the frame; and whether a bar measures the thing the beat
is about. This week add: **it does not check that money figures carry a currency symbol**, and
it passed every portrait frame that was half-empty.

Defects 2, 3 and 4 above were all found by reading frames, not by the gate.

## Toolkit changes

- `runtime/remotion/src/GroundingTheDebtTracker.tsx` — new, reel-local.
- `runtime/remotion/src/Root.tsx` — one new `<Folder>` registering the eight scenes twice.
- `runtime/scripts/generate_audio_kokoro.py` — **GATE P hardened** from a whole-file substring
  search to a verdict-line match. See defect 6. This changes gate semantics for every reel in
  the toolkit: a `PEDAGOGY.md` that merely mentions `VERDICT: PASS` in prose no longer opens
  the gate. Every signed reel in this series carries the verdict on its own line and is
  unaffected.
- No change to any shared `scenes/` component or to any other gate. The unknown-prop lint
  added in week 10 stayed **silent for every beat of both cuts**, including the bookends,
  which is what correct props look like.

## Verification

```
GATE L   clean, first run
GATE V   16:9  FAILED (2 BLOCKER) → fixed → 0 BLOCKER / 0 MAJOR, 24 frames
         9:16  0 BLOCKER / 0 MAJOR, 24 frames
         both re-run with --mp4 pointed at the exact delivered file
PROOF    12 beats: 8 SHOW / 4 justified-HOLD / 0 PUNT
GATE P   PASS — signed by the author (Om Mali), 2026-10-16, after watching the slate cut.
         The gate itself was broken during this build and has been fixed; see defect 6.
         Audio was NOT regenerated after signing.
GATE F   not triggered (no Manim beats)
COST     $0.00
```
