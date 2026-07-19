# SHOTLIST — agent-friendly-cli-checker

**Build an Agent-Friendly CLI Design Checker with Claude** · 16:9 · ~113s est. · 10 beats
Palette: teardown · INK #2A1A0E · CREAM #FFFFFF · CRIMSON #C8102E · PASS #2A7A2A
Source: chapter 10 — agent workflow patterns, CLI design section

Shot-type histogram: remotion 3 · slate 4 · manim 1 · remotion-outro 1. Manim: B04_CLIChecklist.

---

## B00 — remotion NikBearBrownOpen · ~10s
Topic: AGENTIC CLI · lines: Nik Bear Brown / Brutalist + Educational AI / Agent-Friendly CLI Checker / CLI Design Rules / Two Audiences, One Interface

## B01 — slate · ~12s  PROBLEM
Split screen: human CLI view (colored, formatted) vs agent CLI view (raw escape codes, parse error).

## B02 — remotion NikBearBrownTerminalAsk · ~15s  ASK
Command: claude check CLI against 7 agent-friendly rules, pass/fail + agent impact.

## B03 — remotion NikBearBrownCodeBlock · ~15s  CODE
filename: cli_checker.py · 8-line snippet with ANSI_RE check and 5-rule check loop.

## B04 — manim B04_CLIChecklist · ~14s  OUTPUT  ← GRAPHIC SLOT
7-rule checklist: 4 PASS (green) / 3 FAIL (crimson); score summary line.

## B05 — remotion NikBearBrownTerminalAsk · ~15s  CHANGE
Command: update CLI to add --json flag, strip ANSI when piped, re-run checker.

## B06 — slate · ~10s  OUTPUT REVISED
Rule 3 flips FAIL→PASS; score 4/7 → 5/7; two remaining FAILs noted.

## B07 — slate · ~12s  TEARDOWN
"Two audiences" card with 7 rules grouped by ease of fix.

## B08 — slate · ~6s  NEXT STEPS
Next steps + teaser for subagent-summary-protocol.

## B09 — remotion NikBearBrownOutro · ~8s
Brand: Nik Bear Brown / Brutalist + Educational AI / @NikBearBrown / nikbearbrown.com

---

## Slot inventory

| Slot | Status |
|---|---|
| `manim/B04.mp4` | rendered by vox_run.sh via B04_CLIChecklist |
| All other beats | remotion or slate — no media generation needed |
