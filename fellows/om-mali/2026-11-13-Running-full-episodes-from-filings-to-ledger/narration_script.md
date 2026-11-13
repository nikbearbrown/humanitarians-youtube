# Running full episodes from filings to ledger — narration script

**AI Debt Tracker, week 5**

**Target:** 2:05–2:15 · 311 spoken words
About 2:04 at 150 words per minute, 2:13 at 140. Steady, unhurried — let each number land. Spoken forms are written out below where they differ from what's on screen.

The story of this week: the pieces now run as one system, quarter by quarter, and the result is measured against
doing nothing — it finds the new bonds, and the bonds it wrongly adds are named and counted.

---

### 0:00 — Opening · on camera

> Hi I'm Om Mali. This video is about running my AI debt tracker end to end, from a quarter's filings to a ledger
> of every bond the company owes. This is week 5 of the AI Debt Tracker.

*Shot: straight to camera.*

---

### 0:15 — The graph · cut to `adt-w5-graph.png`

> Until now the pieces worked alone. This week they run as one graph. For each company and quarter, code lists the
> filings, triage keeps the ones about debt, and a reader runs on each of those, in parallel. Code then merges what
> they found, retires bonds that have matured, and applies the rest to the opening ledger. Then it checks its own
> work. I ran it on all ninety-five development quarters, and every one finished.

*Shot: left to right along the graph; the three red readers.*

---

### 0:50 — Against doing nothing · cut to `adt-w5-episodes.png`

> The baseline is carrying last quarter's debt forward. On the forty-five quarters graded bond by bond, recall rose
> from ninety-one percent to ninety-eight. The real story is the new bonds. Thirty-four were issued in those
> quarters. Carrying forward finds none of them. The tracker found thirty.

*Shot: the red recall bar, then "30 of 34".*

---

### 1:15 — What it got wrong · cut to `adt-w5-additions.png`

> Precision fell, from ninety-three to ninety. So I checked every bond it added. Forty were real. Ten were existing
> notes read from a prospectus as if new, ten were launch notices with no interest rate yet, and four were the
> banks' option to buy more. All three are fixes to the merge step. The first run also had a timing bug: bonds sold
> after the quarter ended went into it. I fixed that on development data and report both runs.

*Shot: the stacked bar, then each legend line.*

---

### 1:55 — Checked again on fresh filings · cut to `adt-w5-fresh.png`

> I also re-checked last week's pieces on filings nobody had read. Triage found fifteen of fifteen, passing this
> time. The reader beat pattern matching again, ninety-one percent to seventy-four, though asking the model directly
> still reads more numbers. And the answer key agreed on three of four reports.

*Shot: the triage bar past the dashed line, then the three reader bars.*

---

### 2:20 — What's next · on camera

> Next week: those merge fixes, then reading the opening ledger itself instead of borrowing it, and investigators for
> the fifty-three questions the checks raised.

*Shot: end card.*

---

## Notes

**"Every one finished"**: 95 of 95 dev episodes ran end to end — the week 5 check (DESIGN.md §11). The run was stopped
once by the laptop running low on memory and resumed from its checkpoints; that doesn't change the result.

**"The baseline … recall rose from 91 to 98"**: 90.9% → 97.8%, paired +6.9 points (+4.7 to +9.4). Both start from the
same opening ledger, taken from the last report (oracle start), so the gap is what reading added. Don't say the
tracker reads the opening ledger — that's next week.

**"Precision fell, from 93 to 90"**: 92.8% → 90.2%. The breakdown of the 26 false additions is Claude's reading of
each one after scoring (a judgment), labelled as such in the figure. Two more were misreads.

**"A timing bug"**: P55. The first run's precision was 89.2%; recall and new bonds caught were the same. Both are in
`docs/episodes.md`.

**"Fifteen of fifteen"**: last week 8 of 9. One miss would have been 93%, below the 95% line, so it is still a small
check. Labels were written and hashed before the run.

**"Asking the model directly still reads more numbers"**: B2 96%, but with 15 instruments that aren't in the filings
and no cited sentence behind any number. Don't say the reader is more accurate.

**"Three of four"**: four gradable of five drawn; Applied Digital couldn't be graded (P44, P48). TeraWulf is the one
disagreement (P47).

**Not reviewed by a person.** The week was delegated end to end; the gate record says DELEGATED, not CLEARED.

**If you run long,** drop "Then it checks its own work" at 0:15.

## Where every number comes from

| Line | Number | Source |
|---|---|---|
| 0:15 | 95 quarters, every one finished | AI Debt Tracker `docs/episodes.md` |
| 0:50 | 45 quarters; recall 90.9% → 97.8%; 30 of 34 new bonds, B0 0 | `docs/episodes.md` |
| 1:15 | precision 92.8% → 90.2%; 40 real, 10 / 10 / 4; P55 | `docs/episodes.md`, DESIGN.md P55–P58 |
| 1:55 | triage 15 of 15; reader 91% vs B1 74% (B2 96%); answer key 3 of 4 | `docs/triage.md`, `docs/reader.md`, `docs/handcheck.md` |
| 2:20 | 53 open questions | `docs/episodes.md` |

## Figures (in this folder)

- `adt-w5-graph.png` — the episode graph with its counts: 882 filings, 245 kept, parallel readers, 53 questions.
- `adt-w5-episodes.png` — tracker vs carry-forward: recall 97.8% vs 90.9%, precision 90.2% vs 92.8%; new bonds 30 of 34 vs 0.
- `adt-w5-additions.png` — the 66 bonds added in quarters the report itemises: 40 real, 10 old notes, 10 launches, 4 options.
- `adt-w5-fresh.png` — fresh checks: triage 15 of 15, reader 91% / B1 74% / B2 96%, answer key 3 of 4.

Each has an `.svg` beside it. Every number is read from the project's generated reports, and the figure build fails
if any differs from the recorded value.
