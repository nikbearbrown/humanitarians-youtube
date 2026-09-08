# What Is MCP? — script (final, as shot)

Channel claude-hai · Persona Simba · Register Pragmatist · Voice Kokoro `af_bella`
16:9 long cut: 3:36 (215.9s) · 9:16 Shorts: 1:22 (81.9s)

Timestamps and durations are Kokoro-measured from the locked audio, not estimates — this is exactly what's spoken in the final render. Pre-production shot notes and build rationale live in `SCRIPT-what-is-mcp.md`; this file is narration only, dated to the finished cuts.

## 16:9 — long cut

### B00 · INTRO (0:00–0:21)
> Hi, I am Simba, and this video is about MCP — the protocol that lets an AI assistant reach outside tools and data it couldn't otherwise see. Every assistant has that blind spot: your files, your database, the tools your team actually uses. Today we fix it in about eight lines of Python. By the end, you'll have run one.

### B01 · PROBLEM (0:21–0:43)
> Here's the problem in one picture. Before MCP, if you had four AI apps and four tools you wanted them to reach, somebody had to write sixteen separate integrations — every app wired by hand to every tool. Change one tool's A P I, and you fix it in four places. That math is the reason your assistant still can't read your files.

### B02 · CLI (0:43–1:00)
> So let's build one. Notice what I'm asking for — smallest possible, one tool, official S D K. Not a framework, not a wrapper. When you're learning a protocol, you want the least code that still speaks it, because every extra layer hides the exact part you're trying to see.

### B03 · CODE (1:00–1:21)
> And that's the whole server. Eight lines. FastMCP handles the protocol — you write an ordinary Python function and put a decorator on it. But that decorator is doing something specific. It isn't just registering a function. It's publishing a description and a schema that a model reads to decide whether to call this at all. Hold onto that.

### B04 · OUTPUT (1:21–1:45)
> Run it, and this is what Claude actually sees. Not your code — this. A name, a description, and an input schema. That's the entire interface. And look how thin it is. Description: get expenses. No parameters. So the model's only available move is to call it, take the whole file back, every row, every time, and do the arithmetic itself. It works. It's also lazy.

### B05 · CLI (1:45–2:01)
> So let's fix the interface — not the code. I'm asking for three changes: a real parameter, a docstring that says when to use this tool, and a resource. That's MCP's other primitive: read-only context the model can pull in. Watch what happens to the schema.

### B06 · CODE (2:01–2:23)
> Same shape, three real differences. The function takes a category now, so the schema gains a required parameter. The docstring says when to use it — and that sentence isn't a comment, it ships to the model. And the resource exposes which categories exist, so the model can check instead of guess. Notice the work moved into the description.

### B07 · OUTPUT (2:23–2:46)
> Now the schema carries a required parameter, and the description tells the model when this applies. Ask for software: forty-six dollars, three charges. Travel: four hundred thirty-six twenty. Ask for a category that doesn't exist, and it says so — cleanly — instead of handing back a file and hoping. Same data. Same protocol. The whole difference is how the tool described itself.

### B08 · SUMMARY (2:46–3:11)
> So: MCP is a standard way for an AI app to discover and call outside tools, so every app doesn't need custom glue for every tool. Sixteen integrations become eight. But be clear about what it doesn't do. A tool call is somebody's code running on your machine. The spec itself says treat tool descriptions as untrusted, and get user consent before invoking one. Standard access is not safe access.

### B09 · NEXT STEPS (3:11–3:32)
> Your turn. Paste this in with something you genuinely use — a spreadsheet, an A P I at work: design an MCP server for it. What tools should it expose, what should each docstring say, and what belongs as a resource instead of a tool? That last question will teach you the most, because it forces the exact distinction we just built.

### B10 · OUTRO (3:32–3:36)
> What is MCP. Go build one — it's eight lines to start.

## 9:16 — Shorts cut

### B00 · INTRO (0:00–0:12)
> Hi, I am Simba, and this video is about MCP — the standard that lets your AI assistant see your own data. You can write one in about fifteen lines. Here's the whole idea.

### B01 · PROBLEM (0:12–0:25)
> Four AI apps, four tools. Before MCP, somebody hand-wrote sixteen separate integrations. With one shared protocol in the middle, each side implements it once — and sixteen becomes eight.

### B02 · CODE (0:25–0:38)
> Here's a real one. A normal Python function, with a decorator on it. But look at the docstring — that sentence isn't a comment. It ships to the model, and it's how the model decides whether to call this at all.

### B03 · OUTPUT (0:38–0:51)
> Run it. Software: forty-six dollars, three charges. Travel: four hundred thirty-six twenty. And a category that doesn't exist fails cleanly, instead of handing back a whole file and hoping.

### B04 · SUMMARY (0:51–1:06)
> That's MCP. You're not writing glue for every app any more — you're writing one interface, and the description is the part that matters. Just remember: it standardises access, not trust. A tool call is still somebody's code running.

### B05 · NEXT STEPS (1:06–1:16)
> Your turn — take something you actually use and ask Claude to design an MCP server for it. What belongs as a tool, and what belongs as a resource?

### B06 · OUTRO (1:16–1:22)
> Full build, with the before and after, is on the channel. Simba, for Humanitarians AI.

---

Every code listing and every output figure was produced by actually running `server_v1.py` / `server_v2.py` against `expenses.csv` (both alongside this file) — nothing here is illustrative-but-invented. FastMCP's API was verified against the installed package rather than a fetched summary (a README summary had claimed a class, `MCPServer`, that doesn't actually exist in the SDK).
