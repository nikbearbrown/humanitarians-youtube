# Mycroft 9 — "One run, still open" (part 2 of 2: the audit-layer update)

- **Reel folder:** this folder (`Mycroft9_DivijPawar_09-25-2026_one-run-still-open/`). Source repo for every claim: `D:\Code\mycroft\verification-layer`
- **Format:** weekly work-recap video, Mycroft series. First person, Divij's voice.
- **Target runtime:** 7:15–8:00. Narration is about 1,200 words at Kokoro pace.
- **Part 1:** `../Mycroft8_DivijPawar_09-18-2026_the-rule-that-lost/the-rule-that-lost.md`.

---

## Production brief (for downstream refinement: not read aloud)

### Where this sits in the series
The series table in Part 1's brief lists what Mycroft 1–7 already taught. For this
part, these threads matter most. The script calls back to each and re-teaches none:

- **Mycroft 1:** append-only records enforced by the database, and "when two agents disagree,
  the disagreement becomes a first-class output". So don't re-explain append-only, and don't
  re-argue "use another AI to check".
- **Mycroft 3:** averaging and voting amplify shared errors. "Never resolve what you can't
  prove is independent. Surface it." "Machines verify conformance. Humans verify adequacy." So
  **don't** re-argue why the software, a third AI or a vote can't decide.
- **Mycroft 4:** "A flagged contradiction triggers nothing." "The judgment stays with the human.
  That was the point." **This video is the payoff:** a flag now triggers a hard stop.
- **Mycroft 3's four literature types of disagreement** (stylistic, reasoning, high-confidence,
  adversarial) describe *what the disagreement looks like*. B5's classes (data, assumption,
  weighting) describe *what caused it*. Mention the difference in one line and move on.

### What's evidenced vs. being added
The user asked for B4–B6 and U5–U9 to be included because they are being built now. As of
2026-09-26:

| Beats | Status |
|---|---|
| B01–B13 | Logged in `logs/RUN_LOG.md` (BG+U3, B2+B3, BP+U4). BP has no UI yet, so B12 shows recorded output |
| B14–B16 | Roadmap only (B4, B5, B6, U5, U7, U8, U9) |

Beats marked **[verify]** must be checked against the code and RUN_LOG before GATE P is signed.
Specifics that don't match get corrected or cut (DOUBLE-CHECK LAW). Any figure in them that isn't
from a real run must be labelled illustrative on screen.

### Channel rules applied
The same rules as Part 1:
- Narration v3: long, connected sentences, no hooks, no em dashes (human direction).
- No "it's not X, it's Y" tic.
- Framework before example (B01).
- An on-screen artifact on every claim beat; side-by-side held ≥2 s.
- Typeset math.
- Executable evidence only.
- House `graphics_lib.py`, DESIGN.md colours, and never red for "wrong".
- No "Your Turn" beat (channel `CLAUDE.md` §9). The takeaway (the four-part gate) is carried by
  the B19 end card. The falsifiability beats are B09, B11 and B18.
- The opening carries the required intro line and the AI-narration disclosure (§8).

### About the work, not the working (v4)
No callbacks to earlier videos, commits, test counts, logs or roadmap talk, on screen or in
narration. The series table above is context for the refiner only.

### People
- **The reviewer** is a person and is never named on screen (placeholder "J. Reviewer"). Use
  "they". Identity is self-declared, and the script says so.
- **The AI that built the gate** is mentioned once (B07), flatly, to make the P4 point.

---

## Beats

_Generated from `beat_sheet.json` (the source of truth). Edit the sheet, then regenerate._

### B00 — cold open (≈27 s · ClaudeComposerAsk)
**VISUAL:** COLD OPEN LAW (CLAUDE.md SS9) with the required intro line and AI-narration disclosure (SS8). Greeting rotated to 'Konnichiwa'. The narration never says which year is right, on purpose: the system doesn't know, and the video mirrors it. Run ec1a3b44 must still be AWAITING_DECISION on recording day (check before building).

**NARRATION:**
Hi, I am Divij Pawar, and this video is about what happens when two AI agents disagree and a person has to decide between them. The narration you're hearing is AI generated, but the work it describes is mine. This run asked two agents when the first Pokémon game reached North America, and one of them said nineteen ninety-eight while the other said nineteen ninety-six. The system flagged the disagreement and then stopped, and it has been waiting for a person to decide ever since.

### B01 — chapter 1 - recap and the four parts of a gate (≈27 s · B01_FourPartsOfAGate)
**VISUAL:** Framework before example. Recap chip for part 1, one serif line ('a flagged contradiction is only useful if something happens next'), then TRIGGER / STOP / DECIDER / RECORD, reused as a chip in B02-B07.

**NARRATION:**
Part one made the comparison between the two agents stricter, so that figures are now compared by metric, period, unit, and source. This part is about what happens when that comparison finds a real disagreement, because flagging a contradiction is only useful if something actually happens next. A gate like this needs a trigger you can test, a stop that actually holds, a named person who gives a written reason, and a record nobody can edit, and without all four it's really just a warning.

### B02 — chapter 2a - trigger (≈25 s · B02_Trigger)
**VISUAL:** Matrix rows sorted by status (validation/gate.py): only the MISMATCH row gets a gate icon; an UNCORROBORATED row gets a review marker; a pre-gate stored run is tagged NOT_GATED. TRIGGER box lit.

**NARRATION:**
The trigger is deliberately narrow, so a run only waits when two agents cite different values for the same figure and the same period, while a figure that only one agent mentions is shown for review without stopping anything, because there's nothing to decide between. Runs stored before the gate existed are never gated after the fact, since changing the rules on old records is how audit trails get rewritten, and in practice most runs never reach the gate at all.

### B03 — chapter 2b - the decision (≈26 s · B03_DecisionForm)
**VISUAL:** HOLD: screen-recording frames of run ec1a3b44's gate panel expanding in place under the verdict with the matrix still visible (DecisionGate.tsx). Close-ups of the five radio cards and the rationale counter ticking to 20. DECIDER box lit.
**ASSETS:** assets/B03_gate_open_1280.png

**NARRATION:**
The decision form opens in the same place you're already reading, so it never covers the evidence. The reviewer picks one of five outcomes, which are that agent A is right, that agent B is right, that both are wrong, that there's no real conflict, or that the correct value is something they enter themselves, and then they have to give their reasoning in at least twenty characters, which is deliberately too long for something like looks good, before typing their name.

### B04 — chapter 2c - identity and refusals (≈22 s · B04_SmallPrint)
**VISUAL:** Zoom on the name-field hint 'Recorded as entered; not verified.' Then a real 422 refusal body from POST /api/runs/{id}/decisions (capture from the route test or a temp DB, never the live run).

**NARRATION:**
The small print under the name field says that it's recorded as entered and not verified, because the login only carries a permission level and not an actual person, and the screen says that every time. If a decision breaks one of the rules, it's refused and the reason is explained in words, so a decision about a figure that nobody disputed is turned away rather than quietly fixed.

### B05 — chapter 2d - the record (≈7 s · B05_Supersede)
**VISUAL:** Decision stack: card 1, card 2 lands, card 1 dims and is tagged 'superseded, still on record'; chip 'UPDATE / DELETE -> BLOCKED BY A DATABASE TRIGGER'.

**NARRATION:**
A later decision can supersede an earlier one, but both stay on the record, because the database itself blocks edits and deletions.

### B06 — chapter 3a - what an investor sees (≈32 s · B06_InvestorView)
**VISUAL:** Side-by-side auditor vs investor captures of ec1a3b44, then the leak found (one '1998' in a trace search result, capture) and the fix verified: investor read after the fix has 0 x '1998' and 0 x '1996' (RUN_LOG 2026-09-26 correction + verification).
**ASSETS:** assets/B06_auditor_1280.png; assets/B06_investor_1280.png; assets/B06_investor_trace_leak_1280.png; assets/evidence/out/B06_investor_view.json

**NARRATION:**
While a run is waiting, an investor sees the figures the agents agreed on along with a notice, and the server withholds the disputed values and both agents' answers. When I searched the investor's view of this run, nineteen ninety-six never appeared, but nineteen ninety-eight appeared once, inside a search result shown in the run's trace, so the trace now withholds what each search returned while the gate is open, and after that fix the same search finds neither year. The withholding still depends on read access, because a request without a token is served at the level the run was stored with.

### B07 — chapter 3b - the gate I didn't clear (≈9 s · B07_StillOpen)
**VISUAL:** HOLD: capture of run ec1a3b44's gate, awaiting decision; 'decisions recorded: 0' from the evidence.

**NARRATION:**
Nobody has recorded a decision on that run yet, so it is still open, which is exactly how the gate is meant to behave until a person looks at it.

### B08 — chapter 4a - rules that stop a run (≈26 s · B08_HardRules)
**VISUAL:** MATH-TYPESETTING (MathTex): EPS_basic >= EPS_diluted; FCF = OCF - CapEx; Assets = Liabilities + Equity (2% tolerance note). Each gets a 'HARD: gates' tag (validation/constraints.py, gate policy v2).

**NARRATION:**
Two agents can agree with each other and still both be wrong, so each agent's figures are also checked against accounting identities, such as basic earnings per share never being lower than diluted, free cash flow equalling operating cash flow minus capital spending, and assets equalling liabilities plus equity. When an agent's figures break one of those, the run waits for a person just as it does for a mismatch, and the reviewer can confirm the error instead of picking an agent.

### B09 — chapter 4b - claim versus source (≈23 s · B09_ClaimVsSource)
**VISUAL:** Side-by-side, held >=3 s: 'given: revenue $82.9B' | 'wrote: $828.9B', handnote '10x'. Label 'first attempt, halted on format' so it is never read as a live catch. Then the rounding rule: '$109 billion for $109.417B: passes'.

**NARRATION:**
Every figure an agent cites is also checked against the filing it was given, and rounding to the number of digits the agent wrote is allowed. In one Microsoft run, an agent was given revenue of eighty-two point nine billion and wrote eight hundred twenty-eight point nine billion. That attempt failed its format check first, so this check never actually ran on it, but it would have caught the mistake if it had.

### B10 — chapter 4c - rules that only inform (≈25 s · B10_SoftRules)
**VISUAL:** GOOGL real values: net income $112.2B vs operating income $40.77B, shown for both agent B and the filing itself, with an ochre callout 'Unusual, worth a look' (never red). Then the Mycroft 8 'Unrecognised figure $9.11' row resolving to 'filed diluted EPS'.

**NARRATION:**
Other rules only describe what is usually true. On one Google run, net income came out at nearly three times operating income, and the filing showed the same thing, because it reflected a real one-off gain. That's why rules like this never stop a run and only mark the result as unusual and worth a look. The same finding also explained two figures that part one had left unrecognised, which turned out to be Google's filed earnings per share.

### B11 — chapter 4d - the filing, and an honest gap (≈20 s · B11_FilingAndTimeout)
**VISUAL:** Filing check passes (assets = liabilities + equity, $383.3B); then 'model: no reply to a 5-token request within 60 s' and an 'OPEN ISSUE · HIGH' card: no timeout on model calls.

**NARRATION:**
The filing itself goes through the same checks, using the single fetch that has already been made, and Apple's balance sheet adds up. In the middle of this testing, though, the local model stopped responding, to the point where a five-token test request got no reply within sixty seconds, and because model calls have no timeout, a stuck model can hold up a comparison indefinitely.

### B12 — chapter 5a - show me where it says that (≈25 s · B12_SourceExcerpt)
**VISUAL:** Recorded output of find_in_document on the real Apple 10-Q (row, column, value as filed), the live tally 24/24, and the review's Source button that opens the excerpt in place (U6, RUN_LOG 2026-09-26).
**ASSETS:** assets/evidence/out/B12_filing_excerpt.json

**NARRATION:**
Every figure the agents were given can now be found in the original filing, because the system opens the actual SEC document, finds the exact tagged value, and returns the row, the column, and the number as it was filed. In the last batch it found all twenty-four figures and every filed value matched, and in the review each figure now has a source button that opens that excerpt in place, while web figures show the snippet the agent actually read.

### B13 — chapter 5b - watching it run (≈15 s · B13_LiveLanes)
**VISUAL:** Diagram of a real captured event stream (AAPL): one shared SEC fetch drawn once above two tinted agent lanes; event counts from the stream (assets/evidence/out/B13_stream_events.json).
**ASSETS:** assets/B13_lanes.mp4 (real capture); assets/evidence/out/B13_stream_events.json

**NARRATION:**
You can also watch a comparison as it happens. Each agent has its own lane showing what it's doing at that moment, and the single shared SEC fetch is drawn only once, because it only happened once. Every indicator on that screen comes from a real server event.

### B14 — chapter 6a - from figures to a grade (≈23 s · B14_Assessment)
**VISUAL:** [verify] REAL: capture of run 8ecb0922's review summary with both agents' extracted grade, direction and assumptions, labelled model judgment (B4 option 1 extraction + U8; RUN_LOG 2026-09-26).

**NARRATION:**
Analysts don't stop at the figures, because they also make a call, so after each answer passes its checks, a second call to the same model reads that answer and extracts a grade, a direction, the stated assumptions, and up to three key points, all labelled as model judgment. Anything it quotes that isn't in the agent's own answer or inputs is dropped, and when the extraction fails, the run carries on and says so.

### B15 — chapter 6b - why grades differ, and when to agree (≈28 s · B15_DivergenceAndConsensus)
**VISUAL:** [verify] REAL: capture of the same run's driver sentence and the grade gate item (accept A / accept B / set the grade); three driver kinds and the consensus rule typeset beside it.

**NARRATION:**
When two grades differ, the system works out whether the agents used different figures or periods, used the same figures with different assumptions, or differed on neither, in which case it comes down to how they weighed the same evidence. A consensus is only recorded when both the grade and the direction agree and no hard rule has failed, and anything else goes to the gate, where the reviewer can accept one agent's grade or set the grade themselves, while investors see no grade until a person has recorded one.

### B16 — chapter 6c - answer first (≈17 s · B16_AnswerFirst)
**VISUAL:** [verify] REAL: the Markdown export of run 8ecb0922 (GET /api/runs/8ecb0922/export.md), first lines shown as recorded output, over the answer-first order of the review.
**ASSETS:** assets/B16_review_scroll.mp4 (real capture)

**NARRATION:**
The review now reads in the order a person needs it, starting with the answer and whether anything failed a check, followed by the decision, then the evidence figure by figure, then the agents, and finally the underlying machinery, which is folded away. Every review can also be exported as a plain document.

### B17 — chapter 7a - the honest ledger, true now (≈20 s · B17_TrueNow)
**VISUAL:** Honest-ledger list one: what the work now does.

**NARRATION:**
Several things work now that didn't before. A mismatch, a failed hard check, or a grade disagreement stops the run until a person decides, decisions need a reason and can't be edited, and investors don't receive the disputed values, either agent's answer, or anything the searches returned. Accounting rules check each agent and the filing, and every review can be exported as a plain document.

### B18 — chapter 7b - the honest ledger, still not true (≈19 s · B18_StillNotTrue)
**VISUAL:** OUTRO-LAW chapter close: the work's limitations, held uncleared.

**NARRATION:**
Some things still don't work. The decider's name is typed in and never verified, and anyone can create a reviewer token, which is a known security gap. The storage still holds everything and the withholding only happens when the data is read, the grade extraction is the same model judging its own answer, and model calls still have no timeout.

### B19 — close - the smallest true claim (≈25 s · B19_EndCardReprise)
**VISUAL:** OUTRO-LAW close: reprise '1998 | 2 years | 1996 · AWAITING DECISION', the four gate boxes as the takeaway, then 6 END CARD bullets about the work.

**NARRATION:**
The judgment stays with a person, and this is the first time the system can't move forward without one. The smallest true claim I can make is that the machine fetches, reads, compares, checks and grades, and then it stops and waits. If you run agents yourself, take one warning your system raises, give it a trigger, a stop, a person, and a record, and then check that it can't clear itself. For now, this one run is still open.

### B20 — outro (≈4 s · ClaudeTitleOutro)
**VISUAL:** OUTRO LAW: exact title restate, handle, one subline. No stats; B19 carries them.

**NARRATION:**
One run, still open, written down, versioned, and executable. Signing off, Divij Pawar.

---

## Fact-check sheet

| Claim | Source | Status |
|---|---|---|
| Run `ec1a3b44`: A 1998, B 1996, AWAITING_DECISION, 0 decisions; the investor read withholds both values and conclusions **but still contains "1998" once, in a search result in the trace** (live read and fixture, 2026-09-26); the AI didn't decide | RUN_LOG 2026-09-25 BG+U3; fixtures `run_compare_gated_{auditor,investor}.json` | Logged. **Check it is still open on recording day** |
| Only MISMATCH gates; UNCORROBORATED doesn't; pre-gate runs `NOT_GATED` | RUN_LOG BG+U3; `validation/gate.py` | Logged |
| 5 decisions; rationale ≥20; name ≥2; refused, never repaired; superseded; append-only triggers | RUN_LOG BG+U3; `web/db.py` | Logged |
| Identity self-declared; anyone can mint a token | RUN_LOG BG+U3 open issues (`audit-criticals`) | Logged |
| "Four critical security findings" | Mycroft 4 and 7 narration; ledger. **Re-count in `web/self_report.py` before recording** | Check |
| Failed hard checks gate (policy v2); `confirmed_error` decision | RUN_LOG B2+B3 | Logged |
| MSFT $828.9B vs $82.9B was a first attempt that halted on format; check never ran live | RUN_LOG B2+B3 | Logged |
| GOOGL NI $112.2B vs OI $40.77B, also in the filing; the $9.11 is the filed EPS | RUN_LOG B2+B3 | Logged |
| AAPL assets = liabilities + equity, $383.3B, passes | RUN_LOG B2+B3 | Logged |
| Ollama stopped responding; no timeout on model calls | RUN_LOG B2+B3 | Logged |
| Filing excerpt from Apple 10-Q `0000320193-26-000020` | `tests/test_filings.py`, `datasources/filings.py`, `/api/facts/excerpt` | **[verify]** |
| Live lanes, one shared fetch | `web/frontend/src/views/CompareView.tsx`, `state/liveRun.ts` | **[verify]** |
| Assessment block, bull/bear, divergence classes, consensus rule, Set grade, raw-output view | Roadmap B4, B5, U7, U8 | **[verify]** |
| Answer-first review, phone compare mode, Markdown export | Roadmap U5, U7, U9, B6 | **[verify]** |
| Bull BBB / Bear BB, 8% / 3% | Roadmap mock-up | Illustrative. Label it on screen |
| Pokémon Red/Blue reached North America in 1998 | General knowledge (not stated in narration) | The narration deliberately doesn't say who is right |

### Accuracy guardrails
- **Don't say the system knows 1998 is right.** The narration never names a winner, on purpose.
- **"Would have caught it", not "caught it"** (MSFT).
- **Withholding is at read time.** Nothing is deleted or encrypted.
- **Don't show a gated accounting check as live footage.** None has happened yet.
- **Don't say the investor read contains neither year.** It withholds both values and both
  conclusions, but one search result in the trace still shows "1998" (B06). The script says so.
- **Don't draw a click-through excerpt popover as if it were the app.** BP has no UI yet (U6).
