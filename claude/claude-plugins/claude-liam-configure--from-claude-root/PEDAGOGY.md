# PEDAGOGY — claude-liam-configure

## Skill reviewed
`anthropics/claude-plugins-official/external_plugins/discord/skills/configure/SKILL.md`

## What learners will be able to do
- Name the three argument modes: no-args (status), token (save), clear (remove)
- Identify the two state files: `~/.claude/channels/discord/.env` and `access.json`
- Know the "push toward lockdown" rule: `pairing` is a temporary state, `allowlist` is the goal
- Describe the three next-step states (no token / token+pairing / token+allowlist)
- Understand that .env changes need a session restart, but access.json changes take effect immediately

## What makes this teachable
The three-mode dispatch is explicit and covers all user entry points.
The "push toward lockdown" rule is a clear policy directive — not optional, always proactive.
chmod 600 on the .env file makes credential hygiene a built-in, not an afterthought.
The two different restart behaviors (.env vs access.json) are a concrete and memorable contrast.

## Gaps the teardown surfaces
- No token format validation before saving — any string gets written to .env without warning
- "Preserve other keys" in .env is stated but no guidance on what other valid keys exist
- Restart after token save is required but no restart command is given
- access.json described by example but full schema is never stated — can't build a valid file from skill alone
- Discord's own gates (shared-server requirement, Public Bot toggle) mentioned but not explained

## VERDICT: PASS

Three-mode dispatch, lockdown rule, and credential hygiene are well-specified.
Token validation gap and missing access.json schema are the key weaknesses.
