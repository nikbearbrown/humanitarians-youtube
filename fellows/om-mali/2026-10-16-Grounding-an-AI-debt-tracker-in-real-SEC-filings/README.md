# Grounding an AI Debt Tracker in Real SEC Filings — AI Debt Tracker, week 1

Second episode of the **AI Debt Tracker**, a new Mycroft project. Built with `brutalist.art`,
skill `ai-explainer`, channel `claude-hai`. Free and local end to end — `$0.00`.

| | |
|---|---|
| 16:9 master | `Mycroft_OmMali_16_10_2026.mp4` — 3840×2160, 24fps, 213.74s |
| 9:16 master | `vertical/grounding-an-ai-debt-tracker-in-real-sec-filings-916.mp4` — 2160×3840, same length |
| review cuts | `*-slate.mp4` in each folder — beat IDs and running timecode burned in |
| beats | 12 — 4 bookends, 8 body beats, 0 slates |
| voice | Kokoro `am_onyx`, local, the fellow's persistent voice since week 1 |
| gates | GATE L clean · GATE V 0 BLOCKER / 0 MAJOR on both cuts · **GATE P signed by the author, 2026-10-16** · `$0.00` |

**The agent in this video does not exist yet.** Week 1 built the ground under it: the answer
key, the point-in-time server that refuses late filings, the matcher, and the model. B02 says
so on the frame, because a four-box pipeline diagram otherwise reads as a status report.

---

## Figure → beat map

| Beat | Act | Scene (`GroundingTheDebtTracker.tsx`) | Source figure | What it argues |
|---|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | — | *Ground it before you build it* — lands ANSWERED with the three findings |
| B01 | Why debt | `GDTBorrowing` | `adt-w0-borrowing` | $121bn in 2025 against a $28bn average, and nothing watching it |
| B02 | What it will do | `GDTPipeline` | `adt-w0-pipeline` | Four stages — **and the tense**, in writing |
| B03 | The cut-off | `GDTCutoff` | `adt-w0-pipeline` (its lower half) | The answer is published after the evidence; the server refuses anything later |
| B04 | Could it fail | `GDTSpike` | `adt-w0-feasibility` (first two rows only) | Two failure modes, each against its own pass mark |
| B05 | The answer key | `GDTLevels` | `adt-w1-levels` (upper) | **Fifteen, not twenty-one** — the week's real finding |
| B06 | What it grades on | `GDTSplit` | `adt-w1-levels` (bottom strip) | 95 to build on, 400 held back; bonds match 93.4% |
| B07 | The bake-off | `GDTBakeoff` | `adt-w1-bakeoff` | The smallest model won, under one shared pass line |
| B08 | The limits | `GDTLimits` | — (the script's Notes) | Every number above, paired with what narrows it |
| B09 | Verdict | `ClaudeVerdictArtifact` | — | Five findings, one per spoken clause |
| B10 | Handoff | `ClaudeComposerAsk` | — | Inspect your ground truth before you build on it |
| B11 | Outro | `ClaudeTitleOutro` | — | Title restate |

`adt-w0-model.png` is **retired** — its 8B baseline is superseded by the bake-off, and the
reel does not show it. The six PNGs and their SVG sources in `pantry/` are reference only;
every body beat is rebuilt natively in Remotion (REBUILD LAW) and never slots a PNG as media.

## Three things not to get wrong

1. **The agent is not built.** The pipeline on B02 is `DESIGN.md`. Said in B00, written on
   B02's frame, repeated in B09. FACTCHECK row 4.
2. **"Fifteen, not twenty-one" is a measurement, not a correction of bad data.** 21 counted
   companies whose instruments carried a tag; 15 measures how much of each company's debt its
   report actually itemises, against an 80% coverage gate. 14 qualified outright and the
   fifteenth moved up on a 4–4 tie. FACTCHECK row 15 — this is the build's framing assertion.
3. **Every headline figure has a narrower reading, and all five are on camera.** 87.5% is
   56 of 64 (76.7% on the wider denominator, under the line); 21 of 46 is conservative against
   a raw 33 of 46; 93.4% is the per-bond quarters and 85% across all of them; 99% is after six
   truth corrections on 29 documents; $121bn is Bank of America's figure, not this project's.
   B08 exists for exactly this. FACTCHECK rows 9, 12, 18 and 20.

## GATE P was broken during this build

Audio was generated with the gate ON while `PEDAGOGY.md` said `VERDICT: PENDING`, because
`generate_audio_kokoro.py` searched the whole file for the substring `VERDICT: PASS` and
this reel's own PENDING template spelled the phrase out in an instruction. The gate has
been hardened to match a verdict **line** and verified both ways. The author has since
signed, the audio was never regenerated, and the delivered masters are the ones that
cleared GATE V — but **never write `VERDICT: PASS` anywhere in a `PEDAGOGY.md` except as
the signature itself.** `BUILD-LOG.md` defect 6.

## Known defects carried forward

- **`adt-w0-feasibility.png` shows four rows; this reel uses two.** Rows 3 and 4 (matching at
  83.2%, the 8B model at 87.3%) are week 0 figures that week 1 supersedes — 93.4% and the
  bake-off replace them. Showing all four would put two stale numbers beside two current ones.
- **`adt-w1-levels.png` combines two arguments on one figure** — the partition and the bottom
  strip. They are split across B05 and B06 here, because the strip is not a caption on the
  partition.
- The reel's own 9:16 cut is a **re-layout, not a crop**: each scene lays itself out natively
  at 1080×1920 and both cuts are built from the same mp3s, so no number can differ.

## Files

```
beat_sheet.json        the edit — 12 beats, every figure a prop, durations locked to the mp3s
build_beat_sheet.py    writes it from figdata.json, under assertions (--check runs them alone)
figdata.json           the data; nothing on screen is typed by hand
lock_durations.py      writes measured Kokoro durations into durationInSeconds
make_vertical.py       derives vertical/beat_sheet.json and copies the mp3s across
FACTCHECK.md           20 rows; read 4, 7, 9, 12, 15 and 18 first
CHECKS-REPORT.md       PROOF GATE, written before the first compile
PEDAGOGY.md            GATE P — what the author is asked to sign
BUILD-LOG.md           decisions, defects found and fixed, toolkit changes
BUILD-PROMPT.md        the single prompt that rebuilds this reel end to end
description.txt        the long-form description; description-source.txt is the author's
pantry/                the six source figures — REFERENCE, never slotted as media
_qc/                   GATE V frames and REPORT.md
```
