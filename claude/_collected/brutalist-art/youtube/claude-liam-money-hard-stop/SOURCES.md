# SOURCES — claude-liam-money-hard-stop ("Claude, Paused.")

Source: Bear Brown house rule — the HARD STOP money rule now at the top of
`brutalist-art/AGENTS.md` ("If any MCP server, tool, or command is about to
spend money … STOP … ask the human first and wait for an explicit yes").
ai-explainer (standard middle; NOT skill-teardown). Audio: Kokoro am_onyx
(free, local), generated 2026-07-18; durations are ground truth.

## Concrete claims (reuse of facts verified last turn)

Verified against the LIVE Vercel docs 2026-07-18 (see the Vercel reel's
SOURCES.md):
- buy_domain schema takes required registrant PII (name, address, city,
  state, postal, phone, email, country) + optional expectedPrice (a
  price-check number, NOT a confirmation) + renew; executes a real-money
  purchase; no protocol-level confirmation step. (vercel.com tools ref)
- "Always enable human confirmation in your workflows." — verbatim from
  Vercel's Security best practices (vercel.com/docs/agent-resources/vercel-mcp).
- Confused-deputy = consent per client CONNECTION, not per tool call —
  used in B03 as one of the three failure modes.

No new external claims are introduced in this reel; it is an argument built
on already-verified facts + the house rule.

## Framing notes (DOUBLE-CHECK LAW)

- The gun/safety line (B04) and the "one-way door" (B05) are explicit
  metaphors, not factual claims.
- No completed purchase is ever shown or implied; buy_domain is described
  as a capability.
- No tool count or dated version number on screen.
- The three failure modes (prompt injection, confused deputy, autopilot)
  are named at concept level — the point is the class of risk, not a
  specific exploit recipe. Nothing here instructs on performing an attack;
  it teaches the defense (the hard stop).

## Tie-in

This reel is the "why" behind the AGENTS.md rule and the natural companion
to claude-liam-vercel-mcp ("Claude, Trusted."), which is the "where" — the
specific tool that motivated the rule. Same playlist ("Claude Taught").
