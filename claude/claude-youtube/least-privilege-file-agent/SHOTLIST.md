# SHOTLIST -- least-privilege-file-agent
**Simulate Least-Privilege Permission Design for a File Agent with Claude** · 16:9 · ~115s est. (10 beats)
Accents: TEAL = safe/correct; CRIMSON = risk/error.
Source: chapter 03, tools-permissions-and-the-action-surface scope.
Card exclusions honored: no Cowork UI, no connector config, no computer-use.

Shot-type histogram: GRAPHIC 10 (5 Remotion, 5 slates) · no ai stills. Lint: pass.

---
## B00 -- GRAPHIC · remotion · fade · ~5s
Remotion: `NikBearBrownOpen` -- brand open with "Least Privilege Before the Agent Touches a File."

## B01 -- GRAPHIC · slate · fade · ~15s  <- SLATE BEAT
Visual intent: THE WORKING FOLDER IS THE PERMISSION BOUNDARY. Set it before the agent starts.

## B02 -- GRAPHIC · remotion · fade · ~14s
Remotion: `NikBearBrownTerminalAsk` -- terminal shows claude cowork_prep.py generation command

## B03 -- GRAPHIC · remotion · fade · ~14s
Remotion: `NikBearBrownCodeBlock` -- cowork_prep.py displayed with classify function and forbidden/needed patterns

## B04 -- GRAPHIC · slate · fade · ~12s  <- SLATE BEAT (screen-recording)
Visual intent: terminal showing cowork_prep.py manifest: Q3-report.csv=NEEDED, contracts.pdf=FORBIDDEN, .env=FORBIDDEN in red, notes.txt=UNCERTAIN

## B05 -- GRAPHIC · remotion · fade · ~11s
Remotion: `NikBearBrownTerminalAsk` -- revision command hardcoding .env as FORBIDDEN CREDENTIALS

## B06 -- GRAPHIC · slate · fade · ~12s  <- SLATE BEAT (screen-recording)
Visual intent: revised manifest with .env row labeled FORBIDDEN CREDENTIALS, flagged as hardcoded exclusion independent of task description

## B07 -- GRAPHIC · slate · fade · ~12s  <- SLATE BEAT
Visual intent: WORKING FOLDER = PERMISSION BOUNDARY. Narrow it before the agent starts.

## B08 -- GRAPHIC · slate · fade · ~11s  <- SLATE BEAT
Visual intent: Run cowork_prep.py before every file task. Never point the agent at a directory larger than the task.

## B09 -- GRAPHIC · remotion · fade · ~8s
Remotion: `NikBearBrownOutro` -- brand close
