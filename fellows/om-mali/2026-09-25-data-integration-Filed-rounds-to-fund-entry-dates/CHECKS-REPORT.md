# CHECKS-REPORT — joining-filed-rounds-to-fund-entry-dates

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines — motion is the type-on and the result reveal. The interface IS the subject (COLD OPEN LAW). |
| B01 | SHOW | Claim: two filings, joined, and not on a name. Two source cards land naming WHO files each one and what it gives, the existing source is stated as what it cannot say, and the join key `a name` lands and is **struck through** before the real key replaces it. |
| B02 | SHOW | Claim: a name scan is overwhelmingly wrong. One bar draws to 706 and splits 595/111 with the feeder share taking the accent and most of the width; a REAL feeder name then lands with what it actually is. The majority is seen, not asserted. |
| B03 | SHOW | Claim: no string normalisation fixes this. The name-join path is struck through, the identifier path lands beneath it, and two filer cards show the same normalised string resolving to two different companies. |
| B04 | SHOW | Claim: one footnote, five layouts. Three layout kinds land with counts, then the ten filers that carry lots grow as bars with their own lot counts, and the single filer that reports cost at fund level takes the accent. Two of the ten rows read BlackRock under two spellings; they are left exactly as filed, with a line on the frame saying these groups are keyed on a case-sensitive name prefix. |
| B05 | SHOW | Claim: the footnote reaches back, but only sometimes. Seven companies land on a shared time axis, each with its acquisition date and the panel's first mark joined; the three that genuinely predate the panel take the accent and the four that do not dim. |
| B06 | SHOW | Claim: exposure is concentration, not conviction. Manager–company rows land largest-first, each with a percentage-of-net-assets bar grown from the filer's own reported figure. |
| B07 | SHOW | Claim: two independent filings agree. Eighteen gaps fill a day axis and the ten at zero stack visibly at the origin; the clearest case lifts out with its five registrants; three lines then state why the agreement is independent rather than circular. |
| B08 | SHOW | Claim: the denominator is doing the work. The same numerator sits under two denominators side by side, 56% beside 33%, and the reel closes on three things none of it shows. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B05's
  four non-reaching rows at 0.45 and B03's struck name-join card at 0.80
- Comparisons shown side-by-side, held ≥2s ✓ — B01's two sources, B02's two bar segments,
  B03's wrong/right keys and its two colliding filers, B05's entry-vs-mark pairs, B08's two
  denominators all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01 — both sources named by WHO files them, before any result; that
                 asymmetry is what makes B07's agreement evidence rather than arithmetic
WORKED EXAMPLE ✓ B02/B03 — one real feeder name, then one real name collision, followed all
                 the way to why the join key had to change
FALSIFIABILITY ✓ B05 corrects a figure that had titled all seven companies as reaching back
                 when four do not, and says on the frame why the sample is a floor;
                 B08 shows the reel's own headline restated under a second denominator;
                 B07 states the reading that would make the agreement meaningless, and why
                 it does not apply
SCAFFOLDED TASK ✓ B10 — find a join in your own data that keys on a name, and COUNT what
                 share of its matches are the thing you meant
BOOKENDS ✓       B00 cold open · B01 BLUF · B09 verdict · B10 handoff · B11 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop injected by build_beat_sheet.py from
                 figdata_week9.json; the injection ASSERTS the 706-row split and its 84.3%,
                 that feeders DOMINATE rather than merely outnumber, the 249/227/22 lot
                 accounting and that exactly one filer reports at fund level, that only 3 of
                 7 companies reach back, the 18-row corroboration set agreeing with its own
                 summary on the 10 that land at zero, the named Databricks row, and the
                 12 out-of-window dates that turn 56% into 33% — and fails the build otherwise
```

**0 violations.** Three authoring judgment calls are logged in `BUILD-LOG.md` rather than
passed silently: the six script sections split into eight body beats, naming the other 22 lots
on B04 rather than leaving "227 with a cost" to imply 22 have none, and accenting only the
three companies that genuinely reach back on B05.

## The three values not under an assertion

`figdata_week9.json` does not carry the 2014 X.AI name collision, the five-layout taxonomy, or
the $400M Databricks offering amount. All three come from `narration_script.md` and the filings
behind it. Each is passed into the build as a named constant rather than written into a string,
and **each beat that uses one says so in its on-screen source line** rather than citing a file
that does not contain it. `FACTCHECK.md` rows 6, 9 and 18.

Row 6 is the one that carries weight: the collision is the evidence that no better string
normalisation would have fixed the join, which is the whole justification for a human
confirming each identifier. If it is not real, B03 needs rebuilding rather than rewording.

## What this cut is asked NOT to do, and does not

| The README says | This cut |
|---|---|
| **The 84% is the reason for the design, not a side note** | B02 is a whole beat and the bar is drawn so the feeder share dominates the frame; B03 then derives the join key from it. The number is never mentioned in passing. |
| **The corroboration is evidence, not causation** | B07's closing block states the competing reading — a secondary purchase that settled the same day — and the independence claim is spelled out in three lines rather than implied by the count. |
| **The denominator does the work** | B08 exists for this and is the last body beat. Both readings are shown at the same size, with the same numerator, and neither is declared correct. |
| No valuation, no return | B08's closing block, in the report's own words. |
| Red is the primary series, never a warning | Terracotta marks the feeder share, the confirmed key, the dates that land on the day, and the in-window reading the headline came from — the subject of each beat, never a hazard. |
