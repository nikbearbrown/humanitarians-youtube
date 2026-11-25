# Pi Agent Architecture — script (narration as rendered)

Voice: Kokoro `am_onyx` · Persona: Liam (in for Kriti)

Narration copied word for word from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

### B00 · cold open
> Hello, this is Liam, in for Kriti. How does the Pi agent work?

### B01 · overview (BLUF)
> Pi is four thin layers around one loop. The model calls tools until it's done, and every step is saved, so you can rewind.

### B02 · body — layers
> Four packages: one talks to any model, one runs the loop, two face you.

### B03 · body — the loop
> Send context, stream a reply. Tool calls? Run them, loop back. None? Done.

### B04 · body — four tools
> Four default tools: read, write, edit, bash.

### B05 · body — system prompt
> A small system prompt, plus your AGENTS.md and skills.

### B06 · body — hooks
> Extensions hook every tool call — block it, rewrite it, log it.

### B07 · body — session tree
> Each step appends one line, linked to its parent. Rewind, and it branches.

### B08 · body — compaction
> Near the context limit, old turns become a summary.

### B09 · verdict
> Verdict: small core, plain files, everything else bolts on.

### B10 · your turn handoff
> Your turn: 'Design a minimal coding agent for my project in Pi's style. What would you leave out?' Pi is defined by what it skips.

### B11 · outro
> Pi, Unpacked. At Nik Bear Brown.
