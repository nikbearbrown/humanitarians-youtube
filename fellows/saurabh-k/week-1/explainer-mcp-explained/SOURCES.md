# SOURCES — hai-mcp-explained

Every on-screen artifact in this reel is listed here with how it was obtained. Nothing shown
as evidence is a reconstruction or a stock asset. Claim-level verdicts are in
[FACTCHECK.md](FACTCHECK.md); this file records provenance.

## Primary sources — first-party, this machine

**1. The MCP client configuration — `~/.claude.json`**
Read directly on 2026-10-18. Two servers are declared: `apify` over HTTP and `rea` over
stdio, the latter started with `npx -y rea-agents@6.5.0 mcp`. The JSON shown on screen is
trimmed to those two entries and their transport fields. Nothing was added or invented.
Shown in B05.

**2. A real tool definition — `list_browser_targets`, exposed by the `rea` server**
The actual schema the server declared in this session: a name, a description, a required
`cdp_endpoint` argument and an optional `allowed_origins`. Description text is quoted and
trimmed for line length rather than paraphrased. Shown in B06.

**3. A real tool call and its result**
That same tool was called once, with one argument, against `http://127.0.0.1:9222`. Five
page targets came back, titled Job Recommendations / Liked Jobs / Applied Jobs / My Resume /
My Profile. Those are the real titles. The model never browsed anything — it asked, the
server looked, the answer returned as data. Shown in B07.

The browser tabs are transient. The claim is about a call that happened, not a result that
reproduces.

## Secondary — described, not quoted

Beats B02, B04 and B08 describe how MCP is defined: the two sides, the four-term vocabulary
(host, client, server, tool), and the fact that a locally-launched server runs with the
user's permissions. These are consistent with the local evidence above but were **not**
checked against <https://modelcontextprotocol.io> during the build. They are marked
SPEC-ASSERTED in FACTCHECK.md and that verification is still open.

## Illustrative, explicitly not measured

B03's hundred-integrations figure is the standard N x M to N + M framing shown with round
numbers. No survey is cited and none is spoken. It must not be given a source that would
imply it was measured.

## Narration

Kokoro `am_onyx`, generated locally. Disclosed aloud in B00 and recorded in the beat sheet
metadata. The voice is not represented as the fellow's own.
