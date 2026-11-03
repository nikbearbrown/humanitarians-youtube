# assets/ — one-run-still-open

Real evidence only. There are two kinds of file here:

- **Computed outputs** (`evidence/out/*.json`). `evidence/m9_evidence.py` produced them from the live verification layer, read-only.
- **App captures** (`*.png`). `evidence/capture_app.mjs` took them from the locally running
  `/app` with headless Chrome at 2× scale, clicking only view controls.

Per `brutalist.art/docs/EXECUTABLE-EVIDENCE.md`, nothing here is mocked. Show computed
values as recorded output, and show captures as the real app.

**To regenerate** (the server must be running on :8000 for the captures):

```bash
python assets/evidence/m9_evidence.py
node assets/evidence/capture_app.mjs
```

## Files

| File | Beat | Kind | What it is | SHA-256 (first 16) |
|---|---|---|---|---|
| `B03_gate_open_1280.png` | B03-B04 | HOLD | App capture, run ec1a3b44: gate form opened in place (nothing submitted); shows 'Recorded as entered; not verified.' | `74e55ecebda32022` |
| `B06_auditor_1280.png` | B06 | HOLD | App capture, auditor scope: 1998 | 2 years | 1996 | `90c78b03f6ee3898` |
| `B06_investor_1280.png` | B06 | HOLD | App capture, investor scope: values and conclusions 'Withheld' | `887e0f495ba22455` |
| `B06_investor_trace_leak_1280.png` | B06, B18 | HOLD | App capture, investor scope: the trace search result that still shows '| 1998 |' (outlined) | `988d0520b08f0837` |
| `B07_gate_closed_1280.png` | B07 | HOLD | App capture: the gate section, awaiting decision, no decision recorded | `d65f840faa0ad21e` |
| `evidence/capture_app.mjs` | B03-B07 | code | Headless Chrome capture of /app (view controls only) | `2aa86f2b6a72df7b` |
| `evidence/m9_evidence.py` | all | code | Evidence script (read-only; records no decision) | `5344907ab1d88b4f` |
| `evidence/out/B00_B07_gated_run_now.json` | B00, B07 | data | ec1a3b44: AWAITING_DECISION, 0 decisions | `2ca4df645cb68783` |
| `evidence/out/B02_trigger.json` | B02 | data | MISMATCH gates; UNCORROBORATED run is NO_DECISION_NEEDED; pre-gate NOT_GATED | `f299b7951e1bc24b` |
| `evidence/out/B03_B04_decision_rules.json` | B03-B04 | data | validate_decision refusals, verbatim | `7dc6f65f88d7d416` |
| `evidence/out/B06_investor_view.json` | B06 | data | Live + fixture investor reads: '1996' 0, '1998' 1 (in the trace) | `13253114946f65c9` |
| `evidence/out/B08_B11_checks.json` | B08-B11 | data | AAPL checks; GOOGL e592660c heuristic; MSFT ec40e81b $828,860,000,000 | `72ed5ffff213c92e` |
| `evidence/out/B12_filing_excerpt.json` | B12 | data | find_in_document on the real Apple 10-Q: row, column, value as filed | `3f641df300c294a1` |
| `evidence/out/B13_stream_events.json` | B13 | data | Event counts and steps by phase from the captured stream | `a5132100642be039` |
| `evidence/out/B18_ledger.json` | B11, B18 | data | Ledger entries: audit-criticals, ollama-hangs, filing-excerpt-coverage, gate identity | `83175f237f272fd5` |
| `evidence/out/capture_log.txt` | B03-B07 | log | What capture_app.mjs clicked and clipped, with timestamp | `9a985bcc81cc0a7d` |
| `evidence/out/run_env.json` | all | env | Python/platform, checkout HEAD + dirty count, input SHA-256 | `e43440b0c430ea30` |

## Still to capture or build

| Beat | Asset | How |
|---|---|---|
| B13 | assets/B13_lanes.mp4 | Screen-record a real /app#/new compare run (the in-app browser can't save video; record with OS tools), or drive the lanes animation from the stream fixture. |
| B14-B16 | Assessment strips, divergence bins, review scroll, Markdown export | Blocked: B4-B6/U5-U9 are not in the checkout yet. Capture once logged; until then use ILLUSTRATIVE-labelled graphics or cut to the coda. |
| B08 | MathTex rules | Typeset in the scene. |
| B00 | Status on recording day | Re-run m9_evidence.py; ec1a3b44 must still read AWAITING_DECISION. |
