# Both Sides Passed

**Track:** educational (STEM / AI) · **Week ending:** 2026-10-30

> A record can be perfectly valid on the way out and perfectly valid on the way
> in, and still mean something different at each end.

Two cuts delivered separately: a 16:9 master at 3840×2160 and a 9:16 Short at
2160×3840, both 2:20. **No video files are in this repo** — this is the record
of how they were built and why each claim holds.

## The argument

Two services exchange data. Each validates its own side — fields present, types
right, timestamps positive — and both suites are green. The checks live
*inside* the stages; nothing lives on the boundary between them, because the
boundary belongs to neither team.

Take 5,000 synthetic payment events and break them seven ways, each defect
applied on its own. All seven are ordinary integration failures: seconds for
milliseconds, cents for dollars, an unannounced status value, nulls written as
−1, a timezone shift, amounts arriving as strings, late rows duplicating an id.

| Where the check sits | Defects caught |
|---|---|
| Inside each stage, on its own data | **1 of 7** |
| A contract on the batch at the boundary | **6 of 7** |
| Boundary contract **+ distribution shape profile** | **7 of 7** |

In-stage validation catches exactly one: the string amount, because it is the
only defect that changes a *type*. Everything else is a well-formed value that
means something different than intended.

**The seventh defect is the interesting one.** A 5.5-hour timezone shift,
against an epoch timestamp in milliseconds, moves the value by about 0.001% —
far inside any range check anyone would write, so the boundary contract passes
it. But the events have a daily rhythm, and shifting them moves that shape a
long way. Profiling the distribution catches what a range check cannot.

## Reproduce it

```bash
python boundary_evidence.py
```

Pure Python, no download, seconds to run. It prints the three check levels and
which defects each one catches, so the 1 / 6 / 7 in the video can be read off
defect by defect rather than taken on trust.

## Beats

| # | Act | Scene | What it does |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | Both suites green, numbers still wrong |
| B01 | BLUF | `BrutalistHesitantWriter` | "Validation inside a stage cannot see that" |
| B02 | SETUP | `StageRail` | Producer → boundary → consumer; the middle box is the gap |
| B03 | EVIDENCE | `ClaudeBarChart` | 1 / 7, 6 / 7, 7 / 7 |
| B04 | LAND | `CardSet` | The timezone shift the range check cannot see |
| B05 | SOURCE | `FormACard` | Breck et al., Google, 2019 |
| B06 | HANDOFF | `ClaudeComposerAsk` | A prompt for a handoff you own |
| B07 | OUTRO | `HaiTitleOutro` | Title restate · @HumanitariansAI |

## Built for this reel

**Nothing.** `StageRail` (2026-10-09), `CardSet` (2026-10-16), `FormACard` and
`ClaudeBarChart` all rendered unmodified.

Two portrait components were corrected during GATE V, both for the same reason:
`StageRail916` and `ClaudeBarChart916` used a *fixed* card/row height, so three
items claimed only 51% and 29% of a 3840px-tall frame where four or seven
filled it. Both heights now adapt to the item count. Four stages land on
approximately the previous value, so no existing reel changed.

## Honesty notes

- **The defects are synthetic and chosen.** Seven failures I selected as
  representative of pipeline handoffs — not a sample of production incidents,
  and the reel does not present them as one.
- **The shape check initially caught nothing, and that was my bug, not a
  finding.** The generator emitted timestamps spread *uniformly* across the
  day, so a timezone shift did not change the distribution's shape. I fixed the
  generator to produce a realistic diurnal rhythm. The claim was never
  weakened to fit the result; the simulation was made less unrealistic.
  Recorded in `FACTCHECK.md`.
- **"A very large amount of production data"** is deliberately vague because
  the paper's figure is for Google's own platform; no specific volume is
  attributed to it on screen.
- **No claim that in-stage validation is useless.** It catches the type error.
  The finding is about what a stage-local check structurally *cannot* see.

Full ledger in `FACTCHECK.md`, sources in `SOURCES.md`, build record in
`FRICTIONAL.md`.
