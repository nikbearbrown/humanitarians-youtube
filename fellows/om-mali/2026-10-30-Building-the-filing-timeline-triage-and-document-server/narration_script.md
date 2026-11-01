# Building the filing timeline, triage and document server — narration script

**AI Debt Tracker, week 3**

**Target:** 3:00 · ~450 spoken words (441)
About 2:56 at 150 words per minute, 3:09 at 140. Steady, unhurried — let each number land.
Spoken forms are written out below where they differ from what's on screen.

The story of this week: the agent's first real job is finding the debt news among hundreds of
filings — and the check that it misses nothing has to be set up before it runs.

---

### 0:00 — Opening · on camera

> Hi I'm Om Mali. This video is about teaching my AI debt tracker to find the debt news in SEC
> filings — with a filing timeline, a triage step and a document server. This is week 3 of the AI
> Debt Tracker.

*Shot: straight to camera.*

---

### 0:15 — Last week's leftovers · cut to `adt-w3-holdout.png`

> First, last week's leftovers. Three data problems are fixed, and last week's three test reports
> now all agree. But I'd read those reports by now, so I graded five fresh ones, once. Of the three
> that had any debt, only one agreed. The answer key counted the banks' extra allotment on a Super
> Micro convertible as a second bond, and Core Scientific's small notes have no due date anywhere in
> the data. Two new defects — written down for next week, not tuned away.

*Shot: the two bars; then the three names as each is spoken.*

---

### 0:50 — The timeline · cut to `adt-w3-funnel.png`

> Now the agent's first job: finding the news. For every quarter, the timeline gathers each 8-K,
> prospectus and term sheet filed in the window — including the subsidiaries that borrow on a
> company's behalf. Across the development quarters, that's five hundred and ninety-three filings.

*Shot: the top bar, then the line of filing types under the bars.*

---

### 1:08 — Triage · stay on `adt-w3-funnel.png`

> Most aren't about debt at all: earnings, dividends, board changes. Triage sorts them. Five plain
> rules decide two thirds — a new-borrowing item on an 8-K, a prospectus selling notes rather than
> shares, a filing with no debt words at all. Only the doubtful third, a hundred and ninety-nine,
> goes to the small local model, at about three seconds each. A hundred and eighty-four are kept.

*Shot: second bar, ochre bar, red bar in turn.*

---

### 1:38 — The check · cut to `adt-w3-triage.png`

> Does it miss anything? Fifty filings, drawn by a fixed random rule, were labelled against a
> written definition before triage ran — by Claude, a different model from the one being tested.
> Triage found all twenty-four debt filings; the pass line was ninety-five percent. It raised two
> false alarms: a tender offer for Alphabet shares, not notes, and a TeraWulf acquisition. And it
> kept all twenty-two filings that last week's search found announcing a bond change.

*Shot: top bar and the dashed pass line; then the bottom red bar.*

---

### 2:10 — What went wrong · on camera

> Not everything went smoothly. The first run crashed when a model answer got cut off mid-sentence,
> so now an unreadable answer keeps the filing. The check also exposed a bug in last week's search:
> "zero percent" was matching inside "twenty percent". And eight of the model's twenty-one yes
> answers gave a quote that isn't word for word in what it read.

---

### 2:32 — The document server · cut to `adt-w3-docs.png`

> That's why the document server matters. It turns a filing into numbered sentences and table
> cells, so the agent cites "sentence five" instead of retyping one and a half billion dollars. And
> it refuses to open the report the agent will be graded on.

*Shot: the `→ s5` line, then the red refusal.*

---

### 2:48 — What's next · on camera

> Next week: fix the two new defects, check fresh reports again, and build the event reader that
> turns these filings into structured debt events.

*Shot: end card.*

---

## Notes

**"Week 3"** is the third video of this project. The first covered grounding the tracker in SEC
filings, the second the answer key, grader and baseline.

**"Of the three that had any debt, only one agreed"** is the honest centre of the first section. Five
fresh reports were drawn by seed before reading; two (Cipher Mining, TeraWulf) had no debt at those
dates, so they are left out rather than counted as agreements. Dell's totals agree exactly.

**One more mistake, not in the narration:** the hand-check transcription (Claude's) took a Super Micro
coupon from the notes' *original* terms; they were amended in 2025. It's disclosed in
`docs/handcheck.md` and doesn't change the verdict — the double-counted allotment alone makes that
report disagree. If you have time, add: "and one reading mistake was mine."

**"Labelled … by Claude"** must stay. The labels are a model judgment, made before triage ran; the
labels file is byte-for-byte unchanged after the run. Don't say "I labelled".

**"All twenty-four" is recall, not accuracy.** Precision is 24 of 26 and the event type is right on 20 of
24 — both are on screen. Twenty-four positives is a small set; next week runs a fresh triage check.

**"Twenty-two of twenty-two"**: the first version of the report said 21 of 22. The "missed" one was last
week's error — a 0% 2031 convertible credited to an earnings release because "0%" matched inside
"escalates 20%". Fixed (P40); last week's counts didn't change. That is the "zero percent" line.

**"Isn't word for word in what it read"**: the check compares the first 80 characters of the model's
quote with the text it was given. A mismatch can be a paraphrase rather than an invention, so don't
say "made up". The filing is still kept; the event reader must re-check every fact.

**If you run long,** drop "earnings, dividends, board changes" at 1:08 and "mid-sentence" at 2:10.

## Where every number comes from

| Line | Number | Source |
|---|---|---|
| 0:15 | 3 fixes (P35–P37); last week's set 3 of 3; fresh set 1 of 3 gradable, 2 not gradable; P38, P39 | AI Debt Tracker `docs/handcheck.md`; `manifests/handcheck/*.json`; DESIGN.md P35–P39 |
| 0:50 | 593 filings (8-K 469, 424B 94, FWP 30), subsidiaries included | `$AI_DEBT_DATA/week3/pool.json` ← `scripts/triage_eval.py pool` |
| 1:08 | rules 394 (two thirds), model 199, median 3.1 s, kept 184 | `week3/triage_qwen3_4b.json` ← `triage_eval.py run qwen3:4b`; `docs/triage.md` |
| 1:38 | 50 labelled (30 random + 20 debt-word), 24 of 24 found, 2 false alarms, 22 of 22 | `docs/triage.md`, `docs/triage_labels.md`, `manifests/triage_labels.json` |
| 2:10 | first run crashed; P40 "0%" in "20%"; 8 of 21 quotes not found | `docs/triage.md` (Notes on this run); `logs/RUN_LOG.md` 2026-10-31 |
| 2:32 | s5 = Oracle's $1.5 bn 4.200% 2029 notes sentence; target report refused | live call to `documents/store.py` in the figure build |
| 2:48 | next week's plan | DESIGN.md §17 |

## Figures (in this folder)

- `adt-w3-holdout.png` — the answer key re-checked: last week's 3 after fixes (3 of 3), five fresh reports
  (1 of 3 gradable); what each fresh report showed.
- `adt-w3-funnel.png` — 593 filings → 394 decided by rules → 199 asked the model → 184 kept.
- `adt-w3-triage.png` — the week 3 check: 24 of 24 found, 24 of 26 kept are debt, 20 of 24 event types,
  22 of 22 of last week's announcements; the 95% pass line.
- `adt-w3-docs.png` — a filing as addressable pieces: search → `s5`; the graded report refused.

Each has an `.svg` beside it. Every number is read from the project's saved results, and the figure
build fails if any differs from the recorded value.
