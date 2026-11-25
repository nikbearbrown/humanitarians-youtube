# Pi Agent Architecture — Beat Sheet

**Slug:** `claude-liam-pi-agent-architecture` · **Persona:** Liam (in for Kriti) · **Voice:** Kokoro `am_onyx`

Generated from [`beat_sheet.json`](beat_sheet.json), which is the source of truth: edit the JSON, not this table. Start times add up each beat's rendered duration.

## 12 beats, 1:14 (74.4s)

| # | Act | Start | Dur | Pattern | Motion | Narration |
|---|---|---|---|---|---|---|
| B00 | cold open | 0:00 | 5.5s | ClaudeComposerAsk |  | Hello, this is Liam, in for Kriti. How does the Pi agent work? |
| B01 | overview (BLUF) | 0:06 | 9.5s | BrutalistHesitantWriter |  | Pi is four thin layers around one loop. The model calls tools until it's done, and every step is saved, so you can rewind. |
| B02 | body — layers | 0:15 | 6.0s | PiLayers |  | Four packages: one talks to any model, one runs the loop, two face you. |
| B03 | body — the loop | 0:21 | 6.5s | PiLoop |  | Send context, stream a reply. Tool calls? Run them, loop back. None? Done. |
| B04 | body — four tools | 0:28 | 5.0s | PiTools |  | Four default tools: read, write, edit, bash. |
| B05 | body — system prompt | 0:32 | 5.5s | PiPrompt |  | A small system prompt, plus your AGENTS.md and skills. |
| B06 | body — hooks | 0:38 | 6.0s | PiHooks |  | Extensions hook every tool call — block it, rewrite it, log it. |
| B07 | body — session tree | 0:44 | 6.5s | PiSessionTree |  | Each step appends one line, linked to its parent. Rewind, and it branches. |
| B08 | body — compaction | 0:50 | 5.5s | PiCompaction |  | Near the context limit, old turns become a summary. |
| B09 | verdict | 0:56 | 5.5s | PiVerdict |  | Verdict: small core, plain files, everything else bolts on. |
| B10 | your turn handoff | 1:02 | 9.0s | ClaudeComposerAsk |  | Your turn: 'Design a minimal coding agent for my project in Pi's style. What would you leave out?' Pi is defined by what it skips. |
| B11 | outro | 1:10 | 3.9s | ClaudeTitleOutro |  | Pi, Unpacked. At Nik Bear Brown. |
