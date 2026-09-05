# QUESTION

**The question:** How do you build an independent verification protocol for an
agent's output — one where "verified" means something you can actually go
check, not just a word the agent used?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-liam-independent-verification-protocol/beat_sheet.json`
("Build an Independent Verification Protocol for Agent Outputs with Claude",
Teardown-register, CLI-style video, `register: "Teardown"`, `brand:
"claude-liam"`, `style: "cli"`, cold open a `NikBearBrownOpen` title card,
terminal-ask (`NikBearBrownTerminalAsk`) and form-card (`FormBCard`) beats,
Manim body beats, Your Turn, `ClaudeTitleOutro`). Unlike the sibling
constitution redos, this source's body beats (B01–B08) were fully written,
not seeded placeholders — the facts below carry forward largely intact,
compressed for the Plain register and the hai-simple ten-beat shape.

**Why it earns a reel:** the natural shortcut, when an agent finishes a task,
is to ask it to double-check its own work and take "verified" at face value
— it already did the reasoning once, so re-running the same reasoning feels
like confirmation. But a citation that got matched against the agent's own
training data instead of the actual source document can pass that exact
self-check and still be wrong, because the self-check runs on the same
process that made the original error. Independent evidence has to come from
outside the agent's own say-so — an artifact you can inspect without asking
it anything. And the shape of that artifact isn't fixed: it's designed
*before* the task starts, keyed to the output type, so a research task and a
code-change task get structurally identical protocols with completely
different fills.

**Naive framing (B00, corrected on screen):** "The agent says it's verified.
Verified means true. Right?" → corrects "true" to "checkable" (the real
frame: verified doesn't certify truth, it names something inspectable).

**Body facts carried from source (unchanged):**
- the wrong-guess-breaking case: an agent's verification check can match
  citations against its own training data rather than the actual documents,
  and still report "verified" (source B01) — this is the concrete case that
  falsifies self-report as evidence
- the four-field protocol structure: output type, independent evidence, key
  check (the specific likeliest failure), required artifact (source B02/B03)
  — this is the reel's anchor, planted filled for a research task
- the research-task fill: evidence = a source map (file → claim mapping);
  key check = open the cited documents, don't ask the agent to confirm
  (source B04)
- the code-task fill: evidence = run tests and inspect the diff; artifact =
  test run output + diff; key check = diff shows only intended changes
  (source B05/B06) — this is the anchor's payoff, same four boxes, new
  content, proving the structure generalizes across output types
- the summary lesson: verification is designed before the agent starts: the
  evidence artifact you name is what makes the output verifiable instead of
  just claimed (source B07) — this is the reel's carry-out, kept near-verbatim
- next steps: name the output type and the artifact before the task starts;
  verify the artifact exists independently, without asking the agent to
  confirm it (source B08) — folded into the carry-out and the your-turn
  handoff rather than narrated as a separate beat

**Compression, per the constitution-redo precedent:** ten beats — B00
(writer) + B01–B06 (body) + BCRY + BHTF + BOUT — instead of the source's nine
numbered beats plus Your Turn and outro. B01 plants the anchor (the four-field
card filled for a research task); B02 states the wrong guess (self-check is
enough); B03 breaks it with the source's own falsifying case and states the
independence mechanism; B04 states the "designed before the task starts"
mechanism; B05 covers direction A (a checked artifact only proves what its
specific check covers, not the whole task); B06 covers direction B (a
different fill isn't a verdict on the agent — it's the same structure
reapplied) and pays off the anchor with the code-task fill.

**No inference flag.** Every claim here is a description of a defined
procedure (name the output type, the evidence, the check, the artifact,
before the task starts) rather than an empirical claim about model internals
— there is no leap from evidence to conclusion that needs flagging, unlike
the constitution-family redos which made a claim about training's effect on
latent character space. QUESTION.md documents this instead of forcing a flag
where none is needed (per `simple`'s ONE-FLAG LAW: "if the source genuinely
supports everything, there is no flag").
