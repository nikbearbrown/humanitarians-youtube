# SHOTLIST — vox-comma-orphan

**Why a Dataset With Zero Missing Values Can Still Be Missing Your Data** · 16:9 · ~93s est. (11 beats)
Accents: dusty navy `#3D5A80` = matched/joined/counted · crimson `#BF3339` = orphaned/dropped/uncounted (the comma is crimson) · gold `#F5D061` = editor's pen (once per graphic).
Source: chapter 5, the BioTechCo trace — one mechanism only: a punctuation-blind join fragments one filer into buckets that never meet.
Card exclusions honored: no six-step procedure · no normalization code · no fuzzy-matching fix · **no base-rate / Bayes** (that's candidate 05 — no 0.68→0.38, no 8% prior) · no verb taxonomy.

Shot-type histogram: CARD 2 · STILL 1 · DOCUMENT 1 · GRAPHIC 4 · COMPOSITE 3 — max consecutive same-type: 2 (B04–B05). Lint: pass.

---

## B01 — CARD (title) · own · ~10.5s
Cue: "The audit runs clean. Zero missing values…"
Copy: **Why a dataset with zero missing values can still be missing your data** / sub: *the gap lives between two tables*

## B02 — STILL · ai · kenburns · ~9.0s  ← MEDIA SLOT (the only generated plate)
Cue: "Here's the report. Missing values: zero. A green check."
Slot: `media/B02.png`
t2i prompt: printed screenshot of a tidy data-quality audit report, a summary table with a highlighted row reading 'Missing values: 0' beside a green checkmark, pinned like a clipping to aged newsprint, desaturated flat print reproduction, editorial collage
Synthetic — disclosure line in credits. `shot.focus` toward the "0" + check after the plate lands.

## B03 — DOCUMENT · own · highlight · ~8.0s
Cue: "…missing means one thing: an empty cell."
Quote card: **"Every cell is full."** — *— all the missingness check actually verifies*. Gold sweep on "full."

## B04 — GRAPHIC · own · manim · ~9.5s
Cue: "Two separate datasets… you join them on the company name."
Manim: `B04_TwoTables` — two navy stacked-row tables slide in from left/right; serif label "join on name" in the seam. No counts yet.

## B05 — GRAPHIC · own · manim · ~8.0s
Cue: "Match the names, and a company's records line up… flow through the gate and join."
Manim: `B05_JoinGate` — rows converge on a central name-matching gate; matched pairs pass through, merge into a single navy "joined" bucket. Establishes the gate (through-line for B05–B10).

## B06 — COMPOSITE · own · manim · ~10.0s
Cue: "One real company. Twelve filings… ten as BioTechCo LLC, and two with a comma."
Manim: `B06_OneCompany` — 12 row-bars; 10 navy "BioTechCo LLC", 2 with a **crimson comma** "BioTechCo, LLC"; hand bracket + "same legal filer" spans all twelve. Figures verbatim from the chapter (12 = 10 + 2).

## B07 — GRAPHIC · own · manim · ~9.0s — THE SPLIT
Cue: "…one stray comma sends those two rows straight past the gate."
Manim: `B07_CommaSplit` — the twelve advance; a **giant crimson comma** drops at the gate and deflects the 2 rows sideways into a crimson "orphan" bucket; 10 pass to the navy joined bucket. Manim move: split.

## B08 — COMPOSITE · own · manim · ~8.5s
Cue: "Now the count reads ten, not twelve… the wrong denominator."
Manim: `B08_WrongCount` — joined bucket resolves to a big navy **10**; faded struck **12** above; crimson orphan bucket holds **2** apart; serif label "wrong denominator." No approval-rate number printed.

## B09 — GRAPHIC · own · manim · ~9.5s — THE REVEAL
Cue: "And the missingness check?… reports zero missing."
Manim: `B09_CheckSeesNothing` — a magnifier sweeps the columns **within** both tables (cells tick navy); lands on a green "MISSING: 0" chip — the crimson orphan bucket sits outside its path, never scanned.

## B10 — COMPOSITE · own · manim · ~9.0s
Cue: "The gap isn't in either table. It lives between them…"
Manim: `B10_BetweenRing` — B09 end-state; one crimson HandRing lands around the **seam between the two tables** on "between." One ring only.

## B11 — CARD (endcard) · own · ~9.0s
Cue: "Zero missing doesn't mean nothing's missing…"
Copy: **Zero missing ≠ nothing missing.** / sub: *from The Reallocation Engine — chapter 5*

---

## Slot inventory (fill later, any order; rerun vox_run after each drop)

| Slot | Need | From |
|---|---|---|
| `media/B02.png` | printed "Missing values: 0" audit report clipping | t2i prompt above (ai — disclosure) |

Everything else is CARD / DOCUMENT / GRAPHIC / COMPOSITE-manim — no media generation needed for the slate cut.
