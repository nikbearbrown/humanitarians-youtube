# QUESTION

**The question:** "Claude, Writing Hookify Rules." — when someone asks Claude
to write a hookify rule, how does Claude even know to use the
`writing-hookify-rules` skill in the first place? Answered using that skill's
own description field as the concrete case.

**Mode:** redo — source is
`anthropics/claude-plugins-official/youtube/claude-liam-writing-hookify-rules/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" reel:
metadata `register: "Teardown"`, `brand: "claude-liam"`, `source_skill`
pointing at
`claude-plugins-official/plugins/hookify/skills/writing-rules/SKILL.md`.
7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro — B00 was already `ClaudeComposerAsk`
REMOTION, not AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no
substitution beyond the WRITER LAW swap). This reel keeps the question and
the source's body facts, re-registers the narration to Plain, replaces the
cold open with the Brutalist Hesitant Writer, folds the source's BVDT verdict
recap into a proper carry-out beat, and closes with the Humanitarians AI
skin.

**Distinct from the sibling reel:** A separate hai-simple redo already exists
for this same skill under the `claude-code` family
(`claude-code--claude-liam-writing-rules`), built from a richer source that
covers the hookify rule's own internals — frontmatter fields, event types,
pattern precision. That source is not this reel's source and is not reused
here. THIS reel's source (`claude-plugins-official`) is a generic
"skill-teardown" sheet whose actual facts are about the skill mechanism
itself, not the rule format: a skill is a folder Claude reads before acting,
its SKILL.md's description field is literally what fires it (the source's
own B03 "design tell" quotes that description verbatim), the pipeline
executes steps linearly once fired, and the reliability the source's verdict
names is "same input, same output — limited to what the file specifies."
This reel's question is therefore about *skill discovery/matching*, not rule
*authoring* — a different angle on the same skill, so the two reels do not
duplicate content.

**Why it earns a reel:** Newcomers to Claude Code / Claude plugins assume a
skill must be invoked by name, like a command. It isn't: a skill's SKILL.md
carries a plain-language description near the top, and Claude compares the
user's own wording against that description to decide whether to fire it.
The `writing-hookify-rules` skill's real description text is the worked
example: it fires "when the user asks to create a hookify rule, write a hook
rule, configure hookify, add a hookify rule, or needs guidance on hookify
rule syntax and patterns." None of those phrases is a special command — they
are the kind of thing a person would say anyway.

**Naive framing (B00, corrected on screen):** "How do I name the skill I
want to use?" → corrects "name" to "describe" (you don't name a skill to
fire it; you describe the task, and Claude matches your wording against the
file's own description).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works; the instruction set is
  one file, SKILL.md — "the file is the program" (source B01)
- the description near the top of that file states exactly when to use the
  skill; this skill's says it fires for "create a hookify rule," "write a
  hook rule," "configure hookify," "add a hookify rule," or guidance on
  hookify rule syntax and patterns (source B03's exact "design tell" quote)
- once fired, Claude reads SKILL.md and executes each step in order — linear
  execution, no branching unless a step says so (source B02 pipeline)
- verdict: same input produces the same output, every run — but only within
  what the SKILL.md specifies (source BVDT)
- source's Your Turn worked example: paste the trigger phrasing into Claude
  and ask it to read the skill and explain what it will do before doing it
