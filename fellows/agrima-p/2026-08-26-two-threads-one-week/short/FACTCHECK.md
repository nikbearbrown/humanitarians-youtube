# FACTCHECK — two-threads-one-week (v2 revision — "a log, not a highlight reel")

Status: **GATE F — drafted before first render.** This reel's claims are
either (a) code-verifiable — the CODE/OUTPUT beats show the actual scripts
and their actual captured stdout, reproducible by running the two .py files
in this folder — or (b) status claims about the user's own week, supplied
directly by the user and not independently verifiable by this toolkit, so
they are treated as first-person self-report, not investigated fact — or
(c) plain-language paraphrase of the user's own two article summaries,
kept general enough to avoid inventing any number the user didn't supply.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B00/B01 | "Two articles went out this week" / 2 articles published | ✅ PASS (self-report) | User-supplied: "2 articles published" this week | None |
| 2 | B03/B04 | `weekly_log_v1.py` logs every item with its real status, no scoring or tally | ✅ PASS — code-verifiable | Script in this folder; `log()` just iterates and prints `- item (status)` per entry | None — code shown is the code that ran |
| 3 | B04 | Writing thread: 2/2 items published; Loon Project: 3 done (drone acquired, FAA research, strategy doc) / 3 in progress (certification, footage, model training) | ✅ PASS — reproduced | Actually ran: `python3 weekly_log_v1.py` — captured stdout confirms exactly this split. Item list is a direct transcription of the user's own kickoff message. Status wording changed from "pending" to "in progress" — same underlying fact, softer log-register phrasing (user asked to downplay, not hide, the not-yet-done items) | None — real captured output, matches the user's own facts verbatim |
| 4 | B06/B07 | `weekly_log_v2.py` adds a per-thread `standout` line (the first done/published item) above the same ordered entries | ✅ PASS — code-verifiable | Script in this folder; `standout = next(i for i in items if i["status"] in ("done","published"))`, printed before the unchanged per-item loop | None |
| 5 | B07 | Standout for writing = "Fashion Just Got a Data Brain"; standout for Loon Project = "Drone acquired" | ✅ PASS — reproduced | Actually ran: `python3 weekly_log_v2.py` — captured stdout confirms both highlight lines exactly | None — real captured output, not invented |
| 6 | B01/B08 | Article 1 paraphrase: AI reshapes fashion via demand forecasting, faster generative design, virtual try-on cutting returns; a luxury tension between AI supply-chain transparency and craftsmanship branding | ✅ PASS (paraphrase, no invented numbers) | Direct paraphrase of the user-supplied article summary; kept qualitative — no percentages or dates not supplied by the user | None |
| 7 | B01/B08 | Article 2 paraphrase: the open vs closed model performance gap "closing" this year, led in part by DeepSeek/Qwen/Llama/Mistral-class open models | ✅ PASS (paraphrase, no invented numbers) | Direct paraphrase of the user-supplied article summary. The specific 17.5-point-to-under-1 figure is NOT put on screen or read in narration — kept out to avoid a dated, unverified statistic (DOUBLE-CHECK LAW) | None |
| 8 | B04/B07/B08 | All 6 Loon Project items and both articles are shown in every checklist/log beat — nothing hidden or dropped | ✅ PASS — code-verifiable | Per this revision's explicit brief: keep all 8 real items visible, just stop leading with / dwelling on the "pending" count. `WEEK` dict in scenes.py and both scripts carries the full 8-item list unchanged from beat to beat | None — required by this revision |

**No fabricated statistics, no invented benchmark numbers, no item hidden
or dropped from the log — every claim in this reel is either directly
reproducible from the two scripts in this folder, a direct transcription
of what the user told this toolkit about their own week, or a qualitative
paraphrase of the user's own article summaries with no added numbers.**

**GATE F — ready to open for render.**
