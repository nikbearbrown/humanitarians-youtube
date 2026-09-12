# BUILD-LOG — "Use the Tool First."

Built 2026-09-10 as the progress half of the week-03 submission. What actually
happened, in order.

## 1 — Reading the week, not just the brief

The brief pointed at `lyrical-literacy/youtube` and listed four activities:
using Midjourney, researching prompting, taking screenshots, planning.

Measured what was actually there rather than trusting the plan document:

```
ffprobe on midjourney-part-{1..6}/*.mp4   → 3840×2160 × 6
                                          → 200.30 / 196.20 / 182.42
                                            203.94 / 179.23 / 176.88 s
sum                                       → 1138.96s = 18:58.96 → 18:59
ls "Midjourney Screenshots" | wc -l       → 29
wc -l MIDJOURNEY-UI-SPEC.md               → 863
ls scenes/ | grep -c '^Mj'                → 23
```

**Two upstream inconsistencies found.** `MIDJOURNEY-SERIES-PLAN.md` says
"23 captures" in its header and "29 captures" further down — disk says 29. It
also states 18:58, which is the truncation of 18:58.96; the reel rounds to
18:59, per the convention fixed in week-02. Both recorded in FACTCHECK.

**The plan document also gave the reel its spine.** Its section "What the
captures changed" lists five assumptions the screenshots overturned and notes
two whole surfaces missing from the plan. That is a better story than "I took
screenshots", so the correction became the through-line and the brief's four
activities became its inputs.

## 2 — Library-first gate: three needs, three different outcomes

| Need | Outcome |
|---|---|
| six-part series grid | `HaiProgressSeriesCards` scored 14.5 — a real hit, built in week-02 for this. But its card width is `(CONTENT_W − GAP×(n−1))/n`, which at n=6 gives **245px**, too narrow for a 27px serif title. Built a 3×2 variant. |
| plan-vs-reality columns | `MedhavyTwoColumnCard` scored 7.5 with **exactly** the right props. Opened the file: fixed 900px centred card, top-centre spark, no eyebrow. Extending it would change the medhavy channel's render. **Purpose-built instead.** |
| shipped/next roadmap | `HaiProgressRoadmap` + its 916 sibling already existed. **Reused outright, zero lines written.** |

The middle row is the doctrine working: the search returned a lead, reading the
file returned the verdict. Recorded in PROMPTS.md so the next person does not
repeat the search.

## 3 — Components authored

Two landscape + two portrait siblings, registered under
`midjourney-week-progress`:

| Component | Portrait sibling |
|---|---|
| `HaiProgressSeriesGrid` | `HaiProgressSeriesGrid916` |
| `HaiProgressOverturned` | `HaiProgressOverturned916` |
| `HaiProgressKitGrid` | `HaiProgressKitGrid916` |

`HaiProgressSeriesGrid` rounds its total rather than truncating, fixing the
class of bug that put 10:34 on screen against a documented 10:35 in week-02.

## 4 — Audio (the master clock)

```
B00 18.97   B01 22.72   B02 24.43
B03 23.55   B04 21.93   B05 10.50
```

Total **122.10s = 2:02**. Cost $0.00. The first pass came in at 1:51, nine
seconds under the brief, so B04 was lengthened — it had been a bare one-liner
and now names the four accounts the signup guide will cover, which is more
useful anyway. No beat was cut.

## 5 — Render, and a shared-outro defect caught by looking

Rendered all six at 4K, compiled a review cut, read the QC sheet — and **B05
was showing `@NikBearBrown` and a bear mascot** instead of `@HumanitariansAI` /
`Rohan Vijaykumar`, despite the beat sheet passing the correct props.

Cause: `docs/OUTRO-LOCK.md` scopes `ClaudeTitleOutro` to claude-liam /
@NikBearBrown reels **only**, and that component now hardcodes the handle,
renders a mascot, and **silently ignores the `handle` and `subline` props**. It
is documented as such in its own header. Nothing errored; the props were simply
discarded.

`HaiTitleOutro` already existed for exactly this reason — authored during the
Midjourney series, with a header that documents the trap. Switched B05 to it
and re-rendered.

**This would have shipped.** A duration probe and a dimension check both pass
on a reel with the wrong channel's attribution on its end card.

### Two follow-ups from that finding

**Toolkit bug — the skin lint was giving harmful advice.** `compile.py` warned
`palette=claude but the outro is 'HaiTitleOutro' — OUTRO LAW wants
ClaudeTitleOutro`. That lint keyed off **palette** when OUTRO LAW is
**channel**-scoped: a HAI reel uses the claude palette but is a different
channel. Following the warning would reintroduce the bug. Fixed to look up the
wanted outro by `metadata.channel`.

**Week-02 is exposed.** Both week-02 beat sheets still name
`ClaudeTitleOutro`. Their shipped mp4s are fine — rendered before the lock —
but **a rebuild would silently flip their outros**. Recorded in memory; not
changed here, because editing already-merged reels is outside this build's
scope.

## 6 — Visual QC on frames

| Finding | Fix |
|---|---|
| B05 wrong channel attribution | → `HaiTitleOutro` (above) |
| B03 component chips at 18.9px at 1080 base — **below the ~24px TYPESIZE floor**, and leaving the chip column ending well short of the left column | chip type to `0.0222·h` (24px), bigger padding and gap |

Gate V then reported **0 BLOCKER, 0 MAJOR — clean.**

## 7 — Two more toolkit bugs, both blocking the final

**Unencoded sheet read tripped the change-guard.** `compile.py` refused every
final with `Beat sheet changed during rendering`. Line 846 re-read the beat
sheet with `read_text()` and **no encoding** — on Windows that is cp1252, so
the re-read parsed differently from the original for any non-ASCII string, and
this reel's titles are full of `·`, `—` and `×`. The guard was comparing a
UTF-8 parse against a cp1252 parse and always finding a difference. Same family
as the five encoding bugs fixed in week-02. Fixed, plus one more in
`replace_log` handling.

**Masters now land in `renders/`.** The toolkit changed: `compile.py` writes to
`<toolkit>/renders/` unless given `--out`. Passing `--out <reel>` puts the
master back in the reel folder where the rest of the pipeline expects it.

## 8 — Portrait

`shorts.py --no-endcard` rewired all six beats to their `916` siblings on the
first run. `--no-endcard` because B05 is already a branded outro and skipping
the silent card keeps both cuts the same length.

## Outputs

```
2026-09-11_use_the_tool_first_16x9.mp4   3840×2160   122.1s
2026-09-11_use_the_tool_first_9x16.mp4   2160×3840   122.1s
```

## Toolkit changes made in this build

| File | Change |
|---|---|
| `runtime/scripts/compile.py` | UTF-8 on the change-guard sheet re-read and the replace-log read — was refusing every final on Windows |
| `runtime/scripts/compile.py` | OUTRO LAW lint now channel-scoped, not palette-scoped |
| `runtime/remotion/src/scenes/HaiTitleOutro916.tsx` | **new** — HAI portrait end card; without it THE ONDA CHECK had only the @NikBearBrown-locked 916 outro to fall back on |
| `runtime/remotion/src/scenes/HaiProgress{SeriesGrid,Overturned,KitGrid}.tsx` + `916` | **new** — 6 components |
| `runtime/remotion/src/Root.tsx` | registrations |

The encoding bug is the fourth of its kind on this machine. The pattern is now
unambiguous: **any `read_text()` / `write_text()` in this toolkit without an
explicit encoding is a latent Windows failure.**
