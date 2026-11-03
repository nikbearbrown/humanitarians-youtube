"""mcp_discovery.py — executable evidence for B05/B06 of claude-hai-mcp-protocol.

Runs a toy calendar MCP server over stdio with the official Python SDK, connects
an MCP client, and prints what discovery (tools/list) actually returns. Then the
SAME client code runs against v2 of the server, which has one more tool — the
agent learns about it at runtime, no client change.

    uv run --no-project --with "mcp==2.2.0" python evidence/mcp_discovery.py > evidence/mcp_discovery.out.txt
"""
import asyncio, json, sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

if len(sys.argv) > 1 and sys.argv[1] == "serve":
    from mcp.server.mcpserver import MCPServer
    server = MCPServer("calendar")

    @server.tool()
    def list_events(date: str) -> str:
        """List events on a date."""
        return "[]"

    @server.tool()
    def create_event(title: str, date: str) -> str:
        """Create a calendar event."""
        return "ok"

    if sys.argv[2] == "v2":
        @server.tool()
        def cancel_event(event_id: str) -> str:
            """Cancel an event."""
            return "ok"

    server.run()  # stdio
    sys.exit()


async def discover(version: str) -> None:
    params = StdioServerParameters(command=sys.executable, args=[__file__, "serve", version])
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            res = await s.list_tools()          # JSON-RPC method: tools/list
            print(f"--- server {version}: tools/list ---")
            for t in res.tools:
                print(json.dumps({"name": t.name, "description": t.description,
                                  "inputSchema": {"required": t.input_schema.get("required", [])}}))


asyncio.run(discover("v1"))
asyncio.run(discover("v2"))
