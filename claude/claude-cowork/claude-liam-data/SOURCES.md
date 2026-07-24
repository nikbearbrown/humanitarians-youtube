# SOURCES — Claude, By the Numbers (Ch.7)

## Source document
- `books/anthropics/books/claude-cowork-plugins/chapters/ch07-data.txt`
  (from `claude-cowork-plugins.md`, Chapter 7 — *Claude Cowork Plugins*, rev. Spring 2026, "John Collins")

## Corrections applied — DOUBLE-CHECK / datable strip (see book-level FACTCHECK.md)

### Transcription artifacts fixed (speech-to-text, not author errors)
| In source | On screen / in narration | Why |
|---|---|---|
| "Cloud reads both files" / "Cloud produces" / "Cloud examines" / "Cloud handles" / "Cloud reads the spreadsheet" (throughout) | "Claude …" | Pervasive speech-to-text artifact ("Cloud"→"Claude"). |
| "unglamerous" | "unglamorous" | Spelling. |
| "mix panel" / "post-hog" | Mixpanel / PostHog | Standing book-level fix. **These strings do not occur in Ch.7's text** — logged here because the correction is inherited book-wide; no on-screen use in this reel regardless (named analytics tools would be datable). |
| "VillaCup syntax" | "VLOOKUP syntax" | Transcription artifact. |
| "sole apreneurs" / "solar prerner" / "solar operators" | "solo operators" | Transcription artifact. |
| "you may be sorked by date" | "sorted by date" | Transcription artifact (used only as narration paraphrase). |
| "how pivoted. Ables work" | "how pivot tables work" | Transcription artifact. |
| "Disgusting values" | "impossible values (negative sales)" | Transcription artifact; disambiguated by the source's own later "negative values for sales." |
| "Realize my client data" | "Analyze my client data" | Transcription artifact (used in B18 prompt). |
| "Itterate" | "Iterate" | Spelling (B24). |
| "This is in a small shift" | "It's a small shift" (paraphrased) | Transcription artifact. |
| "What he does?" | "What it does" | Transcription artifact. |

### Datable specifics stripped or reframed (DOUBLE-CHECK LAW, sharpened for a long-lived episode)
| In source | Treatment in reel | Why |
|---|---|---|
| Direct DB connectors named: PostgreSQL, BigQuery, Snowflake, "and others" | Compressed to the generic mechanism ("if your data lives in a proper database you connect it; if it lives in spreadsheets — like most readers — you just point Claude at the files"). The three products are **never named** on screen or in narration. | Vendor lists date the episode; the mechanism does not. |
| Export sources: Stripe, QuickBooks, invoicing tool | Genericized to "your payment processor," "your invoicing tool." Fleeting at most, never a beat's subject. | Named third-party tools are datable; fine as examples, never as the subject. |
| "three clients account for 60% of my revenue" | Kept ONLY as a clearly-framed **illustrative example answer** ("say, three clients are sixty percent of revenue…", B07). | Percentages are hypothetical examples, not empirical claims — must stay framed as examples, never world-facts. |
| "one client represents 40% of your income" | Kept ONLY as a framed illustration ("if a single client is, **say**, forty percent…", B19). | Same. |
| Any plugin count / price / platform list | **Absent** — none stated anywhere. | DOUBLE-CHECK LAW: no counts, prices, or platform lists. |

## Claims carried (conceptual spine, verified against source + book FACTCHECK.md)
- The plugin answers plain-language questions about your data and returns a sentence, not a formula or raw table. ✓
- It does data exploration (describes structure, flags outliers, suggests questions), cleaning (and reports what it changed), visualization, and comparison/benchmarking. ✓
- Files already in your Cowork folders (spreadsheets, CSVs, exports) work immediately; direct database connections require credentials during customization. ✓ (stated as mechanism, vendors stripped)
- Revenue-concentration risk is a core solo-operator use; the analysis is only as trustworthy as the data and assumptions — human keeps the judgment. ✓ (matches book FACTCHECK §1 claim 9: percentages illustrative)

## Seeds / determinism
- Manim + Remotion scenes are pure functions of the audio clock; log any RNG seed here at render time.
- No AI-generated real people in this reel; all 6 vox stills (B03, B11, B15, B16, B20, B23) are Tier 1 illustrative — no rights escalation, no named subjects.

## Credits
- Narration: Liam (in for Bear), Kokoro `am_onyx`. Channel: @NikBearBrown.
