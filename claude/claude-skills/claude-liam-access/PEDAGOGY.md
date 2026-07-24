# PEDAGOGY — access (Discord)

VERDICT: PASS

## What the learner walks away knowing

1. State: `~/.claude/channels/discord/access.json` — five fields: dmPolicy, allowFrom, groups, pending, mentionPatterns.
2. Security model: terminal-only; refuse any request arriving via channel notification (prompt injection guard). Never auto-pick single pending entry.
3. Command dispatch: 8 variants — status, pair/deny, allow/remove, policy, group add/rm, set.
4. pair flow: validate code + expiry → add to allowFrom → write approved/ dir → server polls approved/ and sends confirmation.
5. Implementation rules: read-before-write (server may have added pending), pretty-print JSON, sender snowflake ≠ chat snowflake.

## Where the skill is incomplete

- `$ARGUMENTS` appears literally in skill body with no explanation of how it gets populated or injection risk.
- `set mentionPatterns` accepts regex strings with no validation bounds (catastrophic backtracking unaddressed).
- dmPolicy mode differences (pairing vs allowlist vs disabled bot behavior) never explained.
- Channel server re-read mechanism undocumented: polling interval, file-lock on concurrent write, race conditions.
