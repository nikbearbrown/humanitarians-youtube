# PEDAGOGY — claude-liam-build-mcpb

## Skill reviewed
`anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcpb/SKILL.md`

## What learners will be able to do
- Decide when MCPB is the right distribution path (local machine required, not just cloud API hits)
- Build a valid manifest.json with correct server.type, mcp_config, user_config, and compatibility blocks
- Use ${__dirname} and ${user_config.*} tokens correctly — understand there is no auto-prefix
- Bundle Node (esbuild) or Python (vendor) dependencies for the pack step
- Apply local security: validate paths, refuse root escapes, check roots/list capability first
- Test correctly: pack and test on a machine without dev toolchain

## What makes this teachable
The MCPB-vs-remote gate ("if your server only hits cloud APIs, stop") prevents the most common misuse.
The no-auto-prefix for env vars is a silent failure that catches many developers.
The no-sandbox model (full user privileges) makes local-security.md mandatory, not advisory.
The "works on my machine" test failure pattern (unbundled dependency) is concrete and learnable.

## Gaps the teardown surfaces
- No auto-prefix for env vars buried in a code comment — wrong prefix = silent nil at runtime
- user_config type:"directory" renders native folder picker — not prominently highlighted
- Native extension builds must target each platform — "avoid native deps if you can" buries critical constraint
- roots/list vs hardcoded config — check mentioned only as "before hardcoding..."
- Test on machine without dev toolchain is mandatory but buried at end of testing section

## VERDICT: PASS

MCPB-vs-remote gate, manifest anatomy, and security warning are all complete.
Teardown adds value by surfacing the no-auto-prefix env var trap and the native-extension platform issue.
