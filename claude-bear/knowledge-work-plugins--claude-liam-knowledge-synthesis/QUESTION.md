# QUESTION — knowledge-work-plugins--claude-liam-knowledge-synthesis

**Question (as it would actually be asked):** When Claude answers from several
search results at once, does it just pick the one best result — or does it do
something else with all of them?

**Who asked, where:** Nobody asked this one live; it is a `redo`-mode reel
(SUBJECT.json `mode: "redo"`) rebuilding an existing Teardown explainer —
`anthropics/knowledge-work-plugins/youtube/claude-liam-knowledge-synthesis` —
as a general-audience Plain-register hai-simple cut. The source reel explains
Anthropic's `knowledge-synthesis` skill (an enterprise-search Skill.md that
tells Claude how to combine multi-source search results). The name may be
used — it is a public Anthropic skill, not a person.

**Locked facts, carried from the source (unchanged):**
- The skill's job: combine search results from multiple sources into one
  coherent, deduplicated answer, with source attribution kept intact.
- It scores confidence by weighing freshness and authority per source.
- It summarizes effectively when the result set is large.
- Execution is a fixed pipeline: read the SKILL.md, then run its steps in
  order — linear, no branching unless a step says so.
- Same input produces the same output, every run (deterministic).
- The skill only does what its file specifies — nothing outside the spec.
