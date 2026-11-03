# SCRIPT: *The Sum Behind the Number* (Week 28 work video, Mycroft PR #74)

**Draft 1, 2026-10-25.** Angle A, approved by Tanmay 2026-10-25 (see `ANGLE.md`), with the standing instruction to show
nothing negatively and to reframe positively. Structure: A RUNNING TOTAL. One invented portfolio, a block of loss that
grows one named shock at a time, until the workflow's number has been rebuilt from its parts; then my second adder run
beside the original, and the checks that keep the sum honest. About 640 words, roughly 3:15 of speech.

**Framing (positive, per the standing instruction):** the stacking is described as the workflow's **documented design**,
with credit to its README, which prints the same sum as its worked example. The checks are described as what they
protect. The open steps are described as a good list for next time. The finance is not judged. Every portfolio is
invented; the tickers are the workflow's own, said once in B02 and labelled on screen wherever a number appears;
not investment advice, said once. Committed files only (`FACTCHECK.md`). No fellows named; no author named for the workflow.

**TTS spelling:** numbers in words in the narration; digits on screen only. "Mycroft" keeps its real spelling
everywhere; the audio step feeds Kokoro the override `mˈaɪkɹɔft` (MY-croft). Tickers are not spoken (Kokoro mangles
them): the narration says "a chip designer", "a chip maker". "Python" and "JavaScript" are fine as written.

---

### B01 · COLD OPEN, the number
> Tech sector crash: minus seventy-eight percent. That is what one scenario did to a portfolio of three invented chip stocks, ten thousand dollars taken down to twenty-two hundred. Where does seventy-eight come from? Let me take it apart.

*On screen:* from the first frame, one large line "Tech Sector Crash  −78.0%", beneath it "$10,000 → $2,200", the three holdings as small chips (NVDA 40% · AMD 30% · TSM 30%), and an empty stack outline beside the number labelled "made of: ?" (the film's device on screen from the first frame). Evidence panel: `stress-results.json`, c01 (`drawdown_pct`, `initial_portfolio_value`, `final_portfolio_value`). Label: "Invented portfolio". *Refs:* W1.

### B02 · WHAT THIS IS
> Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This week I contributed to Mycroft, a book and a working repository of finance pipelines, and it calls them recipes. One of them, the Scenario Stress Testing Agent, shocks a portfolio with a named scenario and reports what is left. The portfolios here are mine, invented. The tickers come from the workflow's own list. The numbers are scenario arithmetic, not predictions, and not investment advice.

*On screen:* "Mycroft: both a book and a working agentic repository" (README line quoted); the recipe name; a strip of the workflow's local steps (validate, pick the scenario, apply the shocks); "PR #74 · merged"; "Invented portfolios · tickers from the workflow's own map · not investment advice". *Refs:* W2, W3, W4.

### B03 · A SCENARIO IS A LIST
> A scenario is a short list of named shocks. Tech Sector Crash names five. Four are price shocks: market, minus fifteen percent; technology sector, minus thirty; semiconductors, minus thirty-five; and AI stocks, minus forty. The fifth is a volatility number. The engine's rule is simple: for each holding, add up the shocks that belong to it. Hold a guess: if the market alone falls fifteen percent, how far does the biggest holding fall?

*On screen:* the scenario as a card with its five named shocks, each in its own row (market −15%, tech_sector −30%, semiconductor −35%, ai_stocks −40%, volatility_spike 2.5); a caption "the workflow's own template"; then the question "market −15% → the biggest holding falls how far?" held for about 3 s beside an empty bar. Evidence panel: the workflow's `Load_Template_Scenario` node (tech_crash). *Refs:* W5, W6.

### B04 · ONE HOLDING, ONE BLOCK AT A TIME
> Take the biggest holding, a chip designer. Everything belongs to the market, so a block of minus fifteen. It is a semiconductor stock, so minus thirty-five. And it is on the AI list, so minus forty. The engine adds them: minus ninety. The workflow's own README prints this exact sum as its worked example, which is a big part of why it is so easy to check. It even names a different way to combine them, so the rule is a choice you can see.

*On screen:* a single bar for the first holding that grows by one block per sentence (−15, then −35, then −40), each block labelled with the shock that belongs to it and the list it came from; the running total beside the bar ("−15 → −50 → −90"); a small badge "README worked example" with the README's own three lines shown as a quote, and one line "another way to combine them is named in the README". Evidence panels: `stress-results.json` c01, NVDA (`shock_pct` −90, `loss` −3,600); the workflow's README (a vendored file). Label: "Invented portfolio". *Refs:* W7, W8.

### B05 · THE SAME CRASH, DIFFERENT HOLDINGS
> The third holding is a chip maker that is not on the AI list. A block of minus fifteen for the market, minus thirty-five for semiconductors. That is minus fifty, not ninety. The second chip stock takes minus ninety, like the first. Now give each its share: forty percent, thirty, thirty. Thirty-six, plus twenty-seven, plus fifteen makes seventy-eight, and there is the number.

*On screen:* three bars side by side (−90, −90, −50), each shown as its blocks; the weights drawn under them; the arithmetic typeset: 0.40 × 90 = 36, 0.30 × 90 = 27, 0.30 × 50 = 15, total 78; then the headline number from B01 returns, now with the three bars beneath it. Evidence panel: `stress-results.json` c01 (`all_positions`: −90, −90, −50). Label: "Invented portfolio". *Refs:* W9, W10.

### B06 · A MILDER SCENARIO, THE SAME RULE
> A smaller scenario shows the same rule. An aggressive rate hike: market, minus ten percent; growth stocks, minus twenty; technology sector, minus fifteen. Four growth names, equal shares. Three of them take minus thirty. One is also filed under the technology sector, so a third block lands on it, and it takes minus forty-five. The book loses thirty-three point seven five percent, which the workflow labels critical, its word for losses above thirty.

*On screen:* four bars, three at −30 (two blocks each) and one at −45 (three blocks, the third highlighted), equal weights under them; "33.75%" typeset; the label "critical" shown with the thresholds once (above 30%: critical). Evidence panel: `stress-results.json` c12 (`all_positions`, `drawdown_pct` −33.75, `risk_level`). Label: "Invented portfolio". *Refs:* W11, W12.

### B07 · THE TURN, MY ADDER
> Here is the part I wanted to be sure of. To check the original, I wrote a second adder, a Python copy of the engine and its first steps, and ran both on the same portfolios. The original code comes straight out of the workflow file. On twenty-four requests, every number, every label and every message matched. Then I added twelve deliberate breaks to my checks, and each one was caught.

*On screen:* two columns of results, "original" and "mine", for one portfolio, matching row by row; a counter climbing to "24 of 24 identical"; then the self-test list with twelve "BREAK … caught" rows ticking one at a time ("27 of 27 as expected"). Evidence panels: `logs/scenariostresstestingagent/parity-results.json` (24 matching, 0 mismatching); `self-test-results.md`. *Refs:* W13, W14, W15.

### B08 · WHAT THE CHECKS PROTECT
> Before any adding, a validator reads each portfolio, with the workflow's own rules and one addition of mine, and it protects the sum. Portfolios whose shares total six tenths, or one point two, are accepted, because the workflow rescales them to one. A holding with no ticker, a share that is not a number, an empty list: each is stopped, with its reason written down. Ten out of ten of my deliberately flawed portfolios. A sum of nothing never reaches the screen.

*On screen:* a gate drawn once; clean portfolios passing (the c06 and c08 weight totals shown, 0.6 and 1.2, then both rescaled to 1.0); then three defective portfolios stopping one at a time with their reasons, from the audit; the count "10 of 10 stopped, each for its own reason". Evidence panels: `validate-audit.md` (clean 12 of 12 accepted); the defective audit (10 of 10 rejected). Label: "Invented". *Refs:* W16, W17.

### B09 · A GOOD LIST FOR NEXT TIME
> Nothing here calls the outside world. The call to a model, the market-data request and the reply to a caller are written down as hand-offs, not approved. Five items in the recipe are still open, and it says draft, on purpose. That leaves a good list for next time.

*On screen:* the hand-offs with `approved_for_live_action: false`; the recipe's frontmatter (`status: DRAFT`, `todos_open: 5`); the open items as a short checklist (steps 2, 4 and 6, and two mappings) rather than a warning. Evidence panels: the step-5 run log (`live_handoffs`); the recipe's frontmatter. *Refs:* W18, W19.

### B10 · CLOSE
> So next time a stress test gives you one number, ask what was added: which shocks, from which lists, and has anyone run the adder beside the original? A good answer names the terms.

*On screen:* the three questions arrive one per phrase over the first number from B01; the number's parts (the three bars) sit faintly behind them; "A good answer names the terms." held for the last two seconds.

### B11 · OUTRO
> This was Tanmay Kulkarni, for Humanitarians AI. The contribution is pull request seventy-four on the Mycroft repository.

*On screen:* "Humanitarians AI · @HumanitariansAI"; "github.com/nikbearbrown/mycroft · PR #74"; the recipe path.
