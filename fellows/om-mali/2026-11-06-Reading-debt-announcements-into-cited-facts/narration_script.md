# Reading debt announcements into cited facts — narration script

**AI Debt Tracker, week 4**

**Target:** 2:30–2:40 · 371 spoken words
About 2:28 at 150 words per minute, 2:39 at 140. Steady, unhurried — let each number land.
Spoken forms are written out below where they differ from what's on screen.

The story of this week: the agent can now read a debt filing into facts it can point to — and the
honest result is that pointing buys traceability, not accuracy.

---

### 0:00 — Opening · on camera

> Hi I'm Om Mali. This video is about teaching my AI debt tracker to read a debt announcement into
> structured facts, where every number points back to the sentence it came from. This is week 4 of
> the AI Debt Tracker.

*Shot: straight to camera.*

---

### 0:15 — The reader · cut to `adt-w4-grounding.png` (top half)

> Last week the agent learned to find the debt news. This week it reads it. The rule I set at the
> start of the project is that the model never types a number. So the event reader works in three
> steps. Code picks out the passages that state debt terms. The local model lists each bond and, for
> every value, copies the exact words and names the passage. Then code checks those words really are
> in that passage, and parses the number itself.

*Shot: the Alphabet passage, then the copied value.*

---

### 0:45 — The result · cut to `adt-w4-reader.png`

> I tested it on twenty-four filings whose sixty-six bonds and loans were labelled before anything
> ran. The week's check was simple: beat plain pattern matching. It did — ninety-four percent of
> fields right, against eighty-four. But the third bar is the honest one. Just asking the same model
> to type the numbers got every field right. On clean pricing documents, a small model reads numbers
> well. What the reader adds isn't accuracy. It's a cited sentence behind every value.

*Shot: B1 bar, red reader bar, then the ochre B2 bar.*

---

### 1:20 — What the refusal caught · cut to `adt-w4-grounding.png`

> And that check earned its place. For Alphabet's euro bonds, the model "copied" one and a half
> billion dollars — but the filing says euros. It rewrote the currency sign. Those values weren't in
> the text, so they were refused: missing, not wrong. Eight refusals were currency signs like that.

*Shot: the red "refused" line, then the bars.*

---

### 1:42 — Triage, fresh · cut to `adt-w4-triage.png`

> I also re-checked last week's triage on fifty new filings, labelled first. It found eight of nine —
> below my ninety-five percent line. The miss was an IBM prospectus whose cover leaves even the year
> blank. I logged it and didn't tune it away. Nine positives is a small check, and I say so.

*Shot: the red bar short of the dashed line.*

---

### 2:05 — The answer key · cut to `adt-w4-holdout.png`

> The answer key got the same treatment. Five fresh reports, chosen before reading: one agreed. Four
> new defects, each in a different company's tagging — like one Marvell bond tagged under two names.
> Logged for next week.

*Shot: the 1-of-5 bar, then the four names.*

---

### 2:25 — What's next · on camera

> Next week: fix what the fresh checks found, check again on new filings, and connect the reader to a
> ledger, so whole quarters run end to end.

*Shot: end card.*

---

## Notes

**"Week 4"** is the fourth video of this project, after grounding the tracker in SEC filings, the answer
key and baseline, and the filing timeline and triage.

**"The third bar is the honest one"** must stay. B2 read 160 of 160 fields; the reader read 157 of 167. Don't
say the reader is "more accurate". It passes the check it was set (beat B1), and its value is provenance.

**"Labelled before anything ran"**: the labels are Claude's reading of each filing (a model judgment), checked
by machine against the next quarterly report: 51 of 51 new bonds found with the same coupon and year. Don't say
"I labelled".

**"Eight refusals were currency signs"**: 24 copies were refused in all. The other 16 were the word "null"
written as text for a value the filing doesn't state — bookkeeping, no effect on scores. If you have time, add:
"the rest were the model writing the word null."

**"Eight of nine — below my line"** is a failed check, and the video says so. One of the "false alarms" is
probably a labelling error (Applied Digital's $150 m Macquarie financing in an earnings release); labels are not
changed after a run.

**"Chosen before reading"**: one slip — the key's totals for those five reports were printed once before the
transcriptions were written. Disclosed in `docs/handcheck.md`. It doesn't change the result.

**Not reviewed by a person.** The week was delegated end to end; the gate record says DELEGATED, not CLEARED.

**If you run long,** drop "On clean pricing documents, a small model reads numbers well" at 0:45.

## Where every number comes from

| Line | Number | Source |
|---|---|---|
| 0:45 | 24 filings, 66 instruments; 94% (157/167), 84% (135/160), B2 160/160 | AI Debt Tracker `docs/reader.md`, `manifests/reader_truth.json` |
| 1:20 | Alphabet €1,500,000,000 copied as "$1,500,000,000"; 8 currency refusals of 24 | `docs/reader.md`; `$AI_DEBT_DATA/week4/reader_reader.json` |
| 1:42 | 50 fresh filings, 8 of 9, pass line 95%, IBM blank cover (P46) | `docs/triage.md`, `manifests/triage_labels_w4.json` |
| 2:05 | 1 of 5; P41–P44 (Marvell = P42) | `docs/handcheck.md`, `manifests/handcheck/` |
| 2:25 | next week's plan | DESIGN.md §17 |

## Figures (in this folder)

- `adt-w4-grounding.png` — the copy check: Alphabet's euro passage, the "$" copy refused; 227 values in the cited
  passage, 3 in another, 24 refused.
- `adt-w4-reader.png` — fields right: B1 84%, the event reader 94%, B2 100%; extras 1, 29, 9.
- `adt-w4-triage.png` — the fresh triage check, 8 of 9 below the 95% line; last week's set 24 of 24 (calibration).
- `adt-w4-holdout.png` — the answer key on five fresh reports: 1 of 5; four new defects.

Each has an `.svg` beside it. Every number is read from the project's saved results, and the figure build fails
if any differs from the recorded value.
