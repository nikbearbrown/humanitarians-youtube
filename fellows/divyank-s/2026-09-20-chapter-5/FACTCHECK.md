# FACTCHECK.md — Claude, Tested.

Source: `ai1-cli/chapters/05-generate-the-assessments-the-blueprint-promised.md`,
read in full. Every claim below checked verbatim/near-verbatim against that
file, including its own footnoted citations.

| Beat | Claim | Source line | Verdict |
|---|---|---|---|
| A1-2 | Quizzes exploit the testing effect; flashcards exploit the spacing effect; exercises push past recall toward application | line 11-13 | OK — near-verbatim |
| A1-3 | Roediger & Karpicke, 2006: retrieval beat re-reading on a one-week delayed test, ~61% vs. ~40% | line 11 + footnote 1 (Roediger, H.L. & Karpicke, J.D. (2006), "Test-Enhanced Learning," *Psychological Science* 17(3)) | OK — verbatim figures and citation from the chapter's own footnote; the chapter itself flags "confirm the exact experiment when quoting the numbers," repeated here as the source's own caveat, not suppressed |
| A1-4/A1-5 | The spacing effect traces to Ebbinghaus, 1885; Anki's SM-2 algorithm (Woźniak, 1987) is a spacing-effect machine | line 12 + footnotes 2, 3 | OK — verbatim citations |
| A1-6 | "The book eats its own dogfood" — every question grounds in the chapter text | line 15 | OK — verbatim phrase |
| A2-2 | Bloom's taxonomy, Anderson & Krathwohl's 2001 revision: Remember, Understand, Apply, Analyze, Evaluate, Create | line 19 + footnote 4 (Krathwohl, D.R. (2002), "A Revision of Bloom's Taxonomy," *Theory Into Practice*) | OK — verbatim six levels and citation |
| A2-3/A2-4 | "The failure you're hunting is a question that tests a lower level than its outcome demands... It looks fine. It passes for an assessment. And it measures nothing the chapter promised to build." | line 19 | OK — verbatim |
| A3-1 through A3-6 | The real worked example: outcome "the reader can apply the build pipeline to produce an EPUB from a changed chapter"; generated question "What command builds the book?"; the question tests Remember, the outcome demands Apply; the fixed question ("You changed a sentence in chapters/03-*.md but the rebuilt EPUB still shows the old text. Which is the most likely cause, and what do you check first?") | lines 43-52 | OK — **verbatim quotes**, copied exactly from the chapter's own worked example and its "Bear's Copywriting Book" section (lines 69-75), which confirms this is a real, live agent-mode generation, not a fabricated illustration |
| A3-6 | "Generators drift toward Remember because recall questions are the easiest to write" | line 31 | OK — verbatim |
| A4-2 | The four failure symptoms (every question answerable from memory; flashcards feel random; batched then found systemic problems; audit found nothing) | lines 56-61 (the "What can go wrong" table) | OK — verbatim/near-verbatim |
| A4-3 | "Always audit a question against the outcome it claims to serve" | line 61 | OK — verbatim |
| A4-6 | Bridge to Chapter 6: exporting the book, quizzes included, into a course an LMS can import | line 65 | OK — near-verbatim |

## Honesty note on the worked example

Per the chapter's own draft note (line 75), the single-question
generation-and-audit is explicitly real and live, while a full batch run
of `build-quizzes.py` across every chapter was NOT executed in the
chapter's own drafting session. This reel presents the worked example
exactly as the chapter frames it — a real, single-item demonstration of
the failure mode — and does not claim a full quiz suite was generated or
audited.

## Corrections applied

None — no fabrication or drift found; the source is internally consistent
and its own citations are used verbatim.
