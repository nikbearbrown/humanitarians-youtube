# FACTCHECK — hai-mcp-explained

Status: **GATE F — drafted 2026-10-18. 3 rows VERIFIED-LOCAL, 4 rows SPEC-ASSERTED
(need Saurabh's sign-off against primary docs), 1 row ARGUMENT.**

Verdict vocabulary used here:

- **VERIFIED-LOCAL** — checked against first-party evidence on this machine during the
  build. Reproducible by re-reading the named file or re-running the named call.
- **SPEC-ASSERTED** — a statement about how the Model Context Protocol is defined. It is
  consistent with the local evidence, but it was **not** checked against the published
  specification in this session. Verify before publishing.
- **ARGUMENT** — reasoning, not a measurement. Must not be narrated as a cited fact.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|---|---|---|---|---|
| 1 | B02 | MCP has two sides: a server that declares tools, and a client that reads the list and calls them | SPEC-ASSERTED | Consistent with the two servers configured locally and with the tool definitions the host exposes, but the wording is a description of the protocol, not a quotation of it | Confirm against modelcontextprotocol.io before publishing |
| 2 | B02 | The model never touches the machine directly — it can only make a request | SPEC-ASSERTED | Architecturally true of the local setup (the host process owns the connection, not the model) | Keep the framing as mechanism, not a security guarantee |
| 3 | B03 | Before a shared protocol, every app wired every tool by hand; ten apps and ten tools means a hundred integrations | ARGUMENT | The N×M → N+M framing is standard integration reasoning, illustrated with round numbers. No survey or citation is claimed, and none is spoken | Numbers are illustrative — do not add a source that implies measurement |
| 4 | B04 | Four terms: host, client, server, tool — a tool being a name, a description and typed arguments | SPEC-ASSERTED | "Server" and "tool" are directly evidenced below; "host" and "client" are spec terminology | Confirm the four-term vocabulary against primary docs |
| 5 | B05 | `~/.claude.json` on this machine declares two MCP servers: `apify` over HTTP and `rea` over stdio, started with `npx -y rea-agents@6.5.0 mcp` | **VERIFIED-LOCAL** | Read directly from `~/.claude.json` on 2026-10-18. The on-screen JSON is trimmed to the two entries and their transport fields; nothing was invented | Re-read the file if the configuration changes before publishing |
| 6 | B06 | A tool declares a name, a description, and a typed argument schema — shown as `list_browser_targets` with `cdp_endpoint` (required) and `allowed_origins` | **VERIFIED-LOCAL** | The actual tool definition exposed by the `rea` server in this session. Description text is quoted, trimmed for line length | If trimmed wording drifts from the real description, re-trim rather than paraphrase |
| 7 | B07 | That exact tool was called with one argument and returned five open browser tabs, titled Job Recommendations / Liked Jobs / Applied Jobs / My Resume / My Profile | **VERIFIED-LOCAL** | Real call made earlier in the same session against `http://127.0.0.1:9222`; five page targets returned. Titles are the real ones | The tabs are transient — the claim is about a call that happened, not a repeatable result |
| 8 | B08 | A server you install runs on your machine with your permissions; read what it declares before trusting it | SPEC-ASSERTED | True of the stdio server evidenced in row 5, which is launched as a local process by the host | Scope the claim to locally-launched servers if challenged |

## Honesty notes

- **Narration is AI-generated** (Kokoro `am_onyx`). This is disclosed out loud in B00 and
  recorded in the beat sheet metadata. The voice is not represented as Saurabh's.
- **The evidence is first-party.** B05, B06 and B07 come from this machine and this
  session, not from stock footage or a reconstruction.
- **Rows 1, 2, 4 and 8 are the weak ones.** They are ordinary, widely-held descriptions of
  MCP and nothing in the local evidence contradicts them — but they were not checked
  against the published specification during the build. That check is Saurabh's to make
  before this is published.
