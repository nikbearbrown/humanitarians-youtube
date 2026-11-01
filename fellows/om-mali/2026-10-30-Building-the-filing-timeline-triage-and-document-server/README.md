# 2026-10-30 - Building the filing timeline, triage and document server

**Week covered:** 2026-10-26 - 2026-11-01

**Video:** [Mycroft_OmMali_30_10_2026.mp4](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The AI Debt Tracker is an AI agent, run entirely on a laptop, that reads companies' public
filings to keep an up to date record of every bond and loan owed by 25 AI-sector companies, and
is graded against the debt each company later reports officially.

This week built what finds the debt news in the filings and lets the agent quote from them. The
agent itself still cannot read a filing into structured facts.

- **Last week's three answer key problems are fixed**, and last week's three test reports now
  all agree. Those were the reports the fixes were made against, so five fresh reports were
  picked in advance and graded once. Of the three that had any debt, 1 agreed. The two new
  causes, a bank's extra allotment counted as a second bond and small notes with no due date in
  the data, are recorded for next week.
- **A filing timeline for every quarter.** It gathers each announcement, prospectus and term
  sheet filed before the quarter's report, including those from the subsidiaries that borrow on
  a company's behalf: 593 filings across the development quarters.
- **Triage picks out the debt news.** Five plain rules decide two thirds of the filings. Only
  the doubtful 199 go to a small local model, at about 3 seconds each. 184 filings are kept.
- **Triage missed nothing on the check.** 50 filings were labelled by Claude before triage ran.
  24 of them were about debt, and triage kept all 24, plus 2 that were not. It also kept all 22
  filings that last week's search found announcing a bond change.
- **A document server makes filings quotable.** It splits a filing into numbered sentences and
  table cells, so the agent can cite "sentence 5" instead of retyping a number, and it refuses to
  open the report the agent will be graded on.
- **The week's gate is recorded as delegated, not cleared.** The work was handed to Claude end
  to end and has not yet been reviewed by a person. It clears once the triage report and its
  labels are read.

---

## The built reel

Fourth episode of the **AI Debt Tracker**. Built with `brutalist.art`, skill `ai-explainer`,
channel `claude-hai`. Free and local end to end — `$0.00`.

| | |
|---|---|
| 16:9 master | `Mycroft_OmMali_30_10_2026.mp4` — 3840×2160, 24fps |
| 9:16 master | `vertical/building-the-filing-timeline-triage-and-document-server-916.mp4` — 2160×3840, same length |
| review cuts | `*-slate.mp4` in each folder — beat IDs and running timecode burned in |
| beats | 12 — 4 bookends, 8 body beats, 0 slates |
| voice | Kokoro `am_onyx`, local, the fellow's persistent voice since week 1 of the earlier series |

**The agent still cannot read a filing into structured facts.** Week 3 built what *finds* the
filings worth reading, and what lets a future reader *point into* them. B00 says so, B04's
footnote says so, and B08's last row says so again.

---

## Figure → beat map

| Beat | Act | Scene (`BuildingTheTriage.tsx`) | Source figure | What it argues |
|---|---|---|---|---|
| B00 | Cold open | `ClaudeComposerAsk` | — | *Find the debt news, and prove nothing was thrown away* — lands ANSWERED |
| B01 | Last week's leftovers | `W3Recheck` | `adt-w3-holdout` (bars) | 3 of 3 is a calibration; 1 of 3 is the measurement |
| B02 | What the fresh reports showed | `W3Fresh` | `adt-w3-holdout` (names) | Two new defects, named and left open |
| B03 | The timeline | `W3Timeline` | `adt-w3-funnel` (top bar) | A window that closes before the answer is published |
| B04 | Triage | `W3Funnel` | `adt-w3-funnel` | 593 → 394 by rule, 199 to the model, 184 kept |
| B05 | The check | `W3Check` | `adt-w3-triage` | It found everything — now look at the three numbers under that |
| B06 | What went wrong | `W3Wrong` | — (`logs/RUN_LOG.md`) | Three failures, each with what it changed |
| B07 | The document server | `W3Docs` | `adt-w3-docs` | Cite the sentence, never retype the number |
| B08 | The limits | `W3Next` | — (the script's Notes) | Every number above, paired with what narrows it |
| B09 | Verdict | `ClaudeVerdictArtifact` | — | Five findings, one per spoken clause |
| B10 | Handoff | `ClaudeComposerAsk` | — | Label a sample before you run your filter |
| B11 | Outro | `ClaudeTitleOutro` | — | Title restate |

The four PNGs and their SVG sources in `pantry/` are reference only; every body beat is rebuilt
natively in Remotion (REBUILD LAW) and never slots a PNG as media.

## Four things not to get wrong

1. **The agent does not read filings yet.** It finds them and makes them citable.
2. **3 of 3 is a calibration**, on the reports last week's fixes were made against. The
   measured number is **1 of 3**, and the 2 drawn reports that had nothing to grade are drawn
   on the frame as an excluded tail — not counted as agreements, not silently dropped.
   FACTCHECK rows 1 and 3; this is the build's framing assertion.
3. **24 of 24 is recall**, on 24 positives inside a 50-filing sample. Precision is 24 of 26 and
   the event type is right on 20 of 24, both on the same scale directly beneath it. FACTCHECK
   rows 13–14.
4. **The 50 labels are Claude's judgment**, made against a written definition before triage ran
   — a different model from the one tested, but not a person. The reel never says "I labelled".
   FACTCHECK row 16.

## Four drawings that are the argument

- **B01's dashed tail** is excluded, not empty. Dashed border, no fill, labelled `+2`, with
  `1 of 3` beside it. If the dash weight ever drops it starts reading as an unfilled part of
  the score, which is the opposite claim.
- **B04 keeps the full 593 outline on every row.** Four free-standing bars would read as four
  populations; this is one population being narrowed, and the part that fell away stays visible
  as the gap.
- **B05's pass line is one rule through all four tracks**, and on the recall bar it sits inside
  the fill — so "found everything" is seen clearing a mark that was already on the frame.
- **B07 shows the citation resolving**: query → `s5` → the actual sentence. "Cites instead of
  retyping" is seen, not claimed.

## Files

```
beat_sheet.json        the edit — 12 beats, every figure a prop, durations locked to the mp3s
build_beat_sheet.py    writes it from figdata.json, under assertions (--check runs them alone)
figdata.json           the data; nothing on screen is typed by hand
lock_durations.py      writes measured Kokoro durations into durationInSeconds
make_vertical.py       derives vertical/beat_sheet.json and copies the mp3s across
FACTCHECK.md           21 rows; read 3, 5, 9, 12, 13, 16 and 19 first
CHECKS-REPORT.md       PROOF GATE, written before the first compile
PEDAGOGY.md            GATE P — what the author is asked to sign
BUILD-LOG.md           decisions, defects found and fixed, toolkit changes
BUILD-PROMPT.md        the single prompt that rebuilds this reel end to end
description.txt        the long-form description; description-source.txt is the author's
pantry/                the four source figures — REFERENCE, never slotted as media
_qc/                   GATE V frames and REPORT.md
```
