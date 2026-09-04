# QUESTION

**The question:** "Claude, Create Cowork Plugin." — when you ask Claude to
create a Cowork plugin, does it just generate the finished plugin on the
spot, the way asking for a script or a paragraph usually works — or is
something else going on first?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-create-cowork-plugin/beat_sheet.json`
(a Teardown-register batch build, brand `claude-liam`, `@NikBearBrown`, 7
beats: B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro).

**Source defect found, and NOT repeated here:** the source's B00, B03, BVDT,
and BHTF narration each contain a literal unfilled `>` placeholder where a
skill-specific detail was meant to be substituted by the 2026-07-25 batch
builder (`SKILL-EXPLAINERS-BATCH-LOG.md` row 177, `BUILD-SKILL-EXPLAINERS-LOG.md`
lines 118/1263-1269) and never was.

**Unlike the sibling redo `cowork-plugin-customizer`** (whose real SKILL.md
lives only on Bear's separate machine), this skill's real source file IS
present in this workspace:
`/Users/nik/Documents/Cowork/anthropics/knowledge-work-plugins/cowork-plugin-management/skills/create-cowork-plugin/SKILL.md`.
This redo is therefore built from the actual skill text, not from the
source's generic placeholders — richer and more specific than the
`cowork-plugin-customizer` redo could be.

**Facts carried from the real SKILL.md (verified, not invented):**
- The skill runs a five-phase guided conversation: Discovery, Component
  Planning, Design & Clarifying Questions, Implementation, Review & Package.
- Discovery asks what the plugin should do, who will use it, and whether it
  integrates with anything — before any component type is decided.
- Component Planning decides among four component types — Skills (know-how
  or user-triggered actions), MCP servers (reach an outside tool), Agents
  (autonomous multi-step tasks), Hooks (fire automatically on an event) —
  and presents the plan as a table for the user to confirm.
- Implementation (writing every plugin file) is Phase 4 — it runs only
  after Phase 3's design questions are answered and the component plan is
  confirmed in Phase 2.
- The skill's own instruction: "Don't assume 'industry standard' defaults
  are correct" — it asks rather than guesses. Its one stated exception: if
  the user explicitly says "whatever you think is best," it gives a
  specific recommendation and still waits for explicit confirmation before
  writing anything.
- Phase 5 packages the result as a single `.plugin` file, delivered as a
  rich preview the user accepts.

**Anchor (invented example, not a source claim):** "a plugin that onboards
new hires" — a concrete, visualizable scenario used to walk the five phases
concretely. Introduced at B01, paid off at B03. The example itself is not a
fact asserted about Claude; it is illustrative scaffolding for a real
mechanism (the phase order and the confirm-before-build gate).

**Naive framing (B00, corrected on screen):** "Ask Claude to create a
plugin — does it just make it?" → corrects "make" to "plan" (the newcomer's
default read of "create a plugin" is one-shot generation, the same
expectation asking for a script or a paragraph usually satisfies; this
skill's actual first move is a planning conversation, not a write).

**Your Turn (generalized):** `create-cowork-plugin` requires the Cowork
desktop app specifically (per its own `compatibility` field), which a
general viewer may not have open. The lesson generalizes cleanly to any
Claude surface: ask Claude to build something, and before it writes
anything, ask it to lay out its plan in phases and wait for a yes — then
watch whether it asks real questions or guesses.
