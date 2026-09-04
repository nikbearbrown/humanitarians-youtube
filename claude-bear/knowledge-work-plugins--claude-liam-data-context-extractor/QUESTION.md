# QUESTION.md

**Question (as redone for hai-simple):** Does Claude already know your
company's data, or does something have to teach it first?

**Source:** redo of
`anthropics/knowledge-work-plugins/youtube/claude-liam-data-context-extractor`
(a rendered Teardown-register `claude-liam` reel walking through the
`data-context-extractor` Anthropic skill).

**Asker:** nobody named — the source reel framed this as a general skill
teardown, not a specific person's question. Name not applicable.

**Source defect, disclosed:** the source sheet's narration was built from a
template that substitutes the skill's one-line description into four beats
(B00, B03, BVDT, BHTF). In this specific sheet that substitution never
happened — all four occurrences read as a bare `>` where the description
belongs (compare the sibling `claude-liam-build-dashboard`, where the same
template slot is filled: "Build an interactive HTML dashboard with charts,
filters, and tables. Use when creating an executive overview..."). The one
piece of the description that IS present verbatim in the source, not a
placeholder, is the lead-in clause itself: **"Generate or improve a
company-specific data analysis skill by"** (B00, repeated in B03/BVDT/BHTF
before the `>`). This redo carries that confirmed fragment forward as the
skill's stated job and does not invent a completion for the missing clause
or a fabricated list of use cases (no enumerated "N situations" the way
`build-dashboard`'s source stated four) — where `build-dashboard` had a real
enumerated list to preserve, `data-context-extractor`'s source genuinely has
none on record.

**Locked facts carried over (do not alter):** `data-context-extractor`'s
stated job is to generate or improve a company-specific data-analysis
skill — i.e., a tailored SKILL.md built around one company's own data
definitions, so that future analysis requests use those definitions instead
of a generic guess. A "skill" is a folder Claude reads before it works, and
the SKILL.md inside is the whole instruction set, in plain language.
Execution is linear: read the file, work through each step in order, return
the result — nothing runs out of sequence unless a step itself says so. The
boundary: coverage is limited to what the instruction file specifies; same
input still produces the same output, every run, but nothing outside what
the file was given context for.
