# QUESTION.md

**Question (as redone for hai-simple):** Does Claude's instrument-data-to-Allotrope
skill actually understand your lab results — or does it just reformat the file?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-instrument-data-to-allotrope`
(a rendered Teardown-register `claude-liam` reel walking through the
`instrument-data-to-allotrope` Anthropic skill — a lab-instrument-file converter).

**Asker:** nobody named — the source reel framed this as a general skill teardown,
not a specific person's question. Name not applicable.

**Locked facts carried over (do not alter):** the skill converts laboratory
instrument output files — PDF, CSV, Excel, or TXT — into Allotrope Simple Model
(ASM) JSON, or a flattened 2D CSV; it auto-detects which instrument produced the
file; outputs include the full ASM JSON, the flattened CSV, and exportable Python
parser code for data engineers; it's used to standardize instrument data for LIMS
systems, data lakes, and downstream analysis; a "skill" = a folder Claude reads
before acting (LICENSE.txt, requirements.txt, SKILL.md, references/, scripts/ —
5 files total, SKILL.md is the instruction set); execution is linear — read the
file, work each step in order, return the result; the boundary is that only what
the instruction file specifies gets covered — same input, same output, every run.
