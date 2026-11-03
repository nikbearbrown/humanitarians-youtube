# CARRY-OUT.md

**Carry-out line (BCRY narration):**
> Packaging a server as an MCPB makes it runnable without a toolchain — it
> doesn't make it safe. The env var name still has to match exactly, and
> every path check is still yours to write.

**Wrong guess it defeats:** that bundling a local MCP server as an MCPB adds
safety along with portability — like putting the code in a sandboxed
container (B00's hesitant-writer correction, on screen: "safe" → "easy",
landing on "Does bundling it as an MCPB make it easy to run?"; spoken in
narration as "safe"/"easy"; broken at B02 with a falsifying case — the
manifest has no permissions block and no sandbox field to check, so a
packaged MCPB runs with exactly the same file access as the unpackaged
script, path bugs and all).

**Test:** if someone repeats only this sentence next week, it is still true
and still the distinction that matters — not a summary of the whole topic.
