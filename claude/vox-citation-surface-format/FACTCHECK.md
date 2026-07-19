# FACTCHECK — vox-citation-surface-format

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | 12 citations: 4 real, 3 real journal/wrong finding, 5 nonexistent — all identical format | illustrative | Adapted from Candidate 09 card example seed (5 citations → 12 for specificity). Illustrative. Consistent with Walters & Wilder 2023 and Alkaissi & McFarlane 2023 findings cited in Chapter 7. |
| B02 | Marco scenario: 5 papers on green roof cooling, 2 real, 1 reversed finding, 2 hallucinated | illustrative | Adapted from Chapter 7 example seed: "He checks: two exist and say what Claude claims. One exists but says the opposite. Two have real author names but the papers don't exist." |
| B03 | Format gives no signal about which citations are real | ✓ | Chapter 7 opening: "The citation looks right. Author, year, journal name, volume, page range... The source does not exist." |
| B04 | Claude generates text with statistical shape of citations — does not retrieve from database | ✓ | Chapter 7: "the model does not retrieve sources from a database. It generates text that has the statistical shape of scholarly writing, including citations." |
| B05 | Hallucinated and real citations use same pattern; no internal flag | ✓ | Chapter 7: "A citation from Claude is a hypothesis about what a relevant source might look like. Some of those hypotheses correspond to real publications. Some do not. The model cannot reliably tell the difference." |
| B06 | Fluency is not accuracy; voice of scholarship does not prove substance | ✓ | Chapter 7 verbatim: "The voice of scholarship does not prove the substance of scholarship." |
| B07 | Lead vs. evidence distinction | ✓ | Chapter 7: "A lead is a direction worth investigating... Evidence is a verified source... Claude cannot provide evidence directly — it can only provide leads." |
| B08 | Leads-first prompt: search terms + framework names, no citations | ✓ | Chapter 7 AFTER prompt: "Do not cite sources — I will find them myself using these terms." + "Name the frameworks without claiming specific citations." |
| B09 | Richer output = more important to verify; fluency makes check feel unnecessary | ✓ | Chapter 7: "The single most common error in Claude-assisted research is treating a lead as evidence. This happens because Claude's fluency makes its output feel authoritative." |
| B10 | 12 citations verified: 4 real/match, 3 real/wrong, 5 nonexistent | illustrative | Illustrative. Consistent with Chapter 7 verification checklist and cited literature. |
| B11 | Leads-first workflow: search terms → database → provide abstracts → matrix from provided only | ✓ | Chapter 7 leads-first prompt + summarization/matrix patterns: "When a prompt asks Claude to summarize a source, the source must have been provided by you." |
| B12 | Two rules: no citation requests; flag what is not in provided text | ✓ | Chapter 7: search term expansion prompts + "not stated in excerpt" instruction |
| B13 | Citation = hypothesis, not source; verify before citing | ✓ | Chapter 7 core mechanism |

## Exclusions
- No semantic entropy or calibration formalism: CONFIRMED absent
- No retrieval-augmented generation as solution: CONFIRMED absent
- No model-version comparison on citation accuracy: CONFIRMED absent
