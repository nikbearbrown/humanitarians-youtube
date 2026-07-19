# PEDAGOGY — claude-liam-debug-plugins

## Skill reviewed
`anthropics/claude-tag-plugins/claude-tag-troubleshoot/skills/debug-plugins/SKILL.md`

## What learners will be able to do
- Name the six diagnostic steps in order: what arrived → what loaded → what logged → failure ladder → verify zip → report
- Know the five failure modes: zip absent, --plugin-dir missing, extraction error, manifest error, SKILL.md malformed
- Understand the session snapshot rule: configuration changes require a fresh thread; existing threads never reload
- Recognize the stdout gap: structured startup errors go to stdout which is not persisted inside the container
- Know the zip packaging trap: plugin.json must sit at the archive root, not nested inside a folder inside the zip

## What makes this teachable
The six-step ladder is linear and explicit — collect all evidence first, interpret second, report third.
The five failure modes enumerate the full cause space with a specific fix for each.
The session snapshot constraint is the key operational gotcha: common user mistake is to change config and re-ask the same thread.

## Gaps the teardown surfaces
- Step 5 runs `unzip -l` from Bash while the security note says to use Read and Grep — the exception isn't explained
- stdout gap means structured startup errors are permanently undiagnosable from inside the container — no workaround given
- Step 6 report format is prose guidance, not a structured template
- No fallback for a missing or empty /tmp/claude-code.log — skill assumes the file exists
- CLAUDE_CODE_PLUGIN_SEED_DIR seed mounts are identified but cannot be inspected further from inside the skill

## VERDICT: PASS

Security note, six-step linear ladder, five failure modes with specific fixes, session snapshot rule, and zip root packaging trap are well-specified.
stdout gap with no workaround and the unzip Bash exception conflicting with the read-only rule are the key teachable gaps.
