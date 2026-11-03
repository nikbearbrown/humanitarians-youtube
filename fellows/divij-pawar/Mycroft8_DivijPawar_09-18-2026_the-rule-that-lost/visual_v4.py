# Visual descriptions (shot.concept / shot.show) for beats whose scenes changed in v4:
# the video is about the work, so series callbacks, commit panels, test counts, ledger and
# RUN_LOG labels were removed from the scenes (human direction, 2026-09-26). build_sheets.py
# applies these over the original descriptions so beat_sheet.json matches scenes.py.

VISUAL_M8 = {
    "B01": ("Framework before example (PROOF 1-2). One line says what the system does (two agents, one "
            "company, compare the numbers), then the four boxes METRIC / PERIOD / UNIT / SOURCE, reused as a "
            "corner chip in B02-B07.",
            [(0.0, "title: 'ONE TEST FOR EVERY FIGURE'"), (0.2, "line: 'two AI agents, one company, compare the numbers they report'"),
             (0.5, "four boxes build left to right"), (0.85, "caption: 'two figures compare only when all four line up'")]),
    "B04": ("SHOW. The 'status: ok' line with a returned {'error': ...} is a LABELLED RECONSTRUCTION (the old "
            "recorder stored no arguments); 'ok' struck in ink. Then REAL recorded arguments from stored MSFT run "
            "1b691654: start_date after end_date, include_domains ['NASDAQ:MSFT'], include_images as a string; the "
            "query-only retry returned 5 URLs (assets/evidence/out/B04_search_args_and_retry.json). SOURCE box lit.",
            [(0.0, "title: 'A FAILED SEARCH, RECORDED AS OK'"), (0.15, "reconstruction tag + trace line 'status: ok'"),
             (0.3, "returned error expands; 'ok' struck, 'error' written beside it"),
             (0.55, "the model's real search settings, contradictory dates ringed"), (0.85, "caption: 'one retry with the query alone: 5 real results'")]),
    "B05": ("SHOW from real data: bars from the recorded AAPL stream's started_at spans (1 ms start gap, 39.4 s "
            "overlap), labels in a left column (assets/evidence/out/B05_overlap_from_stream.json).",
            [(0.0, "title: 'BOTH AGENTS, AT THE SAME TIME'"), (0.3, "three bars: SEC fetch (shared), AGENT A, AGENT B"),
             (0.6, "overlap shaded: 'in flight together: 39.4 s (start gap 1 ms)'"), (0.85, "source: 'speed-up not measured'")]),
    "B07": ("Structured fraction (no LaTeX on this machine; real text over a drawn bar, italic variables): asset "
            "turnover = revenue / assets = 265.6 / 383.3 = 0.693, recomputed and asserted in-scene. Beside it, "
            "held >=3 s: 'agent wrote 0.13 / 0.12' ringed, '5.3x'. Then net margin and GOOGL ROA cleared.",
            [(0.0, "title: 'A REAL RATIO AND A MADE-UP ONE LOOK THE SAME'"), (0.2, "fraction builds to 0.693"),
             (0.45, "stated 0.13 and 0.12 ringed, '5.3x'"), (0.8, "two checks: net margin OK, GOOGL ROA OK")]),
    "B08": ("SHOW the mis-tag: 'Return on Assets of 18.85%' with only 'Assets' highlighted; the figure drops into "
            "the ASSETS drawer, then EXCLUDED. Then 'EARLIER RESULT: 15 / 16' with the footnote 'the count stands, "
            "part of it came from this mis-tag'.",
            [(0.0, "title: 'HOW THE OLD TAGGER READ IT'"), (0.25, "'18.85%' drops into 'ASSETS' -> 'EXCLUDED'"),
             (0.6, "card: 'EARLIER RESULT: 15 / 16'"), (0.8, "footnote: 'the count stands, part of it came from this mis-tag'")]),
    "B09": ("Falsifiability beat. Bars from zero: old rule 1/16, new rule 6/16. Callouts: '1 real: a fabricated "
            "debt-to-equity ratio of 0.34, caught by both' and '5 can't be judged: ratios with no components'.",
            [(0.0, "title: 'THE BAR: DO NO WORSE THAN THE OLD RULE'"), (0.25, "bars grow: 1/16 and 6/16"),
             (0.5, "callout: the one real catch"), (0.65, "callout: 5 can't be judged"), (0.85, "caption: 'the old runs never recorded what each agent was given'")]),
    "B12": ("HOLD: real /app captures of run 20c538e4, desktop 1280 px and phone 375 px, app palette kept.",
            [(0.0, "title: 'THE COMPARISON, AS A TABLE'"), (0.2, "desktop matrix capture"), (0.7, "phone capture slides in beside it")]),
    "B13": ("HOLD: run 20c538e4's two MATCH rows (capture), then side-by-side, held >=2 s: agent quote 'not "
            "explicitly stated in the Context' vs the context's last line carrying that EPS.",
            [(0.0, "title: 'BOTH AGENTS NOW GET THE SAME FIGURES'"), (0.25, "capture of the MATCH rows + 'EPS: $2.02 = $2.02 · Net income ...'"),
             (0.7, "side-by-side: agent says missing | last context line has it")]),
    "B14": ("Honest-ledger list one: what the work now does.",
            [(0.0, "title: 'WHAT WORKS NOW'"), (0.2, "line: 'every figure carries its period, unit and filing'"),
             (0.4, "line: 'failed searches are recorded as failures'"), (0.6, "line: 'two agents in flight at once'"),
             (0.8, "line: 'ratios recomputed: two hidden errors surfaced'")]),
    "B15": ("OUTRO-LAW chapter close: list two, the work's limitations, held on screen uncleared.",
            [(0.0, "title: 'WHAT STILL DOESN'T'"), (0.2, "line: 'the stricter comparator is opt-in for company runs'"),
             (0.4, "line: 'tagging still depends on wording'"), (0.6, "line: 'the ratio check ignores annual vs quarterly'"),
             (0.8, "line: 'agents skip figures that are in their input'")]),
    "B16": ("OUTRO-LAW close: reprise 15/16 -> 6/16, the four boxes as the takeaway, then 6 END CARD bullets about "
            "the work. B17 carries no stats.",
            [(0.0, "serif line: 'the smallest true claim'"), (0.1, "reprise: '15 / 16 -> 6 / 16'"), (0.25, "four boxes return"),
             (0.4, "bullets: handed FY2018/9-month data; 6 of 16, 1 real, 5 unknown; two 5x ratio errors; the mis-tag; "
                   "first shared-figure match; stricter rule opt-in until runs show what agents were given")]),
}

VISUAL_M9 = {
    "B01": ("Framework before example. Recap chip for part 1, one serif line ('a flagged contradiction is only "
            "useful if something happens next'), then TRIGGER / STOP / DECIDER / RECORD, reused as a chip in B02-B07.",
            [(0.0, "chip: 'PART 1: METRIC · PERIOD · UNIT · SOURCE'"), (0.2, "serif line"),
             (0.55, "four boxes build"), (0.85, "caption: 'without all four, it's only a warning'")]),
    "B05": ("Decision stack: card 1, card 2 lands, card 1 dims and is tagged 'superseded, still on record'; "
            "chip 'UPDATE / DELETE -> BLOCKED BY A DATABASE TRIGGER'.",
            [(0.0, "decision 1"), (0.3, "decision 2 lands; decision 1 dims, tagged superseded"), (0.7, "chip: blocked by a database trigger")]),
    "B07": ("HOLD: capture of run ec1a3b44's gate, awaiting decision; 'decisions recorded: 0' from the evidence.",
            [(0.0, "gate capture"), (0.4, "chip 'AWAITING DECISION' + 'decisions recorded: 0'"), (0.75, "caption: 'the gate is for a person'")]),
    "B11": ("Filing check passes (assets = liabilities + equity, $383.3B); then 'model: no reply to a 5-token request "
            "within 60 s' and an 'OPEN ISSUE · HIGH' card: no timeout on model calls.",
            [(0.0, "title: 'THE FILING GETS THE SAME CHECKS'"), (0.2, "check passes, with its arithmetic"),
             (0.5, "status line: no reply in 60 s"), (0.75, "card: 'OPEN ISSUE · HIGH: no timeout on model calls'")]),
    "B13": ("Diagram of a real captured event stream (AAPL): one shared SEC fetch drawn once above two tinted "
            "agent lanes; event counts from the stream (assets/evidence/out/B13_stream_events.json).",
            [(0.0, "shared bar: 'ONE SEC FETCH, BOTH AGENTS' with its four steps"), (0.4, "lanes A (blue) and B (orange)"),
             (0.8, "caption: steps started / finished / agents done")]),
    "B15": ("[verify] Three bins DATA / ASSUMPTION / WEIGHTING; consensus rule as 'grades match AND no hard rule "
            "failed -> consensus'. On-screen 'ILLUSTRATIVE · NOT BUILT YET' chip until the feature exists.",
            [(0.0, "three bins build"), (0.55, "rule: grades match AND no hard rule failed -> consensus"),
             (0.8, "caption: 'anything else goes to the gate, which can now set the grade'")]),
    "B17": ("Honest-ledger list one: what the work now does.",
            [(0.0, "title: 'WHAT WORKS NOW'"), (0.25, "line: 'a mismatch stops the run until a person decides'"),
             (0.45, "line: 'decisions need a reason and can't be edited'"), (0.65, "line: 'investors don't receive the disputed values or answers'"),
             (0.85, "line: 'hard accounting rules gate; soft rules inform'")]),
    "B18": ("OUTRO-LAW chapter close: the work's limitations, held uncleared, including the trace leak.",
            [(0.0, "title: 'WHAT STILL DOESN'T'"), (0.15, "typed name, never verified"), (0.3, "anyone can mint a reviewer token"),
             (0.45, "a trace search result leaked 1998"), (0.6, "storage holds everything"), (0.75, "no live gated check yet"),
             (0.9, "no model-call timeout")]),
    "B19": ("OUTRO-LAW close: reprise '1998 | 2 years | 1996 · AWAITING DECISION', the four gate boxes as the "
            "takeaway, then 6 END CARD bullets about the work.",
            [(0.0, "serif line + hook card reprise"), (0.15, "four gate boxes return"),
             (0.35, "bullets: mismatch stops the run; 20+ character reason, superseded never edited; values withheld but one "
                    "trace snippet leaked 1998; hard rules gate, soft inform; identity self-declared, no timeout; no live gated check yet")]),
}

VISUAL_M9.update({
    "B06": ("Side-by-side auditor vs investor captures of ec1a3b44, then the leak found (one '1998' in a trace search result, "
            "capture) and the fix verified: investor read after the fix has 0 x '1998' and 0 x '1996' (RUN_LOG 2026-09-26 correction + verification).",
            [(0.0, "auditor | investor captures"), (0.45, "found: '1998' once, in a trace search result (capture)"),
             (0.7, "fixed and verified: 1998 -> 0, 1996 -> 0"), (0.88, "second limit: token-less reads at the stored level")]),
    "B12": ("Recorded output of find_in_document on the real Apple 10-Q (row, column, value as filed), the live tally 24/24, "
            "and the review's Source button that opens the excerpt in place (U6, RUN_LOG 2026-09-26).",
            [(0.0, "recorded output: row | column | value as filed"), (0.6, "tally: 24 / 24 found, every filed value equal"),
             (0.85, "chip: every figure has a Source button")]),
    "B14": ("REAL: capture of run 8ecb0922's review summary with both agents' extracted grade, direction and assumptions, "
            "labelled model judgment (B4 option 1 extraction + U8; RUN_LOG 2026-09-26).",
            [(0.0, "capture: grades and assumptions per agent"), (0.6, "chips: 'second call reads the answer' · 'ungrounded quotes dropped'")]),
    "B15": ("REAL: capture of the same run's driver sentence and the grade gate item (accept A / accept B / set the grade); "
            "three driver kinds and the consensus rule typeset beside it.",
            [(0.0, "three driver kinds"), (0.4, "rule: grade AND direction agree AND no hard failure -> consensus"),
             (0.7, "capture: grade gate item"), (0.9, "investors see no grade until a person sets one")]),
    "B16": ("REAL: the Markdown export of run 8ecb0922 (GET /api/runs/8ecb0922/export.md), first lines shown as recorded output, "
            "over the answer-first order of the review.",
            [(0.0, "review order, answer first"), (0.55, "export.md, first lines as recorded output")]),
    "B17": ("Honest-ledger list one: what the work now does.",
            [(0.0, "title: 'WHAT WORKS NOW'"), (0.25, "mismatch / hard check / grade -> stops for a person"),
             (0.45, "reason required; no edits"), (0.65, "investors get no disputed value, answer or search result"),
             (0.85, "every review exports as a plain document")]),
    "B18": ("OUTRO-LAW chapter close: the work's limitations, held uncleared.",
            [(0.0, "title: 'WHAT STILL DOESN'T'"), (0.2, "typed name, never verified"), (0.4, "anyone can mint a reviewer token"),
             (0.6, "storage holds everything; withheld when read"), (0.8, "extraction: same model judging itself"), (0.9, "no model-call timeout")]),
})

M9_COLD_OPEN_OUTPUT = [
    "Agent A: 1998. Agent B: 1996. Difference: 2 years",
    "The run stops and waits for a named person",
    "Until someone decides, it stays open",
]
