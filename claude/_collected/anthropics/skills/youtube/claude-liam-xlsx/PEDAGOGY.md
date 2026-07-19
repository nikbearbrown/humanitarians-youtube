# PEDAGOGY — claude-liam-xlsx

Skill: xlsx
Register: Teardown (skill-teardown modifier)
Audience: Claude / developers

## What the skill does
Spreadsheet creation, editing, and analysis for .xlsx/.xlsm/.csv/.tsv files. Two tools: pandas (analysis/bulk) and openpyxl (formulas/formatting). Mandatory recalc.py step after formula writes. Financial model color coding and number format standards. ZERO formula errors required.

## Learning objective
Viewer understands: (1) pandas vs openpyxl tool decision, (2) the 6-step workflow including mandatory scripts/recalc.py, (3) never hardcode — always write Excel formulas, (4) financial model color coding and number format standards.

## Teardown structure
- B00: cold open — xlsx trigger, two tools, formula mandate
- B01: anatomy — pandas vs openpyxl decision + 6-step workflow
- B02: design — financial model color/number standards + formula-not-hardcode rule
- B05: gets-right / bites teardown
- BVDT: verdict
- BHTF: handoff
- BOUT: outro

## Key concepts
- Trigger: primary deliverable IS a spreadsheet file
- pandas: analysis, bulk ops, simple export
- openpyxl: formulas, formatting, Excel features
- MANDATORY: scripts/recalc.py after any formula write (LibreOffice recalc + error scan)
- Formula mandate: never calculate in Python and hardcode; write =SUM(B2:B9) not a Python integer
- Color coding: blue=hardcoded, black=formula, green=cross-sheet, red=external, yellow bg=assumption

## VERDICT: PASS
No paid spend required. Free Kokoro pipeline. Skill content is teachable as a standalone unit.
