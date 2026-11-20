# Frictional log — Fact-Checking Chapters 10 and 13

## 2026-10-01 — Chapter 10 checked against registries, Chapter 13 against its own copied sources

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/14gg96SWrgstXFu-8biiSoN1QyQ5aJnql?usp=drive_link
- **Report:** [REPORT.md](REPORT.md)
- **Project repository:** `Medhavy/medhavi-cancer` (private), branch `text-edits`

**What I was working on.**

Chapters 10 (apoptosis and cell death) and 13 (invasion and metastasis). Chapter 10: 114 sentences,
64 flagged, 10 in my scope, 7 revised, 3 approved, 8 text edits in 3 files. Chapter 13: 274
sentences, 131 flagged, 37 in my scope, 22 revised, 15 approved, 24 edits across all 11 files.

**What I tried, and what I expected.**

I expected Chapter 13 to be the usual mix of stale numbers and loose citations. It was not. It lists
a dog cancer among human cancers, and says MMP inhibitors are in active trials when I could find
none. A zero from a registry means nothing on its own, so I ran the same search for pembrolizumab
as a control and got 1,292. Parts of the chapter read like other books, so I measured it: 2,140
copied words in runs of ten or more from 16 NCBI Bookshelf chapters. That explained the strangest
finding, one copied sentence that is right in file 5 and wrong in file 9.

**Where it resisted, and what I did next.**

Chapter 13 did not finish when I thought it had. I had checked that my sources supported my
findings, but not that my own 24 replacement sentences were themselves right. Checking them as if
someone else had written them found four problems, including an "and" where the source says "or".
In Chapter 10 my edits passed every mechanical check and two still read badly aloud. My own
verification script also produced false alarms by mangling the pages it was meant to read, so I
had to check the checker before trusting it.

**What Claude contributed, and what I did with it.**
- Mine: the review itself, every verdict and source, the edit guides and the evidence documents.
- Claude's: help drafting and checking parts of the written record.
- Accepted: corrections to wording where they matched the sources.
- Rejected/changed: any suggestion I could not trace to a source.
- Evidence: the evidence documents and workbooks in the chapter folders, and the merged textbook pull requests.

**What I understand now, and what I still do not.**
- Understood: my corrections are claims and get the same checking as the chapter.
- Not understood: why the audit graded the two copies of the lymphatic sentence the wrong way round.
- Open: nothing outstanding; both chapters' corrections are merged.

## 2026-11-18 — Making the video

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/14gg96SWrgstXFu-8biiSoN1QyQ5aJnql?usp=drive_link

**What I was working on.**

The project update for this review, in 16:9 and 9:16. My reviews had got ahead of my videos, so I
made weeks 8 to 12 together and grouped the chapters by when I reviewed them.

**Where it resisted, and what I did next.**

The first scripts read like a template, so I had them rewritten around what I actually did.
Two things also needed fixing once I looked at the frames. The chart of copied files came out as
mostly empty boxes, and its note implied the VCAM-1 error sat in one of the five half-copied
files, which my record does not show. I replaced the chart and the note.

**What Claude contributed, and what I did with it.**
- Mine: the review, the grouping of the backlog, and sending the first scripts back.
- Claude's: drafting the scripts, the visuals and the renders.
- Accepted: the rewritten scripts, after I checked every line about my own work against my records.
- Rejected/changed: the first scripts, which did not sound like me.
- Evidence: `FACTCHECK.md` in this folder.

**What I understand now, and what I still do not.**
- Understood: a note on a chart has to be true of the bar it sits under.
- Open: nothing.
