# FACTCHECK — MCP: A Universal Plug for AI Tools

Every on-screen and spoken claim, traced to its source. Medhavy paths are relative to `~/Desktop/medhavy/medhavi-hub`. Code outputs are copied verbatim from `code/*.out.txt`.

## B00 · ASK
- Source: bookend (no factual claim beyond the film summary)
- Narration: Hi, I am Shubham L. and this video is about the Model Context Protocol, M C P: the standard way A I assistants discover and call tools. The voice you're hearing is Liam, an A I narrator, reading my script. It's the protocol behind a lot of A I tool integrations, including the one planned for Medhavy two point five.

## B01 · BLUF
- Source: bookend (no factual claim beyond the film summary)
- Narration: Connecting A I to tools used to mean custom glue for every pair. With M C P, every tool speaks one protocol, so any compatible assistant can discover and use it without new glue code.

## B02 · FRAMEWORK
- Source: modelcontextprotocol.io (introduction)
- Narration: The problem is multiplication. Five assistants and ten tools used to mean fifty custom integrations. M C P agrees on the shape of the connection instead. Tools run as M C P servers. Assistants act as M C P clients. Write a server once, and any compatible assistant can use it, the way any device fits a standard port.

## B03 · MECHANISM
- Source: MCP specification: lifecycle, tools/list, tools/call
- Narration: Here's one conversation. The client connects and they agree on a protocol version. Then it asks, tools list: what can you do? The server answers with each tool's name, a description, and the inputs it accepts. The model reads those descriptions, picks a tool, and the client sends tools call with arguments. The result flows back in.

## B04 · WORKED_EXAMPLE
- Source: MCP specification: tools/list result shape (name, description, inputSchema)
- Narration: This is what a tool looks like, in the shape the spec defines. An illustrative example of my own: search textbook. A name, a plain-language description, and a schema for its inputs, a book and a query. On the right, the call a client sends. Notice the description does real work. It's how the model decides when this tool is the right one.

## B05 · FALSIFIABILITY
- Source: MCP specification: security and trust guidance
- Narration: And the catch. A universal plug is also a universal door. A tool runs with whatever permissions it's given, so a write tool really can change data. A server's descriptions can be misleading, so connect only servers you trust. And for anything irreversible, keep a human confirming the call. That's why I'd start Medhavy's interface read-only.

## B06 · VERDICT
- Source: bookend (no factual claim beyond the film summary)
- Narration: So, M C P. One protocol between assistants and tools. Discover with tools list, act with tools call. Every tool declares its name, its description and its inputs. And because tools act for real, trust and human confirmation are part of the design, not an afterthought.

## B07 · YOUR_TURN
- Source: bookend (no factual claim beyond the film summary)
- Narration: Your turn. Ask Claude to design an M C P server for a tool you use every day: three read-only tools and one write tool, with names, descriptions and input schemas, plus how the write tool would ask a human first. Read the descriptions carefully. If you can't tell when each should be used, neither can the model.

## B08 · OUTRO
- Source: bookend (no factual claim beyond the film summary)
- Narration: That was MCP: A Universal Plug for AI Tools. Shubham L., for Humanitarians A I. Thanks for watching.

