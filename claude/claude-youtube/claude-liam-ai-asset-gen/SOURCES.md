# SOURCES — claude-liam-ai-asset-gen
# "Claude, Generated." | ai-asset-gen skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "GPT Image 2 → default image model for high-fidelity general generation, graphic design, UI, banners, typography, and on-image text."
- Source: skills/assets/ai-asset-gen/SKILL.md — Image: Default
- Role: the default model rule for image tasks; on-image text is the decisive signal; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Pass `--wait` to `generate create` so the command blocks until done and prints the result URL itself. Avoid the two-step `create` → `wait` pattern."
- Source: skills/assets/ai-asset-gen/SKILL.md — Workflow step 4
- Role: the --wait contract; one command blocks until URL is printed; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Don't batch-ask. Pick a sane default model and ask one thing at a time only if genuinely missing."
- Source: skills/assets/ai-asset-gen/SKILL.md — UX Rules
- Role: the UX rule that keeps the human in the brief, not the model trivia; stated once, in B07

## Self-demo source
- Phase: model selection decision tree — free, no Higgsfield API call
- Reference: SKILL.md Image section default routing logic (GPT Image 2 for design/typography)
- Output: B04 ClaudeCodeBeat showing task-type decision (image → on-image text → GPT Image 2) + the command that would be issued
- Not faked: decision tree matches SKILL.md Image defaults exactly; command structure matches SKILL.md workflow step 3 exactly; no API call made
