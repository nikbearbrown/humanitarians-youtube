# SHOTLIST.md — one-run-still-open (GATE F)

Per-beat shots. No stock stand-ins: live app captures, computed evidence, or diagrams that enact a sourced claim.

| Beat | Shot type | Scene / pattern | On-screen artifact |
|---|---|---|---|
| B00 | REMOTION | `ClaudeComposerAsk` | COLD OPEN LAW (CLAUDE.md SS9) with the required intro line and AI-narration disclosure (SS8) |
| B01 | GRAPHIC | `B01_FourPartsOfAGate` | Framework before example |
| B02 | GRAPHIC | `B02_Trigger` | Matrix rows sorted by status (validation/gate.py): only the MISMATCH row gets a gate icon; an UNCORROBORATED row gets a review marker; a pre-gate stored run is tagged NOT |
| B03 | GRAPHIC | `B03_DecisionForm` | HOLD: screen-recording frames of run ec1a3b44's gate panel expanding in place under the verdict with the matrix still visible (DecisionGate.tsx) |
| B04 | GRAPHIC | `B04_SmallPrint` | Zoom on the name-field hint 'Recorded as entered; not verified.' Then a real 422 refusal body from POST /api/runs/{id}/decisions (capture from the route test or a temp DB |
| B05 | GRAPHIC | `B05_Supersede` | Decision stack: card 1, card 2 lands, card 1 dims and is tagged 'superseded, still on record'; chip 'UPDATE / DELETE -> BLOCKED BY A DATABASE TRIGGER'. |
| B06 | GRAPHIC | `B06_InvestorView` | Side-by-side, held >=3 s: auditor view '1998 / 2 years / 1996' vs investor view 'Withheld / / Withheld' + banner 'Pending human review' |
| B07 | GRAPHIC | `B07_StillOpen` | HOLD: capture of run ec1a3b44's gate, awaiting decision; 'decisions recorded: 0' from the evidence. |
| B08 | GRAPHIC | `B08_HardRules` | MATH-TYPESETTING (MathTex): EPS_basic >= EPS_diluted; FCF = OCF - CapEx; Assets = Liabilities + Equity (2% tolerance note) |
| B09 | GRAPHIC | `B09_ClaimVsSource` | Side-by-side, held >=3 s: 'given: revenue $82.9B' / 'wrote: $828.9B', handnote '10x' |
| B10 | GRAPHIC | `B10_SoftRules` | GOOGL real values: net income $112.2B vs operating income $40.77B, shown for both agent B and the filing itself, with an ochre callout 'Unusual, worth a look' (never red) |
| B11 | GRAPHIC | `B11_FilingAndTimeout` | Filing check passes (assets = liabilities + equity, $383.3B); then 'model: no reply to a 5-token request within 60 s' and an 'OPEN ISSUE · HIGH' card: no timeout on model |
| B12 | GRAPHIC | `B12_SourceExcerpt` | SHOW recorded output (EXECUTABLE-EVIDENCE): datasources.filings.find_in_document run on the real trimmed Apple 10-Q (accn 0000320193-26-000020): row 'Total net sales', co |
| B13 | GRAPHIC | `B13_LiveLanes` | Diagram of a real captured event stream (AAPL): one shared SEC fetch drawn once above two tinted agent lanes; event counts from the stream (assets/evidence/out/B13_stream |
| B14 | GRAPHIC | `B14_Assessment` | [verify] Two assessment strips, Bull (blue) and Bear (orange) |
| B15 | GRAPHIC | `B15_DivergenceAndConsensus` | [verify] Three bins DATA / ASSUMPTION / WEIGHTING; consensus rule as 'grades match AND no hard rule failed -> consensus' |
| B16 | GRAPHIC | `B16_AnswerFirst` | [verify] HOLD: full review page scroll (summary + checklist, gate, matrix, agents, collapsed trace), then 'Download review' opening a Markdown file |
| B17 | GRAPHIC | `B17_TrueNow` | Honest-ledger list one: what the work now does. |
| B18 | GRAPHIC | `B18_StillNotTrue` | OUTRO-LAW chapter close: the work's limitations, held uncleared, including the trace leak. |
| B19 | GRAPHIC | `B19_EndCardReprise` | OUTRO-LAW close: reprise '1998 / 2 years / 1996 · AWAITING DECISION', the four gate boxes as the takeaway, then 6 END CARD bullets about the work. |
| B20 | REMOTION | `ClaudeTitleOutro` | OUTRO LAW: exact title restate, handle, one subline |
