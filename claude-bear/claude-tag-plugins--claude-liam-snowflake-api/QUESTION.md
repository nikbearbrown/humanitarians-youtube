# QUESTION

**The question:** "Claude, Snowflake Api." — when Claude runs SQL against
Snowflake through the `snowflake-api` skill, what actually comes back from
the submit call, and is it the answer? Answered using the skill's own
documented facts as the concrete case.

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-snowflake-api/beat_sheet.json`
(a Teardown-register "skill-teardown" sheet: metadata `register: "Teardown"`,
`brand: "claude-liam"`, 7 beats — B00 cold open, B01 anatomy, B02 pipeline,
B03 design tell, BVDT verdict, BHTF handoff, BOUT outro — all already
REMOTION, no puppet/AI-video/pantry beat to replace beyond the WRITER LAW
swap). Unlike the `redshift-api` sibling redo, this source is a thin batch
build: `source_skill` points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-tag-plugins/snowflake/skills/snowflake-api/SKILL.md`,
which does not exist on this machine, and every body beat (B01 anatomy, B02
pipeline, B03 design tell, BVDT verdict, BHTF handoff) restates the same
generic SKILL.md frontmatter description rather than adding specific,
distinct technical detail — the same defect class as the `clearance`
sibling logged in HAILOOP-LOG. This reel keeps the question and the one
concrete fact the source's description *does* establish (below), re-
registers the narration to Plain, replaces the cold open with the Brutalist
Hesitant Writer, folds the source's BVDT verdict recap into a proper
carry-out beat, and closes with the Humanitarians AI skin. It does not
invent endpoint paths, header names, or field names beyond what the source
confirms.

**Why it earns a reel:** the source's own description — repeated verbatim
across B00/B01/B03/BVDT/BHTF — establishes exactly this shape: the skill
runs SQL against Snowflake by submitting statements, polling async handles,
fetching result partitions, cancelling, and browsing
warehouses/databases/schemas/tables. Trigger conditions: the user wants to
query Snowflake, asks "what tables are in this schema", checks a
warehouse's status, or mentions `snowflakecomputing.com`, `/api/v2/
statements`, or a Snowflake account identifier (like `xy12345.us-east-1`).
The one fact worth a whole reel: **submitting SQL is async** — the
response to the submit call is a handle to check later, not the rows
themselves; results are fetched afterward, in partitions, once the handle
reaches a terminal state.

**Naive framing (B00, corrected on screen):** "I submit SQL to Snowflake
and get my answer back. Right?" → corrects "answer" to "handle" (the
response to a submit call is a statement handle to poll later — not rows,
not an error, not the answer).

**Body facts carried from source (unchanged, nothing added beyond them):**
- the skill runs SQL against Snowflake: submit statements, poll async
  handles, fetch result partitions, cancel, browse warehouses / databases /
  schemas / tables
- triggers: querying Snowflake, "what tables are in this schema", a
  warehouse's status, `snowflakecomputing.com`, `/api/v2/statements`, an
  account identifier like `xy12345.us-east-1`
- Your Turn: ask Claude to list the tables in a schema and watch whether it
  treats the first response as a handle to poll, not a finished answer.

**Deliberately not invented:** specific request/response field names,
header names, exact terminal-state strings, or partition-count mechanics
beyond "more than one fetch may be needed" — the source's description
confirms the shape (submit → handle → poll → fetch in partitions → cancel
→ browse) but not that level of implementation detail, so this reel states
the shape and stops.
