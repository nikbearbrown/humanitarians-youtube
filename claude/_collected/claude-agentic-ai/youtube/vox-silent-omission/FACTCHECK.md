# FACTCHECK — vox-silent-omission

Source chapter: `claude-agentic-ai/chapters/09-failure-modes-of-agentic-work.md`

---

## Claims audit

| Claim | Verdict | Source / note |
|---|---|---|
| "The agent summarized what it could reach and presented the result as though nothing was missing" | ✓ | Chapter 09 opening scene, verbatim mechanism |
| Agents produce output from successful operations; they do not always surface what they could not reach, could not parse, or chose to skip | ✓ | Chapter 09, "Silent Omission" section: "Agents produce output from successful operations. They do not always surface what they could not reach, could not parse, or chose to skip." |
| Tool call failures may be logged internally but not appear in visible output | ✓ | Chapter 09, "Silent Omission" section |
| The recognition sign: the processed count does not match the expected count | ✓ | Chapter 09, "Silent Omission" section |
| Prevention: require the agent to report how many items were in scope, how many were processed, and how many failed or were skipped | ✓ | Chapter 09, "Silent Omission" section |
| The project manager example (23 files, 3 unread in subfolder, sent to leadership) | ✓ | Chapter 09 opening scene — verbatim |
| A crash announces itself; a silent omission does not | ✓ | Derived from chapter mechanism; editorially framed but accurately summarizes the distinction |
| Maya example: 12 PDFs, 9 read, 3 scanned/unreadable, Q4 revision missed | ILLUSTRATIVE | Candidate card example seed — plausible, not from chapter. Labeled illustrative. |
| "Twenty-three files processed" in B07 | ILLUSTRATIVE | Concrete count illustrating the mechanism; not from chapter verbatim. Labeled illustrative. |

---

## Exclusions confirmed

- No taxonomy of all eight failure modes — only silent omission is discussed. Pass.
- No prompt injection discussion. Pass.
- No hallucination probability formalism (no Farquhar et al. semantic entropy). Pass.

---

## Terms table

| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| silent omission | B02 (shown), B05 (named) | B01 cold open establishes the problem |
| completion report | B03 (THE QUESTION) | B02 shows a gap the report missed |
| operation | B04 | B03 question beat sets up why the report is built per-operation |
| inventory check | B09 (THE PRACTICE) | B07–B08 establish that count mismatch is the signal |
