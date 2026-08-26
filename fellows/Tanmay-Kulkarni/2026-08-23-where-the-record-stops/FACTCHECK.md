# FACTCHECK — Where the Record Stops

Week 19 work video · Humanitarians AI · Tanmay Kulkarni · audited 2026-08-26

Every factual claim in the shipped cuts, spoken **and on screen**. Card and prop text is
audited alongside narration (PLAYBOOK §1) — a fact-check that only reads `narration_text`
misses claims sitting in a visual prop, and this film's props carry several.

Verdicts: **SUPPORTED** · **QUALIFY** (true, needs the stated framing) · **CONSTRUCTED**
(ours, labelled as such on screen) · **UNSUPPORTED**.

Two source classes, and the film's whole subject is keeping them apart:

- **DBS's** — public disclosure, cited in frame.
- **Ours** — the reference implementation at `../dbs_credit_memo/`, which is on disk and
  testable. Claims about it were verified by running it, not by reading it.

---

## Spoken claims — DBS's facts

| Beat | Claim | Verdict | Source |
|---|---|---|---|
| B04 | Specialised agents handle "more than seventy tasks" — **tasks, not agents** | SUPPORTED | DBS newsroom, 19 Aug 2026. The distinction is DBS's own wording; a secondary source (Computer Weekly) characterises "70 to 80 agents", which the case study explicitly does **not** merge in |
| B04 | Raw data in → a review-ready first draft out | SUPPORTED | Same release |
| B04 | About 1,500 employees | SUPPORTED | Same release (following a 150-participant pilot) |
| B04 | Target of at least 30% less prep time | SUPPORTED | Same release — a **stated target**, not a measured result |
| B04 | Baseline: up to 40% of a relationship manager's week | SUPPORTED | Same release, attributed to Han Kwee Juan, Group Head of Institutional Banking |
| B05 | Capability moving at five, governance and control at one; not allowing autonomy until that closes | SUPPORTED | Nimish Panchmatia, Chief Data and Transformation Officer, DBS — Computer Weekly, 28 Jul 2026. Paraphrased in narration; the **verbatim** quote is on screen |
| B05 | "A bank saying that out loud is unusual, and it's to their credit" | **QUALIFY — editorial, and marked as such by tone** | This is the film's judgement, not a fact. The case study independently reaches the same reading: a more candid admission than any prior entry in the series |
| B11 | The workflow DBS's disclosure supports shows review → edit → finalise → submit, with no rejection | SUPPORTED | Case study §4. The illustrated workflow is one continuous path |

## Spoken claims — our own build

| Beat | Claim | Verdict | Verified how |
|---|---|---|---|
| B02 | This is not DBS's system; it is mine, built from what DBS published | SUPPORTED | Repo's own Explicit Non-Claims, quoted on screen |
| B06 | The intake schema, client lookup, gap detection and the finalize stub are inventions | CONSTRUCTED | Each is labelled CONSTRUCTED in its own source file |
| B07 | The gate has no score, no threshold, no rule, and will not start without a decision function | SUPPORTED | `src/human_review_gate.py` — raises `TypeError` at construction |
| B08 | An unrecognised return raises rather than continuing | SUPPORTED | Same file — `ValueError`, with the message shown verbatim |
| B09 | A test hands the gate a garbage answer and checks finalize was never called | SUPPORTED | `tests/test_human_review_gate.py` |
| B09 | "Six modules, six test files, all passing" | SUPPORTED | **Run 2026-08-25**, all six pass. Not taken from the README |
| B10 | The plan had four stages; the code has five | SUPPORTED | `dbs_credit_memo/README.md` documents the refinement |
| B10 | Keeping draft synthesis pure forced client lookup into its own stage | SUPPORTED | Same, and visible in `src/orchestrator.py`'s halt map |
| B11 | The reject path's *name* comes from DBS's language; its *existence* comes from the governance quote | SUPPORTED | Repo documents exactly this distinction |

## On-screen claims

| Beat | On screen | Verdict | Note |
|---|---|---|---|
| B02 | Four Explicit Non-Claims lines | SUPPORTED | Verbatim from the repo README, not paraphrased |
| B04 | CONFIRMED rows + **"DBS newsroom release, 19 August 2026"** | SUPPORTED | Source line added after review 1 found the beat asserting DBS's facts with no citation in frame |
| B05 | Verbatim quote + name, title, organisation, publication, date | SUPPORTED | The model for how every borrowed fact should appear |
| B06 | CONSTRUCTED rows | CONSTRUCTED | Group caption reads "I invented it — and labelled it" |
| B07–B09 | Real code from `human_review_gate.py` and its test | SUPPORTED, **with disclosure below** | |
| B10 | Five stage names + **"My decomposition, not DBS's"** | CONSTRUCTED | Marker added after review 1; without it a viewer joining at that beat could read the five stages as DBS's architecture |
| B11 | The reject-path row, marked *"reasoned, never demonstrated"* | **QUALIFY — deliberately** | Rendered inside BLANK with an explicit note rather than filed under CONSTRUCTED, because it fits neither cleanly |
| B12 | Three questions + the three columns | SUPPORTED | The film's own framework |

### Disclosure: the code on screen is a dedented excerpt

B07–B09 show real lines from the repository, **dedented** and with elisions marked `…`.
Line breaks inside multi-line string literals were re-wrapped to fit the frame; the string
content and every token shown are unchanged. No line on screen is invented. The elision
marks are visible in frame rather than silent — a film about labelling what you changed
should label this too.

Portrait fits roughly half the characters per line of landscape at the same readable size,
which is why the excerpts are short. See `QC-REPORT.md`.

### One prop that needed a decision

`B01`'s composer card carries `modelLabel: "Opus 5"`. The card is a stylised UI, not a claim
about tooling, and the beat's narration makes no claim about which model did anything. It is
accurate — Claude Opus 5 was used in building this — and it is not load-bearing. Recorded
here because it is exactly the class of prop that carried a wrong implication in the topic
video (`Fable 5`, a model that had not been used), and the check should be run every time
rather than assumed.

## Claims deliberately **not** made

| Claim | Why it is absent |
|---|---|
| "70 to 80 agents" | Computer Weekly's characterisation, not DBS's. The film says **tasks**, which is what DBS said |
| Anything tying DBS's ~S$1bn bank-wide AI figure to the credit-memo tool | No DBS source connects them; the case study keeps the three disclosures apart and so does the film |
| That DBS Joy is agentic | It was Gen AI through FY2025 and became agentic only in July 2026. The film does not mention Joy at all |
| That DBS's governance is inadequate | The film says the opposite: DBS is being careful in public and that is to their credit |
| That this repository replicates DBS's architecture, agent count, task breakdown, data sources or review process | The Explicit Non-Claims card says so on screen, in the first 45 seconds |
| A count of memos processed | DBS discloses proportion of time, not throughput. No volume figure exists to state |

## Dated and version-sensitive

- **DBS newsroom release** — 19 August 2026. The 30% figure is a target; if DBS later
  publishes a measured result, B04's framing needs revisiting.
- **Panchmatia quote** — Computer Weekly, 28 July 2026. A governance posture can change.
- **"All six test files pass"** — true as run on 2026-08-25 against the repo at that commit.

## Outstanding

None. Review 1's single production-gate failure (B04's missing citation) is closed and
verified on frame at 85.0s of the paced cut.

## Method

Claims were extracted from `narration_text` **and** from every `shot.remotion.props` string
in both beat sheets, then checked against the DBS sources or against the repository by
running it. Frames were sampled at the moment of each assertion in both aspects — see
`PROOF-REVIEW.md` for what each review pass caught.
