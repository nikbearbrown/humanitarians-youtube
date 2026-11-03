# Mycroft 8 — "The Rule That Lost" (part 1 of 2: the audit-layer update)

- **Reel folder:** this folder (`Mycroft8_DivijPawar_09-18-2026_the-rule-that-lost/`). Source repo for every claim: `D:\Code\mycroft\verification-layer`
- **Format:** weekly work-recap video, Mycroft series. First person, Divij's voice.
- **Target runtime:** 7:00–7:45. Narration is about 1,150 words at Kokoro pace.
- **Part 2:** `../Mycroft9_DivijPawar_09-25-2026_one-run-still-open/one-run-still-open.md`.

---

## Production brief (for downstream refinement: not read aloud)

### Where this sits in the series (read before refining)
Seven Mycroft videos have been published. Each is already on record, so this script **refers
back to them and does not re-teach them**:

| # | Published | Already taught; don't re-explain |
|---|---|---|
| 1 | accountability-mesh | ReasoningObject, append-only records, the retry-once-then-halt rule, "the log is evidence of output, not process" (ADR-06), rejecting "use another AI to check" |
| 2 | chain-of-trust | The chain of proof. "Structure is enforceable. Behavior is observable. Truth, still open." |
| 3 | when-two-agents-disagree | **What cross-validation is**, why disagreement beats agreement, correlated errors, why averaging and voting fail, "surface, don't resolve" |
| 4 | three-files-twenty-one-tests | The set-arithmetic comparator, the fixture producer, one shared run ID, null vs false, breaking tests on purpose |
| 5 | the-number-that-wasnt-there | The fabricated debt-to-equity 0.34, the five tests, 11 of 12 then 7 of 12 flagged |
| 6 | zero-for-sixteen | The labelled corpus (31 runs, 16 false positives, 0 real conflicts), the self_report ledger, the layers, "one fetch, run sequentially", "zero tests on any JavaScript" |
| 7 | fifteen-of-sixteen | concept-aware tagging kills 15 of 16, the same-data test, the model that doesn't read its input, "a legitimate ratio and a fabricated one look identical" |

**This video's job:** report what changed since Mycroft 7, including one correction to
Mycroft 7's headline. Newcomers get a three-sentence recap (B01) and nothing more.

### The correction this video owes (must stay in)
Mycroft 7 reported that concept-aware tagging killed 15 of 16 false positives. This week showed
that part of that came from a tagging mistake: the old tagger read "Return on **Assets**" as
the Assets figure and excluded it. Two of the runs it cleared contained a real internal error
(an asset-turnover figure 5× off the agent's own numbers). The 15-of-16 count itself is
unchanged and still pinned in tests. What changes is how much credit it deserves. Say this
plainly, the way Mycroft 6 and 7 treated their own numbers.

### Channel rules applied (from `fellows/divij-pawar/CLAUDE.md` and `PROOF.md`)
- **Narration style (v3, human direction 2026-09-26):** long, connected sentences with no
  hooks: no fragments, no `...` holds, no set-up questions. It keeps no em dashes (Kokoro
  turns them into commas). Check every beat by ear; split any sentence that runs together
  at its connective, or slow that beat alone (`speed_if_slurred` hints in the sheet).
- **No "it's not X, it's Y" tic** and no "here's precisely why". Scan for it again after any
  edit.
- **Framework before example:** B01 states the four-part test that the rest of the video
  applies.
- **Every claim-bearing beat has an on-screen artifact:** a real screenshot, real run output, or
  a diagram that enacts the sentence. No stock images.
- **Math is typeset** (MathTex): the asset-turnover arithmetic in B07.
- **Side-by-side, held ≥2 s,** at every "X says A, reality is B" moment (B02, B07, B13).
- **Executable evidence:** figures on screen come from real runs and fixtures (listed per beat).
  Nothing is mocked up to look like output.
- **Graphics:** use the house `graphics_lib.py` helpers (`label`/`title`/`serif`/`mono`). Brand
  colours come from `brutalist/DESIGN.md`: red is emphasis only and never means "wrong". Show
  wrong values with an ink strike plus a handnote ring. App screenshots keep the app's own
  palette.
- **No "Your Turn" beat:** Mycroft reels don't have one (channel `CLAUDE.md` §9). The viewer's
  takeaway (the four-box test) is carried by the B16 end card instead. The falsifiability beat is
  B09.
- **Claims check against `D:\Code\mycroft\verification-layer`**, and never against
  `Desktop\mycroft\accountability_layer`.

### Register (match Mycroft 5–7)
- Open cold on a number, then "Quick recap, for anyone new."
- Close with "what works now", then "what still doesn't" (the system's limitations, not project
  status), then "the smallest true claim", then the title restated, then "Signing off, Divij Pawar."
- About the work, not the working (v4): no callbacks to earlier videos, commits, test counts,
  logs or roadmap talk on screen or in narration.
- The opening carries the required intro line ("Hi, I am Divij Pawar, and this video is about...")
  and the AI-narration disclosure (channel `CLAUDE.md` §8).
- Measured and dry. Failures are stated flatly, and the video tells on itself.

### Pronunciation
- EDGAR "ED-gar"
- XBRL "X-B-R-L"
- EPS "E-P-S"
- 10-Q "ten-Q"
- Tavily "TAV-ih-lee"
- Ollama "oh-LAH-mah"

---

## Beats

_Generated from `beat_sheet.json` (the source of truth). Edit the sheet, then regenerate._

### B00 — cold open (≈31 s · ClaudeComposerAsk)
**VISUAL:** COLD OPEN LAW (CLAUDE.md SS9): B00 is the ClaudeComposerAsk bookend, never a custom Manim scene. Opens with the required FELLOWS-SUBMISSION intro line and the AI-narration disclosure (SS8). Greeting rotated to 'Bonjour' (Hola/Ola/Ciao/Namaste already used). The 15/16 vs 6/16 card itself is deferred to the B16 end-card reprise, per Mycroft6/7 precedent. Output lines are <=60 chars for 16:9; trim to <=45 for the 9:16 derivation.

**NARRATION:**
Hi, I am Divij Pawar, and this video is about a stricter way of comparing two AI agents and the test that it failed. The narration you're hearing is AI generated, but the work it describes is mine. The comparator I had built earlier removed fifteen of sixteen false alarms on a set of labelled runs, so I replayed those same sixteen runs through a stricter comparator, which raised six alarms instead of one and so failed the bar I had set for it, although along the way it found two real errors that the older rule had been hiding.

### B01 — chapter 1 - recap and the four-box test (≈22 s · B01_FourBoxTest)
**VISUAL:** Framework before example (PROOF 1-2). One line says what the system does (two agents, one company, compare the numbers), then the four boxes METRIC / PERIOD / UNIT / SOURCE, reused as a corner chip in B02-B07.

**NARRATION:**
The system runs two AI agents on the same company and compares the numbers they report, and until now most of the alarms it raised were false. This work makes that comparison rigorous, and all of it comes down to one test, which is that two figures can only be compared when they agree on what they measure, which period they cover, what unit they're in, and where they came from.

### B02 — chapter 2a - period: what the agents were handed (≈36 s · B02_WhatTheyWereHanded)
**VISUAL:** HOLD + SHOW. Real companyfacts JSON (tests/fixtures/edgar_aapl_companyfacts_sample.json in verification-layer) scrolls in mono, the Revenues fy:2018 entry highlights. Then a side-by-side table, held >=3 s (PROOF side-by-side gate). Values from RUN_LOG 2026-09-24 B0 and tests/test_edgar_facts.py TestLegacyRuleOnRealData. PERIOD box lit in corner.
**ASSETS:** assets/B02_companyfacts_excerpt.png (render from the fixture; do not mock up)

**NARRATION:**
I started with the period, by checking what the SEC data layer had actually been handing to the agents, and found that it asked for the latest value of each figure and got back a bare number with no period or unit attached. For Apple, the revenue it passed along was from fiscal twenty eighteen, under a label Apple stopped using years ago, and the earnings per share of six eighty-eight was really nine months added together, when the quarter itself was two oh two. Net income was year to date as well, and since nothing told the agents any of this, every Apple comparison the system had run until now was built on these figures.

### B03 — chapter 2b - the fix, test first (≈20 s · B03_FactWithPeriod)
**VISUAL:** A bare number '2.02' gains chips one at a time: 'Q3 FY2026', 'USD/share', '10-Q', 'accn 0000320193-26-...'. Then a duration ruler classifies spans: 80-100 days QUARTER, 350-380 ANNUAL, other YTD (datasources/edgar.py select_fact).

**NARRATION:**
Now every figure carries its period, its unit, the filing it came from, and that filing's accession number, quarters are chosen by how many days they actually span, and when a company restates a number, the restated value wins. I wrote the failing test first, against a real Apple payload, so that it pins down both of the wrong choices the old rule was making.

### B04 — chapter 2c - source: a failure recorded as ok (≈26 s · B04_FailureRecordedOk)
**VISUAL:** SHOW. The 'status: ok' line with a returned {'error': ...} is a LABELLED RECONSTRUCTION (the old recorder stored no arguments); 'ok' struck in ink. Then REAL recorded arguments from stored MSFT run 1b691654: start_date after end_date, include_domains ['NASDAQ:MSFT'], include_images as a string; the query-only retry returned 5 URLs (assets/evidence/out/B04_search_args_and_retry.json). SOURCE box lit.

**NARRATION:**
The fourth part of the test is the source, and here the problem was that the web search tool reports some failures by returning an error message rather than raising an error. Because the code only watched for raised errors, a failed search was recorded as a success and the error text was handed to the model as though it were a search result. Now a failed search gets one retry using only the query, and that retry brings back real results.

### B05 — chapter 3 - two agents at once (≈17 s · B05_BarrierAndOverlap)
**VISUAL:** SHOW from real data: bars from the recorded AAPL stream's started_at spans (1 ms start gap, 39.4 s overlap), labels in a left column (assets/evidence/out/B05_overlap_from_stream.json).

**NARRATION:**
The two agents also used to run one after the other, and now they run at the same time. On a live Apple run they started one millisecond apart and worked side by side for thirty-nine seconds, which shows that they really do overlap, although it doesn't show that a run finishes any faster.

### B06 — chapter 4a - metric and unit: comparing figures (≈41 s · B06_FigureNotString)
**VISUAL:** SHOW. A real conclusion sentence splits into tokens: metric eps_diluted, period Q3 FY2026, value 2.02. Tolerance chips from validation/facts.py TOLERANCE. Then the MSFT-format pair from tests/test_facts.py, labelled 'TEST CASE' on screen (it is constructed input, not a stored run): '82,886,000,000.0 | MATCH | $82.9 billion'. Then stored NVDA run 2220eba0: the old rule's only divergent number was '90%'; B1 extracts no figure from it. Evidence: assets/evidence/out/B06_figures_not_strings.json. METRIC and UNIT boxes lit.

**NARRATION:**
The metric and the unit come next, and the new comparator reads each number the way an analyst would, by working out what it's a figure of, which period it covers, and how close two values need to be before they count as the same. Earnings per share has to match to the cent, larger figures get half a percent of room for rounding, and two agents quoting different quarters are shown as different periods rather than flagged as a conflict. In a test built from Microsoft's filing, eighty-two point nine billion and eighty-two billion, eight hundred eighty-six million now count as the same figure, and on a stored Nvidia run, a model's rating of its own confidence at ninety percent no longer counts as a financial figure at all.

### B07 — chapter 4b - the ratio check (≈33 s · B07_RatioRecompute)
**VISUAL:** Structured fraction (no LaTeX on this machine; real text over a drawn bar, italic variables): asset turnover = revenue / assets = 265.6 / 383.3 = 0.693, recomputed and asserted in-scene. Beside it, held >=3 s: 'agent wrote 0.13 / 0.12' ringed, '5.3x'. Then net margin and GOOGL ROA cleared.

**NARRATION:**
One open problem was that a real ratio and a made-up one looked exactly the same to the system, so now, when only one agent states a ratio, the system recomputes it from that agent's own figures. Two Apple runs claimed an asset turnover of zero point one three and zero point one two, but the revenue and assets they reported in the same paragraph work out to zero point six nine, which is more than five times higher. Two Google runs stated a return on assets of eighteen point eight five, which recomputes to eighteen point nine six and is close enough to be cleared.

### B08 — chapter 4c - the correction (≈22 s · B08_WrongDrawer)
**VISUAL:** SHOW the mis-tag: 'Return on Assets of 18.85%' with only 'Assets' highlighted; the figure drops into the ASSETS drawer, then EXCLUDED. Then 'EARLIER RESULT: 15 / 16' with the footnote 'the count stands, part of it came from this mis-tag'.

**NARRATION:**
That brings me to the correction. The old tagger saw the word assets inside the phrase return on assets and filed those ratios under assets, and then it skipped them, because assets was a figure that only one agent had been given. That's how two wrong ratios passed as clean, which means the earlier result of fifteen out of sixteen still stands, but part of it was produced by that mistake.

### B09 — chapter 5a - the test it failed (≈27 s · B09_SixOfSixteen)
**VISUAL:** Falsifiability beat. Bars from zero: old rule 1/16, new rule 6/16. Callouts: '1 real: a fabricated debt-to-equity ratio of 0.34, caught by both' and '5 can't be judged: ratios with no components'.

**NARRATION:**
The bar for the new rule was that it had to do no worse than the old one on the sixteen labelled runs, and it did worse, raising six alarms where the old rule raised one. One of those six is a genuinely fabricated debt-to-equity ratio of zero point three four, which both rules catch, but the other five are ratios stated without the figures behind them, and there's no way to say who was right, because those runs never recorded what each agent had been given.

### B10 — chapter 5b - the decision (≈18 s · B10_OptIn)
**VISUAL:** HOLD: captured app screenshot of run 20c538e4's summary: headline counted from the rows, then 'Recorded verdict (concept-aware rule): Flagged for review' (assets/B10_recorded_verdict_1280.png). Then stored-run key count 7 -> 14 from two real fixtures, 'contexts' highlighted (assets/evidence/out/B10_record_growth.json).
**ASSETS:** assets/B10_recorded_verdict_1280.png; assets/evidence/out/B10_record_growth.json

**NARRATION:**
Because of that result, the new comparison is computed and shown on every company record, while the recorded verdict still comes from the old rule, and the screen always says which rule decided. Every run now also stores what each agent was given, which is exactly the information needed to settle cases like those five on future runs.

### B11 — chapter 6 - three format failures found live (≈35 s · B11_ThreeFormatFailures)
**VISUAL:** HOLD real excerpts: a stored conclusion containing the directive's instruction text (ringed); '[/conclusion]' beside '</conclusion>'; a response starting with a bare '</thought_log>'. Counts from RUN_LOG ('Directive echo, properly' and B1+U2).

**NARRATION:**
The live runs also turned up three problems with the format of the answers. Agents were copying the prompt's own instructions into their answers, which seventeen of a hundred thirty-five stored conclusions had done, so the prompt now leaves the answer tags empty and a check rejects copied text. One version of the prompt also led the model to close its answer with square brackets in three of twenty-two first attempts, and when the model began its reasoning in the same turn as a web search, that opening was being dropped, so the parser now reads the earlier turns too, and the final batch finished with no first-attempt failures across eight agents.

### B12 — chapter 7a - the table (≈20 s · B12_TheMatrix)
**VISUAL:** HOLD: real /app captures of run 20c538e4, desktop 1280 px and phone 375 px, app palette kept.
**ASSETS:** assets/B12_matrix_1280.png; assets/B12_matrix_375.png

**NARRATION:**
The comparison now appears as a table, where each figure gets its own row, with agent A in blue, agent B in orange, and the difference in the column between them. Figures that only one agent was given are folded away so they're never mistaken for a disagreement, and the headline at the top is counted from those rows rather than written by a model.

### B13 — chapter 7b - something in common (≈26 s · B13_FirstRealAgreement)
**VISUAL:** HOLD: run 20c538e4's two MATCH rows (capture), then side-by-side, held >=2 s: agent quote 'not explicitly stated in the Context' vs the context's last line carrying that EPS.
**ASSETS:** assets/B13_shared_rows_1280.png

**NARRATION:**
Most of the earlier false alarms came from the two agents never being handed the same figure, so now both of them are given net income and diluted earnings per share. On Apple, for the first time in company mode, both agents cited the same figure from the same filing and agreed with each other and with the filing, although on Nvidia and Google one agent said that figure was missing, even though it was on the last line of its input.

### B14 — chapter 8a - the honest ledger, true now (≈14 s · B14_TrueNow)
**VISUAL:** Honest-ledger list one: what the work now does.

**NARRATION:**
Several things work now that didn't before. Every figure carries its period, its unit, and its filing, failed searches are recorded as failures, the two agents run at the same time, and ratios are recomputed, which surfaced two real errors that had been hidden.

### B15 — chapter 8b - the honest ledger, still not true (≈15 s · B15_StillNotTrue)
**VISUAL:** OUTRO-LAW chapter close: list two, the work's limitations, held on screen uncleared.

**NARRATION:**
Some things still don't work. The stricter comparator is still opt-in for company runs, tagging still depends on wording, the ratio check doesn't yet account for annual versus quarterly figures, and agents still skip figures they were given, even when those figures are right there in their input.

### B16 — close - the smallest true claim (≈22 s · B16_EndCardReprise)
**VISUAL:** OUTRO-LAW close: reprise 15/16 -> 6/16, the four boxes as the takeaway, then 6 END CARD bullets about the work. B17 carries no stats.

**NARRATION:**
The smallest true claim I can make is that the comparator became stricter and lost its own test, while also catching two errors that the easier rule had been hiding. Before trusting a match between two numbers, it's worth checking what each one measures, which period it covers, what unit it's in, and where it came from, and the decision about which rule counts here still belongs to a person.

### B17 — outro (≈4 s · ClaudeTitleOutro)
**VISUAL:** OUTRO LAW: exact title restate, handle, one subline. No stats; B16 carries them.

**NARRATION:**
The rule that lost, written down, versioned, and executable. Signing off, Divij Pawar.

---

## Fact-check sheet (DOUBLE-CHECK LAW: every row traces to the repo)

| Claim | Source in `D:\Code\mycroft\verification-layer/` |
|---|---|
| FY2018 revenue $265.6B; EPS 6.88 YTD vs 2.02; net income $101.5B vs $29.8B | `logs/RUN_LOG.md` 2026-09-24 B0; `tests/test_edgar_facts.py` (`TestLegacyRuleOnRealData`) |
| "Every Apple comparison in the last three videos" | RUN_LOG B0: "Every stored AAPL cross-agent run and the real-run corpus were produced under this" |
| Tavily returned `{"error"}`, recorded as ok | RUN_LOG B0; `adapters/langchain_adapter.py` `_call_tool` |
| Barrier test; 1 ms start gap; 39.4 s overlap; speed-up not measured | RUN_LOG BL; `tests/test_concurrency_and_stream.py` |
| Tolerances; MSFT-format 82,886,000,000 = $82.9B (**a test case**, `tests/test_facts.py`, not a stored run); NVDA run `2220eba0`'s "90%" no longer a figure | `validation/facts.py` `TOLERANCE`; `assets/evidence/out/B06_figures_not_strings.json` |
| Asset turnover 0.13 / 0.12 vs 0.693 (runs 56965308, 8c67de62); "Return on Assets" mis-tag | RUN_LOG B1+U2; `tests/test_facts.py` `TestAgainstLabeledCorpus` |
| 6 of 16 vs 1 of 16; 1 real + 5 unjudgeable; opt-in; 7 → 14 stored keys | RUN_LOG B1+U2 |
| 17 echoes in 135 stored conclusions | RUN_LOG 2026-09-24 "Directive echo, properly" |
| `[/conclusion]` in 3 of 22 v1.5.1 first attempts; dropped opening turn | RUN_LOG B1+U2 |
| 74 frontend tests, 390 Python tests | Re-run 2026-09-26 (unittest discover; vitest). Re-run before recording |
| First same-figure MATCH: AAPL $29.79B vs $29.788B, $2.02 (run `20c538e4`) | RUN_LOG B2+B3; fixture `web/frontend/tests/fixtures/run_compare_b3_aapl.json` |
| NVDA / GOOGL agent A said diluted EPS missing | RUN_LOG B2+B3 |
| Still uncommitted | `git status` (79 changed paths on 2026-09-26) |

### Accuracy guardrails
- **The 15-of-16 count stands.** Don't say Mycroft 7 was wrong about the count. Say part of it
  came from a mis-tag.
- **The two asset-turnover runs** are internal errors in one agent. They aren't cross-agent
  conflicts, and they aren't flagged. They are *surfaced* ("recomputed wrong").
- **0.693 mixes the stale FY2018 revenue with current assets.** The point is internal
  inconsistency. Never call it Apple's real ratio.
- **The overlap proves concurrency, not speed.**
