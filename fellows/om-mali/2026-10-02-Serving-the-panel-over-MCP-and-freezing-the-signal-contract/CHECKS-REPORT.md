# CHECKS-REPORT — serving-the-panel-over-mcp-and-freezing-the-signal-contract

PROOF GATE, written **before** the first cut compiled (ai-explainer SKILL.md §PROOF GATE).
Classification rules: `skills/make/nopunt/SKILL.md`.

```
12 beats:  8 SHOW  /  4 justified-HOLD  /  0 PUNT-flagged
```

## Per-beat classification

| Beat | Class | Why |
|---|---|---|
| B00 | HOLD (justified) | Bookend. The composer types the ask and lands three answer lines. The interface IS the subject this week — the reel opens inside a client talking to the thing it is about (COLD OPEN LAW). |
| B01 | SHOW | Claim: two deliverables, and the hard part was not the protocol. Two cards land naming what each piece is FOR, then "the protocol" lands as the assumed difficulty and is **struck through** before the real constraints replace it. |
| B02 | SHOW | Claim: the same query has two possible sizes. Two bars draw to scale from one measurement, each carrying its own characters, tokens and rows. The ratio is seen, not asserted. |
| B03 | SHOW | Claim: the envelope is not free. Six tools land on a **diverging** track from a zero line, five to the right and one to the left, each with its signed percentage and its before/after. The sign is the argument, so the geometry carries a sign. |
| B04 | SHOW | Claim: six tools, none of which writes. Six rows land with rows returned against rows available; then three things no tool can do land as **struck lines**, because the claim is an absence and the frame draws absences. |
| B05 | SHOW | Claim: a contract is what it refuses. Nine keys land as chips on one side, ten refused names strike through on the other, and a proof line states what was checked against the emitted file. |
| B06 | SHOW | Claim: suppressed is a value. Four companies land each carrying a `suppressed_reason` chip in the slot where a missing key would be; then two counts land side by side and the difference resolves to one company with zero marks. |
| B07 | SHOW | Claim: the grounding check was not enough. What the model has lands beside three struck things it does not; three guards land with the draft that fails each; the invented-ranking row takes the accent and the contradiction lands beneath it. The fourth check lands below a dashed rule as a later addition. |
| B08 | SHOW | Claim: the checks still miss things. Two misses land with what the check actually read, three setup bugs land as a numbered stack, then the shape they share, then what none of it shows. |
| B09 | HOLD (justified) | Verdict recap. Five findings stagger in, one per spoken clause. Judgment beat — the artifact page is the point (ILLUSTRATE LAW carve-out). |
| B10 | HOLD (justified) | HANDOFF LAW. Typing is the motion and is legal here (one of exactly two typing beats). The prompt is read aloud verbatim and then discussed. |
| B11 | HOLD (justified) | Outro. Title restate, poster-style. Nothing in the line can move. |

No beat is a bare CARD. No beat names an on-screen artifact it does not render.

## Legibility contract (every SHOW/HOLD claim beat)

- Names its on-screen artifact in `shot.show` / `shot.visual_intent` ✓ (all 12)
- ~15–35% negative space ✓ — verified at QC, see `_qc/REPORT.md`
- Un-highlighted elements never below ~40% opacity ✓ — the deepest de-emphasis is B03's
  costlier bars at 0.62 and B07's non-accented guard rows at SOFT
- Comparisons shown side-by-side, held ≥2s ✓ — B02's two bars, B03's two sides of the zero
  line, B05's carried-versus-refused columns, B06's two counts and B07's has-versus-lacks all
  persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓      B01 — both deliverables named by WHAT THEY ARE FOR before any result, and
                 the assumed difficulty struck, so the rest of the reel has somewhere to go
WORKED EXAMPLE ✓ B02/B03 — one real query, measured twice, followed all the way to what the
                 bounding envelope costs on the five tools that did not need it
FALSIFIABILITY ✓ B03 contradicts the reel's own source figures, which show bounding only
                 where it wins; B06 reconciles two of the reel's own numbers that disagree;
                 B07 is the author's stated expectation being wrong, with the draft that
                 proved it quoted verbatim; B08 is two failures that arrived after the
                 figures were drawn
SCAFFOLDED TASK ✓ B10 — list what your most-trusted test supplies that a real caller would
                 not, then withhold one and run it again
BOOKENDS ✓       B00 cold open · B01 BLUF · B09 verdict · B10 handoff · B11 outro
NO-SOURCE-NO-VERDICT ✓ every figure is a prop injected by build_beat_sheet.py from
                 figdata.json or read directly out of signal_example.json; the injection
                 ASSERTS six tools, the 2,151/50 page against its 575,299→17,976 bounds,
                 that the envelope COSTS on five tools and pays on exactly one, that exactly
                 one tool paged and exactly one returned zero rows, that the emitted signal
                 has the nine keys the figure claims AND contains none of the ten refused
                 names, and that listed minus published is one — and fails the build otherwise
```

**0 violations.** Four authoring judgment calls are logged in `BUILD-LOG.md` rather than passed
silently: the six script sections split into eight body beats, adding B03 (which neither the
script nor either figure contains), adding B06's reconciliation of 11 against 10, and drawing
the fourth guard as a later addition rather than a fourth row.

## The three values not under an assertion

`figdata.json` does not carry the fourth guard, the two late misses, or the three setup bugs.
All three come from `README.md` and `narration_script.md`. Each is passed into the build as a
named constant rather than written into a string, and **each beat that uses one says so in its
on-screen source line** rather than citing a file that does not contain it. `FACTCHECK.md` rows
12, 18 and 19.

Row 12 is the one that carries weight: `w11-guards.png` is titled "Three guards" and this reel
says four. The fourth arrived after the figure was drawn. B07 draws it below a dashed rule so a
viewer can see which part is older than the other, rather than silently presenting four rows of
equal provenance. If the fourth check is not real, B07's close and B09's last finding are both
wrong.

## What this cut is asked NOT to do, and does not

| The README says | This cut |
|---|---|
| **Token bounding is the deliverable, not a detail** | B02 and B03 are two whole beats. B02 measures it; B03 measures what it costs. The number is never mentioned in passing. |
| **Read-only is a design decision** | B04 draws it as three struck absences and states the reason — a resolution decision needs a named human — rather than listing read-only as a feature. |
| **The refused fields are structural, not stylistic** | B05's closing block is the structural argument: these filings give a fund's share count, never the company's shares outstanding. The refusal is also *checked against the emitted file* on the frame. |
| The grounding check wasn't enough | B07 exists for this, and quotes the draft that passed. |
| The two late model-facing failures are worth knowing | B08, the last body beat, in the README's own terms. |
| Red is the primary series, never a warning | Terracotta marks the bounded page, the one tool the envelope pays for, the refused names, the suppressed reason and the draft that should not have passed — the subject of each beat, never a hazard. |
