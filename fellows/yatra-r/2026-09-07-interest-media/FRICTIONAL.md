# FRICTIONAL — Interest Media.

> Written 2026-11-03 from this folder's build records (README.md, BUILD-PROMPT.md,
> CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md, QC-LOG.md, SHOTLIST.md, SOURCES.md,
> YOUTUBE.md, beat_sheet.json), not kept week by week during the build.

## 2026-09-07

**Tried / expected.** A concept explainer on feeds moving from "who you know" to "what
you're interested in" — a framing credited to Gary Vaynerchuk, from a script Yatra
supplied already paraphrased. Two instructions attached: credit him by name, don't quote
him; and (standing across the series) invent no statistics. Also asked for: not a
variation of any earlier video, and a stand-in voice — the first episode on this channel
introduced as "Bella, in for Yatra". Target: true 4K in 16:9 and 9:16, free path only.
Result: 13 beats, 2:29.6, eight new `Itm*` scenes.

**Where it resisted, and what was done next.**
- *A topic with no numbers.* No figures were supplied, so the `Itm*` components were built
  with no numeric prop at all, and `ItmSource` has `claimParaphrase` but no `quote` field.
  B04 (volume) was the beat most likely to invite a "X million posts a day" figure; its
  marks are uncounted and its band reads `more than a network can sort`. A regex sweep of
  every on-screen prop string found 0 numerals (the verdict page's `1.`–`5.` list numbers
  are noted as the one exception).
- *"Thousands of followers."* The script's phrase was kept in B07's narration as Yatra's
  own wording but not drawn as a figure; the track reads `build an audience first`.
- *Layout defects found by reading frames.* B07's gate hatching overlapped the node it
  should sit before (BLOCKER); B05's machine was undersized and the lifted key straddled
  its border, needing a second pass to clear the corner (MAJOR); B04's bottom third was
  empty (MAJOR); B02's rename row sat cramped under the card (MINOR). All fixed in scene
  source and re-rendered.
- *The 9:16 cut.* `shorts.py --handle` defaults to `@nikbearbrown`, so the first endcard
  carried another channel's handle (BLOCKER). It also hardcodes a 1080×1920 endcard, which
  a 4K compile upscales (MAJOR). Endcard regenerated with `@Yatra` at 2160×3840; portrait
  B05's key clearance also widened (MINOR).
- *Render timeouts.* Portrait B10–B12 timed out at 30s while the 4K landscape master was
  encoding at the same time. Re-run one after another, all three succeeded.
- *Toolkit gates.* GATE V gives false BLOCKERs in this tree, so ink coverage was measured
  with its own `analyze_frame()` instead; GATE T's script is missing, so its checks were
  done by frame inspection and the numeral sweep. Both logged as substitutions.

**What Claude contributed, and what was accepted / changed.** Yatra supplied the script,
the attribution instruction and the stand-in-voice request. The build side (Claude —
YOUTUBE.md: "Built with Claude") turned the script into the beat sheet, wrote the eight
`Itm*` scenes and their portrait versions, ran audio/render/compile and did the frame QC.
Every claim traces to the script; nothing was researched or added. The records offer, but
do not record a decision on, dropping the spoken "thousands of followers".

**Now understood / still open.**
- Understood: the vertical cut on this channel needs two manual steps — `--handle "@Yatra"`
  and a 2160×3840 endcard.
- Understood: the 30s Remotion timeout is too tight to render and encode 4K at once.
- Open: no date, venue or link was supplied for the Vaynerchuk framing, and none was looked
  up; the credit is to a person for an idea.
- Open: SOURCES.md dates the supplied summary 2026-09-11, after this folder's date.
