# FACTCHECK — Why MCP Exists

Status: claims checked by Claude Code against Anthropic's MCP announcement, the MCP spec and local executable evidence. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

Sign-off: I, Likhith, reviewed the full review cut (16:9 and 9:16). I checked the claims below against the sources and I approve this video for the final master.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02 | APIs already let software talk to software | PASS | common knowledge | — |
| 2 | B03 | Each API has its own auth, format, docs → custom code per tool | PASS | Anthropic: "Every new data source requires its own custom implementation" | examples labelled illustrative |
| 3 | B04 | Each tool becomes an MCP server that any agent calls the same way | PASS | spec: clients speak one protocol to any server | "each built once" makes server authorship explicit |
| 4 | B05 | At runtime the agent asks the server what tools it has | PASS | spec `tools/list`; evidence/mcp_discovery.out.txt (real output) | — |
| 5 | B06 | Add a tool to the server, the agent sees it next time; nothing hardcoded | PASS | evidence v1→v2, same client code; spec `notifications/tools/list_changed` | "next time" (next list), not "instantly" |
| 6 | B07 | Agents chain tools through one interface | PASS | spec: every tool is invoked with `tools/call` (name + arguments) | tools illustrative |
| 7 | B08 | Checkout / universal terminal | EXEMPT | analogy (requester's), labelled | — |
| 8 | B09 | MCP doesn't replace APIs; it's a common language on top | PASS | MCP servers wrap existing APIs | auth caveat added to verdict card |
| 9 | B09 | MCP is an open standard; any vendor can ship a server, any agent can use it | PASS | Anthropic announcement: MCP is "an open standard"; open spec + SDKs | added to fill the verdict card (GATE V); no counts or adopters named |
