# Grounding an AI debt tracker in real SEC filings — narration script

**AI Debt Tracker, week 1**

**Target:** 3:00 · ~440 spoken words (438)
About 2:56 at 150 words per minute, 3:08 at 140. Steady, unhurried — let each number land.
Spoken forms are written out below where they differ from what's on screen.

This is the first video of a **new project**: what it is, why it matters, and the evidence that
it can work, measured on real filings before the agent itself is built.

---

### 0:00 — Opening · on camera

> Hi I'm Om Mali. This video is about the AI Debt Tracker — a new Mycroft project — and how I
> grounded it in real SEC filings before building the agent.

*Shot: straight to camera. Lean on "new project" — a fresh start after the Private AI Valuation
series.*

---

### 0:12 — Why debt · cut to `adt-w0-borrowing.png`

> The AI build-out is increasingly paid for with borrowed money. In twenty twenty-five, the five
> biggest cloud companies sold a hundred and twenty-one billion dollars of US bonds — more than
> four times their recent average. Mycroft has agents for news, patents and hiring, but nothing
> that tracks debt.

*Shot: the two bars. Pause after "a hundred and twenty-one billion dollars".*

---

### 0:32 — What it does · cut to `adt-w0-pipeline.png`

> The agent watches SEC filings from twenty-five AI companies, reads each debt announcement, and
> keeps a ledger of every bond and loan — the amount, the interest rate, the due date — then turns
> it into a signal: total debt, new borrowing, and what falls due in the next two years. It's graded
> against each company's next quarterly report, and a point-in-time server I built refuses it any
> filing published after the report it's graded on.

*Shot: walk left to right across the boxes, then hold on the bottom box at "refuses". This is the
line that makes every later number trustworthy: the agent can't peek at the answer.*

---

### 1:02 — Is it worth building · cut to `adt-w0-feasibility.png`

> First, could it fail? On forty-six real company-quarters, eighty-seven and a half percent of new
> bonds were announced before the report showed them. And just copying last quarter forward is
> wrong almost half the time — so there's something to beat.

*Shot: the first two rows only. The dashed line is the pass mark set before the test — let it
show.*

---

### 1:18 — The answer key · cut to `adt-w1-levels.png` *(new figure)*

> Then I built the answer key: every quarterly report from mid twenty twenty-four to now, for the
> twenty-five AI companies and seventy-five non-AI companies to compare against. The first
> surprise: companies tag their debt more coarsely than they appear to. Microsoft's thirteen
> "bonds" are really thirteen batches of bonds. Oracle's quarterly reports list only the newest
> few. Counted honestly, by how much of the debt is itemised, fifteen companies are graded bond by
> bond — not the twenty-one I'd assumed.

*Shot: the 25 companies as three stacked groups — bond by bond 15, by deal 4, totals only 6 —
with the assumed 21 as a ghost bar. Pause after "not the twenty-one I'd assumed".*

---

### 1:50 — What it grades on · stay on `adt-w1-levels.png`, bottom strip

> So each quarter is graded at the detail its report really gives. That leaves four hundred and
> ninety-five dated test cases — ninety-five to build on, and four hundred held back as the test,
> never tuned on. And bonds now match from one report to the next ninety-three percent of the
> time, above the pass mark I set beforehand.

*Shot: the strip along the bottom — 495 cases, 93.4% matched, pass mark 90%.*

---

### 2:14 — Choosing the model · cut to `adt-w1-bakeoff.png` *(new figure)*

> Last, the model, on my laptop's eight-gigabyte GPU. I gave three local models twenty-nine real
> announcements and no hints, with the rule for picking a winner fixed before the test. The
> smallest won: Qwen3 at four billion parameters read ninety-nine
> percent of the details, in about six seconds a filing, at zero cost. The eight-billion version
> got eighty-eight percent — and sometimes looped on its own answer until it was cut off.

*Shot: three bars, 4B first. Then the seconds and the zero along the bottom.*

---

### 2:43 — What's next · on camera

> The company list and the model are frozen. Next: build the grader and the do-nothing baseline
> first, so the score the agent has to beat exists before the agent does.

*Shot: end card.*

---

## Notes

**Say "Qwen" as "chwen".** Say "eight-K" for 8-K if it comes up; it doesn't in the script.

**Keep the tense honest.** The answer key, the point-in-time server, the matcher and the model
test are built and measured; the agent that reads and keeps the ledger is not built yet. "Watches"
and "reads" at 0:32 describe the design. If that sounds too finished, say "will watch" and "will
read".

**If you run long,** drop "Oracle's quarterly reports list only the newest few" at 1:18 (about
four seconds) — Microsoft carries the point on its own.

**Don't round 87.5% up to "nearly ninety".** It is 56 of 64 genuinely new bonds that carried a
stated interest rate; nine old bonds that were only newly tagged are excluded.

**"Almost half" is the conservative number.** Raw, carry-forward differed from the next report in
33 of 46 quarters, but some of that is companies changing how they tag; 21 of 46 is the count with
a change confirmed by an announcement.

**"Fifteen, not twenty-one".** 21 was the count of companies that *looked* per-bond by counting
tagged members. Measured by coverage (itemised instruments must account for ≥ 80% of total debt),
14 qualified, and the gate moved TeraWulf up on a 4–4 tie: 15. Say "fifteen".

**"Ninety-three percent" is on the per-bond quarters,** the ones graded bond by bond (594 of 636
on the dev split). Across every quarter it is 85%, the gap being Intel and Oracle quarters that
list few bonds and are graded on totals anyway. Don't drop "from one report to the next".

**The model test is one plain prompt, not the finished system,** and 99% is after correcting six
expected values the documents themselves contradicted (95% before; same winner). Twenty-nine
documents is a small set — the 4B lead is large, but say "twenty-nine" so nobody hears it as a
benchmark.

## Where every number comes from

| Line | Number | Source |
|---|---|---|
| 0:12 | $121bn in 2025 vs a $28bn/yr 2020–24 average | Bank of America data, reported by Reuters / Yahoo Finance ("AI hyperscalers will drive higher US corporate bond supply in 2026"); `figdata.json` |
| 0:12 | no Mycroft agent tracks debt | the Mycroft repo's `recipes/` (~99 recipes; none on debt or credit) |
| 0:32 | 25 AI companies; point-in-time server refuses later filings | AI Debt Tracker `universe_v1.json`; `src/ai_debt_tracker/mcp_servers/edgar_pit_core.py` and `tests/test_edgar_pit.py` |
| 1:02 | 46 company-quarters; 87.5% (56/64); 21/46 | `figdata.json` ← spike artifacts; `docs/feasibility.md` |
| 1:18 | 25 + 75 companies; Jul 2024 – Sep 2026 reports; Microsoft's 13 issuance groups; Oracle's partial 10-Qs; 15 per-bond vs 21 assumed | `docs/universe_v1_review.md`, `universe_v1.json`, `manifests/generalisation.csv`, `manifests/week1_gate.json`; DESIGN.md P22–P23 |
| 1:50 | 495 test cases; 93.4% matched (594/636), pass line 90% | `manifests/dev.csv` + `test.csv` (95 + 400); `scripts/f1_matching.py dev`; `docs/feasibility.md` |
| 2:14 | 29 announcements, 3 models; qwen3:4b 99% (141/143), ~6 s median, $0; qwen3:8b 88% with 2 runaway answers; 8 GB GPU | `docs/bakeoff.md` ← `scripts/bakeoff.py report`; `manifests/bakeoff_truth_corrections.json` |
| 2:43 | company list and model frozen | `manifests/week1_gate.json`; `docs/week1_review.md` |

## Figures

Reused: `adt-w0-borrowing.png`, `adt-w0-pipeline.png`, `adt-w0-feasibility.png` (show only its
first two rows). `adt-w0-model.png` is retired — its 8B baseline is superseded by the bake-off.

New, to be generated from the project's saved results (add to `figdata.json` and `make_figures.py`):
- `adt-w1-levels.png` — 25 companies by grading level (15 / 4 / 6) against the assumed 21; bottom
  strip: 495 test cases, 93.4% matched against a 90% pass line.
- `adt-w1-bakeoff.png` — fields read correctly: qwen3:4b 99%, llama3.1:8b 91%, qwen3:8b 88%;
  under each, median seconds per filing and runaway count; $0.
