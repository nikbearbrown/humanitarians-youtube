# Week 9 — Joining filed rounds to fund entry dates

Five figures and a 3:00 narration script. The week's work: two new SEC ingest lanes beside the
marks panel — Form D for offering dates and amounts, and the Reg S-X 12-12 restricted-securities
footnote for acquisition dates and cost — joined on an issuer identity a person confirmed rather
than on a name string.

| File | Beat | What it shows |
|---|---|---|
| `w9-nametrap.png` | 0:35 | 595 of 706 Form D name matches, 84.3%, are feeder vehicles rather than the company |
| `w9-layouts.png` | 1:20 | Five filers, five layouts for the same footnote — one of them with no table at all |
| `w9-entries.png` | 1:55 | Acquisition dates reaching back to January 2015, years before the panel's first mark |
| `w9-exposure.png` | 1:55 | Concentration by manager and company, using each filer's own percentage of net assets |
| `w9-corroborate.png` | 2:20 | 10 of 18 fund acquisition dates land on the exact day an issuer reported a first sale |

SVG sources sit beside each PNG. PNGs are 2917 × 1750. `figdata_week9.json` is the measured data
every figure was drawn from.

## Rules

- Every number is queried from the database at build time
  (`scripts/make_week9_figures.py` in the project repo) and dumped to `figdata_week9.json`
  before anything is drawn. No figure carries a hand-typed value.
- Both QA passes were run: the layout audit reports **0/20 flagged**, and each PNG was read and
  checked for substance.
- Six palette tokens from `brutalist/DESIGN.md`, nothing else. Red is the primary series, never
  a warning colour.

## The three things not to get wrong on camera

**The 84% is the reason for the whole design, not a side note.** A name scan of Form D returns
overwhelmingly feeder vehicles — "Anthropic Jan 2026 a Series of CGF2021 LLC" is a fund raising
money to buy Anthropic shares on the secondary market. Summing their raises per company would
publish figures no company ever filed. That is why the join is keyed on a confirmed EDGAR
identifier.

**The corroboration is evidence, not causation.** A fund buying on the day an issuer reports a
first sale is consistent with participating in that round — and equally consistent with a
secondary purchase that settled the same day. What it is *not* is circular: neither filing cites
the other.

**The denominator does the work.** Only purchases made while a company was still filing Form D
are counted. One company in the set stopped filing in mid-2022, and most of its later purchases
have no round to match; measured against the nearest one they produce gaps of 800 to 1,300 days,
each of which is the distance to the end of the archive rather than a fact about a fund. Left in,
a real 56% reads as 33%.

## What these figures do not show

No valuation, and no return. Neither source carries shares outstanding, so nothing here divides
to a company value. And a footnote cost divided by a later mark is not a return, because the
share count may have changed in between — the split detector built in Week 7 blocked 301 marks
for exactly that reason. Where a single filed row carries both a cost and a value, that ratio is
shown, because it is a comparison the filer made.

## Two defects the accuracy pass caught

1. **`w9-entries` was titled as though every row predated the panel**, and four of seven were
   negative. Only the latest annual and semi-annual per registrant were fetched, so older
   purchases disclosed in older reports are simply not in view. The figure now shows only the
   companies where the footnote genuinely reaches back, and says on its face that the sample is
   a floor rather than a history.
2. **`w9-exposure` truncated manager names into the next column** — "Robinhood Ventures Fund"
   ran into "Databricks". The layout auditor does not catch this, because the two are separate
   text elements sharing a baseline rather than overlapping boxes.

---

## The built reel

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`) — free and local throughout:
Kokoro TTS, Remotion, ffmpeg. **$0.00 spent, no API key used.**

Twelve beats, ~3:38, in **both orientations**: `joining-filed-rounds-to-fund-entry-dates.mp4`
(3840×2160) and `vertical/joining-filed-rounds-to-fund-entry-dates-916.mp4` (2160×3840). The
9:16 cut is a **re-layout, not a crop** — both render from the same components and the same
props, and carry the identical narration MP3s.

The five figures above travel in `pantry/` as **reference**. Every beat is rebuilt native
(REBUILD LAW); no PNG is slotted as media. `w9-exposure` is rebuilt for the second reason this
README gives as well: each column owns its width and clips inside it, so no two text elements
can share a baseline.

| Document | What it is |
|---|---|
| `BUILD-PROMPT.md` | the single paste-ready prompt that rebuilds this reel end to end |
| `BUILD-LOG.md` | decisions taken, and every defect found by reading the rendered frames |
| `CHECKS-REPORT.md` | the PROOF GATE — per-beat SHOW/HOLD classification, written before the first compile |
| `FACTCHECK.md` | 20 rows. **Read rows 6, 9, 14 and 19 before signing.** |
| `PEDAGOGY.md` | GATE P — what the author is being asked to sign off on |
| `description.txt` | the written version of the episode |

**Three values in the reel are not in `figdata_week9.json`** — the 2014 X.AI name collision, the
five-layout taxonomy, and the $400M Databricks offering amount. Each is passed into the build as
a named constant and each beat that uses one says so on screen. Row 6 is the load-bearing one.

**A third defect, found only by reading the rendered frames:** the exposure beat put
"1791.81% of a fund's net assets" on a 4K frame. `max_pct_net_assets` is already a percent —
17.918 means 17.9% — and the scene multiplied it by 100. The layout auditor passed it, because
the type was well-formed and well-contrasted and the number was merely impossible.

Nothing here is published. The masters stay in this folder.
