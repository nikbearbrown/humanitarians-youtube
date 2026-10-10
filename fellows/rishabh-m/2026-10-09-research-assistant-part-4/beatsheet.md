# Design From Real Data — Beat Sheet

**Title:** Design From Real Data
**Slug:** research-assistant-part-4
**Stage:** AI Research Assistant — Stage 2A, metadata ingestion (Oct 5–9)
**Channel:** claude-hai · **Persona:** Rishabh · **Register:** Plain · **Voice:** Kokoro `af_sarah`
**Format:** ai-explainer (16:9 long cut) + purpose-authored 9:16 Short (its own beat sheet, never a crop)

Source: `personal/Documentation/Stage 2 - Data Pipeline.md` (Part 2A) and commits `511c15d`…`22f9c6b`. Both cuts render from `beat_sheet.json` at true 4K. Durations are Kokoro-measured (`actual_duration_s`, including the 1 s hold between beats), not estimates.

## 16:9 — long cut (18 beats, 5:37 / 336.7s, 3840×2160)

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | OPEN | 0:00 | 14.3s | ClaudeComposerAsk | Cold open — composer ask, answered |
| B01 | OPEN | 0:14 | 15.4s | BrutalistHesitantWriter | Executive summary — written and corrected on screen |
| B02 | I — The Goal | 0:30 | 17.4s | AgenticPatternDiagram | arXiv → metadata → Postgres; PDFs next |
| B03 | I — The Goal | 0:47 | 21.0s | ClaudeCodeFile | Never committed — the .gitignore line |
| B04 | II — Four Rules | 1:08 | 19.2s | AgenticPatternDiagram | Four rules for stage two |
| B05 | III — The Build | 1:27 | 16.3s | ClaudeCodeFile | The rate limit has a floor in config |
| B06 | III — The Build | 1:44 | 26.0s | AgenticPatternDiagram | What the real data showed → the decision it forced |
| B07 | III — The Build | 2:10 | 18.7s | ClaudeCodeFile | Skip the entry, raise on the feed |
| B08 | III — The Build | 2:28 | 20.5s | ClaudeCodeFile | One rate limiter, every request |
| B09 | III — The Build | 2:49 | 21.6s | AgenticPatternDiagram | Retry the temporary; fail fast on a bad request |
| B10 | III — The Build | 3:10 | 20.8s | ClaudeCodeFile | One real day — and the 2.79 s gap that wasn't |
| B11 | III — The Build | 3:31 | 24.0s | AgenticPatternDiagram | Migrations run once, before anything starts |
| B12 | III — The Build | 3:55 | 20.8s | ClaudeCodeFile | One upsert per day — atomic and safe to repeat |
| B13 | III — The Build | 4:16 | 19.4s | AgenticPatternDiagram | The first DAG — one row to 527 |
| B14 | IV — When Not To | 4:35 | 15.2s | AgenticPatternDiagram | Size it to the job |
| B15 | V — Verdict | 4:51 | 14.5s | ClaudeVerdictArtifact | Verdict artifact page — seven rules |
| B16 | V — Verdict | 5:05 | 25.7s | ClaudeComposerAsk | Handoff — the viewer's prompt |
| B17 | OUTRO | 5:31 | 5.6s | HaiTitleOutro | Title-restate outro |

## 9:16 — Short (9 beats, 1:23 / 83.0s, 2160×3840)

| # | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|
| S00 | 0:00 | 11.6s | ClaudeComposerAsk916 | composer ask; the answer lands |
| S01 | 0:12 | 8.5s | AgenticPatternDiagram916 | four rules; Real Data First lights |
| S02 | 0:20 | 7.3s | AgenticPatternDiagram916 | 3.0 s loads; 1.0 s is refused |
| S03 | 0:27 | 12.6s | AgenticPatternDiagram916 | observed → decision, two lanes; Strip The Version lights |
| S04 | 0:40 | 8.4s | AgenticPatternDiagram916 | three callers → one limiter → arXiv |
| S05 | 0:48 | 9.2s | AgenticPatternDiagram916 | run twice → still 243 |
| S06 | 0:57 | 8.0s | AgenticPatternDiagram916 | Postgres → migrate → API and Airflow |
| S07 | 1:05 | 7.3s | AgenticPatternDiagram916 | Airflow → same code → Postgres → 527 |
| S08 | 1:13 | 10.1s | HaiTitleOutro916 | title restates; watch next |
