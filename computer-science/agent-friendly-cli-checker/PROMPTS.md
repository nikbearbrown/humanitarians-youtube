# PROMPTS — agent-friendly-cli-checker

Beat-prefixed prompts for open slots. All slate beats are human-filled after render.

## B04 — manim (rendered automatically by vox_run.sh via B04_CLIChecklist)
No prompt needed — Manim scene is defined in vox_scenes.py.

## B01 — slate visual intent
Vertical split screen. LEFT labeled "Human sees": formatted CLI output with green status text, a spinner animation, colored column headers. RIGHT labeled "Agent sees": same raw bytes with \x1b[32m escape codes visible inline, red "JSONDecodeError" annotation at bottom.

## B06 — slate visual intent
Checklist table. Rule 3 row animates: FAIL badge (crimson) swaps to PASS badge (green #2A7A2A). Score counter top-right: "4/7" → "5/7". Rules 5 and 6 remain red with note: "architecture change required."

## B07 — slate visual intent
Teardown card. Header: "CLI serves two audiences." Two columns: "Human at terminal" (left) / "Agent in pipe" (right). Bottom: "Design for one = the other works around it = errors hide." Seven rules listed grouped: Easy fixes (ANSI strip, --json, --quiet) vs Architecture (stderr routing, --dry-run, exit codes).

## B08 — slate visual intent
Numbered next-steps list: 1) run checker on agent-facing CLI 2) fix ANSI strip (10 min) 3) add --json flag 4) plan stderr routing. Teaser line at bottom: "next: subagent summary protocol →"
