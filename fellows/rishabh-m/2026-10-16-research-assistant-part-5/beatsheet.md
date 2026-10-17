# The Queue Is A Query — Beat Sheet

**Title:** The Queue Is A Query
**Slug:** research-assistant-part-5
**Stage:** AI Research Assistant — Stage 2B, PDF processing (Oct 12–16)
**Channel:** claude-hai · **Persona:** Rishabh · **Register:** Plain · **Voice:** Kokoro `af_sarah`
**Format:** ai-explainer (16:9 long cut) + purpose-authored 9:16 Short (its own beat sheet, never a crop)

Source: `personal/Documentation/Stage 2 - Data Pipeline.md` (Part 2B) and commits `f24bfa8`…`10d074b`. Both cuts render from `beat_sheet.json` at true 4K. Durations are Kokoro-measured (`actual_duration_s`, including the 1 s hold between beats), not estimates.

## 16:9 — long cut (17 beats, 4:51 / 290.9s, 3840×2160)

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | OPEN | 0:00 | 14.6s | ClaudeComposerAsk | Cold open — composer ask, answered |
| B01 | OPEN | 0:15 | 14.2s | BrutalistHesitantWriter | Executive summary — written and corrected on screen |
| B02 | I — The Goal | 0:29 | 12.0s | AgenticPatternDiagram | pending → download → Docling → sections |
| B03 | II — Download | 0:41 | 18.4s | ClaudeCodeFile | A 200 is not a PDF until the bytes say so |
| B04 | II — Download | 0:59 | 20.4s | ClaudeCodeFile | Temp file, then one atomic rename |
| B05 | III — Parse | 1:20 | 20.1s | AgenticPatternDiagram | Docling only in Airflow; offline flag |
| B06 | III — Parse | 1:40 | 19.8s | ClaudeCodeFile | Reading order, tables included |
| B07 | IV — Status | 1:59 | 22.4s | AgenticPatternDiagram | pending → parsed / failed / skipped |
| B08 | IV — Status | 2:22 | 17.5s | AgenticPatternDiagram | Two migration gotchas |
| B09 | V — One Paper At A Time | 2:39 | 23.2s | ClaudeCodeFile | One paper fails alone; all failing fails the run |
| B10 | V — One Paper At A Time | 3:02 | 17.1s | ClaudeCodeFile | A new version resets the status |
| B11 | VI — Proof | 3:20 | 19.1s | AgenticPatternDiagram | Happy path, and the failure on purpose |
| B12 | VI — Proof | 3:39 | 15.3s | AgenticPatternDiagram | ~250 papers × ~30–45 s = ~2–3 h of CPU |
| B13 | VII — When Not To | 3:54 | 13.3s | AgenticPatternDiagram | Size it to the job |
| B14 | VIII — Verdict | 4:07 | 12.5s | ClaudeVerdictArtifact | Verdict artifact page — seven rules |
| B15 | VIII — Verdict | 4:20 | 24.2s | ClaudeComposerAsk | Handoff — the viewer's prompt |
| B16 | OUTRO | 4:44 | 6.6s | HaiTitleOutro | Title-restate outro |

## 9:16 — Short (9 beats, 1:20 / 80.4s, 2160×3840)

| # | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|
| S00 | 0:00 | 11.6s | ClaudeComposerAsk916 | composer ask; the answer lands |
| S01 | 0:12 | 5.7s | AgenticPatternDiagram916 | pending → download → Docling → Postgres |
| S02 | 0:17 | 9.2s | AgenticPatternDiagram916 | 200 + %PDF- cached; 200 + HTML rejected |
| S03 | 0:27 | 7.5s | AgenticPatternDiagram916 | temp file → one rename → the PDF |
| S04 | 0:34 | 10.3s | AgenticPatternDiagram916 | Airflow image → offline flag → loud failure |
| S05 | 0:44 | 8.1s | AgenticPatternDiagram916 | pending → three outcomes; failed lights |
| S06 | 0:53 | 9.2s | AgenticPatternDiagram916 | one fails → recorded; all fail → task raises |
| S07 | 1:02 | 8.6s | AgenticPatternDiagram916 | missing PDF → run failed |
| S08 | 1:10 | 10.0s | HaiTitleOutro916 | title restates; watch next |
