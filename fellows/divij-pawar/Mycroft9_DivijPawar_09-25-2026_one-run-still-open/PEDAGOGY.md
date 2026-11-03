# PEDAGOGY.md — one-run-still-open (Mycroft 9; audit-layer update, part 2 of 2)

**GATE P VERDICT: PASS** — Divij Pawar, 2026-09-26 (v4 narration re-approved in chat).

**Corrections after sign-off (2026-09-27), awaiting his review.** Divij confirmed the
verification layer is complete through B6/U9 and directed the render. Checking the RUN_LOG
against the narration showed seven beats describing an earlier state. They were corrected to
match the record, voiced again with the approved voice (am_onyx), and rendered. The list is under
"Corrections after sign-off" below. The signed verdict stands for the teaching arc; **these seven
beats' wording has not been separately re-read by him.** Watch them before publishing.

**Voice gate:** `metadata.approvals.voice` is approved (am_onyx, Divij Pawar, 2026-09-27, in chat).

**Files:**
- **Source script:** `one-run-still-open.md`. Its Beats section is generated from `beat_sheet.json`.
- **Narration:** `../Mycroft8_DivijPawar_09-18-2026_the-rule-that-lost/narration_v4.py` and
  `visual_v4.py`, applied by `build_sheets.py` in that folder.
- **Scenes:** `scenes.py` (16:9) and `short/scenes.py` (native 9:16).
- **Evidence:** `assets/` (see `assets/MANIFEST.md`).
- **Paperwork (GATE F):** `FACTCHECK.md`, which passes `factcheck_check.py`.

**Final files (rendered 2026-09-27):**

| File | Size | Length | Visual QC (Gate V) | Captions |
|---|---|---|---|---|
| `one-run-still-open.mp4` | 3840×2160 | 6:54 | 42 frames, 0 blocker, 0 major | mov_text, 229 cues, SRT check PASS |
| `short/one-run-still-open-short.mp4` | 2160×3840 | 6:54 | 42 frames, 0 blocker, 0 major | same |

---

## Where this sits

This reel continues directly from Mycroft 8 ("The Rule That Lost"). Part one made the comparison
strict; this part is about what happens when that comparison finds a real disagreement, and it
covers the verification layer as built through the last roadmap phase (B6/U9).

It is about the work, not the working (v4 direction). There are no callbacks to earlier videos,
commits, test counts, logs or roadmap talk, on screen or in the narration.

## Beat breakdown — 21 beats (B00–B20), real audio durations

The structure follows `CLAUDE.md` §9:
- **B00:** the `ClaudeComposerAsk` cold open, with the required intro line and the AI-narration
  disclosure.
- **B01:** the framework, a gate's four parts.
- **B02–B16:** one idea per beat.
- **B17–B18:** the honest ledger.
- **B19:** the end-card reprise, which carries the takeaway.
- **B20:** a stat-free `ClaudeTitleOutro`.
- **No "Your Turn" beat.**

| Beat | Act | Words | Audio | Starts |
|---|---|---|---|---|
| B00 | cold open | 85 | 25.6s | 0:00 |
| B01 | chapter 1 - recap and the four parts of a gate | 85 | 24.9s | 0:25 |
| B02 | chapter 2a - trigger | 81 | 22.8s | 0:50 |
| B03 | chapter 2b - the decision | 82 | 21.4s | 1:13 |
| B04 | chapter 2c - identity and refusals | 69 | 19.9s | 1:34 |
| B05 | chapter 2d - the record | 22 | 7.4s | 1:54 |
| B06 | chapter 3a - what an investor sees | 103 | 30.2s | 2:01 |
| B07 | chapter 3b - the gate nobody has cleared | 30 | 8.3s | 2:32 |
| B08 | chapter 4a - rules that stop a run | 82 | 25.3s | 2:40 |
| B09 | chapter 4b - claim versus source | 73 | 19.8s | 3:05 |
| B10 | chapter 4c - rules that only inform | 79 | 22.6s | 3:25 |
| B11 | chapter 4d - the filing, and an honest gap | 65 | 20.1s | 3:48 |
| B12 | chapter 5a - show me where it says that | 81 | 22.7s | 4:08 |
| B13 | chapter 5b - watching it run | 48 | 14.6s | 4:30 |
| B14 | chapter 6a - from figures to a grade | 75 | 20.8s | 4:45 |
| B15 | chapter 6b - why grades differ, and when to agree | 90 | 25.7s | 5:06 |
| B16 | chapter 6c - answer first | 53 | 16.2s | 5:31 |
| B17 | chapter 7a - the honest ledger, works now | 65 | 20.6s | 5:48 |
| B18 | chapter 7b - the honest ledger, still doesn't | 60 | 18.4s | 6:08 |
| B19 | close - the smallest true claim | 80 | 20.2s | 6:27 |
| B20 | outro | 13 | 5.8s | 6:47 |
| **Total** | | **1,421** | **413.3s (6:53)** | |

This is inside the 6–8 minute target. The compiled masters run 6:54 (413.5 s).

## Teaching arc

| Beat | What the viewer walks away holding |
|---|---|
| B00 | The system stopped instead of picking between 1998 and 1996, and it is waiting for a person. |
| B01 | A gate needs four parts: trigger, stop, a named decider with a reason, and a record. Without all four it's only a warning. |
| B02 | The trigger is narrow and testable: only a two-sided disagreement gates, and old runs are never gated retroactively. |
| B03–B05 | The decision ritual: five outcomes, a reason of at least 20 characters, a typed name, refusals explained in words, supersede-not-edit. |
| B06 | **Falsifiability:** the investor view hid the values, but a search result in the trace still showed "1998". It was found, fixed and verified; after the fix neither year appears. Withholding still depends on read access. |
| B07 | Nobody has recorded a decision on that run: the gate is working as designed. |
| B08–B10 | Hard accounting rules gate; claim-vs-source "would have caught" a 10× slip; soft rules inform (a real Google one-off gain). |
| B11 | The filing gets the same checks. Plus an operational gap: model calls have no timeout. |
| B12 | Figures are located in the real filing (24 of 24, all equal), and every figure in the review has a Source button. |
| B13 | Live lanes: every indicator is a real server event. |
| B14 | A second call reads each finished answer and extracts a grade, labelled model judgment, with ungrounded quotes dropped. |
| B15 | Why grades differ (data / assumption / weighting); consensus only when grade and direction agree with no hard failure; otherwise a person sets the grade. |
| B16 | The review reads answer first, and every review exports as a plain document. |
| B17–B18 | What works now, and what still doesn't, held uncleared. |
| B19 | Takeaway: give one warning a trigger, a stop, a person and a record, and check it can't clear itself. |

## Corrections after sign-off (2026-09-27)

Each was checked against the RUN_LOG and the code before being voiced. See `SOURCES.md` for the
evidence behind each row.

| Beat | Before | Now | Why |
|---|---|---|---|
| B06 | a live hole: the trace still leaks "1998" | found, fixed and verified: after the fix the investor read has neither year | RUN_LOG 2026-09-26 correction + verification entries |
| B12 | the click-through view isn't built | every figure in the review has a Source button | U6 built (RUN_LOG 2026-09-26) |
| B14 | agents end with a structured assessment | a second call to the same model extracts it from the finished answer; ungrounded quotes are dropped; a failure is recorded and the run continues | B4 reverted as the default; option 1 extraction built (RUN_LOG 2026-09-26) |
| B15 | consensus when grades match | consensus when grade **and** direction agree; the reviewer accepts a grade or sets it; investors see no grade until then | B5/U8 (RUN_LOG 2026-09-26) |
| B17 | mismatches gate | a mismatch, a failed hard check or a grade split stops the run; investors get no search results either; exports exist | gate policy v3; trace fix; B6 |
| B18 | lists the trace leak and "no live gated check yet" | both removed (fixed, and NVDA `9b1a9e0e` did gate); adds "the grade is the same model judging itself" | RUN_LOG B5/U8 open issues |
| B19 | the machine fetches, reads, compares and checks | adds "and grades" | B5/U8 |

The visuals changed with them. B14–B16 lost their "ILLUSTRATIVE · NOT BUILT YET" chips and now
show real captures of run `8ecb0922` (the grades panel, the grade decision item) and its recorded
Markdown export.

## PROOF rubric self-check

This is scored from the rendered frames' contact sheets, not the final files. Re-score from
`_qc/` frames before submission.

| Criterion | Where | Note |
|---|---|---|
| Framework before examples | B01 | Four boxes, stated before any example |
| Reusable rubric | Four-part gate, plus "can it clear itself?" | B01, B19 |
| Worked example walked live | B03/B04 on the real run `ec1a3b44`; refusals are the server's own text | |
| Falsifiability | **B06** (found, fixed, verified), B09 ("would have", not "did"), B18 | |
| Active task | B19 end card | **Deviation (§9):** Mycroft reels have no scaffolded prompt beat |
| Friction | B00/B07: the video never says which year is right, and nobody has decided | |

**Production gate:**
- **Gate V:** clean on both masters.
- **Side by side:** B06 (auditor | investor) and B09 (given | wrote) are held for 2 seconds or more.
- **Sources on screen:** every claim beat has a source line or a real capture.

## Register & tone

- **Voice:** calm and deliberate; the close is quiet.
- **Narration style (v3/v4):** long, connected sentences with no hooks. Re-voiced beats should be
  checked by ear for rushed commas.
- **Neutrality:** the narration never says which Pokémon year is right.

## Known deviations

1. **No "Your Turn" beat** (§9).
2. **Toolkit gaps:**
   - **Captions:** the toolkit no longer ships `make_srt.py`, so captions are built by
     `make_captions.py` in this folder from `mp3/words.json` and the compiled timeline.
   - **Timeouts:** the model-call timeout is still missing in the verification layer. The
     narration says so (B11, B18).
3. **Portrait layouts:** the 9:16 scenes are native re-layouts (`short/scenes.py`). The small
   four-box corner chip is dropped there, and three scenes (B05–B07) scale their content up to
   pass Gate V's fill minimum.

## What a human reviewer should check before publishing

- [ ] **Watch the seven corrected beats** (B06, B12, B14, B15, B17, B18, B19) in both files.
- [ ] **B14 wording:** "a second call to the same model reads that answer and extracts a grade".
  Confirm this describes the extraction the way you want it presented.
- [ ] **Run `ec1a3b44`** is still AWAITING_DECISION (0 decisions when rendered). If you record a
  decision before publishing, B00, B07 and B19 no longer hold.
- [ ] **Re-voiced beats:** listen for rushed long sentences (B06 and B15 are the longest).
- [ ] **PROOF self-review:** score it from real frames and log it in `PROOF-REVIEW.md` at the reel
  root (not `_qc/`).
