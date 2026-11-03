# QUESTION

**The question:** "Claude, Debug Zoom Integration." — when a Zoom
integration breaks, does Claude just jump in and patch whatever looks
wrong, or does something else happen first?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-debug-zoom-integration/beat_sheet.json`
(a Teardown-register batch build, brand `claude-liam`, `@NikBearBrown`, 7
beats: B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro).

**Source defect found, and NOT repeated here:** the source's B03, BVDT, and
BHTF narration each truncate the skill's own "use when…" clause mid-word
("...MCP transport, or rea.", "...SDK joins, M.", "...sdk joins, m.") — a
batch-builder string-length cut, not a real fact. B00's narration and its
`shot.remotion.props.output` field both carry the complete, untruncated
sentence, so the full text is recovered from within this same source sheet
and used consistently everywhere in this redo:
"Debug broken Zoom implementations quickly. Use when auth, webhooks, SDK
joins, MCP transport, or real-time media workflows are failing and you need
to isolate the layer before proposing a fix."

**Unlike the sibling redo `create-cowork-plugin`** (whose real `SKILL.md`
was present in this workspace), this skill's real source file —
`.../partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md` on
Bear's separate machine — is **unreachable from this workspace** (checked:
path does not exist here; no `zoom-plugin` folder anywhere under
`books/`). This redo is therefore built strictly from what the source
beat_sheet.json itself states, with nothing about the skill invented beyond
its own narration text:

- It is a `SKILL.md` file — a folder Claude reads before it acts. Plain
  language, no hidden logic.
- Purpose (verbatim, untruncated — see above): debug broken Zoom
  implementations quickly; use when auth, webhooks, SDK joins, MCP
  transport, or real-time media workflows are failing and the layer needs
  isolating before any fix is proposed.
- The pipeline lives in a Steps section: Claude reads each step in order
  and executes it. Linear — no branching unless a step says so.
- Same input, same output, every run. The skill has nothing to add outside
  what its file specifies.

**Anchor (invented example, not a source claim):** "the Zoom join button
spins and never connects" — a concrete, visualizable failure walked across
the skill's five named layers (auth, webhooks, SDK join, MCP transport,
real-time media). Introduced at B01, paid off at B03. The specific
resolution (the break lands in MCP transport) is this reel's own
illustrative scaffolding for the real mechanism — isolate before fix — not
a claim about what actually breaks in any real Zoom integration.

**Naive framing (B00, corrected on screen):** "A Zoom join breaks — does
Claude just fix it right away?" → corrects "fix" to "isolate" (the
newcomer's default read of "debug it" is jump straight to a patch; the
skill's actual first move is naming which layer failed, not writing a fix).

**Your Turn (generalized):** `debug-zoom-integration` is scoped to one
partner's Zoom plugin, which a general viewer will not have installed. The
lesson generalizes cleanly to any Claude coding session: before Claude
proposes a fix for a real bug, ask it to name every layer that could be
responsible and check them in order, out loud, before touching code.
