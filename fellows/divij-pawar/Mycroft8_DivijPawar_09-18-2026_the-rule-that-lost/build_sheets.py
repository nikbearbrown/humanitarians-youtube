"""Generate beat_sheet.json for Mycroft 8 and Mycroft 9, and sync each script's Beats section.

The beat sheet is the source of truth; the script's "## Beats" section is regenerated from it
so the two never drift. Production brief and fact-check sheet in the .md are left untouched.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\Code\humanitarians-youtube\fellows\divij-pawar")
WPS = 3.2  # measured: Mycroft1-7 Kokoro am_onyx averaged 3.1-3.6 words/s of actual audio

FIXED = {"folderLabel": "@DivijPawar", "modelLabel": "Fable 5", "effortLabel": "High"}


def beat(bid, act, narration, shot):
    words = len(narration.split())
    return {
        "beat_id": bid,
        "act": act,
        "narration_text": narration,
        "voice": "am_onyx",
        "engine": "kokoro",
        "estimated_duration_s": round(words / WPS),
        "audio_file": f"mp3/beat-{bid}.mp3",
        "actual_duration_s": None,
        "shot": shot,
    }


def manim(scene, concept, show, assets=None, verify=False):
    s = {"type": "GRAPHIC", "source": "manim", "manim": {"scene_class": scene}}
    if verify:
        concept = "[verify] " + concept
    s["concept"] = concept
    if assets:
        s["assets"] = assets
    s["show"] = [{"at": at, "event": ev} for at, ev in show]
    return s


def composer(props, concept, show):
    return {
        "type": "REMOTION",
        "source": "own",
        "remotion": {"pattern": "ClaudeComposerAsk", "props": {**props, **FIXED}},
        "concept": concept,
        "show": [{"at": at, "event": ev} for at, ev in show],
    }


def outro(title, subline, concept):
    return {
        "type": "REMOTION",
        "source": "own",
        "remotion": {"pattern": "ClaudeTitleOutro",
                     "props": {"title": title, "handle": "@DivijPawar", "subline": subline}},
        "concept": concept,
        "show": [{"at": 0.0, "event": f"title card: '{title}'"},
                 {"at": 0.3, "event": "handle: '@DivijPawar'"},
                 {"at": 0.5, "event": f"subline resolves: '{subline}'"}],
    }


COLD_SHOW = [
    (0.0, "Claude composer UI fades in with the greeting"),
    (0.15, "command types in"),
    (0.4, "running line appears"),
    (0.6, "three output lines resolve; the third is the hook the video pays off"),
    (0.85, "hold on the three resolved lines"),
]

APPROVALS = {
    "voice": {
        "status": "approved",
        "reviewer_type": "human",
        "reviewed_by": "Divij Pawar",
        "reviewer": "Divij Pawar",
        "reviewed_at": "2026-09-27T00:52:49+00:00",
        "fingerprint": "9fbee75cc6f2e9898f416028987763bde5975fea9179425289a870171991c85e",
        "subject_sha256": "9fbee75cc6f2e9898f416028987763bde5975fea9179425289a870171991c85e",
        "via": "direct chat answer 2026-09-26: 'Approve am_onyx'"
    },
    "notes": "Voice am_onyx approved by Divij Pawar in chat (2026-09-27T00:52:49+00:00). GATE P signed PASS in PEDAGOGY.md."
}

# ─────────────────────────────────────────────────────────────────────────────
# Mycroft 8 — The Rule That Lost
# ─────────────────────────────────────────────────────────────────────────────
M8 = [
    beat("B00", "cold open",
         "Hi, I am Divij Pawar, and this video is about a stricter way to compare two AI agents, and "
         "the test it failed. The voice you are hearing is AI generated. The work is mine. Last video "
         "ended on fifteen of sixteen. Fifteen false alarms, gone. This week I built a stricter "
         "comparator and replayed the same sixteen runs. It raised six alarms. It lost. It also found "
         "two real errors that the winning rule had been hiding. So this video starts with a correction.",
         composer({
             "command": "Why did the stricter comparator lose, and what did it find?",
             "topic": "CROSS-AGENT VALIDATION",
             "segment": "The Rule That Lost",
             "greeting": "Bonjour, Divij",
             "runningText": "replaying sixteen labelled runs\u2026",
             "output": [
                 "Old rule: 1 alarm in 16 labelled runs. New rule: 6",
                 "Two runs the old rule cleared hide a 5x ratio error",
                 "Part of fifteen of sixteen came from a tagging mistake",
             ]},
             "COLD OPEN LAW (CLAUDE.md SS9): B00 is the ClaudeComposerAsk bookend, never a custom Manim "
             "scene. Opens with the required FELLOWS-SUBMISSION intro line and the AI-narration "
             "disclosure (SS8). Greeting rotated to 'Bonjour' (Hola/Ola/Ciao/Namaste already used). "
             "The 15/16 vs 6/16 card itself is deferred to the B16 end-card reprise, per Mycroft6/7 "
             "precedent. Output lines are <=60 chars for 16:9; trim to <=45 for the 9:16 derivation.",
             COLD_SHOW)),
    beat("B01", "chapter 1 - recap and the four-box test",
         "Quick recap, for anyone new. This project runs two AI agents on the same company and "
         "compares their numbers. For most of its life, its alarms were false. Mycroft six counted "
         "them. Mycroft seven cut them. Since then, the agents can search the web. And a plan got "
         "approved to turn this agreement detector into an audit layer. It has three tiers. Reconcile "
         "the figures. Check the accounting. Then classify what is left. This video is tier one. Most "
         "of it applies a single test. Two figures can only be compared when four things line up. "
         "What it measures. Which period. What unit. And where it came from. Miss one, and a match "
         "means nothing.",
         manim("B01_FourBoxTest",
               "Framework-before-example beat (PROOF rubric 1-2). Recap strip of Mycroft6/7 thumbnails "
               "with one line each, then the three-tier roadmap as three stacked labels with tier 1 "
               "lit, then the four boxes that every later beat re-uses as a chip in its corner.",
               [(0.0, "recap strip: 'MYCROFT 6: 0 / 16 REAL' and 'MYCROFT 7: 15 / 16 CLEARED'"),
                (0.25, "three tiers stack: 'RECONCILE FIGURES' (lit) / 'CHECK ACCOUNTING' / 'CLASSIFY'"),
                (0.5, "four boxes build left to right: METRIC / PERIOD / UNIT / SOURCE"),
                (0.8, "caption: 'miss one, and a match means nothing'"),
                (0.9, "hold")])),
    beat("B02", "chapter 2a - period: what the agents were handed",
         "Start with period. I checked what the SEC data layer was actually handing the agents. It "
         "asked for the latest value of each figure. It got back a bare number. No period. No unit. "
         "For Apple, revenue was a figure from fiscal twenty eighteen. Apple stopped filing under that "
         "label years ago. Earnings per share was six eighty-eight. That is nine months added "
         "together. The quarter was two oh two. Net income was year to date as well. Nothing in the "
         "text said so. Every Apple comparison in the last three videos was built on these numbers. "
         "Assets was the one figure that was right. It is a single point in time.",
         manim("B02_WhatTheyWereHanded",
               "HOLD + SHOW. Real companyfacts JSON (tests/fixtures/edgar_aapl_companyfacts_sample.json "
               "in verification-layer) scrolls in mono, the Revenues fy:2018 entry highlights. Then a "
               "side-by-side table, held >=3 s (PROOF side-by-side gate). Values from RUN_LOG 2026-09-24 "
               "B0 and tests/test_edgar_facts.py TestLegacyRuleOnRealData. PERIOD box lit in corner.",
               [(0.0, "companyfacts JSON scrolls; 'Revenues ... fy: 2018' highlights"),
                (0.25, "table row: 'HANDED: Revenue $265.6B' | 'ACTUALLY: FY2018 annual, retired tag'"),
                (0.4, "row: 'EPS 6.88' | 'nine months year-to-date; quarter was 2.02'"),
                (0.55, "row: 'Net income $101.5B' | 'year-to-date; quarter was $29.8B'"),
                (0.7, "row: 'Assets $383.3B' | 'correct (point in time)'"),
                (0.8, "hold side-by-side >=3 s; caption: 'every Apple comparison until now used these'")],
               assets=["assets/B02_companyfacts_excerpt.png (render from the fixture; do not mock up)"])),
    beat("B03", "chapter 2b - the fix, test first",
         "Now every figure travels with its period, its unit, its filing, and the filing's accession "
         "number. Quarters are picked by their length in days. Eighty to a hundred days is a quarter. "
         "Year to date is a labelled last resort. When a company restates a number, the restatement "
         "wins. The failing test came first, against a real Apple payload. It pins the two wrong picks "
         "the old rule made.",
         manim("B03_FactWithPeriod",
               "A bare number '2.02' gains chips one at a time: 'Q3 FY2026', 'USD/share', '10-Q', "
               "'accn 0000320193-26-...'. Then a duration ruler classifies spans: 80-100 days QUARTER, "
               "350-380 ANNUAL, other YTD (datasources/edgar.py select_fact).",
               [(0.0, "bare mono '2.02'"),
                (0.2, "chips attach: period, unit, form, accession"),
                (0.5, "duration ruler: 'QUARTER 80-100 d' / 'ANNUAL 350-380 d' / 'YTD: last resort'"),
                (0.75, "chip: 'restatement wins (latest filed)'"),
                (0.9, "hold")])),
    beat("B04", "chapter 2c - source: a failure recorded as ok",
         "The fourth box is source. The web search tool reports some failures by returning an error "
         "message instead of raising one. My code only watched for raised errors. So a failed search "
         "was recorded as ok. And the error text went to the model as if it were a search result. "
         "Mycroft four called this null versus false. This was one step worse. A failure recorded as a "
         "success. The logged arguments showed why the searches failed. The model invented settings "
         "that contradict each other. One retry with only the query now returns real results.",
         manim("B04_FailureRecordedOk",
               "SHOW. The pre-fix 'status: ok' line with a returned {'error': ...} is a LABELLED "
               "RECONSTRUCTION from RUN_LOG 2026-09-24 B0 (the old recorder stored no arguments). 'ok' "
               "struck in ink (never red). Then REAL recorded args from stored MSFT run 1b691654 (post-fix, "
               "retried_query_only=true): start_date 2026-06-30 after end_date 2026-03-31, time_range "
               "'CY2026Q2I', include_domains ['NASDAQ:MSFT'], include_images as a string; the query-only "
               "retry returned 5 URLs (assets/evidence/out/B04_search_args_and_retry.json). SOURCE box lit.",
               [(0.0, "trace line: 'tavily_search  status: ok'"),
                (0.2, "result expands: '{\"error\": \"400 Bad Request\"}'"),
                (0.35, "'ok' struck in ink; 'error' written beside it"),
                (0.55, "callback chip: 'MYCROFT 4: NULL vs FALSE'"),
                (0.7, "logged args list, the contradictory ones ringed"),
                (0.85, "retry line: 'query only -> 5 URLs'")])),
    beat("B05", "chapter 3 - two agents at once",
         "Mycroft six said the two agents ran one after the other. Now they run at the same time. The "
         "test for that is simple. Both agents must wait at a barrier until the other arrives. A "
         "sequential run can never reach it. On a live Apple run, the agents started one millisecond "
         "apart. They were in flight together for thirty-nine seconds. I have not measured a speed-up. "
         "Overlap is all this proves. The server also stopped freezing while agents think. The run "
         "list answered in under a tenth of a second, mid-run.",
         manim("B05_BarrierAndOverlap",
               "SHOW from real data: two bars drawn from the AAPL stream run's started_at spans "
               "(RUN_LOG BL table: 1 ms start gap, 39.4 s overlap). Inset: the test's "
               "threading.Barrier(2) line from tests/test_concurrency_and_stream.py. The recorded "
               "stream fixture web/frontend/tests/fixtures/stream_compare_aapl_2026-09-24.txt can "
               "drive the timeline.",
               [(0.0, "callback: 'MYCROFT 6: ONE AFTER THE OTHER'"),
                (0.2, "code inset: 'threading.Barrier(2)'"),
                (0.4, "timeline: bar A and bar B, start gap '1 ms', overlap shaded '39.4 s'"),
                (0.65, "caption: 'overlap proven. speed-up not measured.'"),
                (0.8, "chip: 'GET /api/runs mid-run: 0.057-0.077 s'")])),
    beat("B06", "chapter 4a - metric and unit: comparing figures",
         "Then metric and unit. The new comparator reads each number the way an analyst would. What is "
         "it a figure of? For which period? And how close counts as equal? Earnings per share must "
         "match to the cent. Billions get half a percent for rounding. Percentage changes get a tenth "
         "of a point. Two different quarters are shown as different periods. Nobody is flagged for "
         "that. In a test built from Microsoft's filing, eighty-two point nine billion and eighty-two "
         "billion, eight hundred eighty-six million now count as one figure. And on a stored Nvidia run, "
         "a model rating its own confidence at ninety percent had raised the alarm. That number no "
         "longer counts as a financial figure.",
         manim("B06_FigureNotString",
               "SHOW. A real conclusion sentence splits into tokens: metric eps_diluted, period "
               "Q3 FY2026, value 2.02. Tolerance chips from validation/facts.py TOLERANCE. Then the MSFT-format pair "
               "from tests/test_facts.py, labelled 'TEST CASE' on screen (it is constructed input, not a "
               "stored run): '82,886,000,000.0 | MATCH | $82.9 billion'. Then stored NVDA run 2220eba0: the "
               "old rule's only divergent number was '90%'; B1 extracts no figure from it. Evidence: "
               "assets/evidence/out/B06_figures_not_strings.json. METRIC and UNIT boxes lit.",
               [(0.0, "sentence splits into METRIC / PERIOD / VALUE tokens"),
                (0.3, "tolerance chips: 'EPS: to the cent' / 'dollars: 0.5%' / '% change: 0.1 pt'"),
                (0.55, "constructed example in Microsoft's filed format: '82,886,000,000.0  MATCH  $82.9 billion'"),
                (0.75, "run 2220eba0: old divergent ['90%'] -> 'self-report, not a figure'"),
                (0.9, "hold")])),
    beat("B07", "chapter 4b - the ratio check",
         "Mycroft seven ended on an open problem. A real ratio and a made-up one look the same. Now, "
         "when only one agent states a ratio, the system recomputes it from that agent's own figures. "
         "Two Apple runs claimed an asset turnover of point one three. Their own revenue and assets, "
         "in the same paragraph, give point six nine. That is five times off. The same runs got net "
         "margin right. On two Google runs, return on assets recomputes to eighteen point nine six, "
         "against a stated eighteen point eight five. Close enough. Those are cleared.",
         manim("B07_RatioRecompute",
               "MATH-TYPESETTING (MathTex, mandatory): asset turnover = revenue / assets = 265.6 / 383.3 "
               "= 0.693 with a real fraction bar. Beside it, held >=3 s: 'agent wrote: 0.13' with a "
               "handnote ring '5x'. Runs 56965308 and 8c67de62 (RUN_LOG B1+U2). Then GOOGL ROA 18.85% vs "
               "recomputed 18.96% -> 'recomputed OK'. Verify the arithmetic in the scene: "
               "265.6/383.3 = 0.6929.",
               [(0.0, "callback quote: 'a legitimate ratio and a fabricated one look identical'"),
                (0.2, "MathTex fraction builds: revenue over assets = 0.693"),
                (0.45, "side-by-side: '0.693 recomputed' | 'agent wrote 0.13', ring '5x', hold"),
                (0.7, "chip: 'net margin in the same run: 38.1% vs 38.2%, OK'"),
                (0.85, "GOOGL runs 2c3c4f23, 0f729a69: 'ROA 18.85% stated, 18.96% recomputed: OK'")])),
    beat("B08", "chapter 4c - the correction",
         "Here is the correction. The old tagger saw the word assets inside return on assets. So it "
         "filed those ratios under assets. Then it skipped them, because assets was a figure only one "
         "agent was given. That is how two wrong ratios passed as clean. Fifteen of sixteen still "
         "counts. Part of it came from that mistake. The count stays. The credit shrinks.",
         manim("B08_WrongDrawer",
               "SHOW the mis-tag: the phrase 'Return on Assets of 18.85%' with only the word 'Assets' "
               "highlighted, the figure sliding into a drawer labelled ASSETS, then into 'excluded'. "
               "Then the Mycroft 7 card '15 / 16' with a small ochre footnote 'partly a mis-tag'. Do not "
               "strike the 15; the count is still pinned in tests.",
               [(0.0, "phrase 'Return on Assets of 18.85%'; only 'Assets' highlights"),
                (0.25, "figure drops into drawer 'ASSETS' -> 'EXCLUDED'"),
                (0.5, "Mycroft 7 card: '15 / 16'"),
                (0.7, "ochre footnote under it: 'partly a mis-tag'"),
                (0.85, "caption: 'the count stays. the credit shrinks.'")])),
    beat("B09", "chapter 5a - the test it failed",
         "Before shipping, I set a bar. Replay the sixteen labelled runs. Do no worse than the old "
         "rule. It did worse. The old rule raised one alarm. The new one raised six. One of the six is "
         "the real fabrication from Mycroft five. Both rules keep it. The other five are ratios stated "
         "with no components. Return on assets for a bank. An asset to income ratio. I cannot say who "
         "is right. The old runs never recorded what each agent was given.",
         manim("B09_SixOfSixteen",
               "Falsifiability beat (PROOF rubric 4). Two bars from a zero baseline, ink fill: 'OLD RULE "
               "1 / 16', 'NEW RULE 6 / 16'. Ochre callout splits the 6 into '1 real (Mycroft 5's 0.34)' "
               "and '5 can't be judged'. Numbers pinned in tests/test_facts.py TestAgainstLabeledCorpus.",
               [(0.0, "title: 'THE BAR: NO WORSE THAN THE OLD RULE'"),
                (0.25, "bars grow: '1 / 16' and '6 / 16'"),
                (0.5, "callout: '1 real: the 0.34 from Mycroft 5, kept by both'"),
                (0.65, "callout: '5 cannot be judged: ratios with no components'"),
                (0.85, "caption: 'the old runs never recorded what each agent was given'")])),
    beat("B10", "chapter 5b - the decision",
         "So I followed my own rule. For company runs, the new comparison is computed and shown on "
         "every record. The recorded verdict still comes from the old rule. The screen says which rule "
         "decided. When the two disagree, a note says so. Making the new rule the default is a human "
         "decision. And every new run now stores what each agent was given. Stored records went from "
         "seven fields to fourteen. The evidence for that decision now piles up on its own.",
         manim("B10_OptIn",
               "HOLD: captured app screenshot of run 20c538e4's summary: headline counted from the rows, "
               "then 'Recorded verdict (concept-aware rule): Flagged for review' (assets/B10_recorded_"
               "verdict_1280.png). Then stored-run key count 7 -> 14 from two real fixtures, 'contexts' "
               "highlighted (assets/evidence/out/B10_record_growth.json).",
               [(0.0, "screenshot: headline, then 'Recorded verdict (concept-aware rule)' line highlighted"),
                (0.3, "chip: 'which rule decided is always shown'"),
                (0.55, "chip: 'DEFAULT = A HUMAN DECISION'"),
                (0.7, "JSON key counter: 7 -> 14; 'contexts' highlights"),
                (0.9, "hold")],
               assets=["assets/B10_recorded_verdict_1280.png", "assets/evidence/out/B10_record_growth.json"])),
    beat("B11", "chapter 6 - three format failures found live",
         "Live runs found three problems in the format itself. Agents were copying the prompt's own "
         "instructions into their answers. I replayed every stored conclusion. Seventeen of a hundred "
         "thirty-five had done it. The fix put nothing inside the answer tags, plus a check that "
         "rejects copied text. Then one prompt version made the model close its answer with square "
         "brackets. Three of twenty-two first attempts. And when the model opened its reasoning in the "
         "same turn as a web search, that opening was dropped. The parser now reads the model's "
         "earlier turns. The final batch had zero first-attempt failures across eight agents.",
         manim("B11_ThreeFormatFailures",
               "HOLD real excerpts: a stored conclusion containing the directive's instruction text "
               "(ringed); '[/conclusion]' beside '</conclusion>'; a response starting with a bare "
               "'</thought_log>'. Counts from RUN_LOG ('Directive echo, properly' and B1+U2).",
               [(0.0, "excerpt 1: copied instruction text, ringed; counter '17 / 135'"),
                (0.35, "excerpt 2: '[/conclusion]' vs '</conclusion>'; counter '3 / 22'"),
                (0.6, "excerpt 3: bare '</thought_log>' at top; label 'opening lost in tool turn'"),
                (0.85, "result chip: 'final batch: 0 first-attempt failures, 8 agents'")])),
    beat("B12", "chapter 7a - the table",
         "Mycroft six said every line of interface code had zero tests. The new interface is React, "
         "with seventy-four. Each figure is a row. Agent A is blue. Agent B is orange. The difference sits "
         "between them. Mismatches rise to the top. Figures only one agent was given fold away, so "
         "they never pass for disagreement. The headline is counted from the rows. No model writes it.",
         manim("B12_TheMatrix",
               "HOLD: real screen recording frames of /app at 1280 px (matrix: Figure / Period / A / "
               "Difference / B) and 375 px (cards), app palette kept (human decision 2026-09-24). "
               "Callback chip first.",
               [(0.0, "callback: 'MYCROFT 6: 0 TESTS ON INTERFACE CODE' -> '74'"),
                (0.25, "desktop matrix screenshot; columns labelled"),
                (0.55, "folded group highlights: 'figures only one agent was given'"),
                (0.75, "phone screenshot: rows as cards"),
                (0.9, "hold")],
               assets=["assets/B12_matrix_1280.png", "assets/B12_matrix_375.png"])),
    beat("B13", "chapter 7b - something in common",
         "Mycroft six found the root cause of every false alarm. The two agents were never handed the "
         "same figure. Now both get net income and diluted earnings per share. On Apple, for the first "
         "time in company mode, both agents cited the same figure, from the same filing. They agreed. "
         "The filing agreed. On Nvidia and Google, one agent said that figure was missing. It was the "
         "last line of its input.",
         manim("B13_FirstRealAgreement",
               "HOLD: run 20c538e4 (fixture run_compare_b3_aapl.json) matrix filtered to the two shared "
               "rows, 'Matches the filing' badges visible. Then the NVDA/GOOGL agent-A quote 'not "
               "explicitly stated in the Context' beside the context's last line showing the figure, "
               "held >=2 s.",
               [(0.0, "callback: 'MYCROFT 6: NEVER THE SAME FIGURE'"),
                (0.25, "rows: 'Net income $29.79B MATCH $29.788B', 'EPS (basic or diluted not stated) $2.02 MATCH $2.02'; note: neither agent stated a period"),
                (0.5, "badge: 'matches the filing'"),
                (0.7, "side-by-side: agent quote 'not explicitly stated' | context last line with EPS"),
                (0.9, "hold")],
               assets=["assets/B13_shared_rows_1280.png"])),
    beat("B14", "chapter 8a - the honest ledger, true now",
         "True now that wasn't before. Every figure carries its period, unit and filing. Failed "
         "searches are recorded as failures. The two agents run at once. Ratios are recomputed, and "
         "two real errors surfaced. A shared figure matched across both agents and the filing. Three "
         "hundred ninety Python tests and seventy-four interface tests pass.",
         manim("B14_TrueNow",
               "Ledger list one, built line by line in mono. Test counts re-run 2026-09-26: 390 Python "
               "(unittest discover), 74 frontend (vitest). Re-run on recording day.",
               [(0.0, "title: 'TRUE NOW'"),
                (0.15, "line: 'every figure: period, unit, filing'"),
                (0.3, "line: 'failed searches recorded as failures'"),
                (0.45, "line: 'two agents in flight at once'"),
                (0.6, "line: 'ratios recomputed; 2 real errors surfaced'"),
                (0.75, "line: 'first shared-figure match, confirmed by the filing'"),
                (0.88, "line: '390 Python + 74 interface tests'")])),
    beat("B15", "chapter 8b - the honest ledger, still not true",
         "Still not true. The stricter comparator is opt-in for company runs. Tagging still works on "
         "wording, so some phrasings go unrecognised. The ratio check ignores annual versus quarterly "
         "figures. Agents skip figures they were given. And none of this is committed. That was true "
         "in Mycroft six. It is still true, and the pile is bigger.",
         manim("B15_StillNotTrue",
               "OUTRO-LAW chapter close: list two held on screen, uncleared, never softened. git panel "
               "shows the last commit is still c53746a (same as Mycroft 6/7) and the working-tree "
               "counter (79 changed paths on 2026-09-26; recount on recording day).",
               [(0.0, "title: 'STILL NOT TRUE'"),
                (0.15, "line: 'stricter comparator: opt-in for company runs'"),
                (0.3, "line: 'tagging is by wording'"),
                (0.45, "line: 'ratio check ignores annual vs quarterly'"),
                (0.6, "line: 'agents skip figures they were given'"),
                (0.75, "git panel: 'last commit c53746a' + counter of uncommitted paths"),
                (0.9, "list holds, uncleared")])),
    beat("B16", "close - the smallest true claim",
         "So here is the smallest true claim. The comparator got stricter, and it lost its own test. "
         "It also caught two errors the easier rule had hidden. Before you trust any match, ask four "
         "questions. What does it measure? Which period? What unit? Where did it come from? Six "
         "alarms. One real. Five unknown. And the call on which rule counts still belongs to a person.",
         manim("B16_EndCardReprise",
               "OUTRO-LAW close: reprises the cold open's hook card exactly (15/16 vs 6/16), then 6 END "
               "CARD bullets. This beat carries the stats; B17 carries none. The four-box test returns "
               "as the viewer's takeaway (FELLOWS-SUBMISSION 'concrete takeaway'); Mycroft reels have "
               "no Your Turn beat (CLAUDE.md SS9).",
               [(0.0, "serif line: 'the smallest true claim'"),
                (0.1, "hook card reprise: '15 / 16' | '6 / 16'"),
                (0.25, "four boxes return: METRIC / PERIOD / UNIT / SOURCE"),
                (0.4, "bullet 1: 'agents had been handed FY2018 revenue and 9-month EPS'"),
                (0.5, "bullet 2: 'new rule: 6 of 16 alarms (1 real, 5 unknown), opt-in'"),
                (0.6, "bullet 3: 'recomputed ratios found two 5x asset-turnover errors'"),
                (0.7, "bullet 4: 'part of 15 of 16 came from a Return-on-Assets mis-tag'"),
                (0.8, "bullet 5: 'first shared-figure match across agents and filing'"),
                (0.9, "bullet 6, emphasized: 'nothing here is committed'"),
                (0.98, "hold, cut to black")])),
    beat("B17", "outro",
         "The rule that lost. Written down, versioned, and executable. Signing off, Divij Pawar.",
         outro("The Rule That Lost", "Written down, versioned, and executable.",
               "OUTRO LAW: exact title restate, handle, one subline. No stats; B16 carries them.")),
]

# ─────────────────────────────────────────────────────────────────────────────
# Mycroft 9 — One Run, Still Open
# ─────────────────────────────────────────────────────────────────────────────
V = True  # beats not yet in RUN_LOG
M9 = [
    beat("B00", "cold open",
         "Hi, I am Divij Pawar, and this video is about what happens when two AI agents disagree and a "
         "person has to decide. The voice you are hearing is AI generated. The work is mine. This run "
         "asked two agents when the first Pokémon game reached North America. One said nineteen "
         "ninety-eight. The other said nineteen ninety-six. The system flagged it. Then it stopped. It "
         "has waited for a person ever since. I built the thing that made it wait. And I left it open "
         "on purpose.",
         composer({
             "command": "When two agents disagree, who gets the last word?",
             "topic": "CROSS-AGENT VALIDATION",
             "segment": "One Run, Still Open",
             "greeting": "Konnichiwa, Divij",
             "runningText": "waiting for a decision\u2026",
             "output": [
                 "Agent A: 1998. Agent B: 1996. Difference: 2 years",
                 "The run stops and waits for a named person",
                 "The AI that built the gate never cleared it",
             ]},
             "COLD OPEN LAW (CLAUDE.md SS9) with the required intro line and AI-narration disclosure "
             "(SS8). Greeting rotated to 'Konnichiwa'. The narration never says which year is right, on "
             "purpose: the system doesn't know, and the video mirrors it. Run ec1a3b44 must still be "
             "AWAITING_DECISION on recording day (check before building).",
             COLD_SHOW)),
    beat("B01", "chapter 1 - recap and the four parts of a gate",
         "Quick recap, for anyone new. Part one made the comparison stricter. Figures are now compared "
         "by metric, period, unit and source. Mycroft three said never resolve what you can't prove is "
         "independent. Surface it. Mycroft four built the flag, and said a flagged contradiction "
         "triggers nothing. That stopped being true this week. Part one also showed agents skipping "
         "figures they were given. So the checks in this video matter as much as the gate. A gate needs four parts. A trigger you "
         "can test. A stop that actually holds. A named person with a written reason. And a record "
         "nobody can edit. Leave one out, and you have a warning with extra steps.",
         manim("B01_FourPartsOfAGate",
               "Framework-before-example (PROOF 1-2). Callback cards quote Mycroft 3 ('surface it') and "
               "Mycroft 4 ('a flagged contradiction triggers nothing'); the Mycroft 4 quote gets an ink "
               "strike. Then four boxes: TRIGGER / STOP / DECIDER / RECORD, reused as a corner chip in "
               "B02-B07.",
               [(0.0, "recap chip: 'PART 1: METRIC / PERIOD / UNIT / SOURCE'"),
                (0.2, "quote card: 'Mycroft 3: never resolve what you can't prove is independent'"),
                (0.35, "quote card: 'Mycroft 4: a flagged contradiction triggers nothing' -> ink strike"),
                (0.6, "four boxes build: TRIGGER / STOP / DECIDER / RECORD"),
                (0.85, "caption: 'leave one out: a warning with extra steps'")])),
    beat("B02", "chapter 2a - trigger",
         "The trigger is narrow. A run waits only when two agents cite different values for the same "
         "figure and period. A figure only one agent mentions is shown for review. It does not stop "
         "anything. With only one answer, there is nothing to decide between. And runs stored before "
         "the gate existed are never gated after the fact. Changing the rules on old records is how "
         "audit trails get rewritten. In practice, most runs never gate. In the last company batch, none "
         "did. There were no mismatches.",
         manim("B02_Trigger",
               "Matrix rows sorted by status (validation/gate.py): only the MISMATCH row gets a gate "
               "icon; an UNCORROBORATED row gets a review marker; a pre-gate stored run is tagged "
               "NOT_GATED. TRIGGER box lit.",
               [(0.0, "three matrix rows appear"),
                (0.25, "MISMATCH row: gate icon 'AWAITING DECISION'"),
                (0.45, "UNCORROBORATED row: 'shown for review, does not gate'"),
                (0.65, "old run card: 'NOT GATED: stored before the gate existed'"),
                (0.85, "hold")])),
    beat("B03", "chapter 2b - the decision",
         "The form opens where you are already reading. Nothing covers the evidence. The reviewer "
         "picks one of five outcomes. Agent A is right. Agent B is right. Both are wrong. Not a real "
         "conflict. Or here is the correct value. Each disputed figure gets a checkbox, so the decision "
         "says what it covers. Then they write why. Twenty characters minimum. "
         "Looks good is too short on purpose. And they type a name.",
         manim("B03_DecisionForm",
               "HOLD: screen-recording frames of run ec1a3b44's gate panel expanding in place under the "
               "verdict with the matrix still visible (DecisionGate.tsx). Close-ups of the five radio "
               "cards and the rationale counter ticking to 20. DECIDER box lit.",
               [(0.0, "gate panel expands in place; matrix stays visible below"),
                (0.3, "five radio cards highlight in turn"),
                (0.6, "rationale counter ticks '0 / 20' -> '20 / 20'"),
                (0.75, "'looks good' typed: counter reads '10 / 20', submit disabled"),
                (0.9, "name field focuses")],
               assets=["assets/B03_gate_open_1280.png"])),
    beat("B04", "chapter 2c - identity and refusals",
         "Look at the small print. Recorded as entered. Not verified. The login carries a permission "
         "level. It does not carry a person. So the screen says that, every time. A decision that "
         "breaks a rule is refused, with the reason in words. A decision about a figure nobody disputed "
         "is refused. So is a value with any outcome except the override. Nothing gets quietly fixed.",
         manim("B04_SmallPrint",
               "Zoom on the name-field hint 'Recorded as entered; not verified.' Then a real 422 refusal "
               "body from POST /api/runs/{id}/decisions (capture from the route test or a temp DB, never "
               "the live run).",
               [(0.0, "zoom: 'Recorded as entered; not verified.'"),
                (0.35, "chip: 'token = permission level, not a person'"),
                (0.6, "refusal card: '422: rationale must be at least 20 characters'"),
                (0.85, "caption: 'refused, never repaired'")])),
    beat("B05", "chapter 2d - the record",
         "A later decision can supersede an earlier one. Both stay on the record. The database blocks "
         "edits and deletes, the way Mycroft one set it up.",
         manim("B05_Supersede",
               "Decision stack: card 1 lands, card 2 lands on top, card 1 dims with tag 'superseded' and "
               "stays visible. Callback chip to Mycroft 1's append-only triggers (web/db.py "
               "gate_decisions triggers). RECORD box lit.",
               [(0.0, "decision card 1 lands"),
                (0.3, "decision card 2 lands on top; card 1 dims, tag 'superseded'"),
                (0.6, "chip: 'UPDATE / DELETE -> blocked by trigger'"),
                (0.8, "callback: 'MYCROFT 1: APPEND-ONLY'")])),
    beat("B06", "chapter 3a - what an investor sees",
         "While a run waits, investors see the agreed figures and a notice. The disputed values and "
         "both agents' answers are withheld by the server. Then I searched the investor response for "
         "both years. Nineteen ninety-six never appears. Nineteen ninety-eight appears once. It sits "
         "inside a search result the agent read, shown in the run's trace. The trace is not withheld "
         "yet. So the gate has a hole, and now it is written down. There is a second limit. A read with no "
         "token is served at the run's stored level. That keeps the old interface working. It also "
         "means the withholding is only as strong as read access.",
         manim("B06_InvestorView",
               "Side-by-side, held >=3 s: auditor view '1998 | 2 years | 1996' vs investor view "
               "'Withheld | | Withheld' + banner 'Pending human review'. Then the investor read searched "
               "for both years, live and in the fixture: '1996' 0, '1998' 1, inside a Tavily result in the "
               "trace (assets/evidence/out/B06_investor_view.json). Show that match on screen, ringed; it is "
               "the beat's falsifiability moment.",
               [(0.0, "split screen: AUDITOR | INVESTOR"),
                (0.3, "investor cells read 'Withheld'; banner 'Pending human review'"),
                (0.55, "hold side-by-side"),
                (0.65, "search box: '1996' -> 0 results"),
                (0.75, "search box: '1998' -> 1 result, inside a search result in the trace, ringed"),
                (0.9, "caption: 'the trace is not withheld yet'")],
               assets=["assets/B06_auditor_1280.png", "assets/B06_investor_1280.png", "assets/B06_investor_trace_leak_1280.png", "assets/evidence/out/B06_investor_view.json"])),
    beat("B07", "chapter 3b - the gate I didn't clear",
         "The coding agent that built this never recorded a decision on that run. Clearing a human "
         "gate is the one thing the gate exists to stop. The Pokémon run is still open.",
         manim("B07_StillOpen",
               "Run ec1a3b44 status chip 'AWAITING DECISION' with a date line; decision history panel "
               "reads 'no decisions recorded'. Flat, no drama. Evidence: assets/B07_gate_closed_1280.png, "
               "assets/evidence/out/B00_B07_gated_run_now.json (0 decisions, AWAITING_DECISION).",
               [(0.0, "status chip: 'AWAITING DECISION'"),
                (0.4, "history panel: 'no decisions recorded'"),
                (0.75, "caption: 'the gate is for a person'")])),
    beat("B08", "chapter 4a - rules that stop a run",
         "Two agents can agree and both be wrong. So each agent's figures now go through accounting "
         "rules. Some are identities. Basic earnings per share can't be below diluted. Free cash flow "
         "is operating cash flow minus capital spending. Assets equal liabilities plus equity. Break "
         "one, and the run waits for a person, the same as a mismatch. The choices change too. The "
         "reviewer can confirm the error, instead of picking an agent.",
         manim("B08_HardRules",
               "MATH-TYPESETTING (MathTex): EPS_basic >= EPS_diluted; FCF = OCF - CapEx; Assets = "
               "Liabilities + Equity (2% tolerance note). Each gets a 'HARD: gates' tag "
               "(validation/constraints.py, gate policy v2).",
               [(0.0, "MathTex: EPS_basic >= EPS_diluted"),
                (0.3, "MathTex: FCF = OCF - CapEx"),
                (0.55, "MathTex: Assets = Liabilities + Equity, note 'to 2%'"),
                (0.8, "tag on all three: 'HARD: opens the gate'")])),
    beat("B09", "chapter 4b - claim versus source",
         "Each cited figure is also checked against the filing the agent was given. Rounding to the "
         "digits written is allowed. In one Microsoft run, an agent was handed eighty-two point nine "
         "billion. It wrote eight hundred twenty-eight point nine. That attempt failed its format "
         "check first. So this check never ran on it live. It would have caught it.",
         manim("B09_ClaimVsSource",
               "Side-by-side, held >=3 s: 'given: revenue $82.9B' | 'wrote: $828.9B', handnote '10x'. "
               "Label 'first attempt, halted on format' so it is never read as a live catch. Then the "
               "rounding rule: '$109 billion for $109.417B: passes'.",
               [(0.0, "rule chip: 'rounding to the digits written = not misquoting'"),
                (0.25, "side-by-side: given $82.9B | wrote $828.9B, ring '10x'"),
                (0.55, "label: 'attempt halted on format; check never ran live'"),
                (0.8, "caption: 'would have caught it'")])),
    beat("B10", "chapter 4c - rules that only inform",
         "Other rules are only usually true. On Google, net income was nearly three times operating "
         "income. The filing said so too. That is a real one-off gain. So soft rules never stop a run. "
         "They say unusual, worth a look. It also explained two figures part one left unrecognised. "
         "They were Google's filed earnings per share.",
         manim("B10_SoftRules",
               "GOOGL real values: net income $112.2B vs operating income $40.77B, shown for both agent "
               "B and the filing itself, with an ochre callout 'Unusual, worth a look' (never red). "
               "Then the Mycroft 8 'Unrecognised figure $9.11' row resolving to 'filed diluted EPS'.",
               [(0.0, "heuristic: 'net income <= operating income (usually)'"),
                (0.3, "GOOGL: '$112.2B' vs '$40.77B', agent and filing both"),
                (0.55, "ochre callout: 'unusual, worth a look: does not gate'"),
                (0.8, "'Unrecognised figure $9.11' -> 'filed diluted EPS'")])),
    beat("B11", "chapter 4d - the filing, and an honest gap",
         "The filing itself gets the same checks, from the one fetch already made. Apple's balance "
         "sheet adds up. Then, mid-test, the local model stopped responding. A five token test request "
         "got no reply in sixty seconds. Model calls have no "
         "timeout. So a stuck model can hold a comparison forever. That is in the ledger now.",
         manim("B11_FilingAndTimeout",
               "Checks list row 'Adds up: assets = liabilities + equity, $383.3B (AAPL)'. Then a status "
               "line 'Ollama: no response for 5 min' and a ledger card 'no timeout on model calls: OPEN'.",
               [(0.0, "row: 'filing check: assets = liabilities + equity, $383.3B, adds up'"),
                (0.4, "status: 'model: no response, 5 min'"),
                (0.7, "ledger card: 'no timeout on model calls: OPEN'")])),
    beat("B12", "chapter 5a - show me where it says that",
         "Every figure the agents were given can now be found in the filing itself. The system opens "
         "the actual SEC document and finds the exact tagged value. It returns the row, the column, "
         "and the number as filed. In the last batch, it found all twenty-four figures. Every filed "
         "value matched what the agents were handed. For web figures, it returns the snippet the agent "
         "actually read. The click-through view is the next step. It is not built yet.",
         manim("B12_SourceExcerpt",
               "SHOW recorded output (EXECUTABLE-EVIDENCE): datasources.filings.find_in_document run on the "
               "real trimmed Apple 10-Q (accn 0000320193-26-000020): row 'Total net sales', column 'Three "
               "Months Ended June 27, 2026', displayed '109,417' (millions) = $109.417B; same for Net income "
               "29,789 and Diluted 2.02 (assets/evidence/out/B12_filing_excerpt.json). Then the logged live "
               "tally '24 / 24 found, all equal' (RUN_LOG BP+U4). No UI exists for this yet (U6): do not "
               "draw a popover as if it were the app.",
               [(0.0, "terminal-style recorded output: find_in_document(10-Q, 'Revenues', Q3)"),
                (0.3, "row 'Total net sales' | column 'Three Months Ended June 27, 2026' | '109,417' highlighted"),
                (0.55, "same for Net income 29,789 and Diluted 2.02"),
                (0.75, "tally chip: '24 / 24 figures found, every filed value equal'"),
                (0.9, "caption: 'click-through view: not built yet'")],
               assets=["assets/evidence/out/B12_filing_excerpt.json"])),
    beat("B13", "chapter 5b - watching it run",
         "You can watch a comparison happen. Each agent has its own lane. It shows what that agent is "
         "doing right now. The one shared SEC fetch is drawn once, because it happened once. Every "
         "indicator is a real server event. If the connection drops, the run keeps going. It still lands "
         "in history.",
         manim("B13_LiveLanes",
               "HOLD: screen recording of CompareView.tsx during a real /api/compare/stream run (or "
               "frames driven from stream_compare_aapl_2026-09-24.txt; logged in RUN_LOG BP+U4): blue and orange lanes, live "
               "status lines resolving into citation pills, one shared fetch bar above both.",
               [(0.0, "shared bar: 'one SEC fetch, both agents'"),
                (0.3, "lane A: 'Searching...' -> pills"),
                (0.5, "lane B: 'Thinking... 12s'"),
                (0.8, "caption: 'every indicator is a server event'")],
               assets=["assets/B13_lanes.mp4 (real capture)", "assets/evidence/out/B13_stream_events.json"])),
    beat("B14", "chapter 6a - from figures to a grade",
         "Analysts don't stop at figures. They make a call. So agents now end with a structured "
         "assessment. A grade, a direction, their assumptions, and three key points. When an agent "
         "skips it, the screen shows the raw output, and exactly where the missing piece should be.",
         manim("B14_Assessment",
               "Two assessment strips, Bull (blue) and Bear (orange). Label 'ILLUSTRATIVE' on screen "
               "until a real bull/bear run exists (values from the roadmap mock-up: BBB/Hold/8% vs "
               "BB/Sell/3%). Then 'No structured grade' + 'View raw output' expanding with the expected "
               "spot highlighted. Roadmap B4/U7.",
               [(0.0, "strip A: 'BBB · Hold · growth 8%' (label: illustrative)"),
                (0.25, "strip B: 'BB · Sell · growth 3%'"),
                (0.5, "growth assumptions ringed in ochre"),
                (0.7, "panel: 'No structured grade' -> 'View raw output' expands"),
                (0.9, "expected <assessment> spot highlighted")], verify=V)),
    beat("B15", "chapter 6b - why grades differ, and when to agree",
         "When two grades differ, the system sorts the cause. Different figures or periods. The same "
         "figures with different assumptions. Or neither, which is a matter of weighting. Mycroft "
         "three sorted disagreements by how they look. This sorts them by where they came from. A "
         "consensus is recorded only when the grades match and no hard rule failed. Anything else goes "
         "to the gate, and the reviewer can now set the grade.",
         manim("B15_DivergenceAndConsensus",
               "Three bins: DATA / ASSUMPTION / WEIGHTING. Callback chip to Mycroft 3's four literature "
               "types (stylistic, reasoning, high-confidence, adversarial) as 'how it looks' vs these as "
               "'where it came from'. Consensus rule as a two-condition AND. Roadmap B5/U8.",
               [(0.0, "three bins build: DATA / ASSUMPTION / WEIGHTING"),
                (0.35, "callback chip: 'Mycroft 3: how it looks' vs 'now: where it came from'"),
                (0.6, "rule: 'grades match AND no hard failure -> consensus'"),
                (0.8, "else -> gate, new option 'Set grade'")], verify=V)),
    beat("B16", "chapter 6c - answer first",
         "The review now reads in the order a person needs it. The answer, and whether anything failed "
         "a check. Then the decision. Then the evidence, figure by figure. Then the agents. Then the "
         "machinery, folded away. On a phone, the two agents' key points sit side by side. Every review "
         "exports as a plain document.",
         manim("B16_AnswerFirst",
               "HOLD: full review page scroll (summary + checklist, gate, matrix, agents, collapsed "
               "trace), then 'Download review' opening a Markdown file. Roadmap U5/U9/B6.",
               [(0.0, "page top: summary + checklist"),
                (0.3, "gate, then matrix"),
                (0.55, "agents, then collapsed trace"),
                (0.8, "'Download review' -> Markdown opens")],
               assets=["assets/B16_review_scroll.mp4 (real capture)"], verify=V)),
    beat("B17", "chapter 7a - the honest ledger, true now",
         "True now that wasn't before. A mismatch stops the run until a person decides. Decisions need "
         "a reason, and can't be edited. Investors don't receive the disputed values or either answer. "
         "Accounting rules "
         "check each agent and the filing. Soft rules inform. They never block.",
         manim("B17_TrueNow",
               "Ledger list one in mono. Only logged items (BG+U3, B2+B3); [verify] items join only once "
               "their RUN_LOG entries exist.",
               [(0.0, "title: 'TRUE NOW'"),
                (0.2, "line: 'mismatch -> stop until a person decides'"),
                (0.4, "line: 'reason required; no edits'"),
                (0.6, "line: 'disputed values and answers withheld from investors'"),
                (0.8, "line: 'hard rules gate; soft rules inform'")])),
    beat("B18", "chapter 7b - the honest ledger, still not true",
         "Still not true. The decider's name is typed, not verified. Anyone can mint a reviewer token, "
         "one of the critical security findings from the start. A search result in the trace can still "
         "show a disputed value. The storage still holds everything. "
         "Withholding happens when data is read. No accounting check has stopped a live run yet. Model "
         "calls still have no timeout. And none of it is committed.",
         manim("B18_StillNotTrue",
               "OUTRO-LAW chapter close: list two held uncleared. Recount the critical findings in "
               "web/self_report.py before recording (narration deliberately avoids a number). git panel: "
               "last commit c53746a, uncommitted counter.",
               [(0.0, "title: 'STILL NOT TRUE'"),
                (0.15, "line: 'decider identity: self-declared'"),
                (0.3, "line: 'anyone can mint a reviewer token'"),
                (0.4, "line: 'a trace search result leaked 1998 to the investor view'"),
                (0.5, "line: 'storage holds everything; withheld at read time'"),
                (0.6, "line: 'no live gated accounting check yet'"),
                (0.72, "line: 'no timeout on model calls'"),
                (0.85, "git panel: 'last commit c53746a' + uncommitted counter"),
                (0.95, "list holds, uncleared")])),
    beat("B19", "close - the smallest true claim",
         "Four videos ago I said the judgment stays with the human. This is the first time the system "
         "can't move without one. So here is the smallest true claim. The machine fetches, reads, "
         "compares and checks. Then it stops. If you run agents, find one warning your system raises. "
         "Give it a trigger, a stop, a person, and a record. Then check that it cannot clear itself. "
         "One run, still open.",
         manim("B19_EndCardReprise",
               "OUTRO-LAW close: reprise the cold open's card exactly (1998 | 2 years | 1996, AWAITING "
               "DECISION), then END CARD bullets. The four-part gate returns as the concrete takeaway; "
               "no separate Your Turn beat in Mycroft reels (CLAUDE.md SS9).",
               [(0.0, "hook card reprise: '1998 | 2 years | 1996' + 'AWAITING DECISION'"),
                (0.15, "four boxes return: TRIGGER / STOP / DECIDER / RECORD"),
                (0.35, "bullet 1: 'a mismatch now stops the run for a named person'"),
                (0.45, "bullet 2: 'reason >= 20 chars; decisions superseded, never edited'"),
                (0.55, "bullet 3: 'values and answers withheld; one trace snippet still leaked 1998'"),
                (0.65, "bullet 4: 'hard accounting rules gate; soft rules inform'"),
                (0.75, "bullet 5: 'identity self-declared; no model-call timeout'"),
                (0.85, "bullet 6, emphasized: 'nothing here is committed'"),
                (0.98, "hold, cut to black")])),
    beat("B20", "outro",
         "One run, still open. Written down, versioned, and executable. Signing off, Divij Pawar.",
         outro("One Run, Still Open", "Written down, versioned, and executable.",
               "OUTRO LAW: exact title restate, handle, one subline. No stats; B19 carries them.")),
]


def meta(title, slug, series, continues, note):
    return {
        "title": title, "slug": slug, "topic": "CROSS-AGENT VALIDATION",
        "register": "Periodic update", "audience": "Claude", "brand": "claude-divij",
        "persona": "Divij Pawar", "voice": "am_onyx", "engine": "kokoro", "voice_kokoro": "am_onyx",
        "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5",
        "greeting": None, "folderLabel": "@DivijPawar", "in_for_bear": False,
        "series": series, "continues_from": continues, "source_script": f"{slug}.md",
        "code_source": "D:\\Code\\mycroft\\verification-layer (never Desktop\\mycroft\\accountability_layer)",
        "build_note": note, "approvals": APPROVALS,
    }


def write(folder, slug, md_name, metadata, beats):
    metadata["greeting"] = beats[0]["shot"]["remotion"]["props"]["greeting"]
    words = sum(len(b["narration_text"].split()) for b in beats)
    metadata["narration_words"] = words
    metadata["estimated_runtime_s"] = round(words / WPS)
    for b in beats:  # machine checks from CLAUDE.md SS4
        assert "\u2014" not in b["narration_text"] and "\u2013" not in b["narration_text"], b["beat_id"]
    sheet = {"metadata": metadata, "beats": beats}
    out = ROOT / folder / "beat_sheet.json"
    out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    # sync the script's Beats section from the sheet
    md_path = ROOT / folder / md_name
    md = md_path.read_text(encoding="utf-8")
    lines = ["## Beats", "",
             "_Generated from `beat_sheet.json` (the source of truth). Edit the sheet, then regenerate._",
             ""]
    for b in beats:
        s = b["shot"]
        kind = s["remotion"]["pattern"] if s["type"] == "REMOTION" else s["manim"]["scene_class"]
        lines.append(f"### {b['beat_id']} — {b['act']} (≈{b['estimated_duration_s']} s · {kind})")
        lines.append(f"**VISUAL:** {s['concept']}")
        if s.get("assets"):
            lines.append("**ASSETS:** " + "; ".join(s["assets"]))
        lines.append("")
        lines.append("**NARRATION:**")
        lines.append(b["narration_text"])
        lines.append("")
    new_beats = "\n".join(lines)
    md = re.sub(r"## Beats\n.*?(?=\n---\n\n## Fact-check sheet)", new_beats, md, flags=re.S)
    md_path.write_text(md, encoding="utf-8")
    print(out, len(beats), "beats", words, "words", f"~{words / WPS / 60:.1f} min")



# ── Narration v4 + visuals v4: about the work, not the working (narration_v4.py, visual_v4.py) ──────
sys.path.insert(0, str(Path(__file__).resolve().parent))
from narration_v4 import NARR_M8, NARR_M9, SPEED_IF_SLURRED_M8, SPEED_IF_SLURRED_M9  # noqa: E402
from visual_v4 import VISUAL_M8, VISUAL_M9, M9_COLD_OPEN_OUTPUT  # noqa: E402


def apply_narration(beats, narr, speeds):
    assert set(narr) == {b["beat_id"] for b in beats}, "narration must cover every beat"
    for b in beats:
        b["narration_text"] = narr[b["beat_id"]]
        b["estimated_duration_s"] = round(len(b["narration_text"].split()) / WPS)
        if b["beat_id"] in speeds:
            b["speed_if_slurred"] = speeds[b["beat_id"]]


def apply_visuals(beats, vis):
    for b in beats:
        if b["beat_id"] in vis:
            concept, show = vis[b["beat_id"]]
            verify = b["shot"].get("concept", "").startswith("[verify]") and not concept.startswith("[verify]")
            b["shot"]["concept"] = ("[verify] " if verify else "") + concept
            b["shot"]["show"] = [{"at": at, "event": ev} for at, ev in show]


apply_visuals(M8, VISUAL_M8)
apply_visuals(M9, VISUAL_M9)
M9[0]["shot"]["remotion"]["props"]["output"] = M9_COLD_OPEN_OUTPUT
for b in M9:
    c = b["shot"].get("concept", "")
    b["shot"]["concept"] = c.replace("FEATURE NOT YET IN THE CHECKOUT", "NOT BUILT YET")

apply_narration(M8, NARR_M8, SPEED_IF_SLURRED_M8)
apply_narration(M9, NARR_M9, SPEED_IF_SLURRED_M9)

write("Mycroft8_DivijPawar_09-18-2026_the-rule-that-lost", "the-rule-that-lost", "the-rule-that-lost.md",
      meta("The Rule That Lost", "the-rule-that-lost",
           "Cross-Agent Validation - weekly update, video 6 (audit-layer update, part 1 of 2)",
           "fifteen-of-sixteen/ (Mycroft7). Its cold open answers Mycroft7's headline with a correction: "
           "part of fifteen-of-sixteen came from a Return-on-Assets mis-tag. Assumes Mycroft 3-7 are "
           "common knowledge (see the series table in the script's production brief).",
           "2026-09-26: initial authoring pass, not built. 18 beats (B00-B17). Runtime estimated at the "
           "3.2 words/s measured across Mycroft1-7 actual audio. Mycroft skeleton per CLAUDE.md SS9: "
           "no Your Turn beat; ledger (B14-B15), end-card reprise (B16), stat-free outro (B17)."),
      M8)
write("Mycroft9_DivijPawar_09-25-2026_one-run-still-open", "one-run-still-open", "one-run-still-open.md",
      meta("One Run, Still Open", "one-run-still-open",
           "Cross-Agent Validation - weekly update, video 7 (audit-layer update, part 2 of 2)",
           "the-rule-that-lost/ (Mycroft8). Pays off Mycroft4's 'a flagged contradiction triggers "
           "nothing'. Does not re-argue why software, a third AI or a vote can't decide (Mycroft 1 and 3).",
           "2026-09-26: initial authoring pass, not built. 21 beats (B00-B20). B14-B16 are marked "
           "[verify]: B4-B6/U5-U9 are being added. BP+U4 (B12-B13) are logged; BP has no UI yet. Check each "
           "against verification-layer before GATE P. Mycroft skeleton per CLAUDE.md SS9."),
      M9)
