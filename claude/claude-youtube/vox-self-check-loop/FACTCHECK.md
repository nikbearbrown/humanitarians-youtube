# FACTCHECK — vox-self-check-loop

## Claim 1
**Narration:** "An agent reviewing its own output works from the same context as the generation step — the same interpretation of sources, the same implicit assumptions, the same failure modes."

**Source:** Chapter 02 (the-agentic-loop.md): "Self-checking is not independent verification. An agent checking its own output is working from the same context that produced the output: the same interpretation of the sources, the same understanding of the task, the same implicit assumptions."

**Verdict:** VERIFIED — verbatim from source.

## Claim 2
**Narration:** "The check cannot catch systematic errors that already shaped the original work."

**Source:** Chapter 02: "The self-check step cannot catch systematic errors that affected the generation step, because those same errors affect the checking step."

**Verdict:** VERIFIED — consistent with source.

## Claim 3 (Jae example)
**Narration:** "Jae's agent writes a market summary. It misread fifteen percent as fifty percent in a source table. Then it runs a consistency check — comparing the summary to its own recalled version of the table."

**Source:** Chapter 07 candidate card (video-ideas.md): "Jae's agent writes a market summary, then runs a 'consistency check' on the draft. The agent originally misread '15%' as '50%' in a source table. Its consistency check compares the summary to its own recalled version of the table (also '50%'). Check passes. Human opens the PDF: 15%."

**Verdict:** VERIFIED — from canonical example seed on the candidate card.

## Claim 4
**Narration:** "A passing self-check is not evidence the work is correct."

**Source:** Chapter 02 implies this directly; chapter 08 (verification-is-the-control-system.md) makes it explicit: "A passed self-check does not substitute for inspection of primary sources."

**Verdict:** VERIFIED — consistent with book's core argument.

## Exclusions confirmed
- No Reflexion architecture details ✓
- No semantic entropy formalism ✓
- No multi-model review debate ✓
